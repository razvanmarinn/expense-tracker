"""This module contains the controller for the popup window for creating new accounts"""
from general.util import make_api_post_request, make_api_get_request
from general.headers import headers, base_url
from PyQt6.QtWidgets import QMessageBox


class PopUpAccountsController():
    """This class contains the controller for the popup window for creating new accounts"""
    def __init__(self, view, acc_window, refresher):
        self.view = view
        self.acc_window = acc_window
        self.refresher = refresher
        self.view.pb_add.clicked.connect(self.create_user_account)

    def create_user_account(self):
        """Create account method"""
        endpoint_url = f"{base_url}/accounts/count_accounts/{self.acc_window.user.id}/"
        user_data = make_api_get_request(endpoint_url, headers=headers)
        if user_data >= self.acc_window.max_accounts_per_user:
            QMessageBox.critical(self.view, "Error", "Error occured")
        else:
            endpoint_url = f"{base_url}/accounts/create_account/{self.acc_window.user.id}/{self.view.cb_accountnames.currentText()}/{self.view.le_budgetname.text()}/{self.view.cb_currency.currentText()}"
            user_data = make_api_post_request(endpoint_url, headers=headers)
            if user_data == 'Error occured':
                QMessageBox.critical(self.view, "Error", "Error occured")
                self.view.hide()
            else:
                self.acc_window.cb_dropdown.addItem(self.view.cb_accountnames.currentText())
                self.acc_window.cb_dropdown.update()
                self.refresher.refresh()
                self.view.hide()
