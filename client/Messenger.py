import json
import socket


class Messenger:

    def send(self, msg, client: socket.socket):
        client.send(str(msg).encode('ascii'))

    def receive_data(self, data):
        data = data.decode('ascii')
        return json.loads(data)

    def msg_form(self, type: str, data: dict):
        return json.dumps(
            {
                'type': type,
                'data': data
            }
        )

    def send_auth(self, client: socket.socket):
        username = str(input('Enter your username: '))
        password = str(input('Enter your password: '))
        self.send(self.msg_form('response_login', {
            'username': username,
            'password': password
        }), client)

    def send_message(self, msg, client: socket.socket, user):
        self.send(self.msg_form('chat_message', {
            'message': msg,
            'from': user['username'],
        }), client)
