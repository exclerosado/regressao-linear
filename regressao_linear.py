'''
Descrição: Reprodução de um exercício de Regressão Linear
Autor: Alef Matias
'''

# A lista xi representa os anos de produção
xi = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988]
# A lista yi representa a quantidade produzida
yi = [34, 36, 36, 38, 41, 42, 43, 44, 46]

xiyi = list(map(lambda x,y: x * y, xi, yi))
xi2 = list(map(lambda x: x ** 2, xi))
yi2 = list(map(lambda y: y ** 2, yi))
tamanho = len(xi)

def somatorio(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

somaxi = somatorio(xi)
somayi = somatorio(yi)
somaxiyi = somatorio(xiyi)
somaxi2 = somatorio(xi2)
somayi2 = somatorio(yi2)

r = (tamanho * somaxiyi - (somaxi * somayi)) / ((tamanho * somaxi2 - (somaxi ** 2)) * (tamanho * somayi2 - (somayi ** 2))) ** 0.5

print(f'Coeficiente de correlação: {r:.2f}')

a = (tamanho * somaxiyi - (somaxi * somayi)) / (tamanho * somaxi2 - ((somaxi) ** 2))
xbarra = somaxi / len(xi)
ybarra = somayi / len(yi)
b = ybarra - (a * xbarra)

# Estimando a produção para um ano escolhido
x = 1989

# Equação da reta ajustada
ychapeu = (a * x) + b

print(f'A produção estimada para {x} é de {ychapeu:.2f}.')
