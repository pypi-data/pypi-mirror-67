import os


async def load_uname(hub):
    """
    Verify that POP linux is running on linux
    """
    (
        hub.corn.CORN.kernel,
        hub.corn.CORN.nodename,
        hub.corn.CORN.kernelrelease,
        hub.corn.CORN.kernelversion,
        _,
    ) = os.uname()

    assert (
        hub.corn.CORN.kernel == "Darwin"
    ), "POP-Darwin is only intended for MacOS based systems"

    # Hard-coded corn for mac
    hub.corn.CORN.init = "launchd"
    hub.corn.CORN.osmanufacturer = hub.corn.CORN.manufacturer = "Apple Inc."
    hub.corn.CORN.os_family = "MacOS"
    hub.corn.CORN.ps = "ps auxwww"
