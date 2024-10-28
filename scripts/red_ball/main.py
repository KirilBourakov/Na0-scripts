import sys
import time
import httplib

from threading import Timer
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.2.251"

redBall = None
memory = None


class MainModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """
    def __init__(self, name):
        ALModule.__init__(self, name)

        self.tts = ALProxy("ALTextToSpeech")
        self.motion = ALProxy("ALMotion")
        global memory
        memory = ALProxy("ALMemory")

        memory.subscribeToEvent("redBallDetected",
            "redBall",
            "onRedBallDetected")
        self.subscribed = True
        self.cooldown_active = False

    def onRedBallDetected(self, *_args):
        """ This will be called each time a red ball is detected

        """  
        if self.cooldown_active:
            return

        self.cooldown_active = True
        cooldown_timer = Timer(5, self.reset_cooldown)  # 5-second cooldown
        cooldown_timer.start()

        self.tts.say("GIMME!")

        info = memory.getData(_args[0])
        centerX, centerY, sizeX, sizeY = info[1]
        
        print(centerX)
        head_angle = self.motion.getAngles("HeadYaw", True)[0]

        self.motion.setAngles("HeadYaw",centerX,0.5)
        self.motion.setAngles("HeadPitch",-centerY, 0.5)

    def reset_cooldown(self):
        """ Resets the cooldown flag to allow event handling again """
        self.cooldown_active = False

def main():
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       NAO_IP,         # parent broker IP
       9559)       # parent broker port


    global redBall
    redBall = MainModule("redBall")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print ("Interrupted by user, shutting down")
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()