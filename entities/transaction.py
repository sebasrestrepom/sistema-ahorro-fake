class Transaction:
    def __init__(self, transaction_id, transaction_type, amount=0):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount

    def execute(self):
        pass

class Deposit(Transaction):
    def execute(self):
        print(f"Deposit of {self.amount} completed successfully.")

class Withdrawal(Transaction):
    def execute(self):
        print(f"Withdrawal of {self.amount} completed successfully.")