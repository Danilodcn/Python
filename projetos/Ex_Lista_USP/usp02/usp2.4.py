"""Dados n e uma sequencia de n inteiros positivos, calcular a soma dos numeros da sequencia que sao primos"""

import random


def primos(n):
    primo = True
    for i in range(2, int(n ** (1 / 2)) + 1):

        if n % i == 0:
            primo = False
            break
    return primo


n = int(input('n = '))
lista = []

for i in range(n):
    i = random.random()
    i = int(10 * i)
    lista.append(i)
print(lista)

soma = 0

for i in range(len(lista)):

    if primos(lista[i]):
        soma = soma + lista[i]
print(soma)
