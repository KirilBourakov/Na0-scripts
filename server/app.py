from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import threading
import qi

app = Flask(__name__)
socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')

robot_ip = "192.168.2.251"
port = 9559
session = qi.Session()
session.connect(f"tcp://{robot_ip}:{port}")
motion = session.service("ALMotion")
motion.setStiffnesses("Body", 1.0)
motion.moveInit()

running = True
def walk_manager():
    global running
    while running:
        motion.moveTo(1,0,0)
thread = threading.Thread(target=walk_manager)

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on("walk")
def walk(event):
    if (event == 'down'):
        global running
        running = True
        global thread
        thread.start()
    else:
        print('here')
        running = False
        thread.join()
        thread = threading.Thread(target=walk_manager)
    
