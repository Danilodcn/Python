# a) escreva uma funçao que recebe dois numeros a e b como parametro e devolve o mdc(maximo divisor comum),
# calculado por meio do algoritimo de elclides
# b) escreva um programa que le um inteiro n e uma sequencia de n inteiros nao negativos
# e imprime o mdc de todos os numeros da sequencia

def mdc(a, b):
    resto = 1
    maior = a if a > b else b
    menor = a if a < b else b

    while resto > 0:
        resto = maior % menor
        maior = menor
        menor = resto

    return maior


import random


def lista(n):
    lista = []

    for i in range(n):
        lista.append(random.randrange(1, 100))

    return lista


lista = lista(n=int(input('n = ')))


def mdcSequencia(lista):
    lista2 = lista

    for i in range(len(lista) - 1):
        a = mdc(lista2[0], lista2[1])
        del lista2[0], lista2[0]
        lista2.append(a)

        if a == 1:
            return 1

    return lista2[len(lista2) - 1]


print(mdcSequencia(lista))

