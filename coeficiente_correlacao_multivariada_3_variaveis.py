'''
Aplicação de Regressão Linear Múltivariada
Utilização com 3 variáveis
Autor: Alef Matias
'''

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


# Método para calcular o coeficiente de correlação entre as variáveis
def calcularR(lista1, lista2):
    y = somatorio(lista1)
    x = somatorio(lista2)
    xy = somatorio(multiplicacao(lista1, lista2))
    x2 = somatorio(quadrado(lista2))
    y2 = somatorio(quadrado(lista1))

    r = ((len(lista1) * xy) - (x * y)) / ((len(lista2) * x2 - (x ** 2)) * (len(lista2) * y2 - y ** 2)) ** 0.5

    return r

# Método para calcular o coeficiente de correlação multivariada
def coeficiente(r12, r13, r23):
    r = (((r12 ** 2) + (r13 ** 2) - (2 * r12 * r13 * r23)) / (1 - (r23 ** 2))) ** 0.5

    return r


# Dados
y = [6, 10, 20, 40]
x1 = [8, 6, 14, 20]
x2 = [0, 1, 2, 1]

r_12 = calcularR(x1, y)
r_13 = calcularR(x2, y)
r_23 = calcularR(x1, x2)
r = coeficiente(r_12, r_13, r_23)

print(f'Coeficiente r12 - {r_12:.2f}')
print(f'Coeficiente r13 - {r_13:.2f}')
print(f'Coeficiente r23 - {r_23:.2f}')
print(f'Coeficiente r123 - {r:.2f}')
