"""
    data_layer.py
    ~~~~~~~~~~~~~

    Dette modul implementerer
    funktionerne til bookingsystemet.

"""
from User import User_obj


class UsernameAndPass:

    def __init__(self):
        self._userspass = {}
        self._users = []
        self._id = 0

    def create_user(self, user, password):
        try:
            pass
        if user in self._users and self._userspass[user] == password:
            return True
        else:
            user_id = "user" + str(self._id)
            user_id = User_obj()
            self._id += 1
            self._users.append(user_id)
            self._userspass[user] = password

    def delete_user(self, user):
        self._userspass.pop(user)
        self._users.remove(user)

    def edit_user(self, user, new_password):
        self._userspass[user] = new_password