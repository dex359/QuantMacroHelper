# Input Emulator part of QuickMacro project

import time
import random

import pynput

from Engine import EventHandler


class EmulationError(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class Keyboard:

    def __init__(self):
        pass


class Mouse:

    def __init__(self):
        pass