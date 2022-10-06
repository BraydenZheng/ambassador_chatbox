'''
controller part of the MVC pattern when the business logic is handled
'''
from chatbot import get_response
from auth import register, login
from recordObserver import RecordObserver
from subject import Subject

import sys
sys.path.append('../backend')
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.subject = Subject()
        self.ob = RecordObserver()
        self.subject.addObserver(self.ob)
    
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
        self.subject.notifyObserver(userid, self.model.chat_history)
        return True
    
    #function which calls backend api to get saved user chat history
    def get_chat_history(self, userid):
        chat = self.ob.selectChatRecordByUser(userid)
        self.model.set_initial_chat(chat)
    