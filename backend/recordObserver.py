from db import Db
conn = Db()
import json

# Observer pattern - Observer
# observer used to update chat record in select db

class RecordObserver:
    def selectChatRecordByUser(self, username):
        s = conn.selectChatRecordByUser(username)
        return json.loads(s)


    def update(self, username, content):
        # delete all existing record before inserting
        conn.deleteChatRecordByUser(username)

        # serialize string list for DB insert
        s = json.dumps(content)

        # inserting all chat record before inserting
        conn.addChatRecord(username, s)