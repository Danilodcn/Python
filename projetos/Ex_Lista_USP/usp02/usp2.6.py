"""Dado um inteiro positivo, determine a sua decomposição
em fatores primos calculando tambem a multiplicidade de cada fator"""

#Primereira maneina
n = int(input('n = '))
n2 = n
primo = 2
while True:
    mult = 0
    maior = 0
    while n % primo == 0:
        mult = mult + 1
        n = n / primo
    if maior < mult:
        maior = mult
        print('fator =', primo, 'multiplicidade = ', maior)

    primo = primo + 1

    if n <= 1: break




def primo(n):
    np = 0
    k = 2
    while np < n:
        for i in range(k, k + 1):
            primo = True
            for j in range(2, i):
                if i % j == 0:
                    primo = False
                    break
            if primo:
                q = i
                np = np + 1
        k = k + 1
    return q
