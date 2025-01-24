from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from sys import argv

from test_views import TestViews
from true_views import TrueViews

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    CORS(app,resources={r"/*":{"origins":"*"}})
    socketio = SocketIO(app,debug=True,cors_allowed_origins='*',async_mode='eventlet')
    if len(argv) > 1:
        TestViews(app, socketio)
    else:
        TrueViews(app, socketio)