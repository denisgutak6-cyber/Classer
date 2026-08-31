import re


ANSI_PATTERN = re.compile(
    r"\033(?:\[[0-9;?]*[ -/]*[@-~]|\][^\a]*(?:\a|\033\\))"
)


def strip(text):
    return ANSI_PATTERN.sub("", text)


def has_ansi(text):
    return ANSI_PATTERN.search(text) is not None


def convert(text):
    return text
