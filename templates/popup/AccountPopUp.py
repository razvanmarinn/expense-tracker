from PyQt6.QtWidgets import QDialog
from UI.popup import Ui_Form
from templates.Buttons import AddAccButton




class PopUpWindowAcc(QDialog, Ui_Form):

    def __init__(self, accwindow):
        super().__init__(accwindow)
        self.setupUi(self)
        self.show()
        self.accwindow = accwindow
        self.loginform = self.accwindow.loginf
        self.AddButton = AddAccButton(self)
        self.pb_add.clicked.connect(self.AddButton.functionality)


 