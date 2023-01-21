from src.models import AccountModel, TransactionModel
from src.models import  AccountModel, TransactionModel
from dtos.accounts_dto import AccountDTO
from src.popup.p_accounts import PopUpWindowAcc
from src.popup.p_account_info import AccountInfoPopup
from src.popup.p_transactions import TransactionPopup


class AccountsController():
    def __init__(self, view):
        self.view = view
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()
        self.view.pb_addacc.clicked.connect(self.create_account_poup)
        self.view.pb_removeacc.clicked.connect(self.remove_account)
        self.view.pb_analyze.clicked.connect(self.create_analyze_popup)
        self.view.pb_addtransaction.clicked.connect(self.create_transaction_popup)
        self.view.pb_createtransfer.clicked.connect(self.create_transfer_popup)
        self.view.pb_accountinfo.clicked.connect(self.create_account_info_popup)


    def get_account_data(self, account_id):
        if account_id is None:
            return None
        acc_uuid = self.account_model.get_uuid(account_id)
        balance = self.account_model.get_account_balance(account_id)
        transactions = self.transaction_model.get_transaction_by_acc_id(account_id)
        return AccountDTO(account_id, acc_uuid, balance, transactions)

    def remove_account(self):
        """Remove account from GUI and database"""

        self.transaction_model.delete_transaction_by_acc_id(self.view.account_dto.account_id)
        self.account_model.delete_account(self.view.cb_dropdown.currentText(), self.view.current_user_id)
        self.view.cb_dropdown.removeItem(self.view.cb_dropdown.currentIndex())

    def get_current_account_id(self):
        curr_text = self.view.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        acc_id = self.account_model.get_account_id(curr_text, self.view.current_user_id)
        return acc_id

    # def get_current_account_uuid(self, account_id):
    #     self.view.current_account_uuid = self.account_model.get_uuid(account_id)

    def create_account_poup(self):
        """Create a new account popup"""
        self.view.popup = PopUpWindowAcc(self.view)

    def create_analyze_popup(self):
        """Create a new analyze popup"""
        # Code to create a new analyze popup

    def create_transaction_popup(self):
        """Create a new transaction popup"""
        self.view.popup = TransactionPopup(self.view)

    def create_transfer_popup(self):
        """Create a new transfer popup"""
        # Code to create a new transfer popup

    def create_account_info_popup(self):
        """Create a new account info popup"""
        self.view.popup = AccountInfoPopup(self.view)

    def update_view_data(self):
        """Update the view with data from the model"""
        # Code to update the view with data from the account_model and transaction_model




