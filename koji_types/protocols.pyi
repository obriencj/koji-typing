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
    ArchiveID, ArchiveInfo, ATypeID, ATypeInfo,
    BuildSpecifier, BuildID, BuildLogs, BuildInfo, BuildNVR,
    BuildrootID, BuildrootInfo, BuildrootState,
    BuildState, BTypeInfo, ChangelogEntry, ChannelInfo,
    ChecksumType,
    CGID, CGInfo, CGInitInfo,
    EventID, EventInfo,
    FaultInfo, HostID, HostInfo, ListTasksOptions, MavenInfo,
    NamedID, PackageID, PackageInfo,
    PermInfo, POMInfo, QueryOptions,
    RepoID, RepoInfo, RepoState, RPMID, RPMInfo, RPMNVRA,
    RPMSignature, RPMSigTag, SearchResult, SessionInfo, TagBuildInfo,
    TagID, TagInfo, TagGroupID, TagGroupInfo, TagInheritance, TagPackageInfo,
    TargetID, TargetInfo,
    TaskID, TaskInfo, UserGroup, UserID, UserInfo, UserType,
    WinInfo, )
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

    @staticmethod
    def createTag(
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

    @staticmethod
    def getActiveRepos() -> List[RepoInfo]:
        ...

    def getAllPerms(self) -> List[PermInfo]:
        ...

    def getAPIVersion(self) -> int:
        ...

    def getArchive(
            self,
            archive_id: ArchiveID,
            strict: bool = False) -> ArchiveInfo:
        ...

    def getArchiveType(
            self,
            filename: Optional[str] = None,
            type_name: Optional[str] = None,
            type_id: Optional[ATypeID] = None,
            strict: bool = False) -> ATypeInfo:
        ...

    def getArchiveTypes(self) -> List[ATypeInfo]:
        ...

    def getBuild(
            self,
            buildInfo: Union[str, BuildID],
            strict: bool = False) -> BuildInfo:
        ...

    def getBuildLogs(
            self,
            buildInfo: Union[str, BuildID]) -> BuildLogs:
        ...

    def getBuildroot(
            self,
            buildrootID: int,
            strict: bool = False) -> BuildrootInfo:
        ...

    def getBuildTarget(
            self,
            info: Union[int, str],
            event: Optional[EventID] = None,
            strict: bool = False) -> TargetInfo:
        ...

    def getBuildTargets(
            self,
            info: Optional[Union[int, str]] = None,
            event: Optional[EventID] = None,
            buildTagID: Optional[int] = None,
            destTagID: Optional[int] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[TargetInfo]:
        ...

    def getBuildType(
            self,
            buildInfo: Union[int, str],
            strict: bool = False) -> Dict[str, dict]:
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

    def getLastEvent(
            self,
            before: Union[int, float, None] = None) -> EventInfo:
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
    @staticmethod
    def getRPM(
            rpminfo: Union[str, RPMID, RPMNVRA],
            strict: bool = False) -> Optional[RPMInfo]:
        ...

    @overload
    @staticmethod
    def getRPM(
            rpminfo: Union[str, RPMID, RPMNVRA],
            strict: bool = False,
            *,
            multi: Literal[False]) -> Optional[RPMInfo]:
        ...

    @overload
    @staticmethod
    def getRPM(
            rpminfo: Union[str, RPMID, RPMNVRA],
            strict: bool = False,
            *,
            multi: Literal[True]) -> List[RPMInfo]:
        ...

    @overload
    @staticmethod
    def getRPM(
            rpminfo: Union[str, RPMID, RPMNVRA],
            strict: bool = False,
            multi: bool = False) -> Union[RPMInfo, List[RPMInfo], None]:
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

    @staticmethod
    def getTag(
            tagInfo: Union[str, TagID],
            strict: bool = False,
            event: Optional[EventID] = None,
            blocked: bool = False) -> Optional[TagInfo]:
        ...

    @staticmethod
    def getTagID(
            info: Union[str, TagID, Dict[str, Any]],
            strict: bool = False,
            create: bool = False) -> Optional[TagID]:
        ...

    @staticmethod
    def getTagGroups(
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
    @staticmethod
    def getUser(
            userInfo: Union[str, UserID, None] = None,
            strict: bool = False,
            krb_princs: bool = True) -> UserInfo:
        ...

    @overload
    @staticmethod
    def getUser(
            userInfo: Union[str, UserID, None] = None,
            strict: bool = False,
            krb_princs: bool = True,
            groups: bool = False) -> UserInfo:
        # :since: koji 1.34
        ...

    def getUserGroups(
            self,
            user: Union[int, str]) -> List[UserGroup]:
        # :since: koji 1.35
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

    @staticmethod
    def groupListAdd(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            block: bool = False,
            force: bool = False,
            **opts) -> None:
        ...

    @staticmethod
    def groupListBlock(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID]) -> None:
        ...

    @staticmethod
    def groupListRemove(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            force: bool = False) -> None:
        ...

    @staticmethod
    def groupListUnnblock(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID]) -> None:
        ...

    @staticmethod
    def groupPackageListAdd(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            pkg_name: str,
            block: bool = False,
            force: bool = False,
            **opts) -> None:
        ...

    @staticmethod
    def groupPackageListBlock(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            pkg_name: str) -> None:
        ...

    @staticmethod
    def groupPackageListRemove(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            pkg_name: str) -> None:
        ...

    @staticmethod
    def groupPackageListUnblock(
            taginfo: Union[str, TagID],
            grpinfo: Union[str, TagGroupID],
            pkg_name: str) -> None:
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

    @staticmethod
    def listArchives(
            buildID: Optional[BuildID] = None,
            buildrootID: Optional[BuildrootID] = None,
            componentBuildrootID: Optional[BuildrootID] = None,
            hostID: Optional[HostID] = None,
            type: Optional[str] = None,
            filename: Optional[str] = None,
            size: Optional[int] = None,
            checksum: Optional[int] = None,
            checksum_type: Optional[ChecksumType] = None,
            typeInfo: Optional[Dict[str, Any]] = None,
            queryOpts: Optional[QueryOptions] = None,
            imageID: Optional[int] = None,
            archiveID: Optional[ArchiveID] = None,
            strict: bool = False) -> List[ArchiveInfo]:
        ...

    @staticmethod
    def listBTypes(
            query: Optional[NamedID] = None,
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

    @staticmethod
    def listCGs() -> Dict[str, CGInfo]:
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
            with_owners: bool = True,
            with_blocked: bool = True) -> List[TagPackageInfo]:
        ...

    @staticmethod
    def listRPMs(
            buildID: Optional[BuildID] = None,
            buildrootID: Optional[BuildrootID] = None,
            imageID: Optional[int] = None,
            componentBuildrootID: Optional[BuildrootID] = None,
            hostID: Optional[int] = None,
            arches: Union[Arch, List[Arch], None] = None,
            queryOpts: Optional[QueryOptions] = None,
            draft: Optional[bool] = None) -> List[RPMInfo]:
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
            tag: Union[str, TagID],
            event: Optional[EventID] = None,
            inherit: bool = False,
            prefix: Optional[str] = None,
            latest: bool = False,
            package: Optional[str] = None,
            owner: Optional[Union[str, UserID]] = None,
            type: Optional[str] = None,
            strict: bool = True,
            extra: bool = False,
            draft: Optional[bool] = None) -> List[TagBuildInfo]:
        ...

    def listTaggedArchives(
            self,
            tag: Union[str, TagID],
            event: Optional[EventID] = None,
            inherit: bool = False,
            latest: bool = False,
            package: Optional[str] = None,
            type: Optional[str] = None,
            strict: bool = True,
            extra: bool = True) -> Tuple[List[ArchiveInfo],
                                         List[BuildInfo]]:
        ...

    @staticmethod
    def listTags(
            build: Optional[BuildSpecifier] = None,
            package: Union[str, PackageID, None] = None,
            perms: bool = True,
            queryOpts: Optional[QueryOptions] = None,
            pattern: Optional[str] = None) -> List[TagInfo]:
        ...

    @staticmethod
    def listTaskOutput(
            taskID: TaskID,
            stat: bool = False,
            all_volumes: bool = False,
            strict: bool = False) \
            -> Union[List[str],
                     Dict[str, List[str]],
                     Dict[str, Dict[str, Any]],
                     Dict[str, Dict[str, Dict[str, Any]]]]:
        ...

    def listTasks(
            self,
            opts: Optional[ListTasksOptions] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[TaskInfo]:
        ...

    def massTag(
            self,
            tag: Union[str, TagID],
            builds: List[Union[str, BuildID]]) -> None:
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

    @staticmethod
    def packageListAdd(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            owner: Union[str, UserID, None] = None,
            block: Optional[bool] = None,
            extra_arches: Optional[str] = None,
            force: bool = False,
            update: bool = False) -> None:
        ...

    @staticmethod
    def packkageListBlock(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            force: bool = False) -> None:
        ...

    @staticmethod
    def packageListRemove(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            force: bool = False) -> None:
        ...

    @staticmethod
    def packageListSetArches(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            arches: str,
            force: bool = False) -> None:
        ...

    @staticmethod
    def packageListSetOwner(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            owner: Union[str, UserID],
            force: bool = False) -> None:
        ...

    @staticmethod
    def packageListUnblock(
            taginfo: Union[str, TagID],
            pkginfo: Union[str, PackageID],
            force: bool = False) -> None:
        ...

    @overload
    @staticmethod
    def queryHistory(
            tables: Optional[List[str]] = None,
            *,
            queryOpts: Optional[QueryOptions] = None,
            **kwargs: Any) -> Dict[str, List[Dict[str, Any]]]:
        # :since: koji 1.34
        ...

    @overload  # type: ignore
    @staticmethod
    def queryHistory(
            tables: Optional[List[str]] = None,
            **kwargs: Any) -> Dict[str, List[Dict[str, Any]]]:
        ...

    @staticmethod
    def queryRPMSigs(
            rpm_id: Union[RPMID, str, BuildNVR, None] = None,
            sigkey: Optional[str] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[RPMSignature]:
        ...

    @staticmethod
    def repoInfo(
            repo_id: RepoID,
            strict: bool = False) -> RepoInfo:
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

    @staticmethod
    def tagChangedSinceEvent(
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

    def updateHost(
            self,
            task_load: float,
            ready: bool) -> None:
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

    def assertPolicy(
            self,
            name,
            data: Dict[str, Any],
            default: str = 'deny') -> None:
        ...

    def checkPolicy(
            self,
            name: str,
            data: Dict[str, Any],
            default: str = 'deny',
            strict: bool = False) -> Tuple[bool, str]:
        ...

    def closeTask(
            self,
            task_id: TaskID,
            response: Any) -> None:
        ...

    def completeBuild(
            self,
            task_id: TaskID,
            build_id: BuildID,
            srpm: str,
            rpms: List[str],
            brmap: Optional[Dict[str, BuildrootID]] = None,
            logs: Optional[Dict[Arch, List[str]]] = None) -> BuildInfo:
        ...

    def completeImageBuild(
            self,
            task_id: TaskID,
            build_id: BuildID,
            results: Dict[str, Dict[str, Any]]) -> None:
        ...

    def completeMavenBuild(
            self,
            task_id: TaskID,
            build_id: BuildID,
            maven_results: Any,
            rpm_results: Any) -> None:
        ...

    def completeWinBuild(
            self,
            task_id: TaskID,
            build_id: BuildID,
            results: Dict[str, Dict[str, Any]],
            rpm_results: Any) -> None:
        ...

    @staticmethod
    def createBuildTarget(
            name: str,
            build_tag: Union[str, TagID],
            dest_tag: Union[str, TagID]) -> None:
        ...

    def createMavenBuild(
            self,
            build_info: BuildInfo,
            maven_info: MavenInfo) -> None:
        ...

    @staticmethod
    def deleteBuildTarget(
            buildTargetInfo: Union[str, TargetID]) -> None:
        ...

    def distRepoMove(
            self,
            repo_id: RepoID,
            uploadpath: str,
            arch: Arch) -> None:
        ...

    def evalPolicy(
            self,
            name: str,
            data: Dict[str, Any]) -> str:
        ...

    def failBuild(
            self,
            task_id: TaskID,
            build_id: BuildID) -> None:
        ...

    def failTask(
            self,
            task_id: TaskID,
            response: Any) -> None:
        ...

    def freeTasks(
            self,
            tasks: List[TaskID]) -> None:
        ...

    def getID(self) -> HostID:
        ...

    def getHost(self) -> Tuple[List[HostID], List[TaskID]]:
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

    def importArchive(
            self,
            filepath: str,
            buildinfo: BuildInfo,
            type: str,
            typeInfo: Dict[str, Any]) -> None:
        ...

    def importImage(
            self,
            task_id: TaskID,
            build_info: BuildInfo,
            results: Dict[str, Dict[str, Any]]) -> None:
        ...

    def importWrapperRPMs(
            self,
            task_id: TaskID,
            build_id: BuildID,
            rpm_results: Dict[str, List[str]]) -> None:
        ...

    def initBuild(
            self,
            data: Dict[str, Any]) -> BuildID:
        ...

    def initImageBuild(
            self,
            task_id: TaskID,
            build_info: BuildInfo) -> BuildInfo:
        ...

    def initMavenBuild(
            self,
            task_id: TaskID,
            build_info: BuildInfo,
            maven_info: MavenInfo) -> BuildInfo:
        ...

    def initWinBuild(
            self,
            task_id: TaskID,
            build_info: BuildInfo,
            win_info: WinInfo) -> BuildInfo:
        ...

    def isEnabled(self) -> bool:
        ...

    def moveBuildToScratch(
            self,
            task_id: TaskID,
            srpm: str,
            rpms: List[str],
            logs: Optional[Dict[str, List[str]]] = None) -> None:
        ...

    def moveImageBuildToScratch(
            self,
            task_id: TaskID,
            results: Dict[str, Any]) -> None:
        ...

    def moveMavenBuildToScratch(
            self,
            task_id: TaskID,
            results: Dict[str, Any],
            rpm_results: Dict[str, Any]) -> None:
        ...

    def moveWinBuildToScratch(
            self,
            task_id: TaskID,
            results: Dict[str, Any],
            rpm_results: Dict[str, Any]) -> None:
        ...

    def newBuildRoot(
            self,
            repo: RepoID,
            arch: Arch,
            task_id: Optional[TaskID] = None) -> BuildrootID:
        ...

    def openTask(
            self,
            task_id: TaskID) -> Optional[Dict[str, Any]]:
        ...

    def refuseTask(
            self,
            task_id: int,
            soft: bool = True,
            msg: str = '') -> None:
        ...

    def repoDone(
            self,
            repo_id: RepoID,
            data: Dict[Arch, Tuple[str, List[str]]],
            expire: bool = False,
            repo_json_updates: Optional[Dict[str, Any]] = None) -> None:
        ...

    def repoInit(
            self,
            tag: Union[str, TagID],
            task_id: Optional[TaskID] = None,
            with_src: bool = False,
            with_debuginfo: bool = False,
            event: Optional[EventID] = None,
            with_separate_src: bool = False) -> Tuple[RepoID, EventID]:
        ...

    def setBuildRootList(
            self,
            brootid: BuildrootID,
            rpmlist: List[RPMInfo],
            task_id: Optional[TaskID] = None) -> None:
        ...

    def setBuildRootState(
            self,
            brootid: BuildrootID,
            state: BuildrootState,
            task_id: Optional[TaskID] = None) -> None:
        ...

    def setHostData(
            self,
            hostdata: Dict[str, Any]) -> None:
        ...

    def setTaskWeight(
            self,
            task_id: TaskID,
            weight: float) -> None:
        ...

    def subtask(
            self,
            method: str,
            arglist: List,
            parent: int,
            **opts) -> int:
        ...

    def subtask2(
            self,
            __parent: TaskID,
            __taskopts: Dict[str, Any],
            __method: str,
            *args,
            **opts) -> int:
        ...

    def tagBuild(
            self,
            task_id: TaskID,
            tag: Union[str, TagID],
            build: BuildSpecifier,
            force: bool = False,
            fromtag: Union[str, TagID, None] = None) -> None:
        ...

    def tagNotification(
            self,
            is_successful: bool,
            tag_id: Union[str, TagID, None],
            from_id: Union[str, TagID, None],
            build_id: BuildID,
            user_id: Union[str, UserID, None],
            ignore_success: bool = False,
            failure_msg: str = '') -> None:
        ...

    def taskSetWait(
            self,
            parent: TaskID,
            tasks: Optional[List[TaskID]]) -> None:
        ...

    def taskUnwait(
            self,
            parent: TaskID) -> None:
        ...

    def taskWait(
            self,
            parent: TaskID) -> Tuple[List[int], List[int]]:
        ...

    def taskWaitCheck(
            self,
            parent: TaskID) -> Tuple[List[int], List[int]]:
        ...

    def taskWaitResults(
            self,
            parent: TaskID,
            tasks: Optional[List[TaskID]],
            canfail: Optional[List[int]] = None) -> List[Tuple[int, Any]]:
        ...

    def updateBuildrootArchives(
            self,
            brootid: BuildrootID,
            task_id: TaskID,
            archives: List[ArchiveInfo],
            project: bool = False) -> None:
        ...

    def updateBuildRootList(
            self,
            brootid: BuildrootID,
            rpmlist: List[RPMInfo],
            task_id: Optional[TaskID] = None) -> None:
        ...

    def updateHost(
            self,
            task_load: float,
            ready: bool,
            data: Optional[Dict[str, Any]] = None) -> None:
        ...

    def updateMavenBuildRootList(
            self,
            brootid: BuildrootID,
            task_id: TaskID,
            mavenlist: List[Dict[str, Any]],
            ignore: Optional[List[Union[int, str]]] = None,
            project: bool = False,
            ignore_unknown: bool = False,
            extra_deps: Optional[List[Union[int, str]]] = None) -> None:
        ...

    def verify(self) -> bool:
        ...

    def writeSignedRPM(
            self,
            an_rpm: str,
            sigkey: str,
            force: bool = False) -> None:
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
