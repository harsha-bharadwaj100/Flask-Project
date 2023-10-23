from time import sleep
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('websocket.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('ready')
def caller(msg):
    print(msg)
    socketio.emit('called', 'foo')

if __name__ == '__main__':
    socketio.run(app, debug=True)  # type: ignore
