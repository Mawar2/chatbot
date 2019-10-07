import os, flask, flask_socketio, flask_sqlalchemy
import models

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')

def index():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    #socketio.emit('Someone connected')
    print ('Someone connected!')
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    flask_socketio.emit('update', {
        'data': 'Got your connection!',
        'previous_messages': chat
    })

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')
    
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })

def query():
    messages = models.Message.query.all()
    chat = [m.text + '\n' for m in messages]
    socketio.emit('message received', {
        'message': chat
    })

@socketio.on('new message')
def on_new_message(data):
    print('Data Recieved: ', data)
    new_message = models.Message(data['message'])
    models.db.session.add(new_message)
    models.db.session.commit()
    # lets update this 
    #if new_message[:2] == '!!':
     #   chatbot.Chatbot.get_response(new_message[2:len(new_message)])
    query()
    # message = models.chat_messages(data['username'], data['message'])
    # socketio.emit('message received', {
    #     'message': message 
    # })

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8083)),
        debug=True
    )