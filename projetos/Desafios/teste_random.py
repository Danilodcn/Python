import random, crypt

n = int(input('n = '))

a = 0   #ocorrencias < 5
b = 0   #ocorrencias > 5
c = 0   #verificacao
for i in range(n):
        numero = 10 * random.random()

        if numero < 1:
            a = a + 1
        elif numero > 5:
            b = b + 1
        if (numero > 10) or (numero < 0):
            c = c + 1

print('a = ', a, 'b = ', b, 'c = ', c)