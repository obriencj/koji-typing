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


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enum import Enum as StrEnum

else:
    try:
        from enum import StrEnum
    except ImportError:
        from enum import Enum as StrEnum


__all__ = (
    "Arch",
)


class Arch(StrEnum):
    noarch: str = "noarch"
    athlon: str = "athlon"
    i686: str = "i686"
    geode: str = "geode"
    i586: str = "i586"
    i486: str = "i486"
    i386: str = "i386"
    x86_64: str = "x86_64"
    amd64: str = "amd64"
    ia32e: str = "ia32e"
    ppc64le: str = "ppc64le"
    ppc64p7: str = "ppc64p7"
    ppc64pseries: str = "ppc64pseries"
    ppc64iseries: str = "ppc64iseries"
    ppc64: str = "ppc64"
    ppc: str = "ppc"
    s390x: str = "s390x"
    s390: str = "s390"
    sparc64v: str = "sparc64v"
    sparc64: str = "sparc64"
    sparcv9v: str = "sparcv9v"
    sparcv9: str = "sparcv9"
    sparcv8: str = "sparcv8"
    sparc: str = "sparc"
    alphaev7: str = "alphaev7"
    alphaev68: str = "alphaev68"
    alphaev67: str = "alphaev67"
    alphaev6: str = "alphaev6"
    alphapca56: str = "alphapca56"
    alphaev56: str = "alphaev56"
    alphaev5: str = "alphaev5"
    alphaev45: str = "alphaev45"
    alphaev4: str = "alphaev4"
    alpha: str = "alpha"
    armv7l: str = "armv7l"
    armv6l: str = "armv6l"
    armv5tejl: str = "armv5tejl"
    armv5tel: str = "armv5tel"
    armv7hnl: str = "armv7hnl"
    armv7hl: str = "armv7hl"
    armv6hl: str = "armv6hl"
    arm64: str = "arm64"
    sh4a: str = "sh4a"
    sh4: str = "sh4"
    sh3: str = "sh3"
    ia64: str = "ia64"


# The end.
