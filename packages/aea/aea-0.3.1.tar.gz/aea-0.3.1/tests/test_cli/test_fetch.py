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
"""This test module contains the tests for CLI Registry fetch methods."""

from unittest import TestCase, mock

from click import ClickException
from click.testing import CliRunner

from aea.cli import cli
from aea.cli.fetch import _fetch_agent_locally

from tests.conftest import CLI_LOG_OPTION
from tests.test_cli.tools_for_testing import ContextMock, PublicIdMock


def _raise_sys_exit(self, *args, **kwargs):
    raise SystemExit()


@mock.patch("aea.cli.fetch._add_item")
@mock.patch("aea.cli.fetch.copy_tree")
@mock.patch("aea.cli.fetch.os.path.join", return_value="joined-path")
@mock.patch("aea.cli.fetch._try_get_item_source_path", return_value="path")
@mock.patch("aea.cli.fetch.try_to_load_agent_config")
class FetchAgentLocallyTestCase(TestCase):
    """Test case for fetch_agent_locally method."""

    @mock.patch("aea.cli.fetch.os.path.exists", return_value=False)
    def test_fetch_agent_locally_positive(
        self,
        exists_mock,
        try_to_load_agent_config_mock,
        _try_get_item_source_path_mock,
        join_mock,
        copy_tree,
        add_item_mock,
    ):
        """Test for fetch_agent_locally method positive result."""
        _fetch_agent_locally(ContextMock(), PublicIdMock(), ContextMock())
        copy_tree.assert_called_once_with("path", "joined-path")

    @mock.patch("aea.cli.fetch.os.path.exists", return_value=True)
    def test_fetch_agent_locally_already_exists(self, *mocks):
        """Test for fetch_agent_locally method agent already exists."""
        with self.assertRaises(ClickException):
            _fetch_agent_locally(ContextMock(), PublicIdMock(), ContextMock())

    @mock.patch("aea.cli.fetch.os.path.exists", return_value=False)
    def test__fetch_agent_locally_with_deps_positive(self, *mocks):
        """Test for fetch_agent_locally method with deps positive result."""
        click_context_mock = ContextMock()
        public_id = PublicIdMock.from_str("author/name:0.1.0")
        ctx_mock = ContextMock(
            connections=[public_id],
            protocols=[public_id],
            skills=[public_id],
            contracts=[public_id],
        )
        _fetch_agent_locally(ctx_mock, PublicIdMock(), click_context_mock)

    @mock.patch("aea.cli.fetch.os.path.exists", return_value=False)
    def test__fetch_agent_locally_with_deps_sys_exit(self, *mocks):
        """Test for fetch_agent_locally method with deps system exit catch."""
        click_context_mock = ContextMock()
        click_context_mock.invoke = _raise_sys_exit
        ctx_mock = ContextMock(connections=["1"])
        _fetch_agent_locally(ctx_mock, PublicIdMock(), click_context_mock)


@mock.patch("aea.cli.fetch.fetch_agent")
@mock.patch("aea.cli.fetch._fetch_agent_locally")
class FetchCommandTestCase(TestCase):
    """Test case for CLI fetch command."""

    def setUp(self):
        """Set it up."""
        self.runner = CliRunner()

    def test_fetch_positive(self, *mocks):
        """Test for CLI push connection positive result."""
        self.runner.invoke(
            cli, [*CLI_LOG_OPTION, "fetch", "author/name:0.1.0"], standalone_mode=False,
        )
        self.runner.invoke(
            cli,
            [*CLI_LOG_OPTION, "fetch", "--local", "author/name:0.1.0"],
            standalone_mode=False,
        )
