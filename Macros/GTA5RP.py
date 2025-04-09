#
#

from pynput.keyboard import Key, KeyCode

MAP_DICT = {
    (1920, 1080): {
        "headwear": {303, 314, 30, 30},
        "glasses": {207, 410, 30, 30},
        "test1": {100, 100, 0, 0},
        "test2": {1000, 1000, 0, 0}
    }
}

class Macro:

    def __init__(self, keyboard, mouse):
        self.name = "GTA5RP Extender"
        self.target = "GTA5.exe"
        self.keyboard = keyboard
        self.mouse = mouse
        self.table = {
            Key.shift_r: (self.test, "Test callback")
        }


    def test(self):
        self.keyboard.click("t")