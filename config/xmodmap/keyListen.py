#!/usr/bin/env python3
import subprocess
import time
from evdev import InputDevice, ecodes

dev = InputDevice('/dev/input/by-id/usb-CM_Storm_Keyboard_--_QuickFire_XT-event-kbd')
ids = ["clion", "pycharm", ".c", ".h"]
keycodes = [126, 29]

clion=False
for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            if clion:
                focus = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"], universal_newlines=True)
                if not any(id in focus.lower() for id in ids):
                    clion=False
                    subprocess.call(["/home/akepka/xmodmap/arrowsClionUnset.sh"])

            if event.code in keycodes: 
                focus = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"], universal_newlines=True)
                if event.value == 1 and any(id in focus.lower() for id in ids) and not clion:
                    clion=True
                    subprocess.call(["xmodmap", "/home/akepka/xmodmap/clionHack"])
                elif event.value == 0 and clion:
                    clion=False
                    subprocess.call(["xmodmap", "/home/akepka/xmodmap/clionHackRevert"])

