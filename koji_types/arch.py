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
Koji Types - Architectures

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from enum import StrEnum, auto


__all__ = (
    "Arch",
)


class Arch(StrEnum):
    noarch = auto()

    athlon = auto()
    i686 = auto()
    geode = auto()
    i586 = auto()
    i486 = auto()
    i386 = auto()

    x86_64 = auto()
    amd64 = auto()
    ia32e = auto()

    ppc64le = auto()

    ppc64p7 = auto()
    ppc64pseries = auto()
    ppc64iseries = auto()
    ppc64 = auto()
    ppc = auto()

    s390x = auto()
    s390 = auto()

    sparc64v = auto()
    sparc64 = auto()
    sparcv9v = auto()
    sparcv9 = auto()
    sparcv8 = auto()
    sparc = auto()

    alphaev7 = auto()
    alphaev68 = auto()
    alphaev67 = auto()
    alphaev6 = auto()
    alphapca56 = auto()
    alphaev56 = auto()
    alphaev5 = auto()
    alphaev45 = auto()
    alphaev4 = auto()
    alpha = auto()

    armv7l = auto()
    armv6l = auto()
    armv5tejl = auto()
    armv5tel = auto()

    armv7hnl = auto()
    armv7hl = auto()
    armv6hl = auto()

    arm64 = auto()

    sh4a = auto()
    sh4 = auto()
    sh3 = auto()

    ia64 = auto()


# The end.
