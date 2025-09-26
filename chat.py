from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')

@socketio.on('ReceiveMessage')
def messageReceived():
    print('message was received!!!')

@socketio.on('message')
def send_message(message):
    send(message)
    print(message)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json, callback=messageReceived)

@socketio.on('join')
def on_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    send(username + " is in the room.", to=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)