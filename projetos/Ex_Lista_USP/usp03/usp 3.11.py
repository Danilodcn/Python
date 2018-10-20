# Faça um programa que calcula 1 - 1/2 + 1/3 - 1/4 + ... + 1/9999 - 1/10000 das seguintes maneiras:
# 1. adição de termos da direita para a esquerda
# 2. adição de termos da esquerda para a direita
# 3. adiçao separada dos termos positivos e negativos da esquerda para a direita
# 4. adiçao separada dos termos positivos e negativos da direita para a esquerda


# função para resolução da 1ª maneira
def primeira():
    lista = []
    soma = 0
    for i in range(1, 10001):
        lista.append(i)
    lista = lista[::-1]
    for i in lista:
        if i % 2 == 0:
            soma = soma - (1 / i)
        else:
            soma = soma + (1 / i)
    return soma


# fução para resolução da 2º maneira
def segunda():
    soma = 0
    for i in range(1, 10001):
        if i % 2 == 0:
            soma = soma - (1 / i)
        else:
            soma = soma + (1 / i)
    return soma


# fução para resolução da 3° maneira
def terceira():
    negativos = positivos = 0
    for i in range(1, 10001):
        if i % 2 == 0:
            positivos += 1 / i
        else:
            negativos += 1 / i
    soma = negativos - positivos
    return soma


# fução para resolução da 4° maneira
def quarta():
    lista = []
    for i in range(1, 10001):
        lista.append(i)
    lista = lista[::-1]
    positivos = negativos = soma = 0
    for i in lista:
        if i % 2 == 0:
            positivos += 1 / i
        else:
            negativos += 1 / i
    soma = negativos - positivos

    return soma


def main():
    print('__________RESOLUÇÃO__________\n')
    print('1º maneira: ', primeira())
    print('2° maneira: ', segunda())
    print('3° maneira: ', terceira())
    print('4° maneira: ', quarta())


main()
