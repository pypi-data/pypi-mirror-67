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

"""This module contains the strategy class."""

import os
import time
from typing import Any, Dict, List, Tuple, cast

from aea.helpers.search.models import Description, Query
from aea.mail.base import Address
from aea.skills.base import Model

from packages.fetchai.skills.carpark_detection.carpark_detection_data_model import (
    CarParkDataModel,
)
from packages.fetchai.skills.carpark_detection.detection_database import (
    DetectionDatabase,
)

DEFAULT_SELLER_TX_FEE = 0
DEFAULT_PRICE = 2000
DEFAULT_DB_IS_REL_TO_CWD = False
DEFAULT_DB_REL_DIR = "temp_files_placeholder"
DEFAULT_CURRENCY_ID = "FET"
DEFAULT_LEDGER_ID = "fetchai"


class Strategy(Model):
    """This class defines a strategy for the agent."""

    def __init__(self, **kwargs) -> None:
        """
        Initialize the strategy of the agent.

        :param register_as: determines whether the agent registers as seller, buyer or both
        :param search_for: determines whether the agent searches for sellers, buyers or both

        :return: None
        """
        db_is_rel_to_cwd = (
            kwargs.pop("db_is_rel_to_cwd")
            if "db_is_rel_to_cwd" in kwargs.keys()
            else DEFAULT_DB_IS_REL_TO_CWD
        )
        db_rel_dir = (
            kwargs.pop("db_rel_dir")
            if "db_rel_dir" in kwargs.keys()
            else DEFAULT_DB_REL_DIR
        )

        if db_is_rel_to_cwd:
            db_dir = os.path.join(os.getcwd(), db_rel_dir)
        else:
            db_dir = os.path.join(os.path.dirname(__file__), DEFAULT_DB_REL_DIR)

        self.data_price = kwargs.pop("data_price", DEFAULT_PRICE)

        self.currency_id = kwargs.pop("currency_id", DEFAULT_CURRENCY_ID)

        self.ledger_id = kwargs.pop("ledger_id", DEFAULT_LEDGER_ID)

        self.data_price_fet = (
            kwargs.pop("data_price_fet")
            if "data_price_fet" in kwargs.keys()
            else DEFAULT_PRICE
        )
        self.currency_id = (
            kwargs.pop("currency_id")
            if "currency_id" in kwargs.keys()
            else DEFAULT_CURRENCY_ID
        )
        self.ledger_id = (
            kwargs.pop("ledger_id")
            if "ledger_id" in kwargs.keys()
            else DEFAULT_LEDGER_ID
        )
        self._seller_tx_fee = kwargs.pop("seller_tx_fee", DEFAULT_SELLER_TX_FEE)

        super().__init__(**kwargs)

        self.db = DetectionDatabase(db_dir, False)

        balance = self.context.ledger_apis.token_balance(
            self.ledger_id, cast(str, self.context.agent_addresses.get(self.ledger_id))
        )
        self.db.set_system_status(
            "ledger-status", self.context.ledger_apis.last_tx_statuses[self.ledger_id]
        )

        if not os.path.isdir(db_dir):
            self.context.logger.warning("Database directory does not exist!")

        self.record_balance(balance)
        self.other_carpark_processes_running = False

    def record_balance(self, balance):
        """Record current balance to database."""
        self.db.set_fet(balance, time.time())

    def has_service_description(self):
        """Return true if we have a description."""
        if not self.db.is_db_exits():
            return False

        lat, lon = self.db.get_lat_lon()
        if lat is None or lon is None:
            return False

        return True

    def get_service_description(self) -> Description:
        """
        Get the service description.

        :return: a description of the offered services
        """
        assert self.has_service_description()

        lat, lon = self.db.get_lat_lon()
        desc = Description(
            {
                "latitude": lat,
                "longitude": lon,
                "unique_id": self.context.agent_address,
            },
            data_model=CarParkDataModel(),
        )

        return desc

    def is_matching_supply(self, query: Query) -> bool:
        """
        Check if the query matches the supply.

        :param query: the query
        :return: bool indiciating whether matches or not
        """
        # TODO, this is a stub
        return True

    def has_data(self) -> bool:
        """Return whether we have any useful data to sell."""
        if not self.db.is_db_exits():
            return False

        data = self.db.get_latest_detection_data(1)
        return len(data) > 0

    def generate_proposal_and_data(
        self, query: Query, counterparty: Address
    ) -> Tuple[Description, Dict[str, List[Dict[str, Any]]]]:
        """
        Generate a proposal matching the query.

        :param counterparty: the counterparty of the proposal.
        :param query: the query
        :return: a tuple of proposal and the bytes of carpark data
        """
        tx_nonce = self.context.ledger_apis.generate_tx_nonce(
            identifier=self.ledger_id,
            seller=self.context.agent_addresses[self.ledger_id],
            client=counterparty,
        )

        assert self.db.is_db_exits()

        data = self.db.get_latest_detection_data(1)
        assert len(data) > 0

        del data[0]["raw_image_path"]
        del data[0]["processed_image_path"]

        assert (
            self.data_price_fet - self._seller_tx_fee > 0
        ), "This sale would generate a loss, change the configs!"

        last_detection_time = data[0]["epoch"]
        max_spaces = data[0]["free_spaces"] + data[0]["total_count"]
        proposal = Description(
            {
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
                "price": self.data_price,
                "currency_id": self.currency_id,
                "seller_tx_fee": self._seller_tx_fee,
                "ledger_id": self.ledger_id,
                "last_detection_time": last_detection_time,
                "max_spaces": max_spaces,
                "tx_nonce": tx_nonce if tx_nonce is not None else "",
            }
        )

        data[0]["price_fet"] = self.data_price
        data[0]["message_type"] = "car_park_data"

        return proposal, data[0]
