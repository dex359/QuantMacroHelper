# Utils.py part of QuickMacro project

import time
import ctypes
import winsound
import colorama as cs

import Engine.Config as cfg

# Colorama initialization
cs.just_fix_windows_console()


def fill(string, color):
    return {
        "white":   cs.Fore.WHITE,
        "black":   cs.Fore.BLACK,
        "red":     cs.Fore.RED,
        "green":   cs.Fore.GREEN,
        "blue":    cs.Fore.BLUE,
        "yellow":  cs.Fore.YELLOW,
        "magenta": cs.Fore.MAGENTA,
        "cyan":    cs.Fore.CYAN
    }[color] + string + cs.Fore.WHITE


def move_cursor(row, column):
    ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11), (row << 16) | column)


def get_elapsed_time(start):
    if start:
        elapsed = time.time() - start
        return fill(f"{int(elapsed // 3600):02}:{int((elapsed % 3600) // 60):02}:{int(elapsed % 60):02}", "cyan")
    else:
        return fill("N/A", "red")









