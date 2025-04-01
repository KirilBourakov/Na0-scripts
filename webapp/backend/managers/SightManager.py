from threading import Thread, Event
from time import sleep
import numpy as np
import cv2
import os

class SightManager():
    def __init__(self, session):
        self.camera = session.service("ALVideoDevice")
        self.id = self.camera.subscribeCamera("python_GVM", 0, 3, 11, 30)

        self.thread = None

    def start(self):
        if self.thread is None or not self.thread.is_alive():
            self.thread = CameraThread(self.camera, self.id) 
            self.thread.start() 
        else:
            print("Thread is already running.") 

    def end(self):
        self.thread.stop()
        self.thread.join()
        self.thread = CameraThread(self.camera, self.id)


class CameraThread(Thread):
    def __init__(self, camera, id, *args, **kwargs):
        super(CameraThread, self).__init__(*args, **kwargs)
        self._stop_event = Event()

        self.camera = camera
        self.id = id

    def run(self):
        print(f'starting. self.stopped = {self.stopped()}')
        while(not self.stopped()):
            self.getPhoto()
            sleep(20)

    def getPhoto(self):
        print('getting photo')
        image_data = self.camera.getImageRemote(self.id)
        # get what the na0 is looking at
        image_width = image_data[0]
        image_height = image_data[1]
        image_array = image_data[6]

        image = np.frombuffer(image_array, dtype=np.uint8).reshape(image_height, image_width, 3)
        path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'static', 'sight', 'view.jpg'
        )
        
        print(f'writing to {path}')
        cv2.imwrite(path, image)


    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    
if __name__ == '__main__':
    import qi


    session = qi.Session()
    ip = "192.168.2.251"
    session.connect(f"tcp://{ip}:{9559}")

    sight = SightManager(session)
    print('------ Starting ------')
    sight.start()
    sleep(60)
    print('------ Ending ------')
    sight.end()