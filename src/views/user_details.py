from UI.user_details import Ui_UserDetailsFrame
from general.util import make_api_put_request
from general.headers import headers, base_url
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtTest


class UserDetailsFrame(Ui_UserDetailsFrame):
    def __init__(self, acc_window):
        super().__init__()
        self.acc_window = acc_window
        self.pb_modify_user_details.clicked.connect(lambda: self.modify_user_details())

    def modify_user_details(self):
        endpoint_url = f"{base_url}/user/update_user_details/{self.acc_window.user.id}/{self.le_fullname.text()}/{self.le_email.text()}/{self.le_phonenumber.text()}"
        response = make_api_put_request(endpoint_url, headers=headers)
        QMessageBox.information(self, "Success", "User details updated successfully")
        QtTest.QTest.qWait(250)
        self.acc_window.parent.ui.stackedWidget.setCurrentWidget(self.acc_window.welcome_form)
        return response
