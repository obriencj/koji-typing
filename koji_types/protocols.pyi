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
Koji Types - Client Session Protocol method declarations

:author: Christopher O'Brien <obriencj@gmail.com>
:license: GPL v3
"""


from . import (
    ArchiveInfo, ArchiveTypeInfo, BuildID, BuildInfo, BuildNVR,
    BuildrootID, BuildrootInfo,
    BuildState, BTypeInfo, ChangelogEntry, ChannelInfo,
    CGID, CGInfo, CGInitInfo,
    EventID, EventInfo,
    FaultInfo, HostInfo, ListTasksOptions, MavenInfo,
    PackageID, PackageInfo,
    PermInfo, POMInfo, QueryOptions, RepoInfo, RepoState, RPMInfo,
    RPMSignature, RPMSigTag, SearchResult, SessionInfo, TagBuildInfo,
    TagID, TagInfo, TagGroupInfo, TagInheritance, TagPackageInfo,
    TargetID, TargetInfo,
    TaskID, TaskInfo, UserGroup, UserID, UserInfo, UserType, )
from .arch import Arch

from datetime import datetime
from koji import VirtualCall
from typing import (
    Any, Dict, List, Literal, NoReturn, Optional, Tuple,
    Union, overload, )
from typing_extensions import Protocol
from preoccupied.proxytype import proxytype


class ClientSession(Protocol):

    def build(
            self,
            src: str,
            target: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None,
            channel: Optional[str] = None) -> int:
        ...

    def buildImage(
            self,
            name: str,
            version: str,
            arch: Arch,
            target: str,
            ksfile: str,
            img_type: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None) -> int:
        ...

    def chainBuild(
            self,
            srcs: List[str],
            target: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None,
            channel: Optional[str] = None) -> int:
        ...

    def chainMaven(
            self,
            builds: List[Dict[str, Any]],
            target: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None,
            channel: str = 'maven') -> int:
        ...

    def count(
            self,
            methodName: str,
            *args: Any,
            **kw: Any) -> int:
        ...

    def createTag(
            self,
            name: str,
            parent: Optional[Union[int, str]] = None,
            arches: Optional[str] = None,
            perm: Optional[str] = None,
            locked: bool = False,
            maven_support: bool = False,
            maven_include_all: bool = False,
            extra: Optional[Dict[str, str]] = None) -> int:
        ...

    def disableUser(
            self,
            username: Union[int, str]) -> None:
        ...

    def echo(self, *args) -> List:
        ...

    def editTag2(
            self,
            taginfo: Union[int, str],
            **kwargs) -> None:
        ...

    def enableUser(
            self,
            username: Union[int, str]) -> None:
        ...

    def error(self) -> NoReturn:
        ...

    def exclusiveSession(self, *args, **kwargs) -> None:
        ...

    def failBuild(self, task_id: int, build_id: int) -> None:
        ...

    def fault(self) -> NoReturn:
        ...

    def getAllPerms(self) -> List[PermInfo]:
        ...

    def getAPIVersion(self) -> int:
        ...

    def getArchive(
            self,
            archive_id: int,
            strict: bool = False) -> ArchiveInfo:
        ...

    def getArchiveType(
            self,
            filename: Optional[str] = None,
            type_name: Optional[str] = None,
            type_id: Optional[int] = None,
            strict: bool = False) -> ArchiveTypeInfo:
        ...

    def getArchiveTypes(self) -> List[ArchiveTypeInfo]:
        ...

    def getBuild(
            self,
            buildInfo: Union[int, str],
            strict: bool = False) -> BuildInfo:
        ...

    def getBuildTarget(
            self,
            info: Union[int, str],
            event: Optional[int] = None,
            strict: bool = False) -> TargetInfo:
        ...

    def getBuildTargets(
            self,
            info: Optional[Union[int, str]] = None,
            event: Optional[int] = None,
            buildTagID: Optional[int] = None,
            destTagID: Optional[int] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[TargetInfo]:
        ...

    def getBuildType(
            self,
            buildInfo: Union[int, str],
            strict: bool = False) -> Dict[str, dict]:
        ...

    def getBuildroot(
            self,
            buildrootID: int,
            strict: bool = False) -> BuildrootInfo:
        ...

    def getChangelogEntries(
            self,
            buildID: Optional[int] = None,
            taskID: Optional[int] = None,
            filepath: Optional[str] = None,
            author: Optional[str] = None,
            before: Union[datetime, str, int, None] = None,
            after: Union[datetime, str, int, None] = None,
            queryOpts: Optional[QueryOptions] = None,
            strict: bool = False) -> List[ChangelogEntry]:
        ...

    def getChannel(
            self,
            channelInfo: Union[int, str],
            strict: bool = False) -> ChannelInfo:
        ...

    def getEvent(
            self,
            id: int) -> EventInfo:
        ...

    def getLastEvent(
            self,
            before: Union[int, float, None] = None) -> EventInfo:
        ...

    def getFullInheritance(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            reverse: bool = False) -> TagInheritance:
        ...

    def getGroupMembers(
            self,
            group: Union[int, str]) -> List[UserInfo]:
        ...

    def getUserGroups(
            self,
            user: Union[int, str]) -> List[UserGroup]:
        # :since: koji 1.35
        ...

    def getHost(
            self,
            hostInfo: Union[int, str],
            strict: bool = False,
            event: Optional[int] = None) -> HostInfo:
        ...

    def getInheritanceData(
            self,
            tag: Union[int, str],
            event: Optional[int] = None) -> TagInheritance:
        ...

    def getKojiVersion(self) -> str:
        # :since: koji 1.23
        ...

    @overload
    def getLastHostUpdate(
            self,
            hostID: int) -> Union[str, None]:
        ...

    @overload
    def getLastHostUpdate(
            self,
            hostID: int,
            ts: Literal[False]) -> Union[str, None]:
        ...

    @overload
    def getLastHostUpdate(
            self,
            hostID: int,
            ts: Literal[True]) -> Union[float, None]:
        ...

    @overload
    def getLastHostUpdate(
            self,
            hostID: int,
            ts: bool = False) -> Union[str, float, None]:
        ...

    def getLatestBuilds(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            package: Optional[Union[int, str]] = None,
            type: Optional[str] = None) -> List[TagBuildInfo]:
        ...

    def getLatestMavenArchives(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            inherit: bool = True) -> List[ArchiveInfo]:
        ...

    def getLatestRPMS(
            self,
            tag: Union[int, str],
            package: Optional[Union[int, str]] = None,
            arch: Optional[str] = None,
            event: Optional[int] = None,
            rpmsigs: bool = False,
            type: Optional[str] = None) -> Tuple[List[RPMInfo],
                                                 List[BuildInfo]]:
        ...

    def getLoggedInUser(self) -> UserInfo:
        ...

    def getPackage(
            self,
            info: Union[int, str],
            strict: bool = False,
            create: bool = False) -> PackageInfo:
        ...

    def getPerms(self) -> List[str]:
        ...

    def getRepo(
            self,
            tag: Union[int, str],
            state: Optional[RepoState] = None,
            event: Optional[int] = None,
            dist: bool = False) -> RepoInfo:
        ...

    @overload
    def getRPM(
            self,
            rpminfo: Union[int, str],
            strict: bool = False) -> RPMInfo:
        ...

    @overload
    def getRPM(
            self,
            rpminfo: Union[int, str],
            strict: bool = False,
            *,
            multi: Literal[False]) -> RPMInfo:
        ...

    @overload
    def getRPM(
            self,
            rpminfo: Union[int, str],
            strict: bool = False,
            *,
            multi: Literal[True]) -> List[RPMInfo]:
        ...

    @overload
    def getRPM(
            self,
            rpminfo: Union[int, str],
            strict: bool = False,
            multi: bool = False) -> Union[RPMInfo, List[RPMInfo]]:
        ...

    @overload
    def getRPMHeaders(
            self,
            rpmID: Optional[int] = None,
            taskID: Optional[TaskID] = None,
            filepath: Optional[str] = None,
            headers: Optional[List[str]] = None) -> Dict[str, Any]:
        ...

    @overload
    def getRPMHeaders(
            self,
            rpmID: Optional[int] = None,
            taskID: Optional[TaskID] = None,
            filepath: Optional[str] = None,
            headers: Optional[List[str]] = None,
            strict: Optional[bool] = False) -> Dict[str, Any]:
        # :since: koji 1.29.0
        ...

    def getSessionInfo(
            self,
            details: bool = False,
            user_id: Optional[UserID] = None) -> Union[None, SessionInfo,
                                                       List[SessionInfo]]:
        ...

    def getTag(
            self,
            taginfo: Union[str, TagID],
            strict: bool = False,
            event: Optional[int] = None,
            blocked: bool = False) -> TagInfo:
        ...

    def getTagGroups(
            self,
            tag: Union[str, TagID],
            event: Optional[EventID] = None,
            inherit: bool = True,
            incl_pkgs: bool = True,
            incl_reqs: bool = True,
            incl_blocked: bool = False) -> List[TagGroupInfo]:
        ...

    def getTaskChildren(
            self,
            task_id: TaskID,
            request: Optional[bool] = False,
            strict: Optional[bool] = False) -> List[TaskInfo]:
        ...

    @overload
    def getTaskInfo(
            self,
            task_id: List[TaskID],
            request: bool = False,
            strict: bool = False) -> List[TaskInfo]:
        ...

    @overload
    def getTaskInfo(
            self,
            task_id: TaskID,
            request: bool = False,
            strict: bool = False) -> TaskInfo:
        ...

    @overload
    def getUser(
            self,
            userInfo: Union[str, UserID, None] = None,
            strict: bool = False,
            krb_princs: bool = True) -> UserInfo:
        ...

    @overload
    def getUser(
            self,
            userInfo: Union[str, UserID, None] = None,
            strict: bool = False,
            krb_princs: bool = True,
            groups: bool = False) -> UserInfo:
        # :since: koji 1.34
        ...

    @overload
    def getUserPerms(
            self,
            userID: Union[str, UserID, None] = None) -> List[str]:
        ...

    @overload
    def getUserPerms(
            self,
            userID: Union[str, UserID, None] = None,
            with_groups: bool = True) -> List[str]:
        # :since: koji 1.34
        ...

    def getUserPermsInheritance(
            self,
            userID: Union[str, UserID]) -> Dict[str, List[str]]:
        # :since: koji 1.34
        ...

    def hasPerm(
            self,
            perm: str,
            strict: bool = False) -> bool:
        ...

    def hello(
            self,
            *args) -> str:
        ...

    @property
    def host(self) -> Host:
        ...

    def initWinBuild(
            self,
            task_id: TaskID,
            build_info: BuildNVR,
            win_info: Dict[str, Any]) -> None:
        ...

    def listArchives(
            self,
            buildID: Optional[BuildID] = None,
            buildrootID: Optional[BuildrootID] = None,
            componentBuildrootID: Optional[BuildrootID] = None,
            hostID: Optional[int] = None,
            type: Optional[str] = None,
            filename: Optional[str] = None,
            size: Optional[int] = None,
            checksum: Optional[str] = None,
            typeInfo: Optional[dict] = None,
            queryOpts: Optional[QueryOptions] = None,
            imageID: Optional[int] = None,
            archiveID: Optional[int] = None,
            strict: bool = False) -> List[ArchiveInfo]:
        ...

    def listBTypes(
            self,
            query: Optional[Dict[str, str]] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[BTypeInfo]:
        ...

    def listBuilds(
            self,
            packageID: Optional[PackageID] = None,
            userID: Optional[UserID] = None,
            taskID: Optional[TaskID] = None,
            prefix: Optional[str] = None,
            state: Optional[BuildState] = None,
            volumeID: Optional[int] = None,
            source: Optional[str] = None,
            createdBefore: Optional[str] = None,
            createdAfter: Optional[str] = None,
            completeBefore: Optional[str] = None,
            completeAfter: Optional[str] = None,
            type: Optional[str] = None,
            typeInfo: Optional[Dict] = None,
            queryOpts: Optional[QueryOptions] = None,
            pattern: Optional[str] = None,
            cgID: Optional[CGID] = None,
            draft: Optional[bool] = None) -> List[BuildInfo]:
        ...

    def listCGs(self) -> Dict[str, CGInfo]:
        ...

    def listHosts(
            self,
            arches: Optional[List[str]] = None,
            channelID: Optional[int] = None,
            ready: Optional[bool] = None,
            enabled: Optional[bool] = None,
            userID: Optional[UserID] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[HostInfo]:
        ...

    def listPackages(
            self,
            tagID: Optional[TagID] = None,
            userID: Optional[UserID] = None,
            pkgID: Optional[PackageID] = None,
            prefix: Optional[str] = None,
            inherited: bool = False,
            with_dups: bool = False,
            event: Optional[EventID] = None,
            queryOpts: Optional[QueryOptions] = None,
            with_owners: bool = True) -> List[TagPackageInfo]:
        ...

    def listRPMs(
            self,
            buildID: Optional[BuildID] = None,
            buildrootID: Optional[BuildrootID] = None,
            imageID: Optional[int] = None,
            componentBuildrootID: Optional[int] = None,
            hostID: Optional[int] = None,
            arches: Optional[str] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[RPMInfo]:
        ...

    @overload
    def listUsers(
            self,
            userType: UserType = UserType.NORMAL,
            prefix: Optional[str] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[UserInfo]:
        ...

    @overload
    def listUsers(
            self,
            userType: UserType = UserType.NORMAL,
            prefix: Optional[str] = None,
            queryOpts: Optional[QueryOptions] = None,
            perm: Optional[str] = None,
            inherited_perm: bool = False) -> List[UserInfo]:
        # :since: koji 1.35
        ...

    def listTagged(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            inherit: bool = False,
            prefix: Optional[str] = None,
            latest: bool = False,
            package: Optional[Union[int, str]] = None,
            owner: Optional[Union[int, str]] = None,
            type: Optional[str] = None) -> List[TagBuildInfo]:
        ...

    def listTaggedArchives(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            inherit: bool = False,
            latest: bool = False,
            package: Optional[Union[int, str]] = None,
            type: Optional[str] = None) -> Tuple[List[ArchiveInfo],
                                                 List[BuildInfo]]:
        ...

    def listTags(
            self,
            build: Optional[Union[int, str]] = None,
            package: Optional[Union[int, str]] = None,
            perms: bool = True,
            queryOpts: Optional[QueryOptions] = None,
            pattern: Optional[str] = None) -> List[TagInfo]:
        ...

    @overload
    def listTaskOutput(
            self,
            task_id: int,
            *,
            all_volumes: bool = False,
            strict: bool = False) -> Dict[str, List[str]]:
        ...

    @overload
    def listTaskOutput(
            self,
            task_id: int,
            stat: Literal[False],
            all_volumes: bool = False,
            strict: bool = False) -> Dict[str, List[str]]:
        ...

    @overload
    def listTaskOutput(
            self,
            task_id: int,
            stat: Literal[True],
            all_volumes: bool = False,
            strict: bool = False) -> Dict[str, Dict[str, Dict[str, Any]]]:
        ...

    @overload
    def listTaskOutput(
            self,
            task_id: int,
            stat: bool = False,
            all_volumes: bool = False,
            strict: bool = False) -> Union[Dict[str, List[str]],
                                           Dict[str, Dict[str,
                                                          Dict[str, Any]]]]:
        ...

    def listTasks(
            self,
            opts: Optional[ListTasksOptions] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[TaskInfo]:
        ...

    def massTag(
            self,
            tag: Union[int, str],
            builds: List[Union[int, str]]) -> None:
        # :since: koji 1.30
        ...

    def mavenBuild(
            self,
            url: str,
            target: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None,
            channel: str = 'maven') -> int:
        ...

    def mavenEnabled(self) -> bool:
        ...

    def packageListAdd(
            self,
            taginfo: Union[int, str],
            pkginfo: str,
            owner: Optional[Union[int, str]] = None,
            block: Optional[bool] = None,
            exta_arches: Optional[str] = None,
            force: bool = False,
            update: bool = False):
        ...

    @overload
    def queryHistory(
            self,
            tables: Optional[List[str]] = None,
            *,
            queryOpts: Optional[QueryOptions] = None,
            **kwargs: Any) -> Dict[str, List[Dict[str, Any]]]:
        # :since: koji 1.34
        ...

    @overload  # type: ignore
    def queryHistory(
            self,
            tables: Optional[List[str]] = None,
            **kwargs: Any) -> Dict[str, List[Dict[str, Any]]]:
        ...

    def queryRPMSigs(
            self,
            rpm_id: Optional[int] = None,
            sigkey: Optional[str] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[RPMSignature]:
        ...

    def repoInfo(
            self,
            repo_id: int,
            struct: bool = False) -> RepoInfo:
        ...

    def resubmitTask(
            self,
            taskID: int) -> int:
        ...

    def search(
            self,
            terms: str,
            type: str,
            matchType: str,
            queryOpts: Optional[QueryOptions] = None) -> List[SearchResult]:
        ...

    def setInheritanceData(
            self,
            tag: Union[str, TagID],
            data: TagInheritance,
            clear: bool = False) -> None:
        ...

    def ssl_login(
            self,
            cert: Optional[str] = None,
            ca: Optional[str] = None,
            serverca: Optional[str] = None,
            proxyuser: Optional[str] = None) -> bool:
        ...

    def tagBuild(
            self,
            tag: Union[str, TagID],
            build: Union[str, BuildID],
            force: bool = False,
            fromtag: Union[str, TagID, None] = None) -> None:
        ...

    def tagBuildBypass(
            self,
            tag: Union[str, TagID],
            build: Union[str, BuildID],
            force: bool = False,
            notify: bool = False) -> None:
        ...

    def tagChangedSinceEvent(
            self,
            event: EventID,
            taglist: List[TagID]) -> bool:
        ...

    def untagBuild(
            self,
            tag: Union[str, TagID],
            build: Union[str, BuildID],
            strict: bool = True,
            force: bool = False) -> None:
        ...

    def untagBuildBypass(
            self,
            tag: Union[str, TagID],
            build: Union[str, BuildID],
            strict: bool = True,
            force: bool = False,
            notify: bool = False) -> None:
        ...

    def winBuild(
            self,
            vm: str,
            url: str,
            target: str,
            opts: Optional[Dict[str, Any]] = None,
            priority: Optional[int] = None,
            channel: str = 'vm') -> int:
        ...

    def winEnabled(self) -> bool:
        ...

    def wrapperRPM(
            self,
            build: Union[int, str],
            url: str,
            target: str,
            priority: Optional[int] = None,
            channel: str = 'maven',
            opts: Optional[Dict[str, Any]] = None) -> int:
        ...


class Host(Protocol):

    def failTask(
            self,
            task_id: int,
            response: Any) -> None:
        ...

    def freeTasks(
            self,
            tasks: List[int]) -> None:
        ...

    def getID(self) -> int:
        ...

    def getHostTasks(
            self) -> List[TaskInfo]:
        ...

    def getLoadData(
            self) -> Tuple[List[HostInfo], List[TaskInfo]]:
        ...

    def getTasks(
            self) -> List[TaskInfo]:
        ...

    def refuseTask(
            self,
            task_id: int,
            soft: bool = True,
            msg: str = '') -> None:
        ...

    def setHostData(
            self,
            hostdata: Dict[str, Any]) -> None:
        ...

    def subtask(
            self,
            method: str,
            arglist: List,
            parent: int,
            **opts) -> int:
        ...

    def taskSetWait(
            self,
            parent: int,
            tasks: Optional[List[int]]) -> None:
        ...

    def taskUnwait(
            self,
            parent: int) -> None:
        ...

    def taskWait(
            self,
            parent: int) -> Tuple[List[int], List[int]]:
        ...

    def taskWaitCheck(
            self,
            parent: int) -> Tuple[List[int], List[int]]:
        ...

    def taskWaitResults(
            self,
            parent: int,
            tasks: Optional[List[int]],
            canfail: Optional[List[int]]) -> List[Tuple[int, Any]]:
        ...

    def updateHost(
            self,
            task_load: float,
            ready: bool) -> None:
        ...

    def verify(self) -> bool:
        ...


@proxytype(Host, VirtualCall)
class MultiCallHost(Protocol):
    ...


@proxytype(ClientSession, VirtualCall)
class MultiCallSession(Protocol):

    @property
    def host(self) -> MultiCallHost:
        ...


# The end.
