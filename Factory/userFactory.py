from Factory.vipUser import vipUser


class userFacotry(object):
    def getUser(userType):
        if userType == "VIP":
            return vipUser()