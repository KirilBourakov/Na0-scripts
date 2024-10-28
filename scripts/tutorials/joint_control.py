


import keyboard
import sys
from naoqi import ALProxy
import almath


motion = ALProxy("ALMotion", "192.168.2.251", 9559)
motion.setStiffnesses("Head", 1.0)
motion.moveInit()

def turnHead():
    motion.setAngles("HeadYaw",30.0*almath.TO_RAD,0.1)

def timedTurnHead():
    names = "HeadYaw"
    angleLists = 1.0
    times = 1.0
    isAbsolute = True
    motion.angleInterpolation(names, angleLists, times, isAbsolute)

def timedHead():
    names = "HeadYaw"
    angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
    times      = [1.0,  2.0, 3.0,  4.0, 5.0]
    isAbsolute = True
    motion.angleInterpolation(names, angleLists, times, isAbsolute)

def twoNames():
    names = ["HeadYaw", "HeadPitch"]
    angleLists = [[1.0, -1.0, 1.0, -1.0], [-1.0]]
    times = [[1.0,  2.0, 3.0,  4.0], [ 5.0]]
    isAbsolute = True
    motion.angleInterpolation(names, angleLists, times, isAbsolute)

if __name__ == "__main__":
    keyboard.add_hotkey('1', turnHead)
    keyboard.add_hotkey('2', timedTurnHead)
    keyboard.add_hotkey('3', timedHead)
    keyboard.add_hotkey('4', twoNames)

    while True:
        if keyboard.is_pressed("esc"):
            sys.exit(0)

