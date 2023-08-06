import plistlib
import shutil


async def load_windows_domain(hub):
    hub.corn.CORN.windowsdomain = ""
    hub.corn.CORN.windowsdomaintype = ""
    dsconfigad = shutil.which("dsconfigad")
    if dsconfigad:
        ret = (
            (await hub.exec.cmd.run([dsconfigad, "-show", "-xml"]))
            .stdout.strip()
            .encode()
        )
        if ret:
            hub.corn.CORN.windowsdomaintype = "Unknown"
            plist = plistlib.loads(ret)
            hub.corn.CORN.windowsdomain = plist.get("General Info", {}).get(
                "Active Directory Domain", ""
            )
            hub.corn.CORN.windowsdomaintype = (
                plist.get("Administrative", {}).get("Namespace mode", "").title()
            )
