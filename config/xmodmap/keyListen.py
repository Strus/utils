#!/usr/bin/env python3
import subprocess
import time
from evdev import InputDevice, ecodes

dev = InputDevice('/dev/input/by-id/usb-CM_Storm_Keyboard_--_QuickFire_XT-event-kbd')

clion=False
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        if clion:
            focus = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"], universal_newlines=True)
            if not ("clion" in focus.lower() or "pycharm" in focus.lower() or ".c" in focus.lower()):
                clion=False
                subprocess.call(["/home/akepka/xmodmap/arrowsClionUnset.sh"])

        if event.code == 126 or event.code == 37: 
            focus = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"], universal_newlines=True)
            if event.value == 1 and ("clion" in focus.lower() or "pycharm" in focus.lower() or ".c" in focus.lower()) and not clion:
                clion=True
                subprocess.call(["/home/akepka/xmodmap/arrowsClionSet.sh"])
            elif event.value == 0 and clion:
                clion=False
                subprocess.call(["/home/akepka/xmodmap/arrowsClionUnset.sh"])

