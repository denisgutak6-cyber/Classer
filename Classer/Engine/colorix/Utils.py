from .ANSI import rgb, bg_rgb, color256, bg_color256


def RGB(r, g, b):
    return rgb(r, g, b)


def BG_RGB(r, g, b):
    return bg_rgb(r, g, b)


def COLOR256(value):
    return color256(value)


def BG_COLOR256(value):
    return bg_color256(value)


def gradient(text, start, end):
    if not text:
        return ""

    result = []

    length = max(len(text) - 1, 1)

    for i, char in enumerate(text):
        t = i / length

        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)

        result.append(
            RGB(r, g, b) + char
        )

    return "".join(result)
