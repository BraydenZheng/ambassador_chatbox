import json

from chatbot import get_response
from auth import register, login
from recordService import RecordService

import sys
import pika

sys.path.append('../backend')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='34.125.165.69'))
channel = connection.channel()
channel.queue_declare(queue='chatbot')


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.ob = RecordService()


    #function to display the view
    def start_chatbot(self):
        self.view.run()
    
    #function to get bot reponse from chatterbot library    
    def get_bot_response(self, user_input):
        return get_response(user_input)
    
    #function to get stored user chat history
    def get_user_chat_history(self):
        return self.model.get_chat_history()
    
    #function to add msgs to chat history
    def set_chat_history(self, msg):
        self.model.set_chat_history(msg)
    
    #function which calls backend api to register new user
    def add_new_user(self, user, pwd):
        res = register(user, pwd)
        if res['msg'] == "Success":
            return True
        else:
            return False
    
    #function which calls backend api to handle user login
    def user_login(self, user, pwd):
        return login(user, pwd)

    #function which calls backend api to save user chat hisotry
    def save_chat(self, userid):
        encode_mess = self.model.chat_history
        encode_mess.insert(0, userid)
        channel.basic_publish(exchange='', routing_key='chatbot', body=json.dumps(encode_mess))

        return True
    
    #function which calls backend api to get saved user chat history
    def get_chat_history(self, userid):
        chat = self.ob.selectChatRecordByUser(userid)
        self.model.set_initial_chat(chat)
    