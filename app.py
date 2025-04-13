from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
        return render_template('index.html')

@socketio.on('request_data')
def send_live_data():
    # Simulate live trading data
    data = {"price": random.uniform(100, 200), "volume": random.randint(1000, 5000)}
    emit('update_data', data)

if __name__ == '__main__':
    socketio.run(app)

