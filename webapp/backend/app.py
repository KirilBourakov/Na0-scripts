from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import qi
from MoveManager import MoveManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')

robot_ip = "192.168.2.251"
port = 9559
session = qi.Session()
session.connect(f"tcp://{robot_ip}:{port}")
move_manager = MoveManager(session)

@app.route('/')
def main():
    return "hello"

@socketio.on('connect')
def connect(event):
    print('connected')

@socketio.on("walk")
def walk(event):
    if (event['direction']  == 'down'):
        move_manager.start(event['force'])
    else:
        move_manager.end()
if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)