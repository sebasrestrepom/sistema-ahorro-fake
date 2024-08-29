from entities.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = []

    def save(self, account: Account):
        self.accounts.append(account)

    def find_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None