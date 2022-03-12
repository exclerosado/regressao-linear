'''
Testing Simple Linear Regression of stock prices using yfinance lib
Author: Alef Matias
'''

import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
plt.style.use('dark_background')

# yfinance parameters
start_period = '2011-01-01'
end_period = '2021-12-31'
period_test = '3mo'
stock = 'GOOG'

# Train datas
x_train = pd.DataFrame(yf.download(stock, start=start_period, end=end_period)['Low'].dropna().values.reshape(-1, 1))
y_train = pd.DataFrame(yf.download(stock, start=start_period, end=end_period)['Close']).dropna()

# Test datas
x_test = pd.DataFrame(yf.download(stock, period=period_test)['Low'].dropna().values.reshape(-1, 1))
y_test = pd.DataFrame(yf.download(stock, period=period_test)['Close'].dropna())

regression = linear_model.LinearRegression()

regression.fit(x_train, y_train)
predict = regression.predict(x_test)

print(f"Coeficient of correlation: {r2_score(y_test, predict):.2f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, predict)}")

# Visualizing the train results
plt.scatter(x_train, y_train, color='blue', s=5)
plt.plot(x_train[0], regression.predict(x_train), color='red', linewidth=0.5)
plt.title(f'Train results of {stock}')
plt.show()

# Visualizing the test results
plt.scatter(x_test, y_test, color='lightcoral', s=5)
plt.plot(x_test[0], predict, color='khaki', linewidth=1)
plt.title(f'Test results of {stock}')
plt.show()
