import random

def circulo(x, y):
    if (x > 0) and (y > 0) and (x < 1) and (y < 1):
        print('O ponto ({}, {}) pertence a H'.format(x, y))
        return True
    else:
        print('O ponto ({}, {}) não pertence a H'.format(x, y))
        return False


x = 1.5*random.random()
y = 1.5 * random.random()
circulo(x, y)

