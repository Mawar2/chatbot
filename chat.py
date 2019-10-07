import models

class Chatbot():
    def get_response(self, message):
        if message == 'help':
            chatbot_message = 'try typing \"!! about\" or \"!! chat\" for me to respond'
        elif message == 'about':
            chatbot_message = 'Welcome to Leaky Bot!'
        elif message == 'chat':
            chatbot_message = 'what would you like to chat about?'
        else:
            chatbot_message = "Not really feeling that conversation tbh..."

        new_message = models.Message(chatbot_message)
        models.db.session.add(new_message)
        models.db.session.commit()
        return
    
    def __init__(self):
        return