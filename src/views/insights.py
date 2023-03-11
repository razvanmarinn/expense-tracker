"""Insights view"""
from datetime import datetime
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter
from UI.insights import Ui_InsightsFrame
from src.controllers.insights_controller import InsightsController


class InsightsFrame(Ui_InsightsFrame):
    """Insights Frame"""
    category_list = ['Food', 'Bills', 'Entertainment', 'Transport', 'Other']

    def __init__(self, parent):
        Ui_InsightsFrame.__init__(self)
        self.parent = parent
        self.controller = InsightsController(self, parent)
        self.chart = QChart()
        self.create_chart()
        self.chart.setTitle("Spending by Category")
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_container = QWidget()
        chart_layout = QVBoxLayout(chart_container)
        chart_layout.addWidget(chart_view)
        self.widget_2.setLayout(QVBoxLayout())
        self.widget_2.layout().addWidget(chart_view)
        self.controller.get_next_month_spending()

    def update_data_in_chart(self):
        """Update data in chart"""
        series = QPieSeries()
        series.clear()
        for category in self.category_list:
            if self.controller.get_spending_by_category(self.parent.user.id, datetime.now().month, datetime.now().year, category) > 0:
                series.append(category, self.controller.get_spending_by_category(self.parent.user.id, datetime.now().month, datetime.now().year, category))
        return series

    def create_chart(self):
        """Create chart"""
        series = self.update_data_in_chart()
        self.chart.removeAllSeries()
        self.chart.addSeries(series)
