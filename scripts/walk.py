from pynput import keyboard
import sys
from time import sleep
import qi


def kb(key):
    while True:
        force = [0,0,0]
        if key == "esc":
            sys.exit(0)

        # forward back
        if key == "up":
            force[0] += 0.1
        if key == "down":
            force[0] -= 0.1

        # side to side
        if key == "right":
            force[1] += 0.1
        if key == "left":
            force[1] -= 0.1        
        
        # turn
        if key == "d":
            force[2] += 0.1
        if key == "a":
            force[2] -= 0.1
        print('running')
        # motion.moveTo(*force, _async=True)
def release(key):
    pass

def main():
    # robot_ip = "192.168.2.251"
    # port = 9559
    # session = qi.Session()
    # session.connect(f"tcp://{robot_ip}:{port}")

    # global motion
    # motion = session.service("ALMotion")
    # motion.setStiffnesses("Body", 1.0)
    # motion.moveInit()
    try:
        while True:
            with keyboard.Events() as events:
                event = events.get(0.1)
                print(event)
                if event is not None:
                    print(event.key)
                    kb(event.key)
    except KeyboardInterrupt:
        print("Ending program")

if __name__ == "__main__":
    main()

