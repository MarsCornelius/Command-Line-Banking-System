class Customer:
    def __init__(self, first_name="", last_name="", birth_date="", address="",
                 city="", postal_code="", province="", country="", mobile_no="", email=""):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._address = address
        self._city = city
        self._postal_code = postal_code
        self._province = province
        self._country = country
        self._mobile_no = mobile_no
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        try:
            self._first_name = first_name
        except ValueError:
            print("Invalid first name.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        try:
            self._last_name = last_name
        except ValueError:
            print("Invalid last name.")

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        try:
            self._birth_date = birth_date
        except ValueError:
            print("Invalid birth date.")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        try:
            self._address = address
        except ValueError:
            print("Invalid address.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        try:
            self._city = city
        except ValueError:
            print("Invalid city.")

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        try:
            self._postal_code = postal_code
        except ValueError:
            print("Invalid postal code.")

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, province):
        try:
            self._province = province
        except ValueError:
            print("Invalid province.")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        try:
            self._country = country
        except ValueError:
            print("Invalid country.")

    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        try:
            self._mobile_no = mobile_no
        except ValueError:
            print("Invalid mobile number.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        try:
            self._mobile_no = email
        except ValueError:
            print("Invalid email address.")

