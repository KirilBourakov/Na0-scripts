class TrueViews():
    def __init__(self, app, socketio):
        import qi
        from MoveManager import MoveManager

        self.app = app
        self.socketio = socketio
        session = qi.Session()

        ip = "192.168.2.251"
        session.connect(f"tcp://{ip}:{9559}")
        self.move_manager = MoveManager(session)

        self.register()
        self.socketio.run(app, debug=True,port=5001)

    def register(self):
        @self.app.route('/')
        def main():
            return "hello"

        @self.socketio.on('connect')
        def connect(event):
            print('connected')

        @self.socketio.on("walk")
        def walk(event):
            if (event['direction']  == 'down'):
                self.move_manager.start(event['force'])
            else:
                self.move_manager.end()