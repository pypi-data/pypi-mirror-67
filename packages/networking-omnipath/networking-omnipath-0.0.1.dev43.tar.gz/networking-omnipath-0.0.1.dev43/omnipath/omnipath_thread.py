# Copyright (c) 2019 Intel Corporation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

import threading

import six

from neutron_lib import context as nl_context
from oslo_log import log as logging

from omnipath.common import constants as const
from omnipath.db import api as opadbapi
from omnipath.mechanism_driver import fabric_agent
from omnipath import omnipath_exceptions as omp_exc

LOG = logging.getLogger(__name__)

# TODO(manjeets) use this parameter from config
sync_time = 10


@six.add_metaclass(abc.ABCMeta)
class OmniPathThread(object):

    def __init__(self, start_thread=True, fabric_cli=None):
        self.event = threading.Event()
        self._sync_time = 300
        self.status = False
        self._omni_sync_thread = self._create_omni_sync_thread()
        self._omni_sync_thread_stop = threading.Event()
        self.fabric_cli = fabric_cli if fabric_cli else (
            fabric_agent.FabricAgentClient().cli)
        if start_thread:
            self.start()

    def _create_omni_sync_thread(self):
        return threading.Thread(name='sync', target=self.run_sync)

    def start(self):
        LOG.debug("OMNIPATH/THREAD Starting a new omnipath sync thread")
        if self._omni_sync_thread_stop.is_set():
            self._omni_sync_thread_stop.clear()
            self._omni_sync_thread = self._create_omni_sync_thread()

        if not self._omni_sync_thread.is_alive():
            self._omni_sync_thread.start()

    def stop(self, timeout=None):
        LOG.debug("OMNIPATH/THREAD Stopping the omnipath sync thread")
        if self._omni_sync_thread.is_alive():
            self._omni_sync_thread_stop.set()
            self.set_sync_event()
            self._omni_sync_thread.join(timeout)
            self.fabric_cli.osfa_management_commands("abort")

    def set_sync_event(self):
        self.event.set()

    def run_sync(self):
        while not self._omni_sync_thread_stop.is_set():
            try:
                LOG.debug("OMNIPATH/THREAD run_sync() cycle")
                self.event.wait()
                self.event.clear()
                self.sync_omnipath_operations()
            except Exception:
                LOG.exception("OMNIPATH/THREAD Error on running omnipath "
                              "sync run_sync")

    def _commit_and_reload(self):
        try:
            LOG.debug("OMNIPATH/THREAD opafmvf commit+reload")
            self.fabric_cli.osfa_management_commands(const.OPA_COMMIT)
            self.fabric_cli.osfa_management_commands(const.OPA_RELOAD)
        except Exception:
            LOG.exception("OMNIPATH/THREAD Error on omnipath sync check if "
                          "fabric is up")
            raise omp_exc.FabricAgentCLIError

    def sync_omnipath_operations(self):
        LOG.debug("OMNIPATH/THREAD Started syncing with omnipath fabric")
        try:
            context = nl_context.get_admin_context()
            all_pending_entries = opadbapi.get_all_entries_by_state(
                context, 'pending')
            all_waiting_ports = opadbapi.get_all_entries_by_state(
                context, 'waiting')
            if all_pending_entries:
                for entry in all_pending_entries:
                    try:
                        self._process_entry(context, entry)
                    except Exception:
                        LOG.error(
                            "OMNIPATH/THREAD Error on syncing omnipath entry")
            if all_waiting_ports:
                updated_ports = self._process_port_batch(
                    context, all_waiting_ports)
                if updated_ports > 0:
                    self._commit_and_reload()
        except Exception:
            LOG.error(
                "OMNIPATH/THREAD Error on omnipath sync check if fabric is up")

    def _prepare_ports_batch(self, all_waiting_ports):
        LOG.debug("OMNIPATH/THREAD _prepare_ports_batch()")
        port_add_batch = {}
        port_del_batch = {}
        for port in all_waiting_ports:
            network_id = port.data['network_id']
            if port.data['operation'] == const.OPA_ADD:
                if network_id not in port_add_batch.keys():
                    port_add_batch[network_id] = [(port.data['guid'],
                                                   port.resource_uuid)]
                else:
                    port_add_batch[network_id].append((port.data['guid'],
                                                       port.resource_uuid))
            elif port.data['operation'] == const.OPA_DELETE:
                if network_id not in port_del_batch.keys():
                    port_del_batch[network_id] = [(port.data['guid'],
                                                   port.resource_uuid)]
                else:
                    port_del_batch[network_id].append((port.data['guid'],
                                                      port.resource_uuid))
        return port_add_batch, port_del_batch

    def _process_port_batch(self, context, all_waiting_ports):
        port_add_batch, port_del_batch = self._prepare_ports_batch(
            all_waiting_ports)
        port_bind_ids = []
        port_del_ids = []
        for network in port_add_batch.keys():
            port_args = ["0x{}".format(x[0]) for x in port_add_batch[network]]
            port_guids = " ".join(port_args)
            self.fabric_cli.osfa_config_commands(
                const.OPA_ADD, network, port_guids)
            port_bind_ids = [x[1] for x in port_add_batch[network]]
            opadbapi.update_multiple_rows(context, "completed",
                                          port_bind_ids)

        LOG.debug("OMNIPATH/THREAD all_waiting_ports=%s" % all_waiting_ports)
        for network in port_del_batch.keys():
            port_args = ["0x{}".format(x[0]) for x in port_del_batch[network]]
            port_guids = " ".join(port_args)
            self.fabric_cli.osfa_config_commands(
                const.OPA_REMOVE, network, port_guids)
            port_del_ids = [x[1] for x in port_del_batch[network]]
            opadbapi.update_multiple_rows(context, "completed",
                                          port_del_ids)

        return len(port_bind_ids) + len(port_del_ids)

    def _process_entry(self, context, entry):
        LOG.debug("OMNIPATH/THREAD _process_entry()")
        data = entry.get('data')
        if entry.get('resource_type') == "network":
            net_id = data['id']
            if data['operation'] == const.OPA_CREATE:
                pkey = data['provider:segmentation_id']
                status = self.fabric_cli.osfa_config_commands(
                    const.OPA_CREATE, net_id, pkey)
                op_state = const.OPA_COMPLETED if status == 0 else (
                    const.OPA_FAILED)
                opadbapi.update_row_state(
                    context, const.OPA_COMPLETED, entry)
            elif data['operation'] == const.OPA_DELETE:
                status = self.fabric_cli.osfa_config_commands(
                    const.OPA_DELETE, net_id)
                op_state = const.OPA_COMPLETED if status == 0 else (
                    const.OPA_FAILED)
                self._commit_and_reload()
            opadbapi.update_row_state(context, op_state, entry)
        elif entry.get('resource_type') == 'port':
            net_id = data['network_id']
            port_guid = data['port_guid']
            LOG.debug(
                "OMNIPATH/THREAD adding port guid %s from pending" % port_guid)
            self.fabric_cli.osfa_config_commands(
                const.OPA_ADD, net_id, "0x{}".format(port_guid))
