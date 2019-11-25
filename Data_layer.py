"""
    data_layer.py
    ~~~~~~~~~~~~~

    Dette modul implementerer
    funktionerne til bookingsystemet.

"""
from User import User_obj
import sys

class UsernameAndPass:

    def __init__(self):
        self._userspass = {}
        self._users = []
        self._id = 0

    def _str_to_class(self, user):
        return getattr(sys.modules[__name__], user)

    def login_user(self, user, password):
        if self._userspass[user] == password:
            return True

    def create_user(self, user, password):
        self._userspass[user] = password
        user = self._str_to_class("User_obj")
        self._users.append(user)
        print(self._users)
        for i in self._users:
            print(i)

    def delete_user(self, user):
        self._userspass.pop(user)
        self._users.remove(user)

    def edit_user(self, user, new_password):
        self._userspass[user] = new_password

