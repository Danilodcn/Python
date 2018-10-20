
from math import sqrt, pow
import time

class Isoceles:
    def __init__(self):
        self.base = 16
        self.lado = 17
        self._altura()

    def _altura(self):
        self.altura = sqrt(pow(self.lado, 2) - pow(self.base / 2, 2))
        return self.altura

    def smartLess(self):
        return (self.altura == self.base + 1) or (self.altura == self.base - 1)

    def _lado(self, k = 2):
        self.lado = sqrt(5 * pow(self.base, 2) + k * self.base + 1)

    def proximoTriangulo(self):
        stop = False
        while not stop:
            self.base += 1
            self._lado()
            if self.smartLess():
                break
            else:
                self._lado(-2)


triangulo = Isoceles()
print(triangulo.base, triangulo.altura, triangulo.lado, triangulo.smartLess())
triangulo.proximoTriangulo()
print(triangulo.base, triangulo.altura, triangulo.lado, triangulo.smartLess())
triangulo.proximoTriangulo()
print(triangulo.base, triangulo.altura, triangulo.lado, triangulo.smartLess())
print(time.clock())