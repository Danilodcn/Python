# Dados um inteiro positivo n e uma sequencia de n reais, determinar os numeros
# que compoem a sequnecia e o numero de vezes que cada um deles ocorre na mesma.
from random import randrange


class aleatorio():

    def lista(self, n=20):
        self.lista = []
        for i in range(n):
            self.lista.append(int(randrange(-10, 10)) / 10 + randrange(-10, 10))
        return self.lista


n = int(input("n = "))
dict = {}
lista = aleatorio()

for numero in lista.lista(n):
    if numero not in dict.keys():
        dict[numero] = 1
    else:
        dict[numero] += 1

print("Sequencia : ", end="")
for chave in dict.keys():
    print(chave, "\t", end="")

print("Saída : ")
for chave in dict.keys():
    print(chave, "ocorre", dict[chave])