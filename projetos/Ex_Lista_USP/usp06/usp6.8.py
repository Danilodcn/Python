# Dados dois numeros inteiros m e n, e duas sequencias ordenadas com m e n
# numeros inteiros, obter uma unica sequencia ordenada contendo todos os
# elementos das sequencias sem reetição

from random import randrange as rd

def adicionaLista(lista = [], numero = 0):
    if len(lista) == 0:
        lista.append(numero)
    for i in range(len(lista)):
        if lista[i] > numero:
            lista.insert(i, numero)
            break
    if lista[len(lista) -1] < numero:
        lista.append(numero)

m = 10#int(input("m = "))
n = 12#int(input("n = "))
maior, menor = (m, n)

if m > n:
    maior, menor = (m, n)
else:
    maior, menor = (n, m)

lista = [1, 6, 7, 9]
print(lista)
adicionaLista(lista, 1)
print(lista)