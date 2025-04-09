# EventHandler part of QuickMacro project

import pynput
import psutil
import win32gui
import win32process

# noinspection PyUnresolvedReferences
from Engine import Config as cfg
from Engine.Utils import *
from Engine.InputEmulator import EmulationError


class Handler:

    STATE_MODES = {
        0: fill("DISABLED",          "red"),
        1: fill("ENABLED",           "green"),
        2: fill("WAITING FOR FOCUS", "yellow")
    }

    STATE = 0

    def __init__(self, macro):
        self.macro = macro
        if cfg.ATTACH_TO_PROCESS and not self.macro.target:
            raise ValueError("Target process name is missing when the process binding option is enabled!")
        self.state = 0
        self.start_time = 0
        self.tracked_proc_pool = []
        self.pressed_keys = set()
        self.listener = pynput.keyboard.Listener(
            on_press = self.on_press,
            on_release = self.on_release,
            win32_event_filter = self.win32_event_filter)
    """
    def on_press(self, key):
        print("press: " + str(key))
        if not key in self.pressed_keys:
            self.pressed_keys.add(key)
            if key is cfg.SWITCH_STATE_KEY:
                self.switch()
            else:
                if Handler.STATE == 1:
                    if key in self.macro.table:
                        try:
                            self.macro.table[key][0]()
                        except EmulationError as err:
                            if err.errcode is EmulationError.MACRO_EXEC_INTERRUPTED:
                                self.macro.keyboard.release_all()
    """
    def on_press(self, key):
        try:
            # Попробуем получить vk через атрибут vk
            vk_code = key.vk if hasattr(key, 'vk') else 'N/A'
            print(f"Key: {key}, VK code: {vk_code}")
        except Exception as e:
            print(f"Error: {e}")

    def on_release(self, key):
        pass
        #print("release: " + str(key))
        #self.pressed_keys.remove(key)

    def win32_event_filter(self, msg, data):
        print(msg, data)
        if (msg == 257 or msg == 256) and data.vkCode == 112:  # Key Down/Up & F1
            print("Suppressing F1 up")
            self.listener._suppress = True
        # return False # if you return False, your on_press/on_release will not be called
        else:
            self.listener._suppress = False
        return True

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
            if proc.name() == self.macro.target and not proc in self.tracked_proc_pool:
                self.tracked_proc_pool.append(proc)

    def update(self):
        if cfg.ATTACH_TO_PROCESS:
            self.update_proc_pool()
            if Handler.STATE:
                cts = self.check_target_status()
                if cts:
                    Handler.STATE = cts
                else:
                    self.switch()
        self.render()

    def render(self):
        if cfg.ATTACH_TO_PROCESS:
            target = self.macro.target
            pids_label = ", PID(s): "
            if self.tracked_proc_pool:
                pids = fill(", ".join(str(proc.pid) for proc in self.tracked_proc_pool), "cyan")
            else:
                pids = fill("N/A", "red")
        else:
            target = "ALL"
            pids_label = ""
            pids = ""
        # Output to console
        console_out(fill("QuickMacro v1.0 ", "cyan"), 0)
        console_out("---")
        console_out("State: " + self.STATE_MODES[Handler.STATE] + " ")
        console_out("Target process: " + fill(target, "cyan") + pids_label + pids)
        console_out("Working time: " + fill(get_elapsed_time(self.start_time), "cyan"))

    def switch(self):
        if Handler.STATE:
            Handler.STATE = 0
        else:
            if cfg.ATTACH_TO_PROCESS:
                cps = self.check_target_status()
                if cps:
                    Handler.STATE = cps
                else:
                    beep("err")
                    return
            else:
                Handler.STATE = 1
        self.start_time = time.time() if Handler.STATE else 0
        beep("on" if Handler.STATE else "off")

    def loop(self):
        self.listener.start()
        if cfg.RUN_ON_STARTUP:
            self.switch()
        while True:
            self.update()
            time.sleep(1 / cfg.CONSOLE_UPDATE_FREQUENCY)