"""Criar um programa que mostre todas os milhares cuja a raiz quadrada seja igual a soma de suas dezenas"""


def div_dezenas(n):
    n = str(n)
    tam = len(n)
    if tam != 4:
        print('ERRO!')
    else:
        n1 = n[:2]
        n2 = n[2:]
        n3 = int(n1) + int(n2)
        return n3


numeros = []
for i in range(1000, 10000):
    if i == (div_dezenas(i) ** 2):
        numeros.append(i)

print("Os numeros desejados sao: {}".format(numeros))
