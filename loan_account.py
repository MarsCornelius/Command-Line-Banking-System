class LoanAccount:
    def __init__(self, customer_id, account_no, amount, interest_rate, payoff_amount):
        self._customer_id = customer_id
        self._account_no = account_no
        self._amount = amount
        self._interest_rate = interest_rate
        self._payoff_amount = payoff_amount

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
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        try:
            self._amount = amount
        except ValueError:
            print("Invalid starting balance.")

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        try:
            self._interest_rate = interest_rate
        except ValueError:
            print("Invalid interest rate.")

    @property
    def payoff_amount(self):
        return self._payoff_amount

    @payoff_amount.setter
    def payoff_amount(self, payoff_amount):
        try:
            self._payoff_amount = payoff_amount
        except ValueError:
            print("Invalid payoff amount.")

    def make_payment(self):
        pass

    def make_principal_payment(self):
        pass

    def make_interest_payment(self):
        pass

    def payoff(self):
        pass


class PersonalLoan(LoanAccount):
    def __init__(self, account_no, amount, interest_rate, payoff_amount, reason):
        super().__init__(None, account_no, amount, interest_rate, payoff_amount)
        self._reason = reason

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        try:
            self._reason = reason
        except ValueError:
            print("Invalid reason.")


class MortgageLoan(LoanAccount):
    def __init__(self, account_no, amount, interest_rate, payoff_amount, property_type):
        super().__init__(None, account_no, amount, interest_rate, payoff_amount)
        self._property_type = property_type

    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        try:
            self._property_type = property_type
        except ValueError:
            print("Invalid property type.")
