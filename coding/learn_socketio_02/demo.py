from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO()
socketio.init_app(app)


@socketio.on('my event')
def connect_handler(data):
    emit('my response', data)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
