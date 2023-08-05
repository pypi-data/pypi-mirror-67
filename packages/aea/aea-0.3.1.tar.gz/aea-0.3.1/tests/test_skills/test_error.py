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
"""The test error skill module contains the tests of the error skill."""

import logging
import os
import time
from pathlib import Path
from threading import Thread

from aea.aea import AEA
from aea.crypto.fetchai import FETCHAI
from aea.crypto.ledger_apis import LedgerApis
from aea.crypto.wallet import Wallet
from aea.identity.base import Identity
from aea.mail.base import Envelope
from aea.protocols.default.message import DefaultMessage
from aea.protocols.default.serialization import DefaultSerializer
from aea.registries.resources import Resources
from aea.skills.base import SkillContext
from aea.skills.error.handlers import ErrorHandler

from packages.fetchai.connections.local.connection import LocalNode
from packages.fetchai.protocols.fipa.message import FipaMessage
from packages.fetchai.protocols.fipa.serialization import FipaSerializer

from ..conftest import CUR_PATH, _make_dummy_connection


class TestSkillError:
    """Test the skill: Error."""

    @classmethod
    def setup_class(cls):
        """Test the initialisation of the AEA."""
        cls.node = LocalNode()
        private_key_path = os.path.join(CUR_PATH, "data", "fet_private_key.txt")
        cls.wallet = Wallet({FETCHAI: private_key_path})
        cls.ledger_apis = LedgerApis({}, FETCHAI)
        cls.agent_name = "Agent0"

        cls.connection = _make_dummy_connection()
        cls.connections = [cls.connection]
        cls.identity = Identity(cls.agent_name, address=cls.wallet.addresses[FETCHAI])
        cls.address = cls.identity.address
        cls.my_aea = AEA(
            cls.identity,
            cls.connections,
            cls.wallet,
            cls.ledger_apis,
            timeout=2.0,
            resources=Resources(str(Path(CUR_PATH, "data/dummy_aea"))),
        )
        cls.skill_context = SkillContext(cls.my_aea._context)
        logger_name = "aea.{}.skills.{}.{}".format(
            cls.my_aea._context.agent_name, "fetchai", "error"
        )
        cls.skill_context._logger = logging.getLogger(logger_name)
        cls.my_error_handler = ErrorHandler(
            name="error", skill_context=cls.skill_context
        )
        cls.t = Thread(target=cls.my_aea.start)
        cls.t.start()
        time.sleep(0.5)

    def test_error_handler_handle(self):
        """Test the handle function."""
        msg = FipaMessage(
            message_id=1,
            dialogue_reference=(str(0), ""),
            target=0,
            performative=FipaMessage.Performative.ACCEPT,
        )
        msg.counterparty = "a_counterparty"
        self.my_error_handler.handle(message=msg)

    def test_error_skill_unsupported_protocol(self):
        """Test the unsupported error message."""
        msg = FipaMessage(
            message_id=1,
            dialogue_reference=(str(0), ""),
            target=0,
            performative=FipaMessage.Performative.ACCEPT,
        )
        msg_bytes = FipaSerializer().encode(msg)
        envelope = Envelope(
            to=self.address,
            sender=self.address,
            protocol_id=FipaMessage.protocol_id,
            message=msg_bytes,
        )

        self.my_error_handler.send_unsupported_protocol(envelope)

        envelope = self.my_aea.inbox.get(block=True, timeout=1.0)
        msg = DefaultSerializer().decode(envelope.message)
        assert msg.performative == DefaultMessage.Performative.ERROR
        assert msg.error_code == DefaultMessage.ErrorCode.UNSUPPORTED_PROTOCOL

    def test_error_decoding_error(self):
        """Test the decoding error."""
        msg = FipaMessage(
            message_id=1,
            dialogue_reference=(str(0), ""),
            target=0,
            performative=FipaMessage.Performative.ACCEPT,
        )
        msg_bytes = FipaSerializer().encode(msg)
        envelope = Envelope(
            to=self.address,
            sender=self.address,
            protocol_id=DefaultMessage.protocol_id,
            message=msg_bytes,
        )

        self.my_error_handler.send_decoding_error(envelope)

        envelope = self.my_aea.inbox.get(block=True, timeout=1.0)
        msg = DefaultSerializer().decode(envelope.message)
        assert msg.performative == DefaultMessage.Performative.ERROR
        assert msg.error_code == DefaultMessage.ErrorCode.DECODING_ERROR

    def test_error_unsupported_skill(self):
        """Test the unsupported skill."""
        msg = FipaMessage(
            message_id=1,
            dialogue_reference=(str(0), ""),
            target=0,
            performative=FipaMessage.Performative.ACCEPT,
        )
        msg_bytes = FipaSerializer().encode(msg)
        envelope = Envelope(
            to=self.address,
            sender=self.address,
            protocol_id=DefaultMessage.protocol_id,
            message=msg_bytes,
        )

        self.my_error_handler.send_unsupported_skill(envelope=envelope)

        envelope = self.my_aea.inbox.get(block=True, timeout=1.0)
        msg = DefaultSerializer().decode(envelope.message)
        assert msg.performative == DefaultMessage.Performative.ERROR
        assert msg.error_code == DefaultMessage.ErrorCode.UNSUPPORTED_SKILL

    @classmethod
    def teardown_class(cls):
        """Teardown method."""
        cls.my_aea.stop()
        cls.t.join()
