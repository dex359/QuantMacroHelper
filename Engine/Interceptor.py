# EventHandler part of QuickMacro project
import time

import pynput
import psutil
import win32gui
import win32process

# noinspection PyUnresolvedReferences
from Engine.Utils import *
from Engine import Config as cfg
from Engine.KeyCodes import Key, EVENT
from Engine.test import move_cursor as mc, get_console_size as gcs
cw, ch = gcs()



#Common for all project flag
class State:

    current  = 0

    DISABLED = 0
    ENABLED  = 1
    WAITING  = 2


from Engine.Console import Console


class Main:

    def __init__(self, macro):
        if cfg.ATTACH_TO_PROCESS and not macro.target:
            raise ValueError("Target process name is missing when the process binding option is enabled!")
        self.macro = macro
        self.console = Console(self)
        self.start_time = 0
        self.tracked_proc_pool = []
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
        pass
        """
        try:
            # Попробуем получить vk через атрибут vk
            vk_code = key.vk if hasattr(key, 'vk') else 'N/A'
            print(f"Key: {key}, VK code: {vk_code}")
        except Exception as e:
            print(f"Error: {e}")"""

    def on_release(self, key):
        pass
        #print("release: " + str(key))
        #self.pressed_keys.remove(key)

    def win32_event_filter(self, msg, data):
        if msg == EVENT.WM_KEYDOWN:
            self.console.out("press: " + Key(data.vkCode).key_name)
            if Key(data.vkCode) is Key("home"):
                self.switch()
        if msg == EVENT.WM_KEYUP:
            pass
            #self.log("Keyup", "WARN")
        """
        print(msg, data)
        if (msg == 257 or msg == 256) and data.vkCode == 112:  # Key Down/Up & F1
            print("Suppressing F1 up")
            self.listener._suppress = True
        # return False # if you return False, your on_press/on_release will not be called
        else:
            self.listener._suppress = False
        return True"""

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
            if State.current:
                cts = self.check_target_status()
                if cts:
                    State.current = cts
                else:
                    self.switch()
        self.console.update()

    """def render(self):
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
        move_cursor(self.con_head, 0)
        console_out("----  LOG  ----")
        console_out(fill("QuickMacro v1.0 ", "cyan") + " = " + str(self.con_head))
        console_out("---- STATE ----")
        console_out("State: " + self.STATE_MODES[Main.STATE] + " ")
        console_out("Target process: " + fill(target, "cyan") + pids_label + pids)
        console_out("Working time: " + fill(get_elapsed_time(self.start_time), "cyan"))"""

    """def log(self, msg, level = "LOG"): # also "WARN" and "ERROR"
        if self.con_head > 22:
            move_cursor(30, 0)
            print()
            move_cursor(22, 0)
            self.con_head = 22
        move_cursor(self.con_head, 0)
        print(time.strftime("%H:%M:%S", time.localtime(time.time())), end = " ")
        print("[" + fill(level, {"LOG": "green", "WARN": "yellow", "ERROR": "red"}[level]) + "]", end = " ")
        print(str(msg)  + " = " + str(self.con_head))
        self.con_head += 1
        self.render()"""

    def switch(self):
        if State.current:
            State.current = State.DISABLED
        else:
            if cfg.ATTACH_TO_PROCESS:
                self.update_proc_pool()
                cps = self.check_target_status()
                if cps:
                    State.current = cps
                else:
                    self.console.beep("err")
                    return
            else:
                State.current = State.ENABLED
        self.start_time = time.time() if State.current else 0
        self.console.beep("on" if State.current else "off")

    def loop(self):
        self.listener.start()
        if cfg.RUN_ON_STARTUP:
            self.switch()
        while True:
            self.update()
            time.sleep(1 / cfg.CONSOLE_UPDATE_FREQUENCY)