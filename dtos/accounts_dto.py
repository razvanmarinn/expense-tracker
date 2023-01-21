"""Account DTO"""""
class AccountDTO:
    def __init__(self, account_id, account_uuid, balance, transactions):
        self.account_id = account_id
        self.account_uuid = account_uuid
        self.balance = balance
        self.transactions = transactions