"""This module contains the WelcomeFrame class which is the main page of the application."""
from datetime import datetime
from UI.wpage import Ui_WelcomeFrame
from src.controllers.account_controller import AccountsController
from general.user_avatar import AvatarHandler


class WelcomeFrame(Ui_WelcomeFrame):
    """Welcome Frame class"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.spending_threeshold = 10000
        self.avatar_handler = AvatarHandler(self)
        self.avatar_handler.get_avatar_from_database()
        self.l_username.setText(self.parent.user.username)
        self.pb_addphoto.clicked.connect(self.avatar_handler.open_avatar)
        try:
            self.get_total_balance()
            self.get_this_month_spending()
        except Exception:
            self.l_totalbalance.setText("0")
            self.l_totalspend.setText("0")

    def get_total_balance(self):
        """Get total balance of all accounts"""
        total_balance = AccountsController.total_balance_of_a_user(self.parent.user.id)
        self.l_totalbalance.setText(str(total_balance))

    def get_this_month_spending(self):  # implement sending emails when spending is over the threeshold and stop the user from transfers.
        """Get total spending of this month"""
        spending = AccountsController.get_monthly_spendings(self.parent.user.id, datetime.now().month, datetime.now().year)
        if spending > self.spending_threeshold:
            self.l_totalspend.setStyleSheet("color: red")
        self.l_totalspend.setText(str(spending))
