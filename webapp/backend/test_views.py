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
            '''test route'''
            return "hello"
        
        @self.app.route('/sight')
        def sight():
            '''get an image of what the nao is seeing'''
            path = f"img/{self.curr}.jpg"
            self.curr = self.curr + 1 if self.curr + 1 <= 2 else 0
            return render_template('sight.html', image_path=path)
        
        @self.socketio.on('connect')
        def connect(event):
            '''handle connection to the server'''
            print('connected')
            self.socketio.emit('connected', {
                'code': 200
            })

        @self.socketio.on('moveUpdate')
        def move_update(event):
            '''Handle updates to the nao's movement'''
            direction = ''
            if (event['x'] == 1):
                direction += 'up'
            elif (event['x'] == -1):
                direction += 'down'

            if (event['y'] == 1):
                direction += ' right'
            elif (event['y'] == -1):
                direction += ' left'

            if len(direction) == 0:
                direction = 'Nowhere'
            print(direction)

    