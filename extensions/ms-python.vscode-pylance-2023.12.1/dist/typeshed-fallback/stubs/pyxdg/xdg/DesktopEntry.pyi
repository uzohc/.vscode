import re
from _typeshed import StrPath
from typing_extensions import Literal

from xdg.IniFile import IniFile

class DesktopEntry(IniFile):
    defaultGroup: str
    content: dict[str, dict[str, str]]
    def __init__(self, filename: StrPath | None = None) -> None: ...
    def parse(self, file: StrPath) -> None: ...  # type: ignore[override]
    def findTryExec(self) -> str | None: ...
    def getType(self) -> str: ...
    def getVersion(self) -> float: ...
    def getVersionString(self) -> str: ...
    def getName(self) -> str: ...
    def getGenericName(self) -> str: ...
    def getNoDisplay(self) -> bool: ...
    def getComment(self) -> str: ...
    def getIcon(self) -> str: ...
    def getHidden(self) -> bool: ...
    def getOnlyShowIn(self) -> list[str]: ...
    def getNotShowIn(self) -> list[str]: ...
    def getTryExec(self) -> str: ...
    def getExec(self) -> str: ...
    def getPath(self) -> str: ...
    def getTerminal(self) -> bool: ...
    def getMimeType(self) -> list[re.Pattern[str]]: ...
    def getMimeTypes(self) -> list[str]: ...
    def getCategories(self) -> list[str]: ...
    def getStartupNotify(self) -> bool: ...
    def getStartupWMClass(self) -> str: ...
    def getURL(self) -> str: ...
    def getServiceTypes(self) -> list[str]: ...
    def getDocPath(self) -> str: ...
    def getKeywords(self) -> list[str]: ...
    def getInitialPreference(self) -> str: ...
    def getDev(self) -> str: ...
    def getFSType(self) -> str: ...
    def getMountPoint(self) -> str: ...
    def getReadonly(self) -> bool: ...
    def getUnmountIcon(self) -> str: ...
    def getMiniIcon(self) -> str: ...
    def getTerminalOptions(self) -> str: ...
    def getDefaultApp(self) -> str: ...
    def getProtocols(self) -> list[str]: ...
    def getExtensions(self) -> list[str]: ...
    def getBinaryPattern(self) -> str: ...
    def getMapNotify(self) -> str: ...
    def getEncoding(self) -> str: ...
    def getSwallowTitle(self) -> str: ...
    def getSwallowExec(self) -> str: ...
    def getSortOrder(self) -> list[str]: ...
    def getFilePattern(self) -> re.Pattern[str]: ...
    def getActions(self) -> list[str]: ...
    filename: str
    def new(self, filename: str) -> None: ...
    type: Literal["Application", "Directory"]
    name: str
    def checkExtras(self) -> None: ...
    def checkGroup(self, group: str) -> None: ...
    def checkKey(self, key: str, value: str, group: str) -> None: ...
    def checkType(self, key: str, type: str) -> None: ...
    def checkOnlyShowIn(self, value: str) -> None: ...
    def checkCategories(self, value: str) -> None: ...
