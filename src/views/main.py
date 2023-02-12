"""Main window class"""
import time
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
from UI.ui_main import Ui_MainWindow
from src.views.accounts import AccountsFrame
from src.views.transfers import TransferFrame
from src.views.transactions import TransactionsFrame
from src.views.wpage import WelcomeFrame

class MainWindow(QMainWindow):
    """Main window class"""
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,user)
        self.user = user
        self.current_account_id = 0
        self.account_dto = None

        self.welcome_form = WelcomeFrame(self)
        self.ui.stackedWidget.addWidget(self.welcome_form)
        self.accounts_form = AccountsFrame(self, self.welcome_form)
        self.ui.stackedWidget.addWidget(self.accounts_form)
        self.transfer_form = TransferFrame(self)
        self.ui.stackedWidget.addWidget(self.transfer_form)
        self.transactions_form = TransactionsFrame(self, self.accounts_form,self.welcome_form)
        self.ui.stackedWidget.addWidget(self.transactions_form)
        self.ui.stackedWidget.setCurrentWidget(self.welcome_form)

        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggle_menu(150, True))
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.welcome_form))
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.accounts_form))

        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.transactions_form))

        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.transfer_form))

        #self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        self.show()


    def toggle_menu(self, maxWidth, enable):
        """Toggle menu functionality"""
        if enable:
            self.ui.frame_left_menu.show()
            time.sleep(0.2)
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            if width == 70 :
                widthExtended = maxExtend
                self.animation = QtCore.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
                self.animation.setDuration(700)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
                self.animation.start()
            else:
                widthExtended = standard
                self.animation = QtCore.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
                self.animation.setDuration(400)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
                self.animation.start()
                self.ui.frame_left_menu.hide()
