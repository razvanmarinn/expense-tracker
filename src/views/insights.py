"""Insights view"""
from datetime import datetime
from UI.insights import Ui_InsightsFrame
from general.next_month_spending import NextMonthPredicter


class InsightsFrame(Ui_InsightsFrame):
    """Insights Frame"""
    def __init__(self, parent):
        Ui_InsightsFrame.__init__(self)
        self.parent = parent
        self.next_month_predicter = NextMonthPredicter(datetime.now().year)
        try:
            self.l_value_next_month_sp.setText(str(self.next_month_predicter.predict(self.parent.user.id)))
        except Exception:
            self.l_value_next_month_sp.setText("Error")
