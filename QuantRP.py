import os
import sys
import ctypes

import pynput

from Engine import EventHandler

import time

def test():
    print(time.time())

if __name__ == "__main__":
    handler = EventHandler.Handler("BlueScreenView.exe")
    handler.bind(pynput.keyboard.Key.space, test)
    handler.loop()
