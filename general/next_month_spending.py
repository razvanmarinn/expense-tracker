"""Predicts the next month's spending based on the previous 3 months' spending."""
from abc import ABC, abstractmethod
from statistics import mean
from statsmodels.tsa.arima.model import ARIMA
from general.headers import headers, base_url
from general.util import make_api_get_request


class Predicter(ABC):
    """Abstract class for all predictors."""
    @abstractmethod
    def predict(self, user_id):
        """Predicts the next month's spending based on the previous 3 months' spending."""


class NextMonthPredicter(Predicter):
    """Predicts the next month's spending based on the previous 3 months' spending."""
    def __init__(self, year):
        self.year = year

    def make_api_call_for_month(self, user_id):
        """Makes an API call to get the spending for the current month."""
        endpoint_url = f"{base_url}/users/get_spending_by_year/{user_id}/{self.year}"
        return make_api_get_request(endpoint_url, headers=headers)

    def predict(self, user_id):
        """Predicts the next month's spending based on the previous 3 months' spending."""
        months = self.make_api_call_for_month(user_id=user_id)
        baseline_spending = mean(months)
        if len(months) < 3:
            return baseline_spending
        model = ARIMA(months, order=(1, 1, 1))
        model_fit = model.fit()
        prediction = model_fit.forecast(steps=1, exog=None)[0]
        predicted_spending = prediction + baseline_spending  # noqa: F841
        return round(predicted_spending, 2)
