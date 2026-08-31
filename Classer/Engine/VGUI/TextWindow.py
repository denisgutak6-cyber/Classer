import ctypes

def cr_window(title, text, window_type=2):
    icons = {
        0: 0x10,  # MB_ICONERROR
        1: 0x30,  # MB_ICONWARNING
        2: 0x40   # MB_ICONINFORMATION
    }

    flags = 0x04  # MB_YESNO

    if window_type in icons:
        flags |= icons[window_type]

    result = ctypes.windll.user32.MessageBoxW(
        0,
        text,
        title,
        flags
    )

    return result == 6  # IDYES
