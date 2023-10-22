from time import sleep
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socket = SocketIO(app)

@app.route('/')
def index():
    return render_template('websocket.html')

@socket.on('message')
def handlemsg(msg):
    socket.send("Very Important Message!")


if __name__ == '__main__':
    socket.run(app, debug=True)  # type: ignore
