# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import ConfigParser

from resource_management import *

script_dir = os.path.dirname(os.path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(script_dir, 'download.ini')))

PRESTO_RPM_URL = config.get('download', 'presto_rpm_url')
PRESTO_RPM_NAME = PRESTO_RPM_URL.split('/')[-1]
PRESTO_CLI_URL = config.get('download', 'presto_cli_url')
PRESTO_CLI_NAME = PRESTO_CLI_URL.split('/')[-1]

def create_tpch_connector(node_properties):
        Execute('mkdir -p {0}'.format(node_properties['plugin.config-dir']))
        Execute('echo "connector.name=tpch" > {0}'.format(os.path.join(node_properties['plugin.config-dir'], 'tpch.properties')))