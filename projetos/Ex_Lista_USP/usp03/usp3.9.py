# Dado um inteiro positivo n e n triplas compostas por um símbolo
# de operaçao (+, -, * ou /) e dois numeros reais, calcule #

import random


# Gera uma tripla aleatoria
def tripla():
    i = random.randrange(0,4)
    tripla = []
    if i == 0:
        tripla = tripla + ["+"]
    elif i == 1:
        tripla = tripla + ["-"]
    elif i == 2:
        tripla = tripla + ["*"]
    elif i == 3:
        tripla = tripla + ["/"]

    i = int(100 * random.random())
    tripla = tripla + [i]
    i = int(100 * random.random())
    tripla = tripla + [i]
    return tripla

# Gera n triplas
def tripas(n):
    triplas = []
    for i in range(n):
        triplas.append(tripla())
    return triplas


def main(n):
    triplas =tripas(n)
    for tripla in triplas:
        if tripla[0] == "+":
            res = tripla[1] + tripla[2]
        if tripla[0] == "-":
            res = tripla[1] - tripla[2]
        if tripla[0] == "*":
            res = tripla[1] * tripla[2]
        if tripla[0] == "/":
            res = tripla[1] / tripla[2]
        print(tripla, res)

n = int(input('n = '))

main(n)

