# Faça um programa que le um inteiro positivo n e uma sequencia com n inteiros positivos (x, y)
# e verifica se cada ponto portence ou não a H. O programa deve tambem contar o numero de pontos
# na sequencia que pertencem a H

import random


def h1(x, y):
    if (x <= 0) and (y <= 0) and (y + x ** 2 + 2 * x - 3 <= 0):
        return True
    else:
        return False


def h2(x, y):
    if (x >= 0) and (y + x ** 2 - 2 * x - 3):
        return True
    else:
        return False


def sequencia(n):
    lista = []
    for i in range(n):
        x = random.randrange(-100, 100) * random.random()
        y = random.randrange(-100, 100) * random.random()
        lista.append([x, y])
    return lista


def main(n):
    num = []
    q = 0
    for i in sequencia(n):
        if h1(i[0], i[1]) and h2(i[0], i[1]):
            num.append(i)
            q += 1
    return q, num

n = int(input('n = '))
print(main(n))