from repositories.transaction_repository import TransactionRepository
from entities.transaction import Deposit, Withdrawal

class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def execute_transaction(self, transaction_id, transaction_type, amount, account):
        if transaction_type.lower() == "deposit":
            transaction = Deposit(transaction_id, transaction_type, amount)
        elif transaction_type.lower() == "withdrawal":
            transaction = Withdrawal(transaction_id, transaction_type, amount)
        else:
            raise ValueError("Invalid transaction type.")

        account.execute_transaction(transaction)
        self.repository.save(transaction)
        return transaction