# Dado um real x e um inteiro positivo n, calcular usando a serie de Taylor de grau n
# o valor de cos(x)


import math

pi = math.pi


def fatorial(n):
    fatorial = float(1)
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial



def main(x, n):
    n = int(n)
    cos = 0
    for i in range(n + 1):
        cos = cos + (-1) ** i * x ** (2 * i) / (fatorial(2 * i))
    print(cos)

x = float(input('x = '))
n = int(input('n = '))

if n >= 0:
    main(x, n)

else: print('erro! n negativo.')