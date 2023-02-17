"""Predicts the next month's spending based on the previous 3 months' spending."""
import pandas as pd
from abc import ABC, abstractmethod
from statsmodels.tsa.arima_model import ARIMA
from general.util import make_api_get_request
from general.headers import headers, base_url


class Predicter(ABC):
    """Abstract class for all predictors."""
    @abstractmethod
    def predict(user_id):
        """Predicts the next month's spending based on the previous 3 months' spending."""
        pass


class NextMonthPredicter(Predicter):
    """Predicts the next month's spending based on the previous 3 months' spending."""
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def predict(self, user_id):
        make_api_get_request(f"{base_url}/users/get_spending_by_month/{user_id}/{self.month}/{self.year}", headers=headers)
        data = pd.read_csv('spending_data.csv', index_col='Date', parse_dates=True)
        last_three_months = data.tail(3)
        baseline_spending = last_three_months.mean()
        model = ARIMA(data, order=(1, 1, 1))
        model_fit = model.fit(disp=0)
        prediction = model_fit.forecast(steps=1)[0]
        predicted_spending = prediction + baseline_spending  # noqa: F841
