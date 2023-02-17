"""Predicts the next month's spending based on the previous 3 months' spending."""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


data = pd.read_csv('spending_data.csv', index_col='Date', parse_dates=True)
last_three_months = data.tail(3)
baseline_spending = last_three_months.mean()
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit(disp=0)
prediction = model_fit.forecast(steps=1)[0]
predicted_spending = prediction + baseline_spending
