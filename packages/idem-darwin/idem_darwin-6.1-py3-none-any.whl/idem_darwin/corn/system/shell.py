import os


async def load_shell(hub):
    hub.corn.CORN.shell = os.environ.get("SHELL", "/bin/sh")
