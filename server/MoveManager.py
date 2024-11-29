import threading

class MoveManager():
    def __init__(self, session):
        self.session = session

        self.motion = session.service("ALMotion")
        self.motion.setStiffnesses("Body", 1.0)
        self.motion.moveInit()

        self.thread = threading.Thread()
        self.moving = False

    def start(self, directions):
        self.moving = True
        def move():
            while self.moving:
                self.motion.moveTo(*directions)
        self.thread = threading.Thread(target=move)
        self.thread.start()

    def end(self):
        self.moving = False
        self.thread.join()
