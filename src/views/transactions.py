
from PyQt6.QtWidgets import QFrame
from PyQt6 import QtWidgets, QtGui, QtCore, QtWidgets
from src.controllers.transactions_controller import TransactionController




class TransactionFrame(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self)

        self.parent = parent
        self.setStyleSheet("background-color: rgb(35,35,35)")
        self.setStyleSheet("color: #fff")
        self.l_nume = QtWidgets.QLabel(self)
        self.l_nume.setGeometry(QtCore.QRect(160, 60, 55, 16))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.l_nume.setFont(font)
        self.l_nume.setObjectName("l_nume")
        self.l_value = QtWidgets.QLabel(self)
        self.l_value.setGeometry(QtCore.QRect(160, 90, 55, 16))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.l_value.setFont(font)
        self.l_value.setObjectName("l_value")
        self.pb_addTransactions = QtWidgets.QPushButton(self)
        self.pb_addTransactions.setGeometry(QtCore.QRect(210, 188, 93, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_addTransactions.setFont(font)
        self.pb_addTransactions.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.pb_addTransactions.setObjectName("pb_addTransactions")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(140, 20, 71, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_CreateRecurringPopup = QtWidgets.QPushButton(self)
        self.pb_CreateRecurringPopup.setGeometry(QtCore.QRect(130, 220, 241, 28))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_CreateRecurringPopup.setFont(font)
        self.pb_CreateRecurringPopup.setStyleSheet("background-color:#228be6;\n"
"color:#fff")
        self.pb_CreateRecurringPopup.setObjectName("pb_CreateRecurringPopup")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 10, 191, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_accounts = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_accounts.setStyleSheet("background-color:#228be6\n"
"")
        self.cb_accounts.setObjectName("cb_accounts")
        self.verticalLayout.addWidget(self.cb_accounts)
        self.le_nume = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_nume.setStyleSheet("background-color: #fff")
        self.le_nume.setObjectName("le_nume")
        self.verticalLayout.addWidget(self.le_nume)
        self.le_value = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_value.setStyleSheet("background-color: #fff")
        self.le_value.setObjectName("le_value")
        self.verticalLayout.addWidget(self.le_value)
        self.cb_typeoftacc = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_typeoftacc.setStyleSheet("background-color:#228be6;")
        self.cb_typeoftacc.setObjectName("cb_typeoftacc")
        self.verticalLayout.addWidget(self.cb_typeoftacc)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 201, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pb_add_type_of_category = QtWidgets.QPushButton(self)
        self.pb_add_type_of_category.setGeometry(QtCore.QRect(430, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_add_type_of_category.setFont(font)
        self.pb_add_type_of_category.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.pb_add_type_of_category.setObjectName("pb_add_type_of_category")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

####
        self.category_list = ['Food', 'Bills', 'Entertainment', 'Transport', 'Other']
        self.transaction_model = TransactionController(self, self.parent)
        self.show()
        #self.pb_CreateRecurringPopup.clicked.connect(lambda: self.create_popup("recurring_trans"))
        for i in self.category_list:
            self.cb_typeoftacc.addItem(i)
        #add_drop_down_items(self.acc_window)
        self.cb_typeoftacc.currentText()


    def retranslateUi(self, PopUpTransactions):
        _translate = QtCore.QCoreApplication.translate
        PopUpTransactions.setWindowTitle(_translate("PopUpTransactions", "Transactions "))
        self.l_nume.setText(_translate("PopUpTransactions", "Name"))
        self.l_value.setText(_translate("PopUpTransactions", "Value"))
        self.pb_addTransactions.setText(_translate("PopUpTransactions", "Add"))
        self.label.setText(_translate("PopUpTransactions", "Account"))
        self.pb_CreateRecurringPopup.setText(_translate("PopUpTransactions", "Add a recurring transaction"))
        self.label_3.setText(_translate("PopUpTransactions", "Type of transaction"))
        self.pb_add_type_of_category.setText(_translate("PopUpTransactions", "+"))





