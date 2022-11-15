import json
import socket
import time


class Messenger:
    clients: list[socket.socket] = []
    users: list[str] = []

    @property
    def response_form(self):
        return {
            'type': '',
            'data': {
            }
        }

    def broadcast(self, msg, clients: list[socket.socket] = None):
        for client in clients:
            client.send(str(msg).encode('ascii'))

    def receive(self, data):
        data = data.decode('ascii')
        return json.loads(data)

    def update_onlines(self):
        res = self.response_form
        res['type'] = 'update_onlines'
        res['data']['users'] = [user['username'] for user in self.users]
        self.broadcast(json.dumps(res), self.clients)

    def chat_message(self, msg, from_user, from_client, clients: list[socket.socket] = None):
        res = self.response_form
        res['type'] = 'chat_message'
        res['data']['from'] = from_user['username']
        res['data']['private'] = False
        res['data']['message'] = msg
        # if from_client in clients:
        #     del clients[from_client]
        self.broadcast(json.dumps(res), clients)

    def system_message(self, message, clients: list[socket.socket] = None):
        res = self.response_form
        res['type'] = 'system_message'
        res['data']['message'] = message
        self.broadcast(json.dumps(res), clients)

    def request_login(self, client: socket.socket, alert: str = None):
        res = self.response_form
        res['type'] = 'request_login'
        res['data']['alert'] = alert
        self.broadcast(json.dumps(res), [client])

    def logged_in(self, client: socket.socket, auth=None):
        res = self.response_form
        res['type'] = 'logged_in'
        res['data']['user'] = auth
        self.broadcast(json.dumps(res), [client])

    def receive_login_data(self, data):
        try:
            data = self.receive(data)
            if data['type'] == 'response_login':
                return data['data']
        except:
            return False

    def add_user(self, client: socket.socket, user):
        self.clients.append(client)
        self.users.append(user)
        time.sleep(1)
        self.update_onlines()

    def remove_user(self, client: socket.socket, user):
        self.clients.remove(client)
        client.close()
        self.users.remove(user)
        time.sleep(1)
        self.update_onlines()
