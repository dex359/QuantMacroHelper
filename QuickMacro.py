import os
import sys
import shutil
import ctypes

from Engine import EventHandler
from Engine.InputEmulator import Keyboard, Mouse

# load working scenario
from Macros.GTA5RP import Macro


# noinspection PyBroadException
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    wt_path = shutil.which("wt.exe")
    if wt_path:
        command = f'powershell -NoExit -Command "python \'{script_path}\'"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", wt_path, f'--startingDirectory "{script_dir}" {command}', None, 1)
    else:
        python_path = sys.executable
        command = f'/k cd /d "{script_dir}" && "{python_path}" "{script_path}"'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", command, None, 1)
    sys.exit()

if __name__ == "__main__":
    handler = EventHandler.Handler(Macro(Keyboard(),Mouse()))
    handler.loop()
