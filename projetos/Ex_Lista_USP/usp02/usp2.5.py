"""Dado m, determine os impares consecutivos cuja soma e igual a n*n*n para n assumindo valores entre 1 e m"""

def soma(lista):
    s = 0
    for i in lista:
        s = s + i
    return s

def cubo(n):
    lista = []
    i = 0
    while True:
        i = i + 1
        if i % 2 != 0:
            lista.append(i)


        if len(lista) == n:
            if soma(lista) == n ** 3:
                break
            else: del lista[0]
    return lista

n = int(input('n = '))

print(cubo(n))



