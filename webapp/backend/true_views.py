from flask import render_template 

class TrueViews():
    def __init__(self, app, socketio):
        import qi
        from managers.MoveManager import MoveManager
        from managers.SightManager import SightManager
        from managers.LLMManger import LLMManager

        self.app = app
        self.socketio = socketio
        session = qi.Session()

        ip = "192.168.2.251"
        session.connect(f"tcp://{ip}:{9559}")

        self.move_manager = MoveManager(session)
        self.sight_manager = SightManager(session)
        self.llm_manager = LLMManager(session)

        self.register()
        self.socketio.run(app, debug=True,port=5001)

    def register(self):
        @self.app.route('/')
        def main():
            '''test route'''
            # self.sight_manager.end()
            return "hello"
        
        @self.app.route('/sight')
        def sight():
            '''get an image of what the nao is seeing'''
            path = f"sight/view.jpg"
            return render_template('sight.html', image_path=path)

        @self.socketio.on('connect')
        def connect(event):
            '''handle connection to server'''
            print('connected')
            self.sight_manager.start()
            self.socketio.emit('connected', {
                'code': 200
            })

        @self.socketio.on("moveUpdate")
        def move_update(event):
            '''handle updates to the move manager'''
            print("running ")
            print(event)
            if (event['x'] != 0 or event['y'] != 0):
                self.move_manager.start(event['x'], event['y'])
            else:
                self.move_manager.end()

        @self.socketio.on('userSpeech')
        def speek(event):
            self.llm_manager.respond_to(event['transcript'])

            self.socketio.emit('finishedSpeaking')
    