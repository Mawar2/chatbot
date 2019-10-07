import os, flask, flask_socketio, flask_sqlalchemy, psycopg2, app

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leaky:admin@localhost/postgres'  
db = flask_sqlalchemy.SQLAlchemy(app)
# creates a database object


class Message(db.Model): 
    #__tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    
    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return '<Message text: %s>' % self.text 