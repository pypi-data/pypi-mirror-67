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

import random

import mock
import paramiko

from oslo_config import cfg as config
from oslo_utils import uuidutils

from omnipath.mechanism_driver import fabric_agent
from omnipath.tests.unit import base


class TestOmniPathFabricAgent(base.TestOmniPathBase):

    def setUp(self):
        super(TestOmniPathFabricAgent, self).setUp()
        self.fabric_agent = self.mech_driver.opafmvf.cli

    @mock.patch.object(paramiko.SSHClient, 'set_missing_host_key_policy')
    @mock.patch.object(paramiko.SSHClient, 'connect')
    @mock.patch.object(paramiko.RSAKey, 'from_private_key_file')
    def test_connect(self, mock_key, mock_conn, mock_set):
        self._agent_hostname = config.CONF.ml2_omnipath.ip_address
        mock_key.return_value = 'key'
        self.fabric_agent.connect()
        mock_conn.assert_called_with(self._agent_hostname, port=22,
                                     username=None, pkey='key')

    def test_fabric_agent_management_command_reset(self):
        with mock.patch.object(self.fabric_agent,
                               "execute_command",
                               return_value=0) as mock_fa:
            self.fabric_agent.osfa_management_commands("reset")
            mock_fa.assert_called_once_with(" opafmvf reset")

    def test_fabric_agent_management_command_abort(self):
        with mock.patch.object(self.fabric_agent,
                               "execute_command",
                               return_value=0) as mock_fa:
            self.fabric_agent.osfa_management_commands("abort")
            mock_fa.assert_called_with(" killall -9 opafmvf")

    def test_fabric_agent_config_command_abort(self):
        with mock.patch.object(self.fabric_agent,
                               "execute_command",
                               return_value=0) as mock_fa:
            fake_arg = random.randint(0x0000, 0x7FFF)
            cmd = " opafmvf create fake_vf --pkey "
            self.fabric_agent.osfa_config_commands("create",
                                                   "fake_vf",
                                                   fake_arg)
            mock_fa.assert_called_with(cmd + str(fake_arg))

    def test_exceptions(self):
        with mock.patch.object(fabric_agent.LOG, 'error') as mock_log:
            fake_arg = random.randint(0x0000, 0x7FFF)
            self.fabric_agent.osfa_management_commands("hello")
            mock_log.assert_called()
            self.fabric_agent.osfa_query_commands("hello"
                                                  "fake_vf",
                                                  "fake_arg")
            mock_log.assert_called()
            self.fabric_agent.osfa_config_commands("asdf",
                                                   "fake_vf",
                                                   fake_arg)
            mock_log.assert_called()

    def test_fabric_agent_queries(self):
        with mock.patch.object(self.fabric_agent,
                               "execute_command",
                               return_value=0) as mock_fa:
            command = " opafmvf ismember fake_vf "
            self.fabric_agent.osfa_query_commands("ismember",
                                                  "fake_vf")
            mock_fa.assert_called_once_with(command)

    def test_get_port_status(self):
        with mock.patch.object(self.fabric_agent,
                               "execute_command",
                               return_value=0):
            fake_guid = uuidutils.generate_uuid()
            fake_vf = "fake_vf"
            self.assertEqual(
                self.mech_driver.opafmvf.get_port_status(
                    fake_vf, fake_guid), ("UP"))
