# a) escreva uma função que recebe um inteiro positivo ano, e devolve 1 se o ano é bissexto, 0 caso contrario.escreva uma função que tenha como entrada e saida tres numeros inteiros representando uma data,
# e modifica esses inteiros de modo a eles representarem o dia seguinte
# c) escreva um programa que leia n datas e imprima o dia seguinte para todas elas

import random


def bissexto(ano):
    if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
        return 1
    else:
        return 0


def diaSeguinte(d, m, a):
    mes31 = [1, 3, 5, 7, 8, 10, 12]
    mes30 = [4, 6, 9, 11]
    d += 1
    if (m in mes31) and (d > 32):
        d = 32
    elif (m in mes30) and d > 31:
        d = 31
    elif (d > 30) and (m == 2):
        if bissexto(a):
            d = 30
        else:
            d = 29
    if (m in mes31) and (d == 32):
        m += 1
        d = 1
    elif (m in mes31) and (d == 31):
        m += 1
        d = 1
    elif (m == 2) and bissexto(a) and (d == 30):
        m += 1
        d = 1
    if m == 13:
        a += 1
        m = 1
    return d, m, a


def datas(n):
    k = 0
    t = []
    for i in range(n):
        a = random.randrange(1500, 3501)
        m = random.randrange(1, 13)
        d = random.randrange(1, 32)
        data = diaSeguinte(d, m, a)
        print(f'o proximo dia a data ({d}, {m}, {a}) e {data}')

n=int(input('n = '))
datas(n)
