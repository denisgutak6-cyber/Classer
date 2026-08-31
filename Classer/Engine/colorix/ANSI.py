ESC = "\033"
CSI = ESC + "["


def fg(code):
    return f"{CSI}{code}m"


def bg(code):
    return f"{CSI}{code}m"


def rgb(r, g, b):
    return f"{CSI}38;2;{r};{g};{b}m"


def bg_rgb(r, g, b):
    return f"{CSI}48;2;{r};{g};{b}m"


def color256(value):
    return f"{CSI}38;5;{value}m"


def bg_color256(value):
    return f"{CSI}48;5;{value}m"


RESET = f"{CSI}0m"

BOLD = f"{CSI}1m"
DIM = f"{CSI}2m"
ITALIC = f"{CSI}3m"
UNDERLINE = f"{CSI}4m"
BLINK = f"{CSI}5m"
REVERSE = f"{CSI}7m"
HIDDEN = f"{CSI}8m"
STRIKE = f"{CSI}9m"
