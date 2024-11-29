import threading

class MoveManager():
    def __init__(self, session):
        self.session = session
        self.motion = session.service("ALMotion")
        self.motion.setStiffnesses("Body", 1.0)
        self.motion.moveInit()

    def start(self, directions):
        self.motion.move(*directions)

    def end(self):
        self.motion.stopWalk()
