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
    ArchiveID, ArchiveInfo, BuildID, BuildInfo, BuildNVR,
    BuildrootReference, CGInfo,
    ChannelID, ChecksumType, EventID, NamedID, PackageID, PermID,
    QueryOptions,
    RepoInfo, RepoState, RPMInfo, RPMNVRA, RPMSignature, TagGroupInfo,
    TagFullInheritance, TagFullInheritanceEntry, TagID, TagInfo,
    TagInheritance, TargetID, TargetInfo, TaskID, TaskState,
    UserID, UserInfo,
    UserStatus, )
from koji_types.arch import Arch
from koji_types.protocols import ClientSession
from logging import Logger
from typing import (
    Any, Callable, Dict, Iterator, List, Literal, Optional, Tuple, Type,
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


def _edit_build_target(
        buildTargetInfo: Union[str, int],
        name: str,
        build_tag: Union[str, int],
        dest_tag: Union[str, int]) -> None:
    ...


def _get_build_target(
        task_id: TaskID) -> Optional[TargetInfo]:
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
        tag_id: TagID,
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


@overload
def apply_volume_policy(
        build: BuildInfo,
        strict: bool = False) -> None:
    ...


@overload
def apply_volume_policy(
        build: BuildInfo,
        strict: bool = False,
        *,
        dry_run: Literal[False]) -> None:
    ...


@overload
def apply_volume_policy(
        build: BuildInfo,
        strict: bool = False,
        *,
        dry_run: Literal[True]) -> str:
    ...


@overload
def apply_volume_policy(
        build: BuildInfo,
        strict: bool = False,
        dry_run: bool = False) -> Optional[str]:
    ...


def assert_cg(
        cg: str,
        user: Union[int, str, None] = None) -> None:
    ...


def calculate_chsum(
        path: str,
        checksum_types: List[ChecksumType]) -> Dict[ChecksumType, str]:
    ...


def cancel_build(
        build_id: Union[str, int],
        cancel_task: bool = True) -> bool:
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


def dist_repo_init(
        tag: Union[int, str],
        keys: List[str],
        task_opts: Dict[str, Any]) -> Tuple[int, int]:
    ...


def draft_clause(
        draft: bool,
        table: Optional[str] = None) -> str:
    ...


def edit_build_target(
        buildTargetInfo: Union[str, int],
        name: str,
        build_tag: Union[str, int],
        dest_tag: Union[str, int]) -> None:
    ...


def edit_channel(
        channelInfo: Union[int, str],
        **kw) -> bool:
    ...


def generate_token(
        nbytes: int = 32) -> str:
    ...


def get_active_repos() -> List[RepoInfo]:
    ...


def get_all_arches() -> List[Arch]:
    ...


def get_build_target(
        info: Union[str, int],
        event: Optional[int] = None,
        strict: bool = False) -> TargetInfo:
    ...


def get_build_targets(
        info: Union[str, int, None] = None,
        event: Optional[int] = None,
        buildTagID: Union[str, int, TagInfo, None] = None,
        destTagID: Union[str, int, TagInfo, None] = None,
        queryOpts: Optional[QueryOptions] = None) -> List[TargetInfo]:
    ...


def get_id(
        table: str,
        info: Union[str, int, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[int]:
    ...


def get_maven_build(
        buildInfo: Union[int, str],
        strict: bool = False) -> Dict[str, Any]:
    # TODO: need a return typedict
    ...


def get_package_id(
        info: Union[str, PackageID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[int]:
    ...


def get_perm_id(
        info: Union[str, PermID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[int]:
    ...


def get_tag_groups(
        tag: Union[int, str],
        event: Optional[int] = None,
        inherit: bool = True,
        incl_pkgs: bool = True,
        incl_reqs: bool = True) -> TagGroupInfo:
    ...


def get_tag_id(
        info: Union[int, str, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[int]:
    ...


def get_upload_path(
        reldir: str,
        name: str,
        create: bool = False,
        volume: Optional[str] = None) -> str:
    ...


def get_user(
        userInfo: Union[int, str, None],
        strict: bool = False,
        krb_princs: bool = True,
        groups: bool = False) -> UserInfo:
    ...


def get_verify_class(
        verify: Optional[ChecksumType]) -> Optional[Callable]:
    ...


def get_win_build(
        buildInfo: Union[int, str],
        strict: bool = False) -> Dict[str, Any]:
    # TODO: need a return typedict
    ...


@overload
def grant_cg_access(
        user: Union[str, int],
        cg: Union[str, int]) -> None:
    ...


@overload
def grant_cg_access(
        user: Union[str, int],
        cg: Union[str, int],
        create: Literal[False]) -> None:
    ...


@overload
def grant_cg_access(
        user: Union[str, int],
        cg: str,
        create: Literal[True]) -> None:
    ...


@overload
def grant_cg_access(
        user: Union[str, int],
        cg: Union[str, int],
        create: bool = False) -> None:
    ...


def handle_upload(
        environ: Dict[str, Any]) -> Dict[str, Any]:
    ...


def import_archive(
        filepath: str,
        buildinfo: BuildInfo,
        type: str,
        typeInfo: Dict[str, Any],
        buildroot_id: Optional[int] = None) -> ArchiveInfo:
    ...


def import_archive_internal(
        filepath: str,
        buildinfo: BuildInfo,
        type: str,
        typeInfo: Dict[str, Any],
        buildroot_id: Optional[int] = None,
        fileinfo: Optional[Dict[str, Any]] = None) -> ArchiveInfo:
    ...


def import_build_log(
        fn: str,
        buildinfo: Optional[BuildInfo] = None,
        subdir: Optional[str] = None) -> None:
    ...


def import_rpm(
        fn: str,
        buildinfo: Optional[BuildInfo] = None,
        brootid: Optional[int] = None,
        wrapper: bool = False,
        fileinfo: Optional[Dict[str, Any]] = None) -> RPMInfo:
    ...


def importImageInternal(
        task_id: TaskID,
        build_info: BuildInfo,
        imgdata: Dict[str, Any]) -> None:
    ...


def list_cgs() -> Dict[str, CGInfo]:
    ...


def log_error(
        msg: str) -> None:
    ...


def lookup_channel(
        info: Union[str, ChannelID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[NamedID]:
    ...


def lookup_name(
        table: str,
        info: Union[str, int, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[NamedID]:
    ...


def lookup_package(
        info: Union[str, PackageID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[NamedID]:
    ...


def lookup_perm(
        info: Union[str, PermID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[NamedID]:
    ...


def lookup_tag(
        info: Union[str, TaskID, Dict[str, Any]],
        strict: bool = False,
        create: bool = False) -> Optional[NamedID]:
    ...


def maven_tag_archives(
        tag_id: TagID,
        event_id: Optional[EventID] = None,
        inherit: bool = True) -> Iterator[ArchiveInfo]:
    ...


NameOrID = TypeVar("NameOrID", str, int)


@overload
def name_or_id_clause(
        table: str,
        info: NameOrID) -> Tuple[str, Dict[str, NameOrID]]:
    ...


@overload
def name_or_id_clause(
        table: str,
        info: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    ...


def new_build(
        data: Dict[str, Any],
        strict: bool = False) -> BuildID:
    ...


def new_image_build(
        build_info: BuildInfo) -> None:
    ...


def new_typed_build(
        build_info: BuildInfo,
        btype: str) -> None:
    ...


def parse_json(
        value: Optional[str],
        desc: Optional[str] = None,
        errstr: Optional[str] = None) -> Any:
    ...


def query_rpm_sigs(
        rpm_id: Union[int, str, BuildNVR, None] = None,
        sigkey: Optional[str] = None,
        queryOpts: Optional[QueryOptions] = None) -> List[RPMSignature]:
    ...


def readFullInheritance(
        tag_id: TagID,
        event: Optional[EventID] = None,
        reverse: bool = False) -> TagFullInheritance:
    ...


def readFullInheritanceRecurse(
        tag_id: TagID,
        event: EventID,
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


def remove_external_repo_from_tag(
        tag_info: Union[str, TagID],
        repo_info: int) -> None:
    ...


def remove_host_from_channel(
        hostname: str,
        channel_name: str) -> None:
    ...


def remove_volume(
        volume: str) -> None:
    ...


def rename_channel(
        old: str,
        new: str) -> None:
    ...


def repo_delete(
        repo_id: int) -> int:
    ...


def repo_expire(
        repo_id: int) -> None:
    ...


def repo_expire_older(
        tag_id: TagID,
        event_id: EventID,
        dist: Optional[bool] = None) -> None:
    ...


def repo_info(
        repo_id: int,
        strict: bool = False) -> RepoInfo:
    ...


def repo_init(
        tag: Union[str, TagID],
        task_id: Optional[TaskID] = None,
        with_src: bool = False,
        with_debuginfo: bool = False,
        event: Optional[EventID] = None,
        with_separate_src: bool = False) -> Tuple[int, int]:
    ...


def repo_problem(
        repo_id: int) -> None:
    ...


def repo_ready(
        repo_id: int) -> None:
    ...


def repo_references(
        repo_id: int) -> List[BuildrootReference]:
    ...


def repo_set_state(
        repo_id: int,
        state: RepoState,
        check: bool = True) -> None:
    ...


def reset_build(
        build: Union[str, BuildID]) -> None:
    ...


def revoke_cg_access(
        user: Union[str, UserID],
        cg: Union[str, int]) -> None:
    ...


def rpmdiff(
        basepath: str,
        rpmlist: List[str],
        hashes: Dict[int, Dict[str, str]]) -> None:
    ...


def set_channel_enabled(
        channelname: str,
        enabled: bool = True,
        comment: Optional[str] = None) -> None:
    ...


def set_host_enabled(
        hostname: str,
        enabled: bool = True) -> None:
    ...


def set_tag_update(
        tag_id: TagID,
        utype: int,
        event_id: Optional[EventID] = None,
        user_id: Optional[UserID] = None) -> None:
    ...


def set_user_status(
        user: UserInfo,
        status: UserStatus) -> None:
    ...


def tag_changed_since_event(
        event: EventID,
        taglist: List[int]) -> bool:
    ...


def tag_notification(
        is_successful: bool,
        tag_id: TagID,
        from_id: int,
        build_id: BuildID,
        user_id: UserID,
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
        tag_id: TagID,
        changes: TagInheritance,
        clear: bool = False) -> None:
    ...


def xform_user_krb(
        entry: UserInfo) -> UserInfo:
    ...


# The end.
