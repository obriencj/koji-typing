# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.


"""
Koji CLI Types - typing declatations for koji data structures

Python typing compatible definitions for the Koji dict types and
enumerations

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from . import GOptions

from koji import ClientSession
from typing import Callable, List, Protocol


try:
    from typing import Protocol  # noqa
except ImportError:
    # Python < 3.8 doesn't have typing.Protocol
    class Protocol:
        ...


__all__ = (
    "CLIHandler",
    "CLIProtocol",
)


CLIHandler = Callable[[GOptions, ClientSession, List[str]],
                      int]
"""
The callable signature used by Koji's CLI command handlers.
"""


class CLIProtocol(Protocol):
    """
    A Protocol variation on the `CLIHandler` callable definition.
    """

    def __call__(
            self,
            goptions: GOptions,
            session: ClientSession,
            args: List[str]) -> int:
        ...


# The end.