'''
view part of the MVC pattern
'''
from calendar import c
from tkinter import *
import sys

sys.path.append( '../backend')
from constants import BG_GRAY, BG_COLOR, TEXT_COLOR, FONT, FONT_BOLD, BOT_NAME

class View:
    def __init__(self):
        self.init_window()
        self.init_variables()
    
    #initializes the tkinter main window    
    def init_window(self):
        self.window = Tk()
        self.window.title("CU Boulder Computer Science Chat Bot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        self.window.eval('tk::PlaceWindow . center') #to place the window in center of the screen
        self.window.protocol('WM_DELETE_WINDOW', self.display_save_option)
    
    def init_variables(self):
        self.show_save = False
        self.userid = StringVar()
        self.password = StringVar()
        self.userid_login = StringVar()
        self.password_login = StringVar()
    
    #initializes the different display screens    
    def init_frames(self):
        self.chat_frame = self.create_chat_frame()
        self.sign_frame = self.create_sign_up_frame()
        self.reqister_user_frame = self.create_reqister_user_frame()
        self.login_frame = self.create_login_frame()
    
    def set_control(self, control):
        self.controller = control
        self.init_frames()
        self.show_sign_up_window()
    
    #starts the display of the window    
    def run(self):
        self.window.mainloop()
     
    #creates the main chat screen where user and bot interacts
    #reused the code from https://www.youtube.com/watch?v=RNEcewpVZUQ&t=74s&ab_channel=PythonEngineer    
    def create_chat_frame(self):
        c_frame = Frame(self.window, background=BG_COLOR)
        # head label
        head_label = Label(c_frame, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(c_frame, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(c_frame, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(c_frame, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.handle_button_press)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.handle_button_press(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        return c_frame
    
    #creates the intial screen where user can choose between log in and sign up
    def create_sign_up_frame(self):
        s_frame = Frame(self.window, background=BG_COLOR)
        
        #header
        header = Label(s_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Select Your Choice", font=FONT_BOLD, pady=10)
        header.place(relwidth=1)
        
        #login button
        login_button = Button(s_frame, text="Login", font=FONT_BOLD, width=20, bg=BG_GRAY,
                              command=lambda: self.handle_login_button_press())
        login_button.place(relheight=0.1, relwidth=0.5, relx=0.25, y = 100)
        
        #register button
        reg_button = Button(s_frame, text="Register", font=FONT_BOLD, width=20, bg=BG_GRAY,
                            command=lambda: self.handle_reqister_button_press(None))
        reg_button.place(relheight=0.1, relwidth=0.5, relx=0.25, y = 250)
        
        return s_frame
    
    #creates the sign up screen
    def create_reqister_user_frame(self):
        r_frame = Frame(self.window, background=BG_COLOR)
        
        #header
        header = Label(r_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Please enter details below", font=FONT_BOLD, pady=10)
        header.place(relwidth=1)
        
        #userid label
        userid = Label(r_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Userid *", font=FONT_BOLD)
        userid.place(relheight=0.1, x=125, y = 100)
       
        #userid input
        userid_entry = Entry(r_frame, textvariable=self.userid)
        userid_entry.place(relheight=0.1, relwidth=0.5, x=125, y = 150)
        userid_entry.focus()
        
        #password label
        password = Label(r_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Password *", font=FONT_BOLD)
        password.place(relheight=0.1, x=125, y = 250)
       
        #password input
        password_entry = Entry(r_frame, textvariable=self.password, show='*')
        password_entry.place(relheight=0.1, relwidth=0.5, x=125, y = 300)
        
        #sign up button
        register_button = Button(r_frame, text="Sign Up", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                 command=lambda: self.handle_user_registration(None))
        register_button.place(relheight=0.1, relwidth=0.5, x=125, y = 400)
        
        #home button
        home_button = Button(r_frame, text="Go Back", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.handle_home_button_press(None))
        home_button.place(relheight=0.1, relwidth=0.5, x=125, y = 450)
        
        return r_frame
    
    #creates the user login screen
    def create_login_frame(self):
        l_frame = Frame(self.window, background=BG_COLOR)
        
        #header
        header = Label(l_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Please enter details below", font=FONT_BOLD, pady=10)
        header.place(relwidth=1)
        
        #userid label
        userid = Label(l_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Userid *", font=FONT_BOLD)
        userid.place(relheight=0.1, x=125, y = 100)
       
        #userid input
        userid_entry = Entry(l_frame, textvariable=self.userid_login)
        userid_entry.place(relheight=0.1, relwidth=0.5, x=125, y = 150)
        userid_entry.focus()
        
        #password label
        password = Label(l_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Password *", font=FONT_BOLD)
        password.place(relheight=0.1, x=125, y = 250)
       
        #password input
        password_entry = Entry(l_frame, textvariable=self.password_login, show='*')
        password_entry.place(relheight=0.1, relwidth=0.5, x=125, y = 300)
        
        #log in button
        register_button = Button(l_frame, text="Log In!", font=FONT_BOLD, width=20, bg=BG_GRAY,
                                 command=lambda: self.handle_user_login(None))
        register_button.place(relheight=0.1, relwidth=0.5, x=125, y = 400)
        
        #home button
        home_button = Button(l_frame, text="Go Back", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.handle_home_button_press(None))
        home_button.place(relheight=0.1, relwidth=0.5, x=125, y = 450)
        
        return l_frame
        
    #creates the pop up window to display messages    
    def error_popup(self, text):
        self.popup = Toplevel(self.window)
        self.popup.title("Info")
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        self.popup.geometry("%dx%d+%d+%d" % (200, 150, x + 150, y + 200))
        Label(self.popup, text = text).pack()
    
    #displays the sign up and log in screen
    def show_sign_up_window(self):
        self.sign_frame.place(x=0, y=0, width=470, height=550)
      
    #displays the chat screen    
    def show_main_window(self):
        self.show_save = True
        self.chat_frame.place(x=0, y=0, width=470, height=550)
    
    #displays sign up screen    
    def show_reqister_user_window(self):
        self.reqister_user_frame.place(x=0, y=0, width=470, height=550)
    
    #displays the log in screen    
    def show_login_window(self):
        self.login_frame.place(x=0, y=0, width=470, height=550)
     
    #event handle when send button is pressed durin chat 
    def handle_button_press(self, event):
        msg = self.msg_entry.get()
        self.fetch_bot_response(msg)
    
    #get the bot response and displays on the screen    
    def fetch_bot_response(self, msg):
        sender = self.userid_login.get()
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        bot_res = self.controller.get_bot_response(msg)
        msg2 = f"{BOT_NAME}: {bot_res}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.controller.set_chat_history(msg)
        self.controller.set_chat_history(f"{bot_res}")
        
        self.text_widget.see(END)
    
    #displays the initial chat stored in database    
    def display_chat_history(self, history):
        sender = self.userid_login.get()
        self.msg_entry.delete(0, END)
        
        for i in range(0, len(history)):
            if i % 2 == 0:
                msg1 = f"{sender}: {history[i]}\n\n"
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msg1)
                self.text_widget.configure(state=DISABLED)
            else:
                msg2 = f"{BOT_NAME}: {history[i]}\n\n"
                self.text_widget.configure(state=NORMAL)
                self.text_widget.insert(END, msg2)
                self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
    
    #handles login button press
    def handle_login_button_press(self):
        self.sign_frame.destroy()
        self.login_frame = self.create_login_frame()
        self.show_login_window()
    
    #handles sign up button press        
    def handle_reqister_button_press(self, event):
        self.sign_frame.destroy()
        self.reqister_user_frame = self.create_reqister_user_frame()
        self.show_reqister_user_window()
        
    #handles sign up button press in sign up screen    
    def handle_user_registration(self,event):
        if not self.userid.get():
            self.error_popup("Please enter user id")
            return
        
        if not self.password.get():
            self.error_popup("Please enter password")
            return
        
        if self.controller.add_new_user(self.userid.get(), self.password.get()):
            self.error_popup("User added successfully")
        else:
            self.error_popup("Oops! User already exists.")
    
    #handles home button pressed
    def handle_home_button_press(self, event):
        self.clear_variables()
        self.reqister_user_frame.destroy()
        self.sign_frame = self.create_sign_up_frame()
        self.show_sign_up_window()
    
    #handles log in button in login screen    
    def handle_user_login(self, event):
        if not self.userid_login.get():
            self.error_popup("Please enter user id")
            return
        
        if not self.password_login.get():
            self.error_popup("Please enter password")
            return
        
        if self.controller.user_login(self.userid_login.get(), self.password_login.get()):
            self.login_frame.destroy()
            self.chat_frame = self.create_chat_frame()
            self.show_main_window()
            self.controller.get_chat_history(self.userid_login.get())
            self.display_chat_history(self.controller.get_user_chat_history())
        else:
            self.error_popup("Oops! Please try again later")
            
    def clear_variables(self):
        self.userid.set('')
        self.password.set('')
        self.userid_login.set('')
        self.password_login.set('')
    
    #displays option to save chat before exiting    
    def display_save_option(self):
        if self.show_save:
            popup = Toplevel(self.window)
            popup.title("Choose Options")
        
            x = self.window.winfo_x()
            y = self.window.winfo_y()
            popup.geometry("%dx%d+%d+%d" % (250, 150, x + 150, y + 200))
        
            s_button = Button(popup,text = "Save Chat!", command = lambda: self.handle_chat_save_button_pressed(None))
            s_button.pack()
            
            q_button = Button(popup,text = "Quit!", command = lambda: self.window.destroy())
            q_button.pack()
            
        else:
            self.window.destroy()
    
    #handles save chat button pressed    
    def handle_chat_save_button_pressed(self, event):
        if self.controller.save_chat(self.userid_login.get()):
            self.window.destroy()