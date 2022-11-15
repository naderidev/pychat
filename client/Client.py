import socket, threading
import time
from Messenger import Messenger


class Client(Messenger):
    __host: str = '<Your Host>'
    __port: int = 0000  # Your port
    __user: dict = {}

    def __init__(self):
        self.__connection()
        self.receive()

    def __connection(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.__host, self.__port))
        self.__client = client

    def receive(self):
        while True:
            message = super().receive_data(self.__client.recv(1024))
            msg_type = message['type']
            msg_data = message['data']
            if msg_type == 'request_login':
                if msg_data['alert']:
                    print(f"{msg_data['alert']}", flush=True)
                super().send_auth(self.__client)
            elif not self.__user and msg_type == 'logged_in':
                print("You have successfully logged in!")
                self.__user = msg_data['user']
                write_thread = threading.Thread(target=self.write)
                write_thread.start()
            elif msg_type == 'chat_message':
                print("{f}: {m}".format(f=msg_data['from'], m=msg_data['message']))
                time.sleep(2)

    def write(self):
        while True:
            message = input("")
            super().send_message(message, self.__client, self.__user)


Client()
