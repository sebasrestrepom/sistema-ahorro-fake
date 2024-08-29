class Account:
    def __init__(self, account_id, account_type, opening_date):
        self._account_id = account_id
        self._account_type = account_type
        self._opening_date = opening_date
        self.transactions = []

    @property
    def account_id(self):
        return self._account_id

    def execute_transaction(self, transaction):
        self.transactions.append(transaction)
        print(f"Transaction {transaction.transaction_id} executed in account {self._account_id}")