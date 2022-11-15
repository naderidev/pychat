import socket, threading
from Auth import Auth
from Messenger import Messenger


class Server(Auth, Messenger):
    __host: str = '<Your Host>'
    __port: int = 0000  # Your port

    def __init__(self):
        super().__init__()
        self.__connection()
        self.manager()

    def __connection(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.__host, self.__port))
        server.listen()
        self.__server = server

    def manager(self):
        while 1:
            client, address = self.__server.accept()
            print('Someone Connected with {}'.format(str(address)))
            error = False
            while 1:
                super().request_login(client, alert='The information does not match' if error else None)
                login_info = self.receive_login_data(client.recv(1024))
                if login_info:
                    auth = super().check_auth(username=login_info['username'], password=login_info['password'])
                    if auth:
                        super().logged_in(client, auth)
                        break
                    error = True
            super().add_user(client, auth)
            print('User {} logged in'.format(auth['username']))
            thread = threading.Thread(target=self.handle, args=(client, auth))
            thread.start()

    def handle(self, client, current_user):
        while True:
            try:
                message = super().receive(client.recv(1024))
                super().chat_message(message['data']['message'], current_user, client, self.clients)
            except:
                super().remove_user(client, current_user)
                print('User {} disconnected'.format(current_user['username']))
                break


Server()
