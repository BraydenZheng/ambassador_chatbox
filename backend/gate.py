import json

from flask import Flask, request
from db import Db
conn = Db()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods = ['GET'])
def login():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    passW = conn.loginAuth(username)
    res = passW[0] == str(password)
    return json.dumps(res)

@app.route("/register", methods = ['GET'])
def register():
    usern = request.args.get('username', None)
    passw = request.args.get('password', None)
    if not conn.findUserIdByUsername(usern):
        conn.addUserInfo(usern, passw, usern)
        return {"msg": "Success"}
    else:
        return {"msg": "User Exist"}


# start flask app
app.run(host="0.0.0.0", port=5001)