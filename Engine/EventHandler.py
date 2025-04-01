import time

import ctypes
import pynput
import winsound
import colorama as cs

from Engine import Config as cfg

# Colorama initialization
cs.just_fix_windows_console()

class Handler:

    def __init__(self):
        self.start_time = 0
        self.running = False
        self.pressed_keys = set()
        self.listener = pynput.keyboard.Listener(
            on_press = self._on_press,
            on_release = self._on_release
        )

    def _on_press(self, key):
        if not key in self.pressed_keys:
            self.pressed_keys.add(key)
            if key is cfg.SWITCH_STATE_KEY: self.switch_key_interception()

    def _on_release(self, key):
        self.pressed_keys.remove(key)

    def _get_elapsed_time(self):
        if self.start_time:
            elapsed = time.time() - self.start_time
            return f"{int(elapsed // 3600):02}:{int((elapsed % 3600) // 60):02}:{int(elapsed % 60):02}"
        else:
            return "00:00:00"

    def _voice(self, filename):
        if not cfg.SIlENT_MODE:
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def _move_console_cursor(self, horizontal, vertical):
        ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(-11),
                                                        (vertical << 16) | horizontal)

    def update(self):
        self._move_console_cursor(0, 0)
        print(cs.Fore.CYAN + "QuantRP Macro Engine v 1.0" + "\n")
        self._move_console_cursor(0, 2)
        print(cs.Fore.WHITE + "Status: " + (cs.Fore.GREEN + "ENABLED" if self.running else cs.Fore.RED + "DISABLED"), end = "")
        print(cs.Fore.WHITE + ", Working time: " + cs.Fore.CYAN + self._get_elapsed_time() + "    ")
        self._move_console_cursor(0, 4)

    def switch_key_interception(self):
        self.running = not self.running
        if self.running:
            self.start_time = time.time()
            winsound.PlaySound("rsc/enabled.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            self.start_time = 0
            winsound.PlaySound("rsc/disabled.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.update()

    def loop(self):
        self.listener.start()
        self.switch_key_interception()
        while True:
            self.update()
            time.sleep(1)