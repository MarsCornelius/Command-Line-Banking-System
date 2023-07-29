class Navigation:
    def __init__(self, app_option=0, cust_option=None, dep_option=None, loan_option=None, login_option=None,
                 menu_option=0):
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
        try:
            self._app_option = app_option
        except ValueError:
            print("Invalid option.")

    @property
    def cust_option(self):
        return self._cust_option

    @cust_option.setter
    def cust_option(self, cust_option):
        try:
            self._cust_option = cust_option
        except ValueError:
            print("Invalid option.")

    @property
    def dep_option(self):
        return self._dep_option

    @dep_option.setter
    def dep_option(self, dep_option):
        try:
            self._dep_option = dep_option
        except ValueError:
            print("Invalid option.")

    @property
    def loan_option(self):
        return self._loan_option

    @loan_option.setter
    def loan_option(self, loan_option):
        try:
            self._loan_option = loan_option
        except ValueError:
            print("Invalid option.")

    @property
    def login_option(self):
        return self._login_option

    @login_option.setter
    def login_option(self, login_option):
        try:
            self._login_option = login_option
        except ValueError:
            print("Invalid option.")

    @property
    def menu_option(self):
        return self._menu_option

    @menu_option.setter
    def menu_option(self, menu_option):
        from main import main
        try:
            while True:
                if menu_option.isdigit():
                    if 1 <= int(menu_option) <= 5:
                        self._menu_option = int(menu_option)
                        break
                    else:
                        print("Invalid Option\n")
                        main()
                else:
                    print("Numbers Only.\n")
                    main()

        except TypeError:
            print("Invalid data type.")
