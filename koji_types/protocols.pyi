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
"""  # noqa: Y021


from . import (
    ArchiveInfo, ArchiveTypeInfo, BuildInfo, BuildrootInfo, BuildState,
    BTypeInfo, ChannelInfo, CGInfo, FaultInfo, HostInfo, ListTasksOptions,
    MavenInfo, PackageInfo, PermInfo, POMInfo, QueryOptions, RepoInfo,
    RepoState, RPMInfo, RPMSignature, RPMSigTag, SearchResult,
    TagBuildInfo, TagInfo, TagGroupInfo, TagInheritance, TagPackageInfo,
    TargetInfo, TaskInfo, UserGroup, UserInfo, UserType, )

from koji import VirtualCall
from typing import (
    Any, Dict, List, Literal, Optional, Tuple, Union, overload, )
from preoccupied.proxytype import proxytype


class ClientSessionProtocol:
    # This is non-runtime class which presents the interfaces for the
    # baseline koji hub API calls.

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

    def editTag2(
            self,
            taginfo: Union[int, str],
            **kwargs) -> None:
        ...

    def enableUser(
            self,
            username: Union[int, str]) -> None:
        ...

    def exclusiveSession(self, *args, **kwargs) -> None:
        ...

    def getAllPerms(self) -> List[PermInfo]:
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

    def getChannel(
            self,
            channelInfo: Union[int, str],
            strict: bool = False) -> ChannelInfo:
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
            taskID: Optional[int] = None,
            filepath: Optional[str] = None,
            headers: Optional[List[str]] = None) -> Dict[str, Any]:
        ...

    @overload
    def getRPMHeaders(
            self,
            rpmID: Optional[int] = None,
            taskID: Optional[int] = None,
            filepath: Optional[str] = None,
            headers: Optional[List[str]] = None,
            strict: Optional[bool] = False) -> Dict[str, Any]:
        # :since: koji 1.29.0
        ...

    def getTag(
            self,
            taginfo: Union[int, str],
            strict: bool = False,
            event: Optional[int] = None,
            blocked: bool = False) -> TagInfo:
        ...

    def getTagGroups(
            self,
            tag: Union[int, str],
            event: Optional[int] = None,
            inherit: bool = True,
            incl_pkgs: bool = True,
            incl_reqs: bool = True,
            incl_blocked: bool = False) -> List[TagGroupInfo]:
        ...

    def getTaskChildren(
            self,
            task_id: int,
            request: Optional[bool] = False,
            strict: Optional[bool] = False) -> List[TaskInfo]:
        ...

    @overload
    def getTaskInfo(
            self,
            task_id: int,
            request: bool = False,
            strict: bool = False) -> TaskInfo:
        ...

    @overload
    def getTaskInfo(
            self,
            task_id: List[int],
            request: bool = False,
            strict: bool = False) -> List[TaskInfo]:
        ...

    @overload
    def getUser(
            self,
            userInfo: Optional[Union[int, str]] = None,
            strict: bool = False,
            krb_princs: bool = True) -> UserInfo:
        ...

    @overload
    def getUser(
            self,
            userInfo: Optional[Union[int, str]] = None,
            strict: bool = False,
            krb_princs: bool = True,
            groups: bool = False) -> UserInfo:
        # :since: koji 1.34
        ...

    @overload
    def getUserPerms(
            self,
            userID: Optional[Union[int, str]] = None) -> List[str]:
        ...

    @overload
    def getUserPerms(
            self,
            userID: Optional[Union[int, str]] = None,
            with_groups: bool = True) -> List[str]:
        # :since: koji 1.34
        ...

    def getUserPermsInheritance(
            self,
            userID: Union[int, str]) -> Dict[str, List[str]]:
        # :since: koji 1.34
        ...

    def hasPerm(
            self,
            perm: str,
            strict: bool = False) -> bool:
        ...

    def listArchives(
            self,
            buildID: Optional[int] = None,
            buildrootID: Optional[int] = None,
            componentBuildrootID: Optional[int] = None,
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
            packageID: Optional[int] = None,
            userID: Optional[int] = None,
            taskID: Optional[int] = None,
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
            cgID: Optional[int] = None,
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
            userID: Optional[int] = None,
            queryOpts: Optional[QueryOptions] = None) -> List[HostInfo]:
        ...

    def listPackages(
            self,
            tagID: Optional[int] = None,
            userID: Optional[int] = None,
            pkgID: Optional[int] = None,
            prefix: Optional[str] = None,
            inherited: bool = False,
            with_dups: bool = False,
            event: Optional[int] = None,
            queryOpts: Optional[dict] = None,
            with_owners: bool = True) -> List[TagPackageInfo]:
        ...

    def listRPMs(
            self,
            buildID: Optional[int] = None,
            buildrootID: Optional[int] = None,
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

    @overload
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
            tag: Union[int, str],
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

    def tagBuildBypass(
            self,
            tag: Union[int, str],
            build: Union[int, str],
            force: bool = False,
            notify: bool = False) -> None:
        ...

    def tagChangedSinceEvent(
            self,
            event: int,
            taglist: List[int]) -> bool:
        ...

    def untagBuildBypass(
            self,
            tag: Union[int, str],
            build: Union[int, str],
            strict: bool = True,
            force: bool = False,
            notify: bool = False) -> None:
        ...


@proxytype(ClientSessionProtocol, VirtualCall)
class MultiCallSessionProtocol:
    ...


# The end.