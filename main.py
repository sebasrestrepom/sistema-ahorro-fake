from controllers.user_controller import UserController
from services.user_service import UserService
from services.account_service import AccountService
from services.transaction_service import TransactionService
from repositories.user_repository import UserRepository
from repositories.account_repository import AccountRepository
from repositories.transaction_repository import TransactionRepository

def main():
    user_repo = UserRepository()
    account_repo = AccountRepository()
    transaction_repo = TransactionRepository()

    user_service = UserService(user_repo)
    account_service = AccountService(account_repo)
    transaction_service = TransactionService(transaction_repo)

    controller = UserController(user_service, account_service, transaction_service)

    user = controller.register_user()
    account = controller.create_account(user)
    controller.execute_transaction(account)

if __name__ == "__main__":
    main()