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
Koji Types for kojihub.db

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from . import QueryOptions


__all__ = (
    "QueryProcessorOptions",
)


class QueryProcessorOptions(QueryOptions):

    rowLock: bool

    group: str


# The end.
