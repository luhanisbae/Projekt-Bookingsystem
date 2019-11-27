"""
    data_layer.py
    ~~~~~~~~~~~~~

    Dette modul implementerer
    funktionerne til bookingsystemet.

"""

class UsernameAndPass:

    def __init__(self):
        self._userspass = {}
        self._users = []

    def login_user(self, user, password):
        if self._userspass[user] == password:
            return True

    def create_user(self, user, password):
        if not user in self._users:
            self._userspass[user] = password
            self._users.append(user)

    def delete_user(self, user):
        self._userspass.pop(user)
        self._users.remove(user)

