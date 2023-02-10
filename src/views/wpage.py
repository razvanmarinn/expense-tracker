from UI.wpage import Ui_AcccountsFrame
from src.controllers.account_controller import AccountsController
from datetime import datetime

class WelcomeFrame(Ui_AcccountsFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.l_username.setText(self.parent.user.username)

        try:
            self.get_total_balance()
            self.get_this_month_spending()
        except Exception as e:
            self.l_totalbalance.setText("0")
            self.l_totalspend.setText("0")

    def get_total_balance(self):
        total_balance = AccountsController.total_balance_of_a_user(self.parent.user.id)
        self.l_totalbalance.setText(str(total_balance))

    def get_this_month_spending(self): # TO BE MODIFIED
        spending = AccountsController.get_monthly_spendings(self.parent.user.id, datetime.now().month, datetime.now().year)
        self.l_totalspend.setText(str(spending))