#    Copyright (c) 2019 Intel Corporation
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
#

import mock

from omnipath.db import api as opadbapi
from omnipath.mechanism_driver import fabric_agent
from omnipath import omnipath_thread
from omnipath.tests.unit.mechanism_driver import test_mech_omnipath


class TestOmnipathThread(test_mech_omnipath.TestOmniPathMechanismDriver):

    def setUp(self):
        super(TestOmnipathThread, self).setUp()
        self.fabric_agent = self.mech_driver.opafmvf.cli

    def test__commit_and_reload(self):
        with mock.patch.object(self.fabric_agent,
                               'osfa_management_commands') as mock_mgt:
            self.mech_driver.omnipath_thread._commit_and_reload()
            self.assertEqual(mock_mgt.call_count, 2)
            expected_calls = [mock.call("commit"),
                              mock.call("reload")]
            mock_mgt.assert_has_calls(expected_calls, any_order=True)

    @mock.patch.object(omnipath_thread.OmniPathThread,
                       '_commit_and_reload')
    def test_sync_omnipath_operations(self, mock_cr):
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               'execute_command',
                               return_value=0) as mock_exec:
            context_n = self._get_fake_network_context()
            self.mech_driver.create_network_precommit(context_n)
            res = opadbapi.get_all_entries_by_state(context_n,
                                                    'pending')
            self.mech_driver.omnipath_thread.sync_omnipath_operations()
            if res:
                mock_exec.assert_called()
            context_p = self._get_fake_port_context()
            self.mech_driver.create_port_precommit(context_p)
            resp = opadbapi.get_all_entries_by_state(context_p,
                                                     'waiting')
            self.mech_driver.omnipath_thread.sync_omnipath_operations()
            if resp:
                self.assertTrue(mock_exec.called)

    def test__process_entry(self):
        context_n = self._get_fake_network_context()
        context_p = self._get_fake_port_context()
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               'execute_command') as mock_exec:
            self.mech_driver.create_network_precommit(context_n)
            self.mech_driver.delete_network_precommit(context_n)
            res = opadbapi.get_all_entries_by_state(context_n,
                                                    'pending')
            self.mech_driver.create_port_precommit(context_p)
            resp = opadbapi.get_all_entries_by_state(context_p,
                                                     'waiting')
            self.mech_driver.omnipath_thread._process_entry(
                context_n, res[0])
            self.mech_driver.omnipath_thread._process_entry(
                context_p, resp[0])
            self.assertEqual(mock_exec.call_count, 4)

    def test__process_entry_guid_format(self):
        context_p = self._get_fake_port_context()
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               'osfa_config_commands') as mock_exec:
            self.mech_driver.create_port_precommit(context_p)
            resp = opadbapi.get_all_entries_by_state(context_p,
                                                     'waiting')
            self.mech_driver.omnipath_thread._process_entry(
                context_p, resp[0])
            guid = resp[0]['data']['port_guid']
            netw = resp[0]['data']['network_id']
            mock_exec.assert_called_with(
                'add', netw, "0x{}".format(guid))  # 0x must be added

    def _create_foo_ports(self):
        foo_port1 = mock.MagicMock()
        foo_port2 = mock.MagicMock()
        foo_port1.data = {'id': '234',
                          'operation': 'add',
                          'network_id': 'net-234',
                          'guid': 'fake_guid'}
        foo_port1.resource_uuid = 'fake_uuid'
        foo_port2.data = {'id': '456',
                          'operation': 'delete',
                          'network_id': 'net-456',
                          'guid': 'bogus_guid'}
        foo_port1.resource_uuid = 'fake_uuid'
        foo_port2.resource_uuid = 'bogus_uuid'
        return [foo_port1, foo_port2]

    def test__prepare_ports_batch(self):
        foo_waiting_ports = self._create_foo_ports()
        self.assertEqual(
            self.mech_driver.omnipath_thread._prepare_ports_batch(
                foo_waiting_ports), ({'net-234': [('fake_guid',
                                                   'fake_uuid')]},
                                     {'net-456': [('bogus_guid',
                                                   'bogus_uuid')]}))

    def test_process_port_add(self):
        context = self._get_fake_port_context()
        foo_waiting_ports = mock.MagicMock()
        foo_waiting_ports.data = {'id': '123',
                                  'operation': 'add',
                                  'network_id': 'net-123',
                                  'guid': 'y_guid'}
        foo_waiting_ports.resource_uuid = 'y_uuid'
        foo_ports = [foo_waiting_ports]
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               "execute_command",
                               return_value=0):
            self.assertEqual(
                self.mech_driver.omnipath_thread._process_port_batch(
                    context, foo_ports), 1)

    def test_process_port_batch_del(self):
        context = self._get_fake_port_context()
        foo_waiting_ports = mock.MagicMock()
        foo_waiting_ports.data = {'id': '456',
                                  'operation': 'delete',
                                  'network_id': 'net-456',
                                  'guid': 'x_guid'}
        foo_waiting_ports.resource_uuid = 'x_uuid'
        foo_ports = [foo_waiting_ports]
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               "execute_command",
                               return_value=0):
            self.assertEqual(
                self.mech_driver.omnipath_thread._process_port_batch(
                    context, foo_ports), 1)

    def test__process_port_batch_guid_format(self):
        context = self._get_fake_port_context()
        waiting_ports = self._create_foo_ports()
        with mock.patch.object(fabric_agent.FabricAgentCLI,
                               'osfa_config_commands') as mock_exec:
            self.mech_driver.omnipath_thread._process_port_batch(
                context, waiting_ports)
            mock_exec.assert_any_call('add', 'net-234', '0xfake_guid')
            mock_exec.assert_any_call('remove', 'net-456', '0xbogus_guid')
            self.assertEqual(mock_exec.call_count, 2)
