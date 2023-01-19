"""This module contains the class for the popup window to add a custom category to the combobox"""
from PyQt6.QtWidgets import QDialog
from UI.add_categ import Ui_addcategory

class PopUpAddCategory(QDialog, Ui_addcategory):
    """Popup window to add a custom category"""
    def __init__(self, transaction_window):
        super().__init__(transaction_window)
        self.setupUi(self,transaction_window)
        self.transaction_window = transaction_window
        self.pushButton.clicked.connect(self.add_category)

    def add_category(self):
        """Add the category to the combobox"""
        self.transaction_window.cb_typeoftacc.addItem(self.le_categoryname.text())
        self.hide()
        self.transaction_window.show()
