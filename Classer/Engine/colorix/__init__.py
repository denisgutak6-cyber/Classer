from .ANSI import *
from .Colors import *
from .Cursor import *
from .Terminal import *
from .Windows import *
from .Converter import *
from .Utils import *


_initialized = False


def init():
    global _initialized

    if _initialized:
        return

    enable_ansi()
    _initialized = True


def deinit():
    global _initialized
    _initialized = False


def colorix_init():
    init()
    