# Dados numeros reais x e e, com e>0, calcular uma aproximação para sen(x)
# através da serie de Taylor.
import math
def fatorial(n):
    fatorial = float(1)
    for i in range(1, n + 1):
        fatorial = fatorial * i
    return fatorial


def main(x, e):
    i = 0
    sen = 0
    while True:
        sen = sen + (-1) ** i * x ** (2 * i + 1) / fatorial(2 * i + 1)
        if abs(x ** (2 * i + 1)) / fatorial(2 * i + 1) < e:
            break
        i += 1
    print(sen)


x = float(input('x = '))
e = float(input('e = '))
if e > 0:
    main(x, e)
else: print('Erro! e<=0')
