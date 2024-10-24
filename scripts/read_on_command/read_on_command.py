# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import httplib

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
        global memory
        memory = ALProxy("ALMemory")

        # configure proxies
        self.asr.pause(True)
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
            self.tts.say("I dont know how.")
        else:
            self.tts.say("I dont know what you want.")
        

        self.asr.subscribe("read_asr")
        memory.subscribeToEvent("WordRecognized",
        "reader",
        "read")

    def exit(self):
        self.asr.unsubscribe("read_asr")


def main():

    # broker
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       NAO_IP,         # parent broker IP
       9559)       # parent broker port


    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
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