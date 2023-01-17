from UI.add_categ import Ui_addcategory
from PyQt6.QtWidgets import QDialog




class PopUp_add_category(QDialog, Ui_addcategory):
    def __init__(self, TransactionWindow):
        super().__init__(TransactionWindow)
        self.setupUi(self,TransactionWindow)
        self.TransactionWindow = TransactionWindow
        self.pushButton.clicked.connect(self.add_category)

    def add_category(self):
        
        self.TransactionWindow.cb_typeoftacc.addItem(self.le_categoryname.text())
        self.hide()
        self.TransactionWindow.show()