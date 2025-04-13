# Input Emulator part of QuickMacro project

import time
import math
import random

from pynput import keyboard, mouse

from Engine import Interceptor
from Engine import Config as cfg


class EmulationError(Exception):

    MACRO_EXEC_INTERRUPTED = 1
    KB_DUPLICATE_KEY_PRESS = 2

    def __init__(self, msg, errcode):
        super().__init__(msg)
        self.errcode = errcode


def sleep(min_time, max_time, multiplier = 1):
    if Interceptor.State.current == Interceptor.State.ENABLED:
        time.sleep(random.randint(min_time, max_time) / 1000 * multiplier)
    else:
        raise EmulationError("Macro execution interrupted by switch handler state.",
                             EmulationError.MACRO_EXEC_INTERRUPTED)


class Keyboard:

    def __init__(self, mtpl = cfg.KB_EVENTS_SPEED_MULTIPLIER):
        self.multiplier = mtpl
        self.pressed_pool = set()
        self.controller = keyboard.Controller()

    def _uniform(self, key):
        if isinstance(key, str):
            return keyboard.KeyCode.from_char(key)
        return key

    def press(self, key, press_time = cfg.KB_PRESS_TIME, max_press_time = cfg.KB_MAX_PRESS_TIME):
        key = self._uniform(key)
        if not key in self.pressed_pool:
            self.pressed_pool.add(key)
            self.controller.press(key)
            sleep(press_time, max_press_time, self.multiplier)
        else:
            raise EmulationError("'%s' key already pressed!", EmulationError.KB_DUPLICATE_KEY_PRESS)

    def release(self, key, release_time = cfg.KB_RELEASE_TIME, max_release_time = cfg.KB_MAX_RELEASE_TIME):
        key = self._uniform(key)
        self.pressed_pool.remove(key)
        self.controller.release(key)
        sleep(release_time, max_release_time, self.multiplier)

    def click(self,
              key,
              press_time       = cfg.KB_PRESS_TIME,
              max_press_time   = cfg.KB_MAX_PRESS_TIME,
              release_time     = cfg.KB_RELEASE_TIME,
              max_release_time = cfg.KB_MAX_RELEASE_TIME):
        self.press(key, press_time, max_press_time)
        self.release(key, release_time, max_release_time)

    def release_all(self):
        for key in self.pressed_pool:
            self.controller.release(key)
            self.pressed_pool.remove(key)


class Mouse:

    def __init__(self):
        pass