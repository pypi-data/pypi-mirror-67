# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This test module contains the integration test for the tac skills."""

import os
import time

from aea.test_tools.decorators import skip_test_ci
from aea.test_tools.test_cases import AEAWithOefTestCase


class TestTacSkills(AEAWithOefTestCase):
    """Test that tac skills work."""

    @skip_test_ci
    def test_tac(self, pytestconfig):
        """Run the tac skills sequence."""
        tac_aea_one = "tac_participant_one"
        tac_aea_two = "tac_participant_two"
        tac_controller_name = "tac_controller"

        # create tac controller, agent one and agent two
        self.create_agents(
            tac_aea_one, tac_aea_two, tac_controller_name,
        )

        # prepare tac controller for test
        tac_controller_dir_path = os.path.join(self.t, tac_controller_name)
        os.chdir(tac_controller_dir_path)
        self.add_item("connection", "fetchai/oef:0.2.0")
        self.set_config("agent.default_connection", "fetchai/oef:0.2.0")
        self.add_item("skill", "fetchai/tac_control:0.1.0")
        self.run_install()

        # prepare agents for test
        tac_aea_one_dir_path = os.path.join(self.t, tac_aea_one)
        tac_aea_two_dir_path = os.path.join(self.t, tac_aea_two)

        for agent_path in (tac_aea_one_dir_path, tac_aea_two_dir_path):
            os.chdir(agent_path)

            self.add_item("connection", "fetchai/oef:0.2.0")
            self.set_config("agent.default_connection", "fetchai/oef:0.2.0")
            self.add_item("skill", "fetchai/tac_participation:0.1.0")
            self.add_item("skill", "fetchai/tac_negotiation:0.1.0")
            self.run_install()

        # run tac controller
        os.chdir(tac_controller_dir_path)
        tac_controller_process = self.run_agent("--connections", "fetchai/oef:0.2.0")

        # run two agents (participants)
        os.chdir(tac_aea_one_dir_path)
        tac_aea_one_process = self.run_agent("--connections", "fetchai/oef:0.2.0")

        os.chdir(tac_aea_two_dir_path)
        tac_aea_two_process = self.run_agent("--connections", "fetchai/oef:0.2.0")

        time.sleep(10.0)

        self.terminate_agents(
            [tac_controller_process, tac_aea_one_process, tac_aea_two_process]
        )

        assert self.is_successfully_terminated(), "TAC test not successful."
