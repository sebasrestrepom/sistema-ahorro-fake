from services.user_service import UserService
from services.account_service import AccountService
from services.transaction_service import TransactionService

class UserController:
    def __init__(self, user_service: UserService, account_service: AccountService, transaction_service: TransactionService):
        self.user_service = user_service
        self.account_service = account_service
        self.transaction_service = transaction_service

    def register_user(self):
        identification = input("Enter user identification: ")
        names = input("Enter user names: ")
        age = int(input("Enter user age: "))
        user = self.user_service.register_user(identification, names, age)
        print(f"User {user.show_info()} registered successfully.")
        return user

    def create_account(self, user):
        account_id = input("Enter account ID: ")
        account_type = input("Enter account type (e.g., Savings, Checking): ")
        opening_date = input("Enter account opening date (e.g., 2024-08-27): ")
        account = self.account_service.create_account(account_id, account_type, opening_date, user)
        print(f"Account {account.account_id} created and associated with user {user._names}.")
        return account

    def execute_transaction(self, account):
        transaction_id = input("Enter transaction ID: ")
        transaction_type = input("Enter transaction type (Deposit/Withdrawal): ")
        amount = float(input("Enter transaction amount: "))
        transaction = self.transaction_service.execute_transaction(transaction_id, transaction_type, amount, account)
        print(f"Transaction {transaction.transaction_id} completed successfully.")