from entities.transaction import Transaction

class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def save(self, transaction: Transaction):
        self.transactions.append(transaction)

    def find_all(self):
        return self.transactions