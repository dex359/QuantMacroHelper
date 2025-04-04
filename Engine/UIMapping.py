# Map of in-game user interface elements positions

import random
import ctypes

class UIMap:

    def __init__(self, m):
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        try:
            self.map = m[(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))]
        except KeyError:
            raise RuntimeError("Macro error: UI element map missing for current screen resolution.")

    def __call__(self, area):
        if isinstance(area, str):
            tx, ty, xs, ys = self.map[area]
        elif isinstance(area, set):
            tx, ty, xs, ys = area
        else:
            raise ValueError("Incorrect parameter 'area', "
                             "should either be a string, name in UIMap table, or set with 4 parameters.")
        return tx + random.randint(0 - xs, xs), ty + random.randint(0 - ys, ys)
