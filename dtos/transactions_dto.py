"""Transaction DTO class"""
class TransactionDTO:
    def __init__(self, transaction):
        self.account_id = transaction.account_id
        self.transaction_id = None
        self.value = transaction.value
        self.name = transaction.name
        self.date = transaction.date
        self.type_of = transaction.type_of
        self.userid = transaction.userid
