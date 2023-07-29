class DepositAccount:
    def __init__(self, customer_id, account_no, acct_type, opening_balance, current_balance, interest_rate):
        self._customer_id = customer_id
        self._account_no = account_no
        self._acct_type = acct_type
        self._opening_balance = opening_balance
        self._current_balance = current_balance
        self._interest_rate = interest_rate

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        try:
            self._customer_id = customer_id
        except ValueError:
            print("Invalid customer id.")

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, account_no):
        try:
            self._account_no = account_no
        except ValueError:
            print("Invalid account number.")

    @property
    def acct_type(self):
        return self._acct_type

    @acct_type.setter
    def acct_type(self, acct_type):
        try:
            self._acct_type = acct_type
        except ValueError:
            print("Invalid account type.")

    @property
    def opening_balance(self):
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        try:
            self._opening_balance = opening_balance
        except ValueError:
            print("Invalid opening balance.")

    @property
    def current_balance(self):
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        self._current_balance = current_balance

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        try:
            self._interest_rate = interest_rate
        except ValueError:
            print("Invalid interest rate.")

    def open_account(self):
        pass

    def close_account(self):
        pass

    def deposit_funds(self):
        pass

    def withdraw_funds(self):
        pass


class Saving(DepositAccount):
    def __init__(self, account_no, acct_type, opening_balance, current_balance, interest_rate, minimum_balance):
        super().__init__(None, account_no, acct_type, opening_balance, current_balance, interest_rate)
        self._minimum_balance = minimum_balance

    @property
    def minimum_balance(self):
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        try:
            self._minimum_balance = minimum_balance
        except ValueError:
            print("Invalid minimum balance.")

    def apply_interest_rate(self):
        pass


class Chequing(DepositAccount):
    def __init__(self, account_no, acct_type, opening_balance, interest_rate, current_balance, overdraft_limit):
        super().__init__(None, account_no, acct_type, opening_balance, current_balance, interest_rate)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, overdraft_limit):
        try:
            self._overdraft_limit = overdraft_limit
        except ValueError:
            print("Invalid overdraft limit.")
