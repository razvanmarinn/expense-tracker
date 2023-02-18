"""Accounts form GUI functionality / Controller FOR ACCOUNTS """
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from general.util import add_drop_down_items
from src.controllers.account_controller import AccountsController
from UI.accounts2 import Ui_AcccountsFrame


class AccountsFrame(Ui_AcccountsFrame):
    max_accounts_per_user = 3

    """Accounts Frame"""
    def __init__(self, parent, welcome_form):
        Ui_AcccountsFrame.__init__(self)
        self.parent = parent
        self.user = parent.user
        self.welcome_form = welcome_form
        add_drop_down_items(self.user.id, self)
        self.controller = AccountsController(self, self.welcome_form)
        self.le_search.textChanged.connect(self.search)
        self.account_dto = self.controller.get_account_data(self.controller.get_current_account_id())
        self.cb_dropdown.currentIndexChanged.connect(self.set_data)
        self.pb_addacc.clicked.connect(self.controller.create_account_poup)
        self.pb_removeacc.clicked.connect(self.controller.remove_account)
        self.pb_accountinfo.clicked.connect(self.controller.create_account_info_popup)
        self.pb_export.clicked.connect(lambda: (self.controller.export_to_csv(), self.controller.export_to_pdf()))
        self.retranslateUi(self)
        self.set_data()

    def set_data(self):
        """Set data from database into accounts display table"""
        acc_id = self.controller.get_current_account_id()
        self.parent.current_account_id = acc_id
        self.account_dto = self.controller.get_account_data(acc_id)
        self.parent.account_dto = self.account_dto

        try:
            self.l_balance_value.setText(str(self.account_dto.balance))
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
        except AttributeError:
            self.l_balance_value.setText("0.0")
            self.tw_showinfo.setRowCount(0)

    def search(self, search_text):
        """Search for a transaction in the table"""
        if search_text == "":
            self.tw_showinfo.setCurrentItem(None)
            return
        self.tw_showinfo.setCurrentItem(None)
        matching_items = self.tw_showinfo.findItems(search_text, Qt.MatchFlag.MatchContains)
        if matching_items:
            first_match = matching_items[0]
            column_index = first_match.column()
            for item in matching_items:
                item.setSelected(True)
            self.tw_showinfo.sortByColumn(column_index, Qt.SortOrder.AscendingOrder)
