import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
plt.style.use('dark_background')

# Variáveis de treinamento
x_train = np.array([1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]).reshape(-1, 1)
y_train = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

# Variáveis de teste
x_test = np.array([1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980]).reshape(-1, 1)
y_test = np.array([20, 22, 23, 28, 31, 26, 27, 32, 33, 45, 34, 35, 36, 38, 41])

# Instanciando o objeto de regressão linear
regression = linear_model.LinearRegression()

# Ajustando os dados de treinamento
regression.fit(x_train, y_train)

# Testando os dados no modelo
y_predict = regression.predict(x_test)

print(f'Coeficients: {regression.coef_}\nMean squared error: {mean_squared_error(y_test, y_predict):.2f}\nDetermination: {r2_score(y_test, y_predict):.2f}')

plt.scatter(x_test, y_test, color='green')
plt.plot(x_test, y_predict, color='red', linewidth=1)
plt.show()
