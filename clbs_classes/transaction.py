class Transaction:
    def __init__(self, account_no="", transaction_type="", transaction_id="",
                 amount=0, transfer_from="", transfer_to=""):
        self._account_no = account_no
        self._transaction_type = transaction_type
        self._transaction_id = transaction_id
        self._amount = amount
        self._transfer_from = transfer_from
        self._transfer_to = transfer_to

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
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        try:
            self._transaction_type = transaction_type
        except ValueError:
            print("Invalid transaction type")

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        try:
            self._transaction_id = transaction_id
        except ValueError:
            print("Invalid transaction ID.")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        try:
            self._amount = amount
        except ValueError:
            print("Invalid amount.")

    @property
    def transfer_from(self):
        return self._transfer_from

    @transfer_from.setter
    def transfer_from(self, transfer_from):
        try:
            self._transfer_from = transfer_from
        except ValueError:
            print("Invalid transfer account.")

    @property
    def transfer_to(self):
        return self._transfer_to

    @transfer_to.setter
    def transfer_to(self, transfer_to):
        try:
            self._transfer_to = transfer_to
        except ValueError:
            print("Invalid deposit account.")

    def display_transaction_history(self, account_no):
        pass
