import sys

from . import Text

from .INFO import ErrorCodes
from .INFO import INFVal

from .VGUI import TextWindow
from .VGUI import Lang

from .colorix import *
from .auderix import audio

colorix.init()


def ShowInfo():
    # Якщо передано --engine-no-banner,
    # банер не показуємо
    if "--engine-no-banner" in sys.argv:
        return

    Text.println(f"{Lang.name}{INFVal.ENGINE_NAME}")
    Text.println(f"{Lang.version}{INFVal.ENGINE_VERSION}")
    Text.println(f"{Lang.author}{INFVal.ENGINE_AUTHOR}")
    Text.println(f"{Lang.build}{INFVal.ENGINE_BUILD}")


ShowInfo()
