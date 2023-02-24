"""Insights view"""
from datetime import datetime
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter
from UI.insights import Ui_InsightsFrame
from general.next_month_spending import NextMonthPredicter


class InsightsFrame(Ui_InsightsFrame):
    """Insights Frame"""
    def __init__(self, parent):
        Ui_InsightsFrame.__init__(self)
        self.parent = parent
        self.get_next_month_spending()
        self.chart = QChart()
        self.series = QPieSeries()
        self.series.append("Category 1", 10)
        self.series.append("Category 2", 20)
        self.series.append("Category 3", 30)
        self.chart.addSeries(self.series)
        self.chart.setTitle("Spending by Category")
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_container = QWidget()
        chart_layout = QVBoxLayout(chart_container)
        chart_layout.addWidget(chart_view)
        self.widget_2.setLayout(QVBoxLayout())
        self.widget_2.layout().addWidget(chart_view)

    def get_next_month_spending(self):
        """Get next month spending"""
        next_month_predicter = NextMonthPredicter(datetime.now().year)
        try:
            self.l_value_next_month_sp.setText(str(next_month_predicter.predict(self.parent.user.id)))
        except Exception:
            self.l_value_next_month_sp.setText("Error")
