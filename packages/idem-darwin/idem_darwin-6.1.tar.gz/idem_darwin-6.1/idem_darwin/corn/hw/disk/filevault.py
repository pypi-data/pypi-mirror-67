import shutil


async def load_filevault_enabled(hub):
    """
    Find out whether FileVault is enabled, via fdesetup.
    """
    fdesetup = shutil.which("fdesetup")
    if fdesetup:
        hub.corn.CORN.filevault = (
            "FileVault is On."
            == (await hub.exec.cmd.run([fdesetup, "status"])).stdout.strip()
        )
