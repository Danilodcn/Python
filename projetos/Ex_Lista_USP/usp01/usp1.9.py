"""Dado n e dois numeros inteiros i e j, imprimir em ordem crescente
os n primeiros naturais que sao multiplos de i ou j e ou de ambos. """

n = int(input('n = '))
i = int(input('i = '))
j = int(input('j = '))
numero = 0
n2 = 0
while True:
    if (numero % i == 0) or (numero % j == 0):
        print(numero)
        n2 = n2+1
    numero = numero + 1
    if n2 == n:
        break
