import logging
import shutil

log = logging.getLogger(__name__)


async def load_computer_name(hub):
    scutil = shutil.which("scutil")
    if scutil:
        hub.corn.CORN.computer_name = (
            await hub.exec.cmd.run([scutil, "--get", "ComputerName"])
        ).stdout.strip()
