# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import numpy as np
import cv2
import subprocess

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "192.168.2.251"


# Globals
reader = None
memory = None


class ReaderModule(ALModule):
    """ A simple module able to read text when told to

    """
    def __init__(self, name):
        ALModule.__init__(self, name)

        # create needed proxies
        self.tts = ALProxy("ALTextToSpeech")
        self.asr = ALProxy("ALSpeechRecognition", NAO_IP, 9559)
        self.camera = ALProxy("ALVideoDevice", NAO_IP, 9559)
        self.basic_awareness = ALProxy("ALBasicAwareness", NAO_IP, 9559)
        self.id = self.camera.subscribeCamera("python_GVM", 0, 3, 11, 30)
        global memory
        memory = ALProxy("ALMemory")

        # configure proxies
        self.basic_awareness.stopAwareness()
        self.asr.pause(True)
        self.asr.setVisualExpression(False)
        self.asr.setLanguage("English")
        self.asr.setVocabulary(['read'], False)
        self.asr.subscribe("read_asr")
        self.asr.pause(False)

        memory.subscribeToEvent("WordRecognized",
            "reader",
            "read"
        )

    def read(self, *_args):
        """ This will be called each time a word is recongnized 

        """
        word_detected = memory.getData(_args[0])
        memory.unsubscribeToEvent("WordRecognized",
            "reader")
        self.asr.unsubscribe("read_asr")

        if (word_detected[0] == 'read' and word_detected[1] > 0.4):
            self.tts.say("Reading.")
            image_data = self.camera.getImageRemote(self.id)

            # get what the na0 is looking at
            image_width = image_data[0]
            image_height = image_data[1]
            image_array = image_data[6]

            image = np.frombuffer(image_array, dtype=np.uint8).reshape(image_height, image_width, 3)

            cv2.imwrite("C:\\Users\\alexb\\Desktop\\na0\\scripts\\read_on_command\\img.png", image)

            process = subprocess.Popen(['python3', 'easyocr_reader.py', 'img.png'], 
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True
                                )
            stdout, stderr = process.communicate()
            print(stderr)
            print(stdout)
            if (len(stdout.strip()) > 0):
                self.tts.say("I think it says.")
                self.tts.say(stdout)
            else:
                "I can't find an text"

        else:
            self.tts.say("I dont know what you want.")
        

        self.asr.subscribe("read_asr")
        memory.subscribeToEvent("WordRecognized",
        "reader",
        "read")

    def exit(self):
        self.basic_awareness.startAwareness()
        self.asr.unsubscribe("read_asr")


def main():

    # broker
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       NAO_IP,         # parent broker IP
       9559)       # parent broker port

    global reader
    reader = ReaderModule("reader")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print ("Interrupted by user, shutting down")
        myBroker.shutdown()
        reader.exit()
        sys.exit(0)



if __name__ == "__main__":
    main()