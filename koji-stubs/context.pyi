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
Koji - typing stubs

Typing annotations stub for koji.context

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from typing import Any


context: ThreadLocal


class ThreadLocal:

    # Removed in koji 1.36
    # def __delattr__(self, key: str) -> None:
    #     ...
    #
    # def __getattr__(self, key: str) -> Any:
    #     ...
    #
    # def __setattr__(self, key: str, value: Any) -> None:
    #     ...

    def _threadclear(self) -> None:
        # :since: koji 1.36
        ...


# The end.
