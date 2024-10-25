


import keyboard
import sys
from time import sleep
from naoqi import ALProxy


def kb(motion):
    while True:
        force = [0,0,0]
        if keyboard.is_pressed("esc"):
            sys.exit(0)

        # forward back
        if keyboard.is_pressed("up") and not keyboard.is_pressed("down"):
            force[0] += 0.1
        if not keyboard.is_pressed("up") and keyboard.is_pressed("down"):
            force[0] -= 0.1

        # side to side
        if not keyboard.is_pressed("left") and keyboard.is_pressed("right"):
            force[1] += 0.1
        if not keyboard.is_pressed("right") and keyboard.is_pressed("left"):
            force[1] -= 0.1
        
        # turn
        if not keyboard.is_pressed("a") and keyboard.is_pressed("d"):
            force[2] += 0.1
        if keyboard.is_pressed("a") and not keyboard.is_pressed("d"):
            force[2] -= 0.1

        motion.post.moveTo(*force)



def main():
    motion = ALProxy("ALMotion", "192.168.2.251", 9559)
    motion.setStiffnesses("Body", 1.0)
    motion.moveInit()
    kb(motion)

if __name__ == "__main__":
    main()

