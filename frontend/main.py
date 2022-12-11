'''
main function from where execution of frontend starts
creating model, view and control classes

'''

import sys
sys.path.append('../backend')
from chatbot import init_chatbot

from model import Model
from view import View
from controller import Controller

if __name__ == "__main__":
    init_chatbot() #initilaizing chatbot using chatterbot library
    model = Model()
    view = View()
    control = Controller(view, model)
    view.set_control(control)
    control.start_chatbot() #displaying the frontend 