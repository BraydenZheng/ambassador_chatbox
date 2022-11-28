# User auth Service

from db import Db
conn = Db()
# login api
# auth username, password
# @return boolean
def login(username, password):
    passW = conn.loginAuth(username)
    return passW[0] == str(password)

# register api
def register(usern, passw):
    # allow register only if user not exist
    if not conn.findUserIdByUsername(usern):
        conn.addUserInfo(usern, passw, usern)
        return {"msg": "Success"}
    else:
        return {"msg": "User Exist"}
