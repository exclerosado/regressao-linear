'''
Calculando coeficiente de correlação utilizando dados da bolsa de valores com a biblioteca yfinance
Autor: Alef Matias
'''

import yfinance as yf


def coeficient(action, period, col1, col2):
    x = yf.download(action, period=period)[col1]
    y = yf.download(action, period=period)[col2]

    length = len(yf.download(action, period=period))
    sumX = x.sum()
    sumY = y.sum()
    xy = x * y
    sumXY = xy.sum()
    xSquared = x ** 2
    ySquared = y ** 2
    sumXSquared = xSquared.sum()
    sumYSquared = ySquared.sum()

    rCoeficient = (length * sumXY - (sumX * sumY)) / ((length * sumXSquared - (sumX ** 2)) * (length * sumYSquared - (sumY ** 2))) ** 0.5

    return rCoeficient


print(f"R Coeficient: {coeficient('AMZN', '1y', 'High', 'Close'):.2f}")
