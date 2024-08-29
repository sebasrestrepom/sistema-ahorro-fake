from entities.person import Person

class User(Person):
    def __init__(self, identification, names, age):
        super().__init__(identification, names, age)
        self.accounts = []

    def associate_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_id} associated with {self._names}")