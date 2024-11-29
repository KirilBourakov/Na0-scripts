from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from MoveManager import MoveManager
import qi

app = Flask(__name__)
socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')
robot_ip = "192.168.2.251"
port = 9559
session = qi.Session()
session.connect(f"tcp://{robot_ip}:{port}")
move_manager = MoveManager(session)


@app.route('/')
def main():
    return render_template('index.html')

@socketio.on("walk")
def walk(event):
    if (event == 'down'):
        move_manager.start([1,0,0])
    else:
        move_manager.end()
