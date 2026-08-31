import os
import ctypes


STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004


def is_windows():
    return os.name == "nt"


def enable_ansi():
    if not is_windows():
        return True

    kernel32 = ctypes.windll.kernel32

    for handle_id in (
        STD_OUTPUT_HANDLE,
        STD_ERROR_HANDLE
    ):
        handle = kernel32.GetStdHandle(handle_id)

        if handle == -1:
            continue

        mode = ctypes.c_uint()

        if not kernel32.GetConsoleMode(
            handle,
            ctypes.byref(mode)
        ):
            continue

        kernel32.SetConsoleMode(
            handle,
            mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        )

    return True
