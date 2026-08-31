import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def clear_line():
    sys.stdout.write("\033[2K\r")
    sys.stdout.flush()


def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def title(text):
    if os.name == "nt":
        os.system(f"title {text}")
    else:
        sys.stdout.write(f"\033]0;{text}\007")
        sys.stdout.flush()


def bell():
    sys.stdout.write("\a")
    sys.stdout.flush()
    