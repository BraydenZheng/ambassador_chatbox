'''
Interaction of chatbot with the chatterbot library

Singleton and Decorator patterns are used
'''
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#singleton pattern
#https://peps.python.org/pep-0318/#examples
def singleton(cls):
    obj = cls()
    # Always return the same object
    cls.__new__ = staticmethod(lambda cls: obj)
    # Disable __init__
    try:
        del cls.__init__
    except AttributeError:
        pass
    return cls

#decorator pattern
@singleton
class chatbot(object):
    def __init__(self):
        self.chatbot = ChatBot("OOAD")
    
    def getBot(self):
        return self.chatbot

chatbot = chatbot().getBot()

def get_response(message):
    return chatbot.get_response(message)

#training the chatbot
def train_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer.train("../data/custom_train_data.json")

#start the chatbot
def init_chatbot():
    train_chatbot(chatbot)
