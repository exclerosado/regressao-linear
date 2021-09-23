"""
Aplicação de Regressão Linear Múltipla em Ações
Empresa utilizada: PETROBRAS
Código do papel: PETR4
Período: 01/08/2021 a 31/08/2021
Fonte: investing.com
"""


# Método para obter o somatório das listas
def somatorio(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma


# Método para multiplicar duas listas
def multiplicacao(lista1, lista2):
    xy = list(map(lambda x, y: x * y, lista1, lista2))
    return xy


# Método para elevar os itens de uma lista ao quadrado
def quadrado(lista):
    quad = list(map(lambda x: x ** 2, lista))
    return quad


# Obtendo o somatório das listas
def calcularR(lista1, lista2):
    y = somatorio(lista1)
    x = somatorio(lista2)
    xy = somatorio(multiplicacao(lista1, lista2))
    x2 = somatorio(quadrado(lista2))
    y2 = somatorio(quadrado(lista1))

    r = ((len(lista1) * xy) - (x * y)) / ((len(lista2) * x2 - (x ** 2)) * (len(lista2) * y2 - y ** 2)) ** 0.5

    return r


def coeficiente(r12, r13, r23):
    r = (((r12 ** 2) + (r13 ** 2) - (2 * r12 * r13 * r23)) / (1 - (r23 ** 2))) ** 0.5
    return r


# Dados
fechamento = [26.41, 26.85, 26.28, 28.35, 28.39, 28.19, 28.28, 28.67, 29.10, 29.35, 28.64, 27.03, 26.79, 26.64, 26.60,
              27.02, 27.58, 27.73, 27.49, 28.49, 28.30, 27.19]
maxima = [27.41, 26.87, 26.77, 28.98, 28.54, 28.21, 28.78, 28.99, 29.19, 29.61, 29.24, 27.63, 27.31, 26.87, 26.63,
          27.31, 27.63, 27.83, 27.88, 28.49, 28.71, 28.23]
minima = [26.37, 25.79, 25.95, 28.06, 28.02, 27.67, 28.24, 27.97, 28.50, 29.02, 28.24, 26.45, 26.65, 26.13, 26.17,
          26.77, 27.24, 27.38, 27.47, 27.67, 28.26, 26.99]
volume = [70.04, 71.53, 87.58, 222.99, 50.80, 75.03, 84.02, 97.61, 94.92, 84.74, 100.31, 92.96, 85.28, 80.25, 84.94,
          69.50, 49.60, 45.93, 40.64, 76.10, 60.86, 109.91]
variacao = [-1.86, 1.67, -2.12, 7.88, 0.14, -0.70, 0.32, 1.38, 1.50, 0.86, -2.42, -5.62, -0.89, -0.56, -0.15, 1.58,
            2.07, 0.54, -0.87, 3.64, -0.67, -3.92]


print('Correlação entre Valor de Fechamento, Volume e Variação')
print(f'Coeficiente r12 - {calcularR(volume, fechamento):.2f}')
print(f'Coeficiente r13 - {calcularR(variacao, fechamento):.2f}')
print(f'Coeficiente r23 - {calcularR(volume, variacao):.2f}')
print(f'Coeficiente r123 - {coeficiente(calcularR(volume, fechamento), calcularR(variacao, fechamento), calcularR(volume, variacao)):.2f}\n')

print('Correlação entre Valor de Fechamento, Máxima e Mínima')
print(f'Coeficiente r12 - {calcularR(maxima, fechamento):.2f}')
print(f'Coeficiente r13 - {calcularR(minima, fechamento):.2f}')
print(f'Coeficiente r23 - {calcularR(maxima, minima):.2f}')
print(f'Coeficiente r123 - {coeficiente(calcularR(maxima, fechamento), calcularR(minima, fechamento), calcularR(maxima, minima)):.2f}')
