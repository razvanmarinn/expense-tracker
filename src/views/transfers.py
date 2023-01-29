
from PyQt6.QtWidgets import QFrame
from PyQt6 import QtWidgets
from PyQt6 import QtCore, QtWidgets
from src.models import TransferModel, Transfer




class TransferFrame(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)
        self.setStyleSheet("background-color: rgb(35,35,35)")
        self.setStyleSheet("color: #fff")
        self.le_uuid = QtWidgets.QLineEdit(self)
        self.le_uuid.setGeometry(QtCore.QRect(130, 60, 181, 22))
        self.le_uuid.setObjectName("le_uuid")
        self.pb_createtransfer = QtWidgets.QPushButton(self)
        self.pb_createtransfer.setGeometry(QtCore.QRect(40, 250, 131, 28))
        self.pb_createtransfer.setObjectName("pb_createtransfer")
        self.l_iban = QtWidgets.QLabel(self)
        self.l_iban.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.l_iban.setObjectName("l_iban")
        self.l_value = QtWidgets.QLabel(self)
        self.l_value.setGeometry(QtCore.QRect(40, 100, 55, 16))
        self.l_value.setObjectName("l_value")
        self.le_value = QtWidgets.QLineEdit(self)
        self.le_value.setGeometry(QtCore.QRect(130, 100, 113, 22))
        self.le_value.setObjectName("le_value")
        self.l_description = QtWidgets.QLabel(self)
        self.l_description.setGeometry(QtCore.QRect(40, 150, 81, 16))
        self.l_description.setObjectName("l_description")
        self.le_description = QtWidgets.QLineEdit(self)
        self.le_description.setGeometry(QtCore.QRect(140, 150, 191, 61))
        self.le_description.setObjectName("le_description")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.parent = parent
        self.transfer_model = TransferModel()
        self.pb_createtransfer.clicked.connect(self.create_transfer)

    def create_transfer(self):
        """Create transfer method"""
        new_transfer = Transfer(self.parent.current_account_id, self.le_uuid.text(), int(self.le_value.text()), self.le_description.text())
        self.transfer_model.create_transfer(new_transfer)
        self.hide()





    def retranslateUi(self, createtransfer):
        _translate = QtCore.QCoreApplication.translate
        createtransfer.setWindowTitle(_translate("createtransfer", "Form"))
        self.pb_createtransfer.setText(_translate("createtransfer", "Create Transfer"))
        self.l_iban.setText(_translate("createtransfer", "UUID"))
        self.l_value.setText(_translate("createtransfer", "VALUE"))
        self.l_description.setText(_translate("createtransfer", "DESCRIPTION"))
