import datetime
import dateutil.tz as tz
import locale
import sys


async def load_info(hub):
    """
    Provides
        defaultlanguage
        defaultencoding
    """
    try:
        (
            hub.corn.CORN.locale_info.defaultlanguage,
            hub.corn.CORN.locale_info.defaultencoding,
        ) = locale.getdefaultlocale()
    except Exception:  # pylint: disable=broad-except
        # locale.getdefaultlocale can ValueError!! Catch anything else it might do
        hub.corn.CORN.locale_info.defaultlanguage = "unknown"
        hub.corn.CORN.locale_info.defaultencoding = "unknown"


async def load_default_encoding(hub):
    hub.corn.CORN.locale_info.detectedencoding = sys.getdefaultencoding() or "ascii"


async def load_timezone(hub):
    hub.corn.CORN.locale_info.timezone = datetime.datetime.now(tz.tzlocal()).tzname()
