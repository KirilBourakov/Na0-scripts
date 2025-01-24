from flask import render_template

class TestViews():
    def __init__(self, app, socketio):
        self.app = app
        self.socketio = socketio

        self.curr = 0

        
        self.register()
        self.socketio.run(app, debug=True,port=5001)

    def register(self):
        @self.app.route('/')
        def main():
            return "hello"
        
        @self.app.route('/sight')
        def sight():
            path = f"img/{self.curr}.jpg"
            self.curr = self.curr + 1 if self.curr + 1 <= 2 else 0
            return render_template('sight.html', image_path=path)

    