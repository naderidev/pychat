import json


class Auth:
    __authentication_filename = 'users.json'

    def __init__(self):
        self.users = json.loads(open(self.__authentication_filename, 'rb').read().decode('utf-8'))

    def get_user(self, username):
        for u in self.users:
            if u['username'] == username:
                return u
        return False

    def check_auth(self, username, password):
        user = self.get_user(username)
        if user:
            return user if user['password'] == password else False
        return False

