from repositories.account_repository import AccountRepository
from entities.account import Account

class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, account_id, account_type, opening_date, user):
        account = Account(account_id, account_type, opening_date)
        user.associate_account(account)
        self.repository.save(account)
        return account