class TestViews():
    def __init__(self, app, socketio):
        self.app = app
        self.socketio = socketio

        self.register()

        self.socketio.run(app, debug=True,port=5001)

    def register(self):
        @self.app.route('/')
        def main():
            return "hello"
    