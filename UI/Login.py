# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(400, 300)
        LoginForm.setStyleSheet("background-color: #adb5bd")
        self.b_createacc = QtWidgets.QPushButton(LoginForm)
        self.b_createacc.setGeometry(QtCore.QRect(120, 170, 141, 28))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.b_createacc.setFont(font)
        self.b_createacc.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.b_createacc.setObjectName("b_createacc")
        self.layoutWidget = QtWidgets.QWidget(LoginForm)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 80, 139, 88))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_username.setStyleSheet("background-color:#fff;\n"
"color: #000\n"
"")
        self.le_username.setObjectName("le_username")
        self.verticalLayout.addWidget(self.le_username)
        self.le_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_password.setStyleSheet("background-color:#fff;\n"
"color: #000")
        self.le_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.le_password.setObjectName("le_password")
        self.verticalLayout.addWidget(self.le_password)
        self.b_login = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.b_login.setFont(font)
        self.b_login.setStyleSheet("background-color:#228be6;\n"
"color: #fff")
        self.b_login.setObjectName("b_login")
        self.verticalLayout.addWidget(self.b_login)
        self.l_loggedin = QtWidgets.QLabel(LoginForm)
        self.l_loggedin.setGeometry(QtCore.QRect(60, 230, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_loggedin.setFont(font)
        self.l_loggedin.setText("")
        self.l_loggedin.setObjectName("l_loggedin")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(140, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login"))
        self.b_createacc.setText(_translate("LoginForm", "Create Account"))
        self.le_username.setPlaceholderText(_translate("LoginForm", "Enter username"))
        self.le_password.setPlaceholderText(_translate("LoginForm", "Enter password"))
        self.b_login.setText(_translate("LoginForm", "Login"))
        self.label.setText(_translate("LoginForm", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec())
