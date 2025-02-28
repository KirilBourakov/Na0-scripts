class MoveManager():
    def __init__(self, session):
        self.session = session
        self.motion = session.service("ALMotion")
        self.motion.setStiffnesses("Body", 1.0)
        self.motion.moveInit()

    def start(self, x, y):
        print(x, y)
        self.motion.move(x, y, 0)

    def end(self):
        self.motion.stopWalk()
