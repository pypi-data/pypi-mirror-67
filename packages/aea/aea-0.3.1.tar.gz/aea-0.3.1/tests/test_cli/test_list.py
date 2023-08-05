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

"""This test module contains the tests for the `aea list` sub-command."""

import json
import os
import shutil
import tempfile
from pathlib import Path
from unittest import TestCase, mock

import jsonschema
from jsonschema import Draft4Validator

from aea.cli import cli
from aea.test_tools.click_testing import CliRunner

from tests.test_cli.constants import FORMAT_ITEMS_SAMPLE_OUTPUT

from ..conftest import (
    AGENT_CONFIGURATION_SCHEMA,
    CLI_LOG_OPTION,
    CONFIGURATION_SCHEMA_DIR,
    CUR_PATH,
)


class TestListProtocols:
    """Test that the command 'aea list protocols' works as expected."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.schema = json.load(open(AGENT_CONFIGURATION_SCHEMA))
        cls.resolver = jsonschema.RefResolver(
            "file://{}/".format(Path(CONFIGURATION_SCHEMA_DIR).absolute()), cls.schema
        )
        cls.validator = Draft4Validator(cls.schema, resolver=cls.resolver)
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        # copy the 'dummy_aea' directory in the parent of the agent folder.
        shutil.copytree(Path(CUR_PATH, "data", "dummy_aea"), Path(cls.t, "dummy_aea"))
        cls.runner = CliRunner()
        os.chdir(Path(cls.t, "dummy_aea"))

        with mock.patch(
            "aea.cli.list._format_items", return_value=FORMAT_ITEMS_SAMPLE_OUTPUT
        ):
            cls.result = cls.runner.invoke(
                cli, [*CLI_LOG_OPTION, "list", "protocols"], standalone_mode=False
            )

    def test_exit_code_equal_to_zero(self):
        """Assert that the exit code is equal to zero (i.e. success)."""
        assert self.result.exit_code == 0

    def test_correct_output(self):
        """Test that the command has printed the correct output."""
        compare_text = "{}\n".format(FORMAT_ITEMS_SAMPLE_OUTPUT)
        assert self.result.output == compare_text

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestListConnections:
    """Test that the command 'aea list connections' works as expected."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.schema = json.load(open(AGENT_CONFIGURATION_SCHEMA))
        cls.resolver = jsonschema.RefResolver(
            "file://{}/".format(Path(CONFIGURATION_SCHEMA_DIR).absolute()), cls.schema
        )
        cls.validator = Draft4Validator(cls.schema, resolver=cls.resolver)
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        # copy the 'dummy_aea' directory in the parent of the agent folder.
        shutil.copytree(Path(CUR_PATH, "data", "dummy_aea"), Path(cls.t, "dummy_aea"))
        cls.runner = CliRunner()
        os.chdir(Path(cls.t, "dummy_aea"))

        with mock.patch(
            "aea.cli.list._format_items", return_value=FORMAT_ITEMS_SAMPLE_OUTPUT
        ):
            cls.result = cls.runner.invoke(
                cli, [*CLI_LOG_OPTION, "list", "connections"], standalone_mode=False
            )

    def test_exit_code_equal_to_zero(self):
        """Assert that the exit code is equal to zero (i.e. success)."""
        assert self.result.exit_code == 0

    def test_correct_output(self):
        """Test that the command has printed the correct output."""
        compare_text = "{}\n".format(FORMAT_ITEMS_SAMPLE_OUTPUT)
        assert self.result.output == compare_text

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


class TestListSkills:
    """Test that the command 'aea list skills' works as expected."""

    @classmethod
    def setup_class(cls):
        """Set the test up."""
        cls.schema = json.load(open(AGENT_CONFIGURATION_SCHEMA))
        cls.resolver = jsonschema.RefResolver(
            "file://{}/".format(Path(CONFIGURATION_SCHEMA_DIR).absolute()), cls.schema
        )
        cls.validator = Draft4Validator(cls.schema, resolver=cls.resolver)
        cls.cwd = os.getcwd()
        cls.t = tempfile.mkdtemp()
        # copy the 'dummy_aea' directory in the parent of the agent folder.
        shutil.copytree(Path(CUR_PATH, "data", "dummy_aea"), Path(cls.t, "dummy_aea"))
        cls.runner = CliRunner()
        os.chdir(Path(cls.t, "dummy_aea"))

        with mock.patch(
            "aea.cli.list._format_items", return_value=FORMAT_ITEMS_SAMPLE_OUTPUT
        ):
            cls.result = cls.runner.invoke(
                cli, [*CLI_LOG_OPTION, "list", "skills"], standalone_mode=False
            )

    def test_exit_code_equal_to_zero(self):
        """Assert that the exit code is equal to zero (i.e. success)."""
        assert self.result.exit_code == 0

    def test_correct_output(self):
        """Test that the command has printed the correct output."""
        compare_text = "{}\n".format(FORMAT_ITEMS_SAMPLE_OUTPUT)
        assert self.result.output == compare_text

    @classmethod
    def teardown_class(cls):
        """Tear the test down."""
        os.chdir(cls.cwd)
        try:
            shutil.rmtree(cls.t)
        except (OSError, IOError):
            pass


@mock.patch("aea.cli.common.try_to_load_agent_config")
class ListContractsCommandTestCase(TestCase):
    """Test that the command 'aea list contracts' works as expected."""

    def setUp(self):
        """Set the test up."""
        self.runner = CliRunner()

    @mock.patch("aea.cli.list._get_item_details")
    @mock.patch("aea.cli.common._validate_config_consistency")
    @mock.patch("aea.cli.common._format_items")
    def test_list_contracts_positive(self, *mocks):
        """Test list contracts command positive result."""
        result = self.runner.invoke(
            cli, [*CLI_LOG_OPTION, "list", "contracts"], standalone_mode=False
        )
        self.assertEqual(result.exit_code, 0)
