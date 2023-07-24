class Application:
    def __init__(self, first_name="", last_name="", account_no="", acct_type="", email="",
                 destination="kmcgooding@gmail.com", subject="", message=""):
        self._first_name = first_name
        self._last_name = last_name
        self._account_no = account_no
        self._acct_type = acct_type
        self._email = email
        self._subject = subject
        self._message = message
        self._destination = destination

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
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        self._account_no = account_no

    @property
    def acct_type(self):
        return self._acct_type

    @acct_type.setter
    def acct_type(self, acct_type):
        self._acct_type = acct_type

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        self._subject = subject

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    def apply_for_account(self):
        pass

    def apply_for_loan(self, first_name, last_name, account, acct_type):
        pass

    def make_an_enquiry(self,):
        pass
