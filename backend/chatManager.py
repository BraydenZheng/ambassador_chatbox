from db import Db
conn = Db()
import sys, os
import json
import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='34.125.165.69'))
    channel = connection.channel()

    channel.queue_declare(queue='chatbot')


    def callback(ch, method, properties, body):
        b = json.loads(body)
        username = b[0]
        content = b[1:]

        # delete all existing record before inserting
        conn.deleteChatRecordByUser(username)

        # serialize string list for DB insert
        s = json.dumps(content)

        # inserting all chat record before inserting
        conn.addChatRecord(username, s)

    channel.basic_consume(queue='chatbot', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()





if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
