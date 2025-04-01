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
            return f"{int(elapsed // 3600):02}:{int((elapsed % 3600) // 60):02}:{int(elapsed % 60):02}"
        else:
            return "00:00:00"

    @staticmethod
    def play_sfx(filename):
        if not cfg.SIlENT_MODE:
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)


class Handler:

    STATE_MODE = {
        0: Helpers.format("DISABLED", "red"),
        1: Helpers.format("ENABLED", "green"),
        2: Helpers.format("WAITING FOR FOCUS", "yellow")
    }

    VALID_PROC_STATES = psutil.STATUS_RUNNING, psutil.STATUS_SLEEPING

    def __init__(self, tracked = None):
        if not tracked and cfg.ATTACH_TO_PROCESS:
            raise ValueError("Process name is missing when the process binding option is enabled!")
        self.tracked_proc_name = tracked
        self.active_proc_pool = []
        self.state = 0
        self.start_time = 0
        self.pressed_keys = set()
        self.listener = pynput.keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release
        )

    def on_press(self, key):
        if not key in self.pressed_keys:
            self.pressed_keys.add(key)
            if key is cfg.SWITCH_STATE_KEY: self.switch_state()

    def on_release(self, key):
        self.pressed_keys.remove(key)

    def check_proc_pool(self):
        # find foreground pid
        hwnd = win32gui.GetForegroundWindow()
        _, fpid = win32process.GetWindowThreadProcessId(hwnd)
        # remove closed process
        for proc in self.active_proc_pool:
            if not proc.status() in self.VALID_PROC_STATES:
                self.active_proc_pool.remove(proc)
        # update active target process list
        if not self.active_proc_pool or not fpid in (proc.pid for proc in self.active_proc_pool):
            for proc in psutil.process_iter(["name"]):
                if proc.name() == self.tracked_proc_name and not proc in self.active_proc_pool:
                    self.active_proc_pool.append(proc)
        # return new status
        if self.active_proc_pool:
            return 1 if fpid in (proc.pid for proc in self.active_proc_pool) else 2
        else:
            return 0



    def update(self):
        if cfg.ATTACH_TO_PROCESS:
            cps = self.check_proc_pool()
            if self.state:
                if cps:
                    self.state = cps
                else:
                    self.switch_state()


        Helpers.move_cursor(0, 0)
        print(Helpers.format("QuickMacro v1.0 ", "cyan"))
        Helpers.move_cursor(0, 2)
        print("State: " + self.STATE_MODE[self.state] + " " * 20)
        print("Target process: " + Helpers.format(tracked_process_name, "cyan") + " " * 20)
        print("Working time: " + Helpers.format(Helpers.get_elapsed_time(self.start_time), "cyan") + " " * 20)



    def switch_state(self):
        if self.state:
            self.state = 0
            self.start_time = 0
            Helpers.play_sfx("rsc/disabled.wav")
        else:

            self.state = 1
            self.start_time = time.time()
            Helpers.play_sfx("rsc/enabled.wav")

    def loop(self):
        self.listener.start()
        if cfg.RUN_ON_STARTUP:
            self.switch_state()
        while True:
            self.update()
            time.sleep(1)