import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
oneyearback = datetime.now() - relativedelta(years=1)
gme = yf.Ticker("GME")

gme.info

gme_data = gme.history(period="5y", interval="1wk")

gme_data['MA5'] = gme_data['Close'].rolling(5).mean()
gme_data['MA30'] = gme_data['Close'].rolling(30).mean()
gme_data = gme_data.dropna()

#plt.figure(figsize(10, 8))
gme_data['MA5'].loc[oneyearback:today].plot(label='MA5')
gme_data['MA30'].loc[oneyearback:today].plot(label='MA30')
gme_data['Close'].loc[oneyearback:today].plot(label='Close')
plt.legend()
plt.show()