from .ANSI import fg, bg


# Foreground

BLACK = fg(30)
RED = fg(31)
GREEN = fg(32)
YELLOW = fg(33)
BLUE = fg(34)
MAGENTA = fg(35)
CYAN = fg(36)
WHITE = fg(37)

DEFAULT = fg(39)


# Bright foreground

GRAY = fg(90)
BRIGHT_RED = fg(91)
BRIGHT_GREEN = fg(92)
BRIGHT_YELLOW = fg(93)
BRIGHT_BLUE = fg(94)
BRIGHT_MAGENTA = fg(95)
BRIGHT_CYAN = fg(96)
BRIGHT_WHITE = fg(97)


# Background

BLACK_BG = bg(40)
RED_BG = bg(41)
GREEN_BG = bg(42)
YELLOW_BG = bg(43)
BLUE_BG = bg(44)
MAGENTA_BG = bg(45)
CYAN_BG = bg(46)
WHITE_BG = bg(47)

DEFAULT_BG = bg(49)


# Bright background

GRAY_BG = bg(100)
BRIGHT_RED_BG = bg(101)
BRIGHT_GREEN_BG = bg(102)
BRIGHT_YELLOW_BG = bg(103)
BRIGHT_BLUE_BG = bg(104)
BRIGHT_MAGENTA_BG = bg(105)
BRIGHT_CYAN_BG = bg(106)
BRIGHT_WHITE_BG = bg(107)
