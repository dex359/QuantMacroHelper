# Console.py part of QuickMacro project
import os
import sys
import time
import struct
import ctypes
from ctypes import wintypes

import winsound
import colorama as cs

from Engine import Config as cfg
from Engine.Interceptor import State




# Colorama initialization
cs.just_fix_windows_console()


# CURSOR_INFO struct
class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize",       ctypes.c_int),
                ("bVisible",    ctypes.c_bool)]


# COORD struct
class COORD(ctypes.Structure):
    _fields_ = [("X",          wintypes.SHORT),
                ("Y",          wintypes.SHORT)]


# SMALL_RECT struct
class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left",       wintypes.SHORT),
                ("Top",        wintypes.SHORT),
                ("Right",      wintypes.SHORT),
                ("Bottom",     wintypes.SHORT)]


# SCREEN_BUFFER_INFO struct
class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [("dwSize",              COORD),
                ("dwCursorPosition",    COORD),
                ("wAttributes", wintypes.WORD),
                ("srWindow",       SMALL_RECT),
                ("dwMaximumWindowSize", COORD)]




class Console:

    STD_OUTPUT_HANDLE = -11

    LOG   = 3
    WARN  = 2
    ERROR = 1

    def __init__(self, eh):
        self.eh = eh
        self.width = 0
        self.height = 0
        self.handle = ctypes.windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE)
        self.log_buffer = []
        self._updating = False
        if cfg.CONSOLE_HIDE_CURSOR:
            self._hide_cursor()


    def _update_size(self):
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        success = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(self.handle, ctypes.byref(csbi))
        if not success:
            raise ctypes.WinError()
        width = csbi.srWindow.Right - csbi.srWindow.Left + 1
        height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
        if width != self.width or height != self.height:
            self.width = width
            self.height = height
            os.system("cls")

    def _move_cursor(self, col, row):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.handle, COORD(col, row))


    def _hide_cursor(self):
        cursor_info = CONSOLE_CURSOR_INFO()
        ctypes.windll.kernel32.GetConsoleCursorInfo(self.handle, ctypes.byref(cursor_info))
        cursor_info.bVisible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(self.handle, ctypes.byref(cursor_info))


    def _show_cursor(self):
        cursor_info = CONSOLE_CURSOR_INFO()
        ctypes.windll.kernel32.GetConsoleCursorInfo(self.handle, ctypes.byref(cursor_info))
        cursor_info.bVisible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(self.handle, ctypes.byref(cursor_info))


    @staticmethod
    def beep(msg):
        if not cfg.SILENT_MODE:
            if msg == "on":
                winsound.PlaySound("rsc/enabled.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif msg == "off":
                winsound.PlaySound("rsc/disabled.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            elif msg == "err":
                winsound.Beep(200, 90)
                winsound.Beep(200, 90)


    @staticmethod
    def fill(string, color):
        return {
            "white":   cs.Fore.WHITE,
            "black":   cs.Fore.BLACK,
            "red":     cs.Fore.RED,
            "green":   cs.Fore.GREEN,
            "blue":    cs.Fore.BLUE,
            "yellow":  cs.Fore.YELLOW,
            "magenta": cs.Fore.MAGENTA,
            "cyan":    cs.Fore.CYAN,
            "grey":    cs.Fore.WHITE + cs.Style.DIM,
        }[color] + string + cs.Style.RESET_ALL


    @staticmethod
    def _len(string):
        l = 0
        r = True
        for s in string:
            if s == "\x1b":
                r = False
            if r:
                l += 1
            elif s == "m":
                r = True
        return  l


    def _ljust(self, string, arg):
        l = self._len(string)
        if l < arg:
            return string + " " * (arg - l)
        else:
            return string


    def get_elapsed_time(self, start):
        if start:
            elapsed = time.time() - start
            return self.fill(f"{int(elapsed // 3600):02}:{int((elapsed % 3600) // 60):02}:{int(elapsed % 60):02}", "cyan")
        else:
            return self.fill("00:00:00", "grey")



    def out(self, msg, lvl = 3, flush = True):
        self.log_buffer.insert(0, (time.strftime("%H:%M:%S", time.localtime(time.time())), msg, lvl))
        if flush:
            self.update()


    def update(self):
        if self._updating:
            return
        self._updating = True
        header_l = []
        header_r = []
        body = []
        self._update_size()
        # Сontent generation
        # header
        header_l.append(self.fill("QuickMacro v1.0", "cyan"))
        spacer = self.fill("---", "grey")
        header_l.append(spacer)
        header_l.append("State: " + {State.DISABLED: self.fill("DISABLED", "red"),
                                     State.ENABLED:  self.fill("ENABLED", "green"),
                                     State.WAITING:  self.fill("WAITING FOR FOCUS", "yellow")}[State.current])
        if cfg.ATTACH_TO_PROCESS:
            header_l.append("Target process: " + self.fill(self.eh.macro.target, "cyan"))
            if self.eh.tracked_proc_pool:
                header_l.append("PID(s): " + self.fill(", ".join(str(proc.pid) for proc in self.eh.tracked_proc_pool), "cyan"))
            else:
                header_l.append("PID(s): " + self.fill("N/A", "grey"))
        else:
            header_l.append("Target process: " + self.fill("ALL", "cyan"))
        header_l.append("Working time: " + self.get_elapsed_time(self.eh.start_time))
        header_l.append(spacer)
        header_l.append("")
        header_r.append("")
        lj = max(len(cfg.SWITCH_STATE_KEY), 5)
        ssk = self._ljust(self.fill("<" + cfg.SWITCH_STATE_KEY + ">", "cyan"), lj)
        if cfg.RUN_ON_STARTUP:
            ros = self._ljust("True", lj)
        else:
            ros = self._ljust(self.fill("False", "grey"), lj)
        if cfg.ATTACH_TO_PROCESS:
            atp = self._ljust("True", lj)
        else:
            atp = self._ljust(self.fill("False", "grey"), lj)
        if cfg.SILENT_MODE:
            sm = self._ljust("True", lj)
        else:
            sm = self._ljust(self.fill("False", "grey"), lj)
        cll = self._ljust({3: self.fill("ALL", "green"),
                           2: self.fill("WARN", "yellow"),
                           1: self.fill("ERROR", "red"),
                           0: self.fill(" - ", "grey")}[cfg.CONSOLE_LOG_LEVEL], lj)
        header_r.append(self.fill("switch key: ", "grey") + ssk)
        header_r.append(self.fill("run on startup: ", "grey") + ros)
        header_r.append(self.fill("attach to process: ", "grey") + atp)
        header_r.append(self.fill("silent mode: ", "grey") + sm)
        header_r.append(self.fill("console log-level: ", "grey") + cll)
        # body
        for x in range(max(len(header_l), len(header_r))):
            try: left = header_l[x]
            except IndexError: left = ""
            try: right = header_r[x]
            except IndexError: right = ""
            if cfg.CON_LEFT_MARGIN + self._len(left + " " + right) + cfg.CON_RIGHT_MARGIN > self.width:
                left = left[:-((cfg.CON_LEFT_MARGIN + self._len(left + " " + right) + cfg.CON_RIGHT_MARGIN) - self.width - 3)] + "..."
            body.append(cfg.CON_LEFT_MARGIN * " " + left +
                        " " * (self.width - (cfg.CON_LEFT_MARGIN + self._len(left + right) + cfg.CON_RIGHT_MARGIN)) +
                        right + cfg.CON_RIGHT_MARGIN * " ")
        # log
        for x in range(cfg.CON_TOP_MARIN):
            body.insert(0, " " * self.width)
        head = len(body)
        for t, m, l in self.log_buffer:
            if len(body) + cfg.CON_BOTTOM_MARGIN + 1 >= self.height:
                break
            if l > cfg.CONSOLE_LOG_LEVEL:
                continue
            msg_time = self.fill(t, "grey")
            msg_lvl = " [" + {3: self.fill("LOG", "green"),
                             2: self.fill("WARN", "yellow"),
                             1: self.fill("ERROR", "red")}[l] + "] "
            if self._len(msg_time) + self._len(msg_lvl) + len(m) + cfg.CON_LEFT_MARGIN + cfg.CON_RIGHT_MARGIN < self.width:
                m = self._ljust(m, self.width - (self._len(msg_time) + self._len(msg_lvl) + len(m) + cfg.CON_LEFT_MARGIN + cfg.CON_RIGHT_MARGIN))
            body.insert(head, " " * cfg.CON_LEFT_MARGIN + msg_time + msg_lvl + m)
        for x in range(cfg.CON_BOTTOM_MARGIN):
            body.append(" " * self.width)
        # draw out
        self._move_cursor(0, 0)
        print("\n".join(body), flush = True)
        self._updating = False
