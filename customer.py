class Customer:
    def __init__(self, first_name="", last_name="", birth_date="", address="",
                 city="", province="", country="", mobile_no=""):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._address = address
        self._city = city
        self._province = province
        self._country = country
        self._mobile_no = mobile_no

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, province):
        self._province = province

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, mobile_no):
        self._mobile_no = mobile_no
