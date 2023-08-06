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
"""Wrapper for Pexpect to use in tests."""
import os
import sys
import time
from typing import List, Optional, Union

if os.name == "nt":

    class PexpectSpawn:
        def __init__(self, *args, **kwargs):
            pass

        def __getattr__(self, item):  # type: ignore
            return item


else:
    from pexpect import spawn  # type: ignore
    from pexpect.exceptions import TIMEOUT  # type: ignore

    class PexpectSpawn(spawn):  # type: ignore
        """Utility class to make aea cli test easier."""

        def __init__(self, *args, **kwargs):
            """Init pexpect.spawn."""
            kwargs["use_poll"] = True
            super().__init__(*args, **kwargs)

        def control_c(self) -> None:
            """Send control c to process started."""
            self.sendcontrol("c")

        @property
        def returncode(self) -> Optional[Union[int, str]]:
            """Get return code of finished process."""
            return self.exitstatus  # type: ignore

        def wait_to_complete(self, timeout: float = 5) -> None:
            """Wait process to complete.

            Terminate automatically after timeout.
            Set returncode to terminated if terminated.

            :param timeout: how many seconds wait process to finish before kill.
            """
            if self.exitstatus is not None:  # type: ignore
                return

            start_time = time.time()

            while start_time + timeout > time.time() and self.isalive():
                time.sleep(0.001)

            if self.isalive():
                self.terminate(force=True)
                self.wait()
                self.exitstatus = "Terminated!"
            else:
                self.wait()

        @classmethod
        def aea_cli(cls, args) -> "PexpectSpawn":
            """Start aea.cli.

            :param args: list of arguments for aea.cli.

            :return: PexpectSpawn
            """
            return cls(
                "python",
                ["-m", "aea.cli", "-v", "DEBUG", *args],
                env=os.environ.copy(),
                encoding="utf-8",
                logfile=sys.stdout,
            )

        def expect_all(self, pattern_list: List[str], timeout: float = 10) -> None:
            """
            Wait for all patterns appear in process output.

            :param pattern_list: list of string to expect
            :param timeout: timeout in seconds

            :return: None
            """
            pattern_list = list(pattern_list)

            start_time = time.time()
            while pattern_list:
                time_spent = time.time() - start_time
                if time_spent > timeout:
                    raise TIMEOUT(timeout)
                idx = self.expect_exact(pattern_list, timeout - time_spent)
                pattern_list.pop(idx)
