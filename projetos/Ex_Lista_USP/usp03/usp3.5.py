# Dados a, b e c, calcular as raízes de uma equação do 2° grau da forma a*x**2 + b*x + c = 0
# especificando se as raízes sãp duplas, distintas ou complexas.

import math


def raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        imag = math.sqrt(-1 * delta)

        r1 = complex((-1 * b) / (2 * a), imag / (2 * a))
        r2 = complex((-1 * b) / (2 * a), -1 * imag / (2 * a))


    else:
        real = math.sqrt(delta)
        r1 = (-1 * b) / (2 * a) + real / (2 * a)
        r2 = (-1 * b) / (2 * a) - real / (2 * a)


    if (delta >= 0) and (r1 == r2):
        print('a.   RAIZ DUPLA ', r1)
    elif (delta > 0) and (r1 != r2):
        print('b.   REAIS DISTINTAS %.2f, %.2f' %(r1, r2))
    elif delta < 0:
        print('c.   COMPLEXAS {}, {}'.format(r1, r2))


print('Na equação a*x**2 + b*x + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
raizes(a, b, c)