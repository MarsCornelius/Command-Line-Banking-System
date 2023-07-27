
class Login:
    def __init__(self, username="", password=""):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        try:
            self._username = username
        except ValueError:
            print("Invalid username.")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        try:
            self._password = password
        except ValueError:
            print("Invalid username.")
