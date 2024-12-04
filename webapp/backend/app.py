from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')

@app.route('/')
def main():
    return "hello"

@socketio.on('connect')
def connect(event):
    print('connected')

@socketio.on("walk")
def walk(event):
    print('event imitted')

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)