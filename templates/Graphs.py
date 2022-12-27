from UI.analysis import Ui_Graph
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sqlite3
from PyQt6.QtWidgets import QMainWindow

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class GraphForm(QMainWindow, Ui_Graph):
    def __init__(self, AccWindow):
        super().__init__(AccWindow)
        self.AccWindow = AccWindow
        self.setupUi(self, AccWindow)
        self.makeGraph()
        self.show()


    def makeGraph(self):
        db = sqlite3.connect("expense_tracker.db")
        d = db.cursor()
        curr_text = self.AccWindow.cb_dropdown.currentText() # CURRENT DROPDOWN TEXT
        
        
        
        d.execute("SELECT * from transactions WHERE account_id = :accid" , {'accid': self.AccWindow.current_ACCOUNT_id})
        temp2 = d.fetchall()
        
        list_of_transactions = []
    
        if temp2 != None:
            for i in temp2:
                list_of_transactions.append(i)
        print(list_of_transactions)

        sc = MplCanvas(self, width=5, height=4, dpi=100)

        x=[]
        y=[]
        for i in range(len(list_of_transactions)):
            x.append(list_of_transactions[i][0])
            y.append(list_of_transactions[i][3])
        sc.axes.plot(x,y) 
       
       
        
      
        self.setCentralWidget(sc)

        