"""Accounts form GUI functionality / Controller FOR ACCOUNTS """
from PyQt6.QtWidgets import QApplication, QDialog, QFrame
from PyQt6 import QtWidgets
from src.models import AccountModel
from general.util import add_drop_down_items
from src.controllers.account_controller import AccountsController
from PyQt6 import QtCore, QtGui, QtWidgets


class AccountsFormTab(QFrame):
    """Accounts form GUI functionality"""
    def __init__(self, parent):
        QFrame.__init__(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(35,35,35)")
        self.l_accounts = QtWidgets.QLabel(self)
        self.l_accounts.setGeometry(QtCore.QRect(50, 20, 134, 62))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.l_accounts.setFont(font)
        self.l_accounts.setStyleSheet("color : #fff")
        self.l_accounts.setObjectName("l_accounts")
        self.l_transactions = QtWidgets.QLabel(self)
        self.l_transactions.setGeometry(QtCore.QRect(50, 180, 251, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.l_transactions.setFont(font)
        self.l_transactions.setStyleSheet("color : #fff\n"
"")
        self.l_transactions.setObjectName("l_transactions")
        self.tw_showinfo = QtWidgets.QTableWidget(self)
        self.tw_showinfo.setGeometry(QtCore.QRect(40, 230, 641, 191))
        self.tw_showinfo.setStyleSheet("background-color:#228be6;\n"
"")
        self.tw_showinfo.setObjectName("tw_showinfo")
        self.tw_showinfo.setColumnCount(5)
        self.tw_showinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        item.setFont(font)
        self.tw_showinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        item.setFont(font)
        self.tw_showinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        item.setFont(font)
        self.tw_showinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        item.setFont(font)

        self.tw_showinfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        item.setFont(font)
        self.tw_showinfo.setHorizontalHeaderItem(4, item)
        self.tw_showinfo.horizontalHeader().setStretchLastSection(True)
        self.tw_showinfo.verticalHeader().setDefaultSectionSize(37)
        self.tw_showinfo.verticalHeader().setMinimumSectionSize(30)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 40, 471, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_dropdown = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_dropdown.setStyleSheet("background-color: #fff")
        self.cb_dropdown.setObjectName("cb_dropdown")
        self.horizontalLayout_2.addWidget(self.cb_dropdown)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_addacc = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_addacc.setFont(font)
        self.pb_addacc.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.pb_addacc.setObjectName("pb_addacc")
        self.horizontalLayout.addWidget(self.pb_addacc)
        self.pb_removeacc = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_removeacc.setFont(font)
        self.pb_removeacc.setStyleSheet("background-color:#228be6; \n"
"color: #fff")
        self.pb_removeacc.setObjectName("pb_removeacc")
        self.horizontalLayout.addWidget(self.pb_removeacc)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 80, 192, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.l_balance = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.l_balance.setFont(font)
        self.l_balance.setStyleSheet("color : #fff")
        self.l_balance.setObjectName("l_balance")
        self.horizontalLayout_3.addWidget(self.l_balance)
        self.l_balance_value = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.l_balance_value.setFont(font)
        self.l_balance_value.setStyleSheet("color : #Fff")
        self.l_balance_value.setObjectName("l_balance_value")
        self.horizontalLayout_3.addWidget(self.l_balance_value)

        font = QtGui.QFont()
        font.setFamily("OCR A Extended")

        self.pb_accountinfo = QtWidgets.QPushButton(self)
        self.pb_accountinfo.setGeometry(QtCore.QRect(540, 180, 131, 28))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_accountinfo.setFont(font)
        self.pb_accountinfo.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.pb_accountinfo.setObjectName("pb_accountinfo")


        QtCore.QMetaObject.connectSlotsByName(self)

        self.parent = parent
        self.user = parent.user
        self.max_accounts_per_user = 3 # STATIC VARIABLE
        self.account_model = AccountModel()
        self.current_nr_of_acc = self.account_model.count_accounts(parent.user.id)
        add_drop_down_items(self)
        self.controller = AccountsController(self)
        self.account_dto = self.controller.get_account_data(self.controller.get_current_account_id())
        #self.cb_dropdown.currentIndexChanged.connect(partial(self.set_data, self.account_dto))
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)
        self.pb_addacc.clicked.connect(self.controller.create_account_poup)
        self.pb_removeacc.clicked.connect(self.controller.remove_account)
        self.pb_accountinfo.clicked.connect(self.controller.create_account_info_popup)

        self.retranslateUi(self)
        self.set_data()

    def set_data(self):
        """Set data from database into accounts display table"""
        acc_id = self.controller.get_current_account_id()
        self.parent.current_account_id = acc_id
        self.account_dto = self.controller.get_account_data(acc_id)
        self.parent.account_dto = self.account_dto
        if acc_id  is not None:
           # self.controller.get_current_account_uuid(self.account_dto.account_id)
           # print(self.account_dto.balance)
            self.l_balance_value.setText(str(self.account_dto.balance))
            #transactions = self.transaction_model.get_transaction_by_acc_id(self.current_account_id)
            self.tw_showinfo.setRowCount(len(self.account_dto.transactions))

            for row, transaction in enumerate(self.account_dto.transactions):
                id_tabel = QtWidgets.QTableWidgetItem(str(transaction[0]))
                name_tabel = QtWidgets.QTableWidgetItem(transaction[1])
                value_tabel = QtWidgets.QTableWidgetItem(str(transaction[2]))
                type_tabel = QtWidgets.QTableWidgetItem(str(transaction[3]))
                date_tabel = QtWidgets.QTableWidgetItem(str(transaction[4]))
                self.tw_showinfo.setItem(row, 0, id_tabel)
                self.tw_showinfo.setItem(row, 1, name_tabel)
                if transaction[2] < 0:
                        value_tabel.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
                else:
                        value_tabel.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
                self.tw_showinfo.setItem(row, 2, value_tabel)
                self.tw_showinfo.setItem(row, 3, date_tabel)
                self.tw_showinfo.setItem(row, 4, type_tabel)



    def retranslateUi(self, AccountsForm):
        _translate = QtCore.QCoreApplication.translate
        AccountsForm.setWindowTitle(_translate("AccountsForm", "Accounts"))
        AccountsForm.setToolTip(_translate("AccountsForm", "<html><head/><body><p><br/></p></body></html>"))
        self.l_accounts.setText(_translate("AccountsForm", "Accounts"))
        self.l_transactions.setText(_translate("AccountsForm", "Transactions"))
        item = self.tw_showinfo.horizontalHeaderItem(0)
        item.setText(_translate("AccountsForm", "ID"))
        item = self.tw_showinfo.horizontalHeaderItem(1)
        item.setText(_translate("AccountsForm", "Name"))
        item = self.tw_showinfo.horizontalHeaderItem(2)
        item.setText(_translate("AccountsForm", "Price"))
        item = self.tw_showinfo.horizontalHeaderItem(3)
        item.setText(_translate("AccountsForm", "Type"))
        item = self.tw_showinfo.horizontalHeaderItem(4)
        item.setText(_translate("AccountsForm", "Date"))
        self.pb_addacc.setText(_translate("AccountsForm", "Add account"))
        self.pb_removeacc.setText(_translate("AccountsForm", "Remove account"))
        self.l_balance.setText(_translate("AccountsForm", "Balance:"))
        self.l_balance_value.setText(_translate("AccountsForm", "0"))
        self.pb_accountinfo.setText(_translate("AccountsForm", "Account info"))
