import os


async def load_osarch(hub):
    hub.corn.CORN.osarch = os.uname().machine
