"""
Dados um numero inteiro positivo n e n interios positivos, determinar o maximo divisor com a todos eles
"""
from random import random as rd


n = int(input('n = '))

lista = []
for i in range(n):
    lista = lista + [int(100 * rd())]
lista = lista + [n]
lista = sorted(lista)


print(lista)


menor = lista[0]
mdc = 1
for i in range(len(lista)):
    if menor > lista[i]:
        menor = lista[i]
for j in range(1, menor + 1):
    achei = True
    for k in range(len(lista)):
        if lista[k] % j != 0:
            achei = False
    if achei:
        mdc = j

print(mdc)
