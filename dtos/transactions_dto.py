"""Transaction DTO class"""

class TransactionDTO:
    """Transaction Data Transfer Object class"""
    def __init__(self, transaction):
        self.account_id = transaction.account_id
        self.transaction_id = None
        self.value = transaction.value
        self.name = transaction.name
        self.date = transaction.date
        self.type_of = transaction.type_of
        self.userid = transaction.userid

    def __str__(self):
        """String representation of the TransactionDTO class"""
        return f"Account ID: {self.account_id}\n Id: {self.transaction_id}, Value: {self.value}, Name: {self.name}, Date: {self.date}, Type_of: {self.type_of}, Userid: {self.userid}"
