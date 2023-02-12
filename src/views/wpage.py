from UI.wpage import Ui_WelcomeFrame
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from src.controllers.account_controller import AccountsController
from datetime import datetime

class WelcomeFrame(Ui_WelcomeFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.l_username.setText(self.parent.user.username)
        self.pb_addphoto.clicked.connect(self.open_avatar)
        try:
            self.get_total_balance()
            self.get_this_month_spending()
        except Exception as e:
            self.l_totalbalance.setText("0")
            self.l_totalspend.setText("0")

    def get_total_balance(self):
        total_balance = AccountsController.total_balance_of_a_user(self.parent.user.id)
        self.l_totalbalance.setText(str(total_balance))

    def get_this_month_spending(self):
        spending = AccountsController.get_monthly_spendings(self.parent.user.id, datetime.now().month, datetime.now().year)
        self.l_totalspend.setText(str(spending))


    def open_avatar(self):
        fname = QFileDialog.getOpenFileName(self.parent, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        if fname[0]:

            self.pixmap = QPixmap(fname[0]).scaled(self.l_photo.width(), self.l_photo.height(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.l_photo.setPixmap(self.pixmap)

