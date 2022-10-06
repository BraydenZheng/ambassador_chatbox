'''
model of the MVC pattern where chat history is stored
'''
class Model:
    def __init__(self):
        self.chat_history = []
    
    #getter for chat history
    def get_chat_history(self):
        return self.chat_history
    
    #setter function to save on going chat to the chat history
    def set_chat_history(self, msg):
        self.chat_history.append(msg)
    
    #setter function to initilize the chat history when user logs in
    def set_initial_chat(self, chat):
        self.chat_history = chat
        