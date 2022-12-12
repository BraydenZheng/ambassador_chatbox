# Chatbot implementation in Tkinter
<h2>Team members : Bofan Zheng, Sarthak Maniar

## Language: 
Python 3.9.12 \
all other required package includes in requirements.txt

<h2> Steps to run application </h2>
Recommend to create a virtual environment (anaconda / virtualenv)
1. install the libraries in requirements.txt (pip install -r requirements.txt)
2. change to frontend directory and run python main.py

<br>

<h3> Frontend: </h3>
MVC pattern is used to display the chatbot GUI. <br>
view.py contains all the code for the UI. model.py conatins all the data and controller.py handles the business logic.

<br> 

<h4> Steps to interact with chatbot: </h4>
1. Initial screen has options to login and sign up. <br>
2. On click of login button, user is presented with the userid and password input after filling the deatils press log in button. If the user is already reqistered chatbot screen appears. <br>
2. On click of sign up button, user is presented with the userid and password input after filling the deatils press sign up button. If the user is not already reqistered, user will be added. <br>
3. In the chatbot screen, user should type the message and hit enter or send button. <br>
4. Before closing the window, a pop up appears where the user will be asked to whether save chat.

<br>

## Reference
1. GUI: https://www.youtube.com/watch?v=RNEcewpVZUQ&t=74s&ab_channel=PythonEngineer 
