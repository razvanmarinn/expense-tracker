"""Insights Controller"""
from datetime import datetime
from general.headers import headers, base_url
from general.util import make_api_get_request
from general.next_month_spending import NextMonthPredicter


class InsightsController:
    """Insights Controller"""
    def __init__(self, view, parent):
        self.view = view
        self.parent = parent

    def get_spending_by_category(self, user_id, month, year, category):
        """Get spending by category"""
        endpoint_url = f"{base_url}/users/get_spending_by_category/{user_id}/{month}/{year}/{category}"
        return make_api_get_request(endpoint_url, headers=headers)

    def get_next_month_spending(self):
        """Get next month spending"""
        next_month_predicter = NextMonthPredicter(datetime.now().year)
        try:
            self.view.l_value_next_month_sp.setText(str(next_month_predicter.predict(self.parent.user.id)) + " € ")
        except Exception:
            self.view.l_value_next_month_sp.setText("Error")
