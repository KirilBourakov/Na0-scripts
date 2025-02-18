class TrueViews():
    def __init__(self, app, socketio):
        import qi
        from webapp.backend.managers.MoveManager import MoveManager

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
            '''test route'''
            return "hello"

        @self.socketio.on('connect')
        def connect(event):
            '''handle connection to server'''
            print('connected')
            self.socketio.emit('connected', {
                'code': 200
            })

        @self.socketio.on("moveUpdate")
        def move_update(event):
            '''handle updates to the move manager'''
            if (event['x'] != 0 and event['y'] != 0):
                self.move_manager.start([event['x'], event['y']])
            else:
                self.move_manager.end()