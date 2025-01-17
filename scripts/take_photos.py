import qi
import time
import sys
import os
import cv2
import numpy as np

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
    
    def photo(self):
        
        for i in range(3):
            self.tts.say("Click")
            image_data = self.camera.getImageRemote(self.id)
            # get what the na0 is looking at
            image_width = image_data[0]
            image_height = image_data[1]
            image_array = image_data[6]

            image = np.frombuffer(image_array, dtype=np.uint8).reshape(image_height, image_width, 3)
            path = os.path.join(os.path.dirname(__file__), f'{i}.jpg')
            cv2.imwrite(path, image)

def main(IP, PORT):
    url =  f"tcp://{IP}:{PORT}"
    app = qi.Application(["HumanGreeter", "--qi-url=" + url])

    reader = Reader(app)
    reader.photo()

if __name__ == "__main__":
    IP = "192.168.2.251"
    PORT = 9559
    main(IP, PORT)