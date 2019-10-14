import models, json, random, requests_oauthlib, os

# Twitter API setup
url = "https://api.twitter.com/1.1/search/tweets.json?q=lauv"

oauth = requests_oauthlib.OAuth1(
        os.getenv("N8GHmjLh4c4ErNnAz0XR8iQ5h"),
        os.getenv("D670rnMTpckt5teCwMkAEuknDVnjVpD9o2uctr44FxOVA4dPy9")
    )

class Chatbot():
    def get_response(self, message):
        if message == 'help':
            chatbot_message = 'try typing \"!!about\" or \"!!chat\" or \"!!inspire\"  for me to respond'
        elif message == '!!about':
            chatbot_message = 'Welcome to Leaky Bot!'
        elif message == '!!chat':
            chatbot_message = 'what would you like to chat about?'
        elif message == '!!inspire':
            response = requests.get(url, auth=oauth)
            json_body = response.json()
            random_data = random.randint(0,9)
            tweetfeed = json_body['statuses'][random_data]['text']
        else:
            chatbot_message = "Not really understanding that command... try typing help for more options!"

        new_message = models.Message(chatbot_message)
        models.db.session.add(new_message)
        models.db.session.commit()
        return
    
    def __init__(self):
        return