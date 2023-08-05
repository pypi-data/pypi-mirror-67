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

NETWORK_PKEY = "pkey"

OPA_BINARY = "opafmvf"

# Operations
OPA_CREATE = "create"
OPA_ADD = "add"
OPA_REMOVE = "remove"
OPA_DELETE = "delete"
OPA_COMMIT = "commit"
OPA_ABORT = "abort"
OPA_EXIST = "exist"
OPA_RESTART = "restart"
OPA_ISMEMBER = "ismember"
OPA_ISNOTMEMBER = "isnotmember"
OPA_RESET = "reset"
OPA_RELOAD = "reload"

# Statuses
OPA_NF = 2
OPA_SUCCESS = 0
OPA_FAIL = 1

# States
OPA_COMPLETED = "completed"
OPA_FAILED = "failed"

ALLOWED_OPA_COMMANDS = (OPA_CREATE, OPA_ADD,
                        OPA_REMOVE, OPA_DELETE,
                        OPA_COMMIT, OPA_RESTART,
                        OPA_ISMEMBER, OPA_ISNOTMEMBER,
                        OPA_RESET, OPA_RELOAD)
