from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt6.QtWidgets import QMainWindow
from UI.analysis import Ui_Graph
import sqlite3 ; """Sqlite module"""

class MplCanvas(FigureCanvasQTAgg):
    """Mpl canvas class"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class GraphForm(QMainWindow, Ui_Graph):
    """Graph Form class"""
    def __init__(self, acc_window):
        super().__init__(acc_window)
        self.acc_window = acc_window
        self.setupUi(self, acc_window)
        self.make_graph()
        self.show()


    def make_graph(self):
        db = sqlite3.connect("expense_tracker.db")
        db_cursor = db.cursor()

        db_cursor.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': self.acc_window.current_account_id})
        temp2 = db_cursor.fetchall()

        list_of_transactions = []

        if temp2 is not None:
            list_of_transactions.extend(iter(temp2))
        mpl_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        x_axis=[]
        y_axis=[]
        for list_of_transaction in list_of_transactions:
            x_axis.append(list_of_transaction[0])
            y_axis.append(list_of_transaction[3])
        mpl_canvas.axes.plot(x_axis,y_axis)

        self.setCentralWidget(mpl_canvas)

