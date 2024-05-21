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
Koji Plugin Types - typing declatations for koji data structures

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from typing import TYPE_CHECKING, Callable


if TYPE_CHECKING:
    from typing_extensions import Protocol
else:
    Protocol = object


__all__ = (
    "CallbackHandler",
    "CallbackProtocol",
)


CallbackHandler = Callable[[str, ...], None]


class CallbackProtocol(Protocol):

    def __call__(
            self,
            cbtype: str,
            *args, **kwargs) -> None:
        ...


# The end.
