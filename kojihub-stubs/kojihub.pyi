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
Koji Hub - typing stubs

Typing annotations stub for kojihub

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from koji import ParameterError
from koji_types import (
    BuildInfo, BuildNVR, CGInfo, ChecksumType, QueryOptions, RepoInfo,
    RPMInfo, RPMNVRA, RPMSignature, TagGroupInfo, TagFullInheritance,
    TagFullInheritanceEntry, TagInheritance, TaskState, UserInfo,
    UserStatus, )
from koji_types.arch import Arch
from koji_types.protocols import ClientSession
from logging import Logger
from typing import (
    Any, Callable, Dict, List, Literal, Optional, Tuple, Type,
    TypeVar, Union, overload, )


NUMERIC_TYPES: Tuple[Type, ...]

logger: Logger


class MultiSum:

    def __init__(
            self,
            checksum_types: List[ChecksumType]):
        ...

    def update(self, buf: bytes) -> None:
        ...

    def to_hexdigest(self) -> Dict[ChecksumType, str]:
        ...


class RootExports(ClientSession):
    ...


class Task:

    fields: Tuple[Tuple[str, str], ...]
    id: int
    logger: Logger

    def __init__(
            self,
            id: Any):
        ...

    def _close(
            self,
            result: Any,
            state: TaskState) -> bool:
        ...

    def _split_fields(
            self,
            fields: Optional[Tuple[Tuple[str, str], ...]] = None) \
            -> Tuple[List[str], List[str]]:
        ...

    def assertHost(
            self,
            host_id: int) -> None:
        ...

    def assertOwner(
            self,
            user_id: Optional[int] = None) -> None:
        ...

    def free(self) -> bool:
        ...

    def getOwner(self) -> int:
        ...

    def lock(
            self,
            host_id: int,
            newstate: str = 'OPEN',
            force: bool = False) -> bool:
        ...

    def open(
            self,
            host_id: int) -> Optional[Dict[str, Any]]:
        ...

    def setPriority(
            self,
            priority: int,
            recurse: bool = False) -> None:
        ...

    def setWeight(
            self,
            weight: float) -> None:
        ...

    def verifyHost(
            self,
            host_id: Optional[int] = None) -> bool:
        ...


# === functions ===


def _delete_event_id() -> None:
    ...


def _promote_build(
        build: Union[str, int],
        force: bool = False) -> BuildInfo:
    ...


def _scan_sighdr(
        sighdr: bytes,
        fn: str) -> Tuple[str, str]:
    ...


def _writeInheritanceData(
        tag_id: int,
        changes: TagInheritance,
        clear: bool = False) -> None:
    ...


def add_host_to_channel(
        hostname: str,
        channel_name: str,
        create: bool = False,
        force: bool = False) -> None:
    ...


def add_rpm_sig(
        an_rpm: str,
        sighdr: bytes) -> None:
    ...


def calculate_chsum(
        path: str,
        checksum_types: List[ChecksumType]) -> Dict[ChecksumType, str]:
    ...


def check_noarch_rpms(
        basepath: str,
        rpms: List[str],
        logs: Optional[Dict[Arch, List[str]]]) -> List[str]:
    ...


def check_rpm_sig(
        an_rpm: str,
        sigkey: str,
        sighdr: bytes) -> None:
    ...


_CVT = TypeVar("_CVT")

def convert_value(
        value: Any,
        cast: _CVT,
        message: Optional[str] = None,
        exc_type: Type[BaseException] = ParameterError,
        none_allowed: bool = False,
        check_only: bool = False) -> Optional[_CVT]:
    ...


def create_rpm_checksum(
        rpm_id: int,
        sigkey: str,
        chsum_dict: Dict[ChecksumType, str]) -> None:
    ...


def delete_rpm_sig(
        rpminfo: Union[int, str, RPMNVRA],
        sigkey: Optional[str],
        all_sigs: bool = False) -> None:
    ...


def draft_clause(
        draft: bool,
        table: Optional[str] = None) -> str:
    ...


def edit_channel(
        channelInfo: Union[int, str],
        **kw) -> bool:
    ...


def get_active_repos() -> List[RepoInfo]:
    ...


def get_tag_groups(
        tag: Union[int, str],
        event: Optional[int] = None,
        inherit: bool = True,
        incl_pkgs: bool = True,
        incl_reqs: bool = True) -> TagGroupInfo:
    ...


def get_verify_class(
        verify: Optional[ChecksumType]) -> Optional[Callable]:
    ...


def handle_upload(
        environ: Dict[str, Any]) -> Dict[str, Any]:
    ...


def importImageInternal(
        task_id: int,
        build_info: BuildInfo,
        imgdata: Dict[str, Any]) -> None:
    ...


def list_cgs() -> Dict[str, CGInfo]:
    ...


def log_error(
        msg: str) -> None:
    ...


def query_rpm_sigs(
        rpm_id: Union[int, str, BuildNVR, None] = None,
        sigkey: Optional[str] = None,
        queryOpts: Optional[QueryOptions] = None) -> List[RPMSignature]:
    ...


def readFullInheritance(
        tag_id: int,
        event: Optional[int] = None,
        reverse: bool = False) -> TagFullInheritance:
    ...


def readFullInheritanceRecurse(
        tag_id: int,
        event: int,
        order: TagFullInheritance,
        top: TagFullInheritanceEntry,
        hist: Dict[int, TagFullInheritance],
        currdepth: int,
        maxdepth: int,
        noconfig: bool,
        pfilter: List[str],
        reverse: bool) -> TagFullInheritance:
    ...


def recycle_build(
        old: BuildInfo,
        data: BuildInfo) -> None:
    ...


@overload
def reject_draft(
        data: BuildInfo,
        *,
        error: Optional[Type[BaseException]] = None) -> None:
    ...


@overload
def reject_draft(
        data: BuildInfo,
        is_rpm: Literal[False],
        error: Optional[Type[BaseException]] = None) -> None:
    ...


@overload
def reject_draft(
        data: RPMInfo,
        is_rpm: Literal[True],
        error: Optional[Type[BaseException]] = None) -> None:
    ...


@overload
def reject_draft(
        data: Union[BuildInfo, RPMInfo],
        is_rpm: bool = False,
        error: Optional[Type[BaseException]] = None) -> None:
    ...


def remove_host_from_channel(
        hostname: str,
        channel_name: str) -> None:
    ...


def rename_channel(
        old: str,
        new: str) -> None:
    ...


def rpmdiff(
        basepath: str,
        rpmlist: List[str],
        hashes: Dict[int, Dict[str, str]]) -> None:
    ...


def set_host_enabled(
        hostname: str,
        enabled: bool = True) -> None:
    ...


def set_tag_update(
        tag_id: int,
        utype: int,
        event_id: Optional[int] = None,
        user_id: Optional[int] = None) -> None:
    ...


def set_user_status(
        user: UserInfo,
        status: UserStatus) -> None:
    ...


def tag_changed_since_event(
        event: int,
        taglist: List[int]) -> bool:
    ...


def tag_notification(
        is_successful: bool,
        tag_id: int,
        from_id: int,
        build_id: int,
        user_id: int,
        ignore_success: bool = False,
        failure_msg: str = '') -> None:
    ...


def untagged_builds(
        name: Optional[str] = None,
        queryOpts: Optional[QueryOptions] = None,
        draft: Optional[bool] = None) -> List[BuildNVR]:
    ...


def verify_host_name(
        name: str) -> None:
    ...


def verify_name_internal(
        name: str) -> None:
    ...


def verify_name_user(
        name: Optional[str] = None,
        krb: Optional[str] = None) -> None:
    ...


def write_signed_rpm(
        an_rpm: str,
        sigkey: str,
        force: bool = False) -> None:
    ...


def writeInheritanceData(
        tag_id: int,
        changes: TagInheritance,
        clear: bool = False) -> None:
    ...


def xform_user_krb(
        entry: UserInfo) -> UserInfo:
    ...


# The end.
