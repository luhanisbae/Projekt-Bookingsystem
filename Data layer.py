"""
    data_layer.py
    ~~~~~~~~~~~~~

    Dette modul implementerer
    funktionerne til bookingsystemet.

"""
from User import User_obj


class BookingSystem:

    def __init__(self):
        self._userspass = {}
        self._users = []

    def create_user(self, user, password):
        if user in self._users:
            pass
        else:
            user = User_obj()
            self._users.append(user)
            self._userspass[user] = password

    def delete_user(self, user):
        self._userspass.pop(user)
        self._users.remove(user)

    def edit_user(self, user, new_password):
        self._userspass[user] = new_password