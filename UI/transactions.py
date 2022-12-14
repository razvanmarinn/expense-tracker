# Form implementation generated from reading ui file 'trans.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PopUpTransactions(object):
    def setupUi(self, PopUpTransactions, AccWindow):
        PopUpTransactions.setObjectName("PopUpTransactions")
        PopUpTransactions.resize(496, 285)
        PopUpTransactions.setStyleSheet("background-color:rgb(92, 90, 94);\n"
"")
        self.l_nume = QtWidgets.QLabel(PopUpTransactions)
        self.l_nume.setGeometry(QtCore.QRect(160, 60, 55, 16))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.l_nume.setFont(font)
        self.l_nume.setObjectName("l_nume")
        self.l_value = QtWidgets.QLabel(PopUpTransactions)
        self.l_value.setGeometry(QtCore.QRect(160, 90, 55, 16))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.l_value.setFont(font)
        self.l_value.setObjectName("l_value")
        self.pb_addTransactions = QtWidgets.QPushButton(PopUpTransactions)
        self.pb_addTransactions.setGeometry(QtCore.QRect(210, 188, 93, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_addTransactions.setFont(font)
        self.pb_addTransactions.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.pb_addTransactions.setObjectName("pb_addTransactions")
        self.label = QtWidgets.QLabel(PopUpTransactions)
        self.label.setGeometry(QtCore.QRect(140, 20, 71, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_CreateRecurringPopup = QtWidgets.QPushButton(PopUpTransactions)
        self.pb_CreateRecurringPopup.setGeometry(QtCore.QRect(130, 220, 241, 28))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.pb_CreateRecurringPopup.setFont(font)
        self.pb_CreateRecurringPopup.setStyleSheet("background-color:#228be6;\n"
"color:#fff")
        self.pb_CreateRecurringPopup.setObjectName("pb_CreateRecurringPopup")
        self.layoutWidget = QtWidgets.QWidget(PopUpTransactions)
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
        self.cb_typeoftacc.addItem("")
        self.cb_typeoftacc.addItem("")
        self.cb_typeoftacc.addItem("")
        self.cb_typeoftacc.addItem("")
        self.verticalLayout.addWidget(self.cb_typeoftacc)
        self.label_3 = QtWidgets.QLabel(PopUpTransactions)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 201, 20))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(PopUpTransactions)
        QtCore.QMetaObject.connectSlotsByName(PopUpTransactions)

    def retranslateUi(self, PopUpTransactions):
        _translate = QtCore.QCoreApplication.translate
        PopUpTransactions.setWindowTitle(_translate("PopUpTransactions", "Transactions "))
        self.l_nume.setText(_translate("PopUpTransactions", "Name"))
        self.l_value.setText(_translate("PopUpTransactions", "Value"))
        self.pb_addTransactions.setText(_translate("PopUpTransactions", "Add"))
        self.label.setText(_translate("PopUpTransactions", "Account"))
        self.pb_CreateRecurringPopup.setText(_translate("PopUpTransactions", "Add a recurring transaction"))
        self.cb_typeoftacc.setItemText(0, _translate("PopUpTransactions", "Food"))
        self.cb_typeoftacc.setItemText(1, _translate("PopUpTransactions", "Shopping"))
        self.cb_typeoftacc.setItemText(2, _translate("PopUpTransactions", "Services"))
        self.cb_typeoftacc.setItemText(3, _translate("PopUpTransactions", "Traveling"))
        self.label_3.setText(_translate("PopUpTransactions", "Type of transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUpTransactions = QtWidgets.QWidget()
    ui = Ui_PopUpTransactions()
    ui.setupUi(PopUpTransactions)
    PopUpTransactions.show()
    sys.exit(app.exec())
