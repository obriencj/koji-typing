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

Typing annotations stub for koji.arch

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""  # noqa: Y021


from koji_types.arch import Arch
from typing import Dict, List, Tuple, Optional


arches: Dict[Arch, Arch]
multilibArches: Dict[Arch, Tuple[Arch, ...]]


def archDifference(
        myarch: Arch,
        targetarch: Arch) -> int:
    ...


def canCoinstall(
        arch1: Arch,
        arch2: Arch) -> bool:
    ...


def getArchList(
        thisarch: Optional[Arch] = None) -> List[Arch]:
    ...


def getBestArchFromList(
        archlist: List[Arch],
        myarch: Optional[Arch] = None) -> Arch:
    ...


def isMultiLibArch(
        arch: Optional[Arch] = None) -> bool:
    ...


def legitMultiArchesInSameLib(
        arch: Arch) -> List[Arch]:
    ...


def score(
        arch: Arch) -> int:
    ...


# The end.
