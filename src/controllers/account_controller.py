"""Account Controller"""
from src.models import  AccountModel, TransactionModel
from src.views.popup.p_accounts import PopUpWindowAcc
from src.views.popup.p_account_info import AccountInfoPopup
from src.dtos.accounts_dto import AccountDTO


class AccountsController():
    """Account controller class"""
    def __init__(self, view):
        self.view = view
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()



    def get_account_data(self, account_id):
        """Get account data from database"""
        if account_id is None:
            return None
        acc_uuid = self.account_model.get_uuid(account_id)
        balance = self.account_model.get_account_balance(account_id)
        transactions = self.transaction_model.get_transaction_by_acc_id(account_id)
        return AccountDTO(account_id, acc_uuid, balance, transactions)

    def remove_account(self):
        """Remove account from GUI and database"""

        self.transaction_model.delete_transaction_by_acc_id(self.view.account_dto.account_id)
        self.account_model.delete_account(self.view.cb_dropdown.currentText(), self.view.user.id)
        self.view.cb_dropdown.removeItem(self.view.cb_dropdown.currentIndex())

    def get_current_account_id(self):
        """Get the current account id"""
        curr_text = self.view.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        acc_id = self.account_model.get_account_id(curr_text, self.view.user.id)
        return acc_id

    # def get_current_account_uuid(self, account_id):
    #     self.view.current_account_uuid = self.account_model.get_uuid(account_id)

    def create_account_poup(self):
        """Create a new account popup"""
        self.view.popup = PopUpWindowAcc(self.view)

    def create_account_info_popup(self):
        """Create a new account info popup"""
        self.view.popup = AccountInfoPopup(self.view)



