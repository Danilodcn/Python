# a) faça uma funçao arctang que recebe um numero real x, com 0 <= x <= 0, e devolve uma aproximação
# do arco tangente de x (em radianos) usando a serie de Taylor para a função arco tangente
# b) faca uma fução angulo que que recebe um ponto de cordenadas cartesianas reais (x, y),
# com x>=0 e y>=0, e devolve o angulo formado pelo vetor (x, y) e o eixo horizontal
# c) faca um programa que dado n pontos no primeiro quadrante atraves de suas cordenadas cartesianas,
# determina o ponto que forma o menor angulo com o eixo horizontal#
import math, random

def arctang(x):
    i = 1
    parcela1 = parcela2 = 1
    arctang = 0
    while (abs(parcela1) > 0.000001) or (abs(parcela2) > 0.000001):
        parcela1, parcela2 = (x ** i / i, x ** (i + 2) / (i + 2))
        parcela = parcela1 - parcela2
        arctang += parcela
        i += 4
    return arctang


def radGraus(rad):
    grau = float(180 * rad / math.pi)
    return grau


def angulo(x, y):
    if x < y:
        tang = float(x / y)
        x = arctang(tang)
        x = 90 - radGraus(x)
        return x
    else:
        tang = y / x
        x = arctang(tang)
        x = radGraus(x)
        return x


def ponto():
    return [random.randrange(1,100), random.randrange(1, 100)]

def pontos(n):
    maior = angulo(ponto()[0], ponto()[1])
    lista = [maior]
    for i in range(n - 1):
        menor = angulo(ponto()[0], ponto()[1])
        lista.append(menor)
        if maior > menor:
            maior = menor
    return maior, lista

n = pontos(12)
print(n[1][0], n)