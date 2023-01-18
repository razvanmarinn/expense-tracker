

class TransferToSameAccountException(Exception):
    def __init__(self, message):
        self.message = message
class NoAccountException(Exception):
    def __init__(self, message):
        self.message = message