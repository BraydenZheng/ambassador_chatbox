# use pypika package for ease of SQL build
import pypika
from pypika import MySQLQuery, Table, Field, Order
import mysql.connector

from datetime import datetime

# unify database Access Service
class Db:
  # db connection info
  mydb = mysql.connector.connect(
    host="34.135.215.224",
    user="bofan",
    password="bofan",
    auth_plugin="mysql_native_password",
    database='chatbot'
  )


# return all chat record from db
  def selectChatRecord(self):
    record = Table('chat_history')
    q = MySQLQuery.from_(record)\
      .select('id', 'SentUserId', 'Format', 'TextContent')\
       .orderby('id', order=Order.desc)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
    return myresult

  # delete all chat record by certain user
  def deleteChatRecordByUser(self, username):
    id = self.findUserIdByUsername(username)
    record = Table('chat_history')
    q = MySQLQuery.from_(record) \
      .delete() \
      .where(record.SentUserId == id)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchone()
    self.mydb.commit()
    return myresult

  # select all chat record by ceratin user
  def selectChatRecordByUser(self, username):
    id = self.findUserIdByUsername(username)
    record = Table('chat_history')
    profile = Table('user_profile')
    q = MySQLQuery.from_(record) \
      .left_join(profile) \
      .on(profile.id == record.SentUserId) \
      .select(record.TextContent) \
      .where(record.SentUserId == id)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchone()
    if myresult is not None:
      return myresult[0];
    else:
      return ""


# add chat record for certain user
  def addChatRecord(self, username, text, f=0):
    id = self.findUserIdByUsername(username)[0]
    customers = Table('chat_history')
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    q = MySQLQuery.into(customers).columns('SentUserId', 'Format', 'TextContent', 'DateTime').insert(id, f, text, formatted_date)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    self.mydb.commit()

# return password for select user
  def loginAuth(self, username):
    profile = Table('user_profile')
    q = MySQLQuery.from_(profile) \
      .select(profile.password)\
      .where(profile.username == username)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchone()
    return myresult

# register user: insert username, password .. other info
  def addUserInfo(self, username, password, name):
    profile = Table('user_profile')
    q = MySQLQuery.into(profile).columns('username', 'password', 'name').insert(username, password, name)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchone()
    self.mydb.commit()
    return myresult

# return user id for certain username
  def findUserIdByUsername(self, username):
    profile = Table('user_profile')
    q = MySQLQuery.from_(profile) \
      .select(profile.id) \
      .where(profile.username == username)
    q = q.get_sql()
    mycursor = self.mydb.cursor()
    mycursor.execute(q)
    myresult = mycursor.fetchone()
    return myresult

