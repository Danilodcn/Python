# Faça um programa para resolver o seguinte problema:
# São dadas  as cordenadas reais x e y de um ponto, o numero natural n,
# e as cordenadas reais de n pontos(1<=n<=100). Deseja-se calcular e imprimir
# sem repetiçao os raios das circunferencias centradas no ponto (x, y)
# que passa por pelo menos um dos n pontos dados

from random import randrange

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distancia(self, other):
        from math import sqrt
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def origem(self):
        self.x = 0
        self.y = 0


def main():
    MAX, MIN = (1, -1)
    x, y = [randrange(MIN, MAX + 1), randrange(MIN, MAX + 1)]
    n = randrange(1, 21)
    pontos = []
    for i in range(n):
        pontos.append(Ponto(randrange(MIN, MAX + 1), randrange(MIN, MAX + 1)))

    p = Ponto(x, y)

    distancias = []
    for ponto in pontos:
        distancia = p.distancia(ponto)
        if distancia not in distancias:
            distancias.append(distancia)

    print(distancias, n)

if __name__ == '__main__':
    main()