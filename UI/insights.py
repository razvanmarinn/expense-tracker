from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFrame


class Ui_InsightsFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("TransferFrame")
        self.resize(936, 478)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(35,35,35)")
        self.l_estimated_next_month_spending = QtWidgets.QLabel(self)
        self.l_estimated_next_month_spending.setGeometry(QtCore.QRect(210, 370, 371, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.l_estimated_next_month_spending.setFont(font)
        self.l_estimated_next_month_spending.setStyleSheet("color : #fff;")
        self.l_estimated_next_month_spending.setObjectName("l_estimated_next_month_spending")
        self.l_value_next_month_sp = QtWidgets.QLabel(self)
        self.l_value_next_month_sp.setGeometry(QtCore.QRect(600, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.l_value_next_month_sp.setFont(font)
        self.l_value_next_month_sp.setStyleSheet("color : #fff;")
        self.l_value_next_month_sp.setObjectName("l_value_next_month_sp")
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setGeometry(QtCore.QRect(210, 80, 501, 221))
        self.widget_2.setObjectName("widget_2")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, TransferFrame):
        _translate = QtCore.QCoreApplication.translate
        TransferFrame.setWindowTitle(_translate("TransferFrame", "Frame"))
        self.l_estimated_next_month_spending.setText(_translate("TransferFrame", "Estimated next month spendings:"))
        self.l_value_next_month_sp.setText(_translate("TransferFrame", "value"))
