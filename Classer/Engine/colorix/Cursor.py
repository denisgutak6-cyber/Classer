from .ANSI import CSI


def up(amount=1):
    return f"{CSI}{amount}A"


def down(amount=1):
    return f"{CSI}{amount}B"


def right(amount=1):
    return f"{CSI}{amount}C"


def left(amount=1):
    return f"{CSI}{amount}D"


def move(row, column):
    return f"{CSI}{row};{column}H"


def home():
    return f"{CSI}H"


def save():
    return f"{CSI}s"


def restore():
    return f"{CSI}u"


def hide():
    return f"{CSI}?25l"


def show():
    return f"{CSI}?25h"
