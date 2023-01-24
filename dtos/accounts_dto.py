"""Account DTO"""""
from dtos.transactions_dto import TransactionDTO
class AccountDTO:
    """Account Data Transfer Object class"""
    def __init__(self, account_id: int, account_uuid: str ,balance: int, transactions: list[TransactionDTO]):
        self.account_id = account_id
        self.account_uuid = account_uuid
        self.balance = balance
        self.transactions = transactions


    def __str__(self):
        """String representation of the AccountDTO class"""
        transactions_str = [str(transaction) for transaction in self.transactions]
        transactions_str = ", ".join(transactions_str)
        return f"AccountDTO(account_id={self.account_id}, account_uuid={self.account_uuid}, balance={self.balance}, transactions=[{transactions_str}])"
