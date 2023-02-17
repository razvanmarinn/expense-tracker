"""This module contains all the custom exceptions used in the project."""


class TransferToSameAccountException(Exception):
    """This exception is raised when the user tries to transfer money to the same account"""
    def __init__(self, message):
        self.message = message


class NoAccountException(Exception):
    """This exception is raised when the user tries to use an account that doesn't exist"""
    def __init__(self, message):
        self.message = message


class NoTransactionWithThisIdException(Exception):
    """This exception is raised when the user tries to use a transaction that doesn't exist"""
    def __init__(self, message):
        self.message = message
