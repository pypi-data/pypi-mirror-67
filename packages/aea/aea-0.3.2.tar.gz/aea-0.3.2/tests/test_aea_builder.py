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
""" This module contains tests for aea/aea_builder.py """
import os
import re
from pathlib import Path

import pytest

from aea.aea_builder import AEABuilder
from aea.configurations.base import ComponentType
from aea.crypto.fetchai import FETCHAI
from aea.exceptions import AEAException

from tests.common.utils import timeit_context

from .conftest import CUR_PATH, ROOT_DIR, skip_test_windows


@skip_test_windows()
def test_default_timeout_for_agent():
    """
    Tests agents loop sleep timeout
    set by AEABuilder.DEFAULT_AGENT_LOOP_TIMEOUT
    """
    agent_name = "MyAgent"
    private_key_path = os.path.join(CUR_PATH, "data", "fet_private_key.txt")
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(FETCHAI, private_key_path)
    builder.DEFAULT_AGENT_LOOP_TIMEOUT = 0.05

    """ Default timeout == 0.05 """
    aea = builder.build()
    assert aea._timeout == builder.DEFAULT_AGENT_LOOP_TIMEOUT

    with timeit_context() as time_result:
        aea._spin_main_loop()

    assert time_result.time_passed > builder.DEFAULT_AGENT_LOOP_TIMEOUT
    time_0_05 = time_result.time_passed

    """ Timeout == 0.001 """
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(FETCHAI, private_key_path)
    builder.DEFAULT_AGENT_LOOP_TIMEOUT = 0.001

    aea = builder.build()
    assert aea._timeout == builder.DEFAULT_AGENT_LOOP_TIMEOUT

    with timeit_context() as time_result:
        aea._spin_main_loop()

    assert time_result.time_passed > builder.DEFAULT_AGENT_LOOP_TIMEOUT
    time_0_001 = time_result.time_passed

    """ Timeout == 0.0 """
    builder = AEABuilder()
    builder.set_name(agent_name)
    builder.add_private_key(FETCHAI, private_key_path)
    builder.DEFAULT_AGENT_LOOP_TIMEOUT = 0.0

    aea = builder.build()
    assert aea._timeout == builder.DEFAULT_AGENT_LOOP_TIMEOUT

    with timeit_context() as time_result:
        aea._spin_main_loop()

    assert time_result.time_passed > builder.DEFAULT_AGENT_LOOP_TIMEOUT
    time_0 = time_result.time_passed

    assert time_0 < time_0_001 < time_0_05


def test_add_package_already_existing():
    """
    Test the case when we try to add a package (already added) to the AEA builder.

    It should fail because the package is already present into the builder.
    """
    builder = AEABuilder()
    fipa_package_path = Path(ROOT_DIR) / "packages" / "fetchai" / "protocols" / "fipa"
    builder.add_component(ComponentType.PROTOCOL, fipa_package_path)

    expected_message = re.escape(
        "Component 'fetchai/fipa:0.1.0' of type 'protocol' already added."
    )
    with pytest.raises(AEAException, match=expected_message):
        builder.add_component(ComponentType.PROTOCOL, fipa_package_path)


def test_when_package_has_missing_dependency():
    """
    Test the case when the builder tries to load the packages,
    but fails because of a missing dependency.
    """
    builder = AEABuilder()
    expected_message = re.escape(
        "Package 'fetchai/oef:0.2.0' of type 'connection' cannot be added. "
        "Missing dependencies: ['(protocol, fetchai/fipa:0.1.0)', '(protocol, fetchai/oef_search:0.1.0)']"
    )
    with pytest.raises(AEAException, match=expected_message):
        # connection "fetchai/oef:0.1.0" requires
        # "fetchai/oef_search:0.1.0" and "fetchai/fipa:0.1.0" protocols.
        builder.add_component(
            ComponentType.CONNECTION,
            Path(ROOT_DIR) / "packages" / "fetchai" / "connections" / "oef",
        )
