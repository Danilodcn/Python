class Racionais():
    def __init__(self, nun, den = 1):
        self.nun = nun
        self.den = den

    def __str__(self):
        return str(self.nun)+"/"+str(self.den)

    def simplifica(self):
        m, n = (self.nun, self.den)
        if n > m:
            n, m = (m, n)
        res = 1
        while res > 0:
            res = n % m
            m, n = (res, m)
        self.nun = int(self.nun / n)
        self.den = int(self.den / n)

    def soma(self, nun):
        den = self.den * nun.den
        nun = self.nun * nun.den + nun.nun * self.den
        return Racionais(nun, den)

    def sub(self, nun):
        den = self.den * nun.den
        nun = self.nun * nun.den - nun.nun * self.den
        return Racionais(nun, den)

    def multiplica(self, other):
        nun = self.nun * other.nun
        den = self.den * other.den
        return Racionais(nun, den)

    def divide(self, other):
        nun = self.nun * other.den
        den = self.den * other.nun
        return Racionais(nun, den)

    def __add__(self, other):
        return self.soma(other)

    def __sub__(self, other):
        return self.sub(other)

m = Racionais(2, 4)
n = Racionais(3, 4)

print(m.multiplica(n), m.divide(n))

