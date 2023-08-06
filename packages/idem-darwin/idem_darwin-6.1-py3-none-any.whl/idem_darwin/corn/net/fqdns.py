import logging
import shutil
import socket
from typing import List

log = logging.getLogger(__name__)


async def _get_fqdns(fqdn: str, protocol: int) -> List[str]:
    default = socket.getdefaulttimeout()
    socket.setdefaulttimeout(1)
    try:
        result = socket.getaddrinfo(fqdn, None, protocol)
        return sorted({item[4][0] for item in result})
    except socket.gaierror as e:
        log.debug(e)
    socket.setdefaulttimeout(default)
    return []


async def load_fqdns(hub):
    scutil = shutil.which("scutil")
    if scutil:
        hub.corn.CORN.localhost = (
            await hub.exec.cmd.run([scutil, "--get", "LocalHostName"])
        ).stdout.strip()
        hostname = shutil.which("hostname")
        if hostname:
            hub.corn.CORN.fqdn = (
                await hub.exec.cmd.run([hostname, "-f"])
            ).stdout.strip()

            log.debug("loading fqdns based grains")
            hub.corn.CORN.host, hub.corn.CORN.domain = hub.corn.CORN.fqdn.partition(
                "."
            )[::2]
            if not hub.corn.CORN.domain:
                hub.corn.CORN.domain = "local"
                hub.corn.CORN.fqdn += ".local"
            if "." not in hub.corn.CORN.localhost:
                hub.corn.CORN.localhost += f".{hub.corn.CORN.domain}"
            hub.corn.CORN.fqdn_ip4 = await _get_fqdns(
                hub.corn.CORN.fqdn, socket.AF_INET
            )
            hub.corn.CORN.fqdn_ip6 = await _get_fqdns(
                hub.corn.CORN.fqdn, socket.AF_INET6
            )
            hub.corn.CORN.fqdns = hub.corn.CORN.fqdn_ip4 + hub.corn.CORN.fqdn_ip6
