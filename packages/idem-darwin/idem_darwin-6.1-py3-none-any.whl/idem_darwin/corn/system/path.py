import os
import sys


async def load_cwd(hub):
    """
    Current working directory
    """
    hub.corn.CORN.cwd = os.getcwd()


async def load_path(hub):
    """
    Return the path
    """
    # Provides:
    #   path
    hub.corn.CORN.path = os.environ.get("PATH", "").strip()


async def load_pythonpath(hub):
    """
    Return the Python path
    """
    # Provides:
    #   pythonpath
    hub.corn.CORN.pythonpath = sorted(sys.path, key=str.casefold)


async def load_executable(hub):
    """
    Return the python executable in use
    """
    # Provides:
    #   pythonexecutable
    hub.corn.CORN.pythonexecutable = sys.executable
