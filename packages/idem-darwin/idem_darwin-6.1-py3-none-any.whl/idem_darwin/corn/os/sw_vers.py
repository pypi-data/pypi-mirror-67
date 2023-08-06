import shutil
from typing import List, Tuple

_MAC_CODENAME_MAP = {
    15: ("macOS", "Catalina"),
    14: ("macOS", "Mojave"),
    13: ("macOS", "High Sierra"),
    12: ("macOS", "Sierra"),
    11: ("OS X", "El Capitan"),
    10: ("OS X", "Yosemite"),
    9: ("OS X", "Mavericks"),
    8: ("OS X", "Mountain Lion"),
    7: ("OS X", "Lion"),
    6: ("Mac OS X", "Snow Leopard"),
    5: ("Mac OS X", "Leopard"),
    4: ("Mac OS X", "Tiger"),
    3: ("Mac OS X", "Panther"),
    2: ("Mac OS X", "Jaguar"),
    1: ("Mac OS X", "Puma"),
    0: ("Mac OS X", "Cheetah"),
}


def _get_codename(osrelease_info: List[int]) -> Tuple[str, str]:
    if osrelease_info[1] in _MAC_CODENAME_MAP:
        return _MAC_CODENAME_MAP[osrelease_info[1]]
    else:
        return "macOS", "UNKNOWN"


async def load_os_release(hub):
    sw_vers = shutil.which("sw_vers")
    if sw_vers:
        hub.corn.CORN.osrelease = (
            await hub.exec.cmd.run([sw_vers, "-productVersion"])
        ).stdout.strip()
        osname = (await hub.exec.cmd.run([sw_vers, "-productName"])).stdout.strip()
        hub.corn.CORN.osfullname = f"{osname} {hub.corn.CORN.osrelease}"
        hub.corn.CORN.osrelease_info = (
            int(x) for x in hub.corn.CORN.osrelease.split(".")
        )
        hub.corn.CORN.osmajorrelease = hub.corn.CORN.osrelease_info[0]
        hub.corn.CORN.os, hub.corn.CORN.oscodename = _get_codename(
            hub.corn.CORN.osrelease_info
        )
        hub.corn.CORN.osfinger = (
            f"{osname} {hub.corn.CORN.osrelease}-{hub.corn.CORN.osmajorrelease}"
        )


async def load_os_build(hub):
    sw_vers = shutil.which("sw_vers")
    if sw_vers:
        hub.corn.CORN.osbuild = (
            await hub.exec.cmd.run([sw_vers, "-buildVersion"])
        ).stdout.strip()
