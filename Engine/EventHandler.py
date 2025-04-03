# EventHandler part of QuickMacro project

import time
import ctypes

import pynput
import psutil
import win32gui
import win32process
import winsound
import colorama as cs

from Engine import Config as cfg


# Colorama initialization
cs.just_fix_windows_console()


class Helpers:

    @staticmethod
    def format(string, color):
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

    @staticmethod
    def move_cursor(horizontal, vertical):
        ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11),
                                                        (vertical << 16) | horizontal)
    @staticmethod
    def get_elapsed_time(start):
        if start:
            elapsed = time.time() - start
            return Helpers.format(f"{int(elapsed // 3600):02}:{int((elapsed % 3600) // 60):02}:{int(elapsed % 60):02}", "cyan")
        else:
            return Helpers.format("N/A", "red")

    @staticmethod
    def play_sfx(filename):
        if not cfg.SIlENT_MODE:
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

    @staticmethod
    def console_out(string, row = None):
        if not row is None:
            Helpers.move_cursor(row, 0)
        print(string.ljust(cfg.CONSOLE_WIDTH))

class Handler:

    STATE_MODES = {
        0: Helpers.format("DISABLED", "red"),
        1: Helpers.format("ENABLED", "green"),
        2: Helpers.format("WAITING FOR FOCUS", "yellow")
    }

    def __init__(self, target = None):
        if cfg.ATTACH_TO_PROCESS and not target:
            raise ValueError("Target process name is missing when the process binding option is enabled!")
        self.state = 0
        self.start_time = 0
        self.target_proc_name = target
        self.tracked_proc_pool = []
        self.pressed_keys = set()
        self.listener = pynput.keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release
        )

    def on_press(self, key):
        if not key in self.pressed_keys:
            self.pressed_keys.add(key)
            if key is cfg.SWITCH_STATE_KEY: self.switch()

    def on_release(self, key):
        self.pressed_keys.remove(key)

    def check_target_status(self):
        hwnd = win32gui.GetForegroundWindow()
        _, fpid = win32process.GetWindowThreadProcessId(hwnd)
        if self.tracked_proc_pool:
            return 1 if fpid in (proc.pid for proc in self.tracked_proc_pool) else 2
        else:
            return 0

    def update_proc_pool(self):
        # remove from list dead processes
        for proc in self.tracked_proc_pool:
            try:
                assert proc.is_running() and proc.status() != psutil.STATUS_ZOMBIE
            except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied, AssertionError):
                self.tracked_proc_pool.remove(proc)
        # add to list new launched processes
        for proc in psutil.process_iter(["name"]):
            if proc.name() == self.target_proc_name and not proc in self.tracked_proc_pool:
                self.tracked_proc_pool.append(proc)

    def update(self, check_state = True):
        if cfg.ATTACH_TO_PROCESS:
            self.update_proc_pool()
            if self.state:
                cts = self.check_target_status()
                if cts:
                    self.state = cts
                else:
                    self.switch()
        self.render()

    def render(self):
        if cfg.ATTACH_TO_PROCESS:
            target = self.target_proc_name
            pids_label = ", PID(s): "
            if self.tracked_proc_pool:
                pids = Helpers.format(", ".join(str(proc.pid) for proc in self.tracked_proc_pool), "cyan")
            else:
                pids = Helpers.format("N/A", "red")
        else:
            target = "ALL"
            pids_label = ""
            pids = ""
        # Output to console
        Helpers.console_out(Helpers.format("QuickMacro v1.0 ", "cyan"), 0)
        Helpers.console_out("---")
        Helpers.console_out("State: " + self.STATE_MODES[self.state] + " ")
        Helpers.console_out("Target process: " + Helpers.format(target, "cyan") + pids_label + pids)
        Helpers.console_out("Working time: " + Helpers.format(Helpers.get_elapsed_time(self.start_time), "cyan"))

    def switch(self):
        if self.state:
            self.state = 0
        else:
            if cfg.ATTACH_TO_PROCESS:
                cps = self.check_target_status()
                if cps:
                    self.state = cps
                else:
                    return
            else:
                self.state = 1
        self.start_time = time.time() if self.state else 0
        Helpers.play_sfx("rsc/enabled.wav" if self.state else "rsc/disabled.wav")

    def loop(self):
        self.listener.start()
        if cfg.RUN_ON_STARTUP:
            self.switch()
        while True:
            self.update()
            time.sleep(1/cfg.UPDATE_FREQUENCY)