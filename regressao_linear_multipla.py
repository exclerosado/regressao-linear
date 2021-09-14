'''
Descrição: Reprodução de um exercício de Regressão Linear Múltipla
Autor: Alef Matias
'''

def somatorio(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


y = [6, 10, 20, 40]
x1 = [8, 6, 14, 20]
x2 = [0, 1, 2, 1]

x1barra = somatorio(x1) / len(x1)
x2barra = somatorio(x2) / len(x2)
ybarra = somatorio(y) / len(y)


def colunas(lista, media):
    resultado = []
    for i in lista:
        resultado.append(i - media)
    return resultado


Y = colunas(y, ybarra)
x1i = colunas(x1, x1barra)
x2i = colunas(x2, x2barra)

Yx1 = list(map(lambda x, y: x * y, Y, x1i))
Yx2 = list(map(lambda x, y: x * y, Y, x2i))
x1x2 = list(map(lambda x, y: x * y, x1i, x2i))
x12 = list(map(lambda x: x ** 2, x1i))
x22 = list(map(lambda x: x ** 2, x2i))

somaYx1 = somatorio(Yx1)
somax22 = somatorio(x22)
somaYx2 = somatorio(Yx2)
somax1x2 = somatorio(x1x2)
somax12 = somatorio(x12)

b1 = ((somaYx1 * somax22) - (somaYx2 * somax1x2)) / (somax12 * somax22 - (somax1x2 ** 2))
b2 = ((somaYx2 * somax12) - (somaYx1 * somax1x2)) / (somax12 * somax22 - (somax1x2 ** 2))
b0 = ybarra - (b1 * x1barra) - (b2 * x2barra)

print(f'Beta1 = {b1:.2f}')
print(f'Beta2 = {b2:.2f}')
print(f'Beta0 = {b0:.2f}')

estimarx1 = 3
estimarx2 = 2

ychapeu = b0 + (b1 * estimarx1) + (b2 * estimarx2)

print(f'Resultado = {ychapeu:.2f}')
