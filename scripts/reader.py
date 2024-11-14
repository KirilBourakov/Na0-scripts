import qi
import time
import sys
import os
import cv2
import numpy as np
import easyocr

class Reader():
    def __init__(self, app):
        app.start()
        session = app.session

        self.tts = session.service("ALTextToSpeech")
        self.asr = session.service("ALSpeechRecognition")
        self.camera = session.service("ALVideoDevice")
        self.id = self.camera.subscribeCamera("python_GVM", 0, 3, 11, 30)
        self.basic_awareness = session.service("ALBasicAwareness")
        self.memory = session.service("ALMemory")

        # set up asr
        self.basic_awareness.stopAwareness()
        self.asr.setLanguage("English")
        self.asr.setVocabulary(["read"], False)
        self.asr.subscribe("asr")

        self.subscriber = self.memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.on_word_recognized)
    
    def on_word_recognized(self, value):
        print(value)
        if value[0] == 'read' and value[1] > 0.4:
            self.tts.say("I am reading")

            image_data = self.camera.getImageRemote(self.id)
            # get what the na0 is looking at
            image_width = image_data[0]
            image_height = image_data[1]
            image_array = image_data[6]

            image = np.frombuffer(image_array, dtype=np.uint8).reshape(image_height, image_width, 3)
            path = os.path.join(os.path.dirname(__file__), sys.argv[1])
            cv2.imwrite(path, image)
            # read
            reader = easyocr.Reader(['en'], gpu=False, verbose=False)
            text = reader.readtext(sys.argv[1])
            words = ""
            for t in text:
                words += " " +t[-2]

            if (len(words.strip()) > 0):
                self.tts.say("I think it says.")
                self.tts.say(words)
            else:
                self.tts.say("I can't find an text")
        elif (value[1] > 0.3):
            self.tts.say("I don't know what you want.")

    def run(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.asr.unsubscribe("asr")
            print("Interrupted by user, stopping.")
            self.app.stop()
            sys.exit(0)


def main(IP, PORT):
    url =  f"tcp://{IP}:{PORT}"
    app = qi.Application(["HumanGreeter", "--qi-url=" + url])

    reader = Reader(app)
    reader.run()

if __name__ == "__main__":
    IP = "192.168.2.251"
    PORT = 9559
    main(IP, PORT)