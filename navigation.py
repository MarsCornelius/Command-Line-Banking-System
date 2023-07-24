from customer import Customer
from login import Login
from menu import welcome


class Navigation:
    def __init__(self, app_option=None, cust_option=None, dep_option=None, loan_option=None, login_option=None,
                 menu_option=""):
        self._app_option = app_option
        self._cust_option = cust_option
        self._dep_option = dep_option
        self._loan_option = loan_option
        self._login_option = login_option
        self._menu_option = menu_option

    @property
    def app_option(self):
        return self._app_option

    @app_option.setter
    def app_option(self, app_option):
        self._app_option = app_option

    @property
    def cust_option(self):
        return self._cust_option

    @cust_option.setter
    def cust_option(self, cust_option):
        self._cust_option = cust_option

    @property
    def dep_option(self):
        return self._dep_option

    @dep_option.setter
    def dep_option(self, dep_option):
        self._dep_option = dep_option

    @property
    def loan_option(self):
        return self._loan_option

    @loan_option.setter
    def loan_option(self, loan_option):
        self._loan_option = loan_option

    @property
    def login_option(self):
        return self._login_option

    @login_option.setter
    def login_option(self, login_option):
        self._login_option = login_option

    @property
    def menu_option(self):
        return self._menu_option

    @menu_option.setter
    def menu_option(self, menu_option):
        while True:
            if menu_option.isnumeric():
                if 1 <= int(menu_option) <= 5:
                    self._menu_option = int(menu_option)
                    break
                else:
                    print("Incorrect Value\n")
                    welcome()
            else:
                print("Numbers Only.\n")
                welcome()
