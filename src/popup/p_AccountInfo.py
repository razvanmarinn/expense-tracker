from UI.info import Ui_Form
from PyQt6.QtWidgets import QDialog


class AccountInfoPopup(QDialog, Ui_Form):

    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.setupUi(self, AccWindow)
        self.AccWindow = AccWindow
        self.show()

        self.l_iban.setText(self.AccWindow.current_accout_iban)
        self.l_accountid.setText(str(self.AccWindow.current_account_id))