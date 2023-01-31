"""Account Controller"""
from src.models import  AccountModel, TransactionModel
from src.views.popup.p_accounts import PopUpWindowAcc
from src.views.popup.p_account_info import AccountInfoPopup
from src.dtos.accounts_dto import AccountDTO
from general.util import make_api_get_request, make_api_delete_request
from src.controllers.transactions_controller import TransactionController
from src.headers import headers


class AccountsController():
    """Account controller class"""
    def __init__(self, view):
        self.view = view
        self.account_model = AccountModel()
        self.transaction_model = TransactionModel()


    def get_account_data(self, account_id):
        """Get account data"""
        endpoint_url = "http://{}:{}/accounts/get_account_by_id/{}".format("127.0.0.1", "8000", account_id)
        user_data = make_api_get_request(endpoint_url, headers=headers)
        print(user_data)
        if user_data is None:

            return None
        else:
            transactions = self.get_transactions(account_id)
            return AccountDTO(user_data["id"], user_data["uuid"], user_data["balance"], transactions)

    def get_transactions(self, account_id):
        """Get all transactions for a specific account"""
        endpoint_url = "http://{}:{}/transactions/get_transactions/{}".format("127.0.0.1", "8000", account_id)
        return make_api_get_request(endpoint_url, headers=headers)


    def remove_account(self):
        """Remove an account"""
        transaction_controller = TransactionController(self.view, self)
        transaction_controller.delete_transaction_by_acc_id(self.view.account_dto.account_id)
        endpoint_url = "http://{}:{}/accounts/delete_account/{}/{}".format("127.0.0.1", "8000", self.view.cb_dropdown.currentText(), self.view.user.id)
        make_api_delete_request(endpoint_url, headers=headers)
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



