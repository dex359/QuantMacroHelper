# Input Emulator part of QuickMacro project

import time
import math
import random

from pynput import keyboard, mouse

from Engine import EventHandler as eh
from Engine import Config as cfg


class EmulationError(Exception):

    def __init__(self, msg):
        super().__init__(msg)


def sleep(min_time, max_time):
    if eh.Handler.state:
        time.sleep(random.randint(min_time, max_time)/1000)
    else:
        raise EmulationError("Macro execution interrupted by switch handler state.")


class Keyboard:

    def __init__(self, multiplier = cfg.KB_EVENTS_SPEED_MULTIPLIER):
        self.mp = multiplier
        self.keyboard = keyboard.Controller()

    def press(self,
              key,
              press_min_t = cfg.MIN_PRESS_TIME,
              press_max_t = cfg.MAX_PRESS_TIME):
        self.keyboard.press(key)
        sleep(press_min_t * self.mp, press_max_t * self.mp)

    def release(self,
                key,
                release_min_t = cfg.MIN_RELEASE_TIME,
                release_max_t = cfg.MAX_RELEASE_TIME):
        self.keyboard.release(key)
        sleep(release_min_t * self.mp, release_max_t * self.mp)

    def click(self,
              key,
              press_min_t   = cfg.MIN_PRESS_TIME,
              press_max_t   = cfg.MAX_PRESS_TIME,
              release_min_t = cfg.MIN_RELEASE_TIME,
              release_max_t = cfg.MAX_RELEASE_TIME):
        self.press(key, press_min_t, press_max_t)
        self.release(key, release_min_t, release_max_t)



class Mouse:

    def __init__(self,
                 multiplier     = cfg.MS_EVENTS_SPEED_MULTIPLIER,
                 discretization = cfg.MS_MOVS_DISCRETIZATION):
        self.mp = multiplier
        self.dc = discretization
        self.mouse = mouse.Controller()

    def press(self,
              button,
              press_min_t = cfg.MIN_PRESS_TIME,
              press_max_t = cfg.MAX_PRESS_TIME):
        self.mouse.press(button)
        sleep(press_min_t * self.mp, press_max_t * self.mp)

    def release(self,
                button,
                release_min_t = cfg.MIN_RELEASE_TIME,
                release_max_t = cfg.MAX_RELEASE_TIME):
        self.mouse.release(button)
        sleep(release_min_t * self.mp, release_max_t * self.mp)

    def click(self,
              button,
              press_min_t   = cfg.MIN_PRESS_TIME,
              press_max_t   = cfg.MAX_PRESS_TIME,
              release_min_t = cfg.MIN_RELEASE_TIME,
              release_max_t = cfg.MAX_RELEASE_TIME):
        self.press(button, press_min_t, press_max_t)
        self.release(button, release_min_t, release_max_t)

    def move(self, tx, ty):
        cx, cy = self.mouse.position
