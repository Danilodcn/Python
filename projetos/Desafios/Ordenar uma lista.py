"""Ordena uma lista"""

#Ordenar lista
def ordenar_lista(lista):

    tamanho = len(lista)
    for i in range(0, tamanho - 1):
        for j in range(i + 1, tamanho):
            print(j)
            if lista[i] > lista[j]:
                menor = lista[j]
                lista[j] = lista[i]
                lista[i] = menor
    return


print('PROGRAMA PARA ORDENAR UMA LISTA')
lista = []
while True:
    n = int(input('Digite um número: '))
    if n == 0: break
    lista.append(n)
    print(lista)



ordenar_lista(lista)