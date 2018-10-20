# a) escreva uma função bloco que receba como paramentro um inteiro n,
# uma sequencia com n inteiros devolvendo uma dos seguintes valores:
# 0, se os n elementos da lista forem pares
# 1, se os n elementos da lista forem impares
# -1, se entre os n numeros da lista existe elementos com paridade diferente

# b) usando a função anterior escreva um programa que receba uma funçao como entrada
# e verifica se ela e piramidal m-alternante


import random


# Obtendo a lista com n inteiros
def lista(n):
    lista = []

    for i in range(n):
        lista.append(random.randrange(0, 100000))

    return lista


lista = lista(n=int(input('n = ')))


# função que determina se todos os elementos de uma lista sao iguais
def iguais(lista):
    iguais = True

    for i in lista:
        if i != lista[0]:
            iguais = False
            break

    return iguais


# função bloco
# retorna 0 se todos os elementos da lista forem pares
# retorna 1 se todos os elementos forem impares
# retorna -1 se entre os elementos da lista exixte elementos com paridade diferente
def bloco(lista):
    bloco = []

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            bloco.append(0)

        else:
            bloco.append(1)

    if iguais(bloco):
        return bloco[0]

    else:
        return -1


# resolução da segunda parte
# determina se a lista pode ser dividida
def divisao(lista):
    i, soma = [1, 0]

    while soma <= len(lista):
        soma += i
        i += 1

        if soma == len(lista):
            return True

    return False


# divide a lista
def div_segmentos(lista):
    div_segmentos = []
    antes = depois = i = 0

    while depois + i + 1 <= len(lista):
        i += 1
        a = lista[antes:depois + i]
        div_segmentos.append(a)
        antes = depois = depois + i

    return div_segmentos


# funçao principal
def main(lista):
    piramidal = False

    if divisao(lista):  # o codigio deve ser executado se a lista pode ser "dividida"
        segmentos = div_segmentos(lista)
        paridade = []
        piramidal = True

        for i in segmentos:
            if bloco(i) == -1:
                piramidal = False
                break
            paridade.append(bloco(i))

        if piramidal:
            for i in range(len(paridade) - 1):
                if paridade[i] == paridade[i + 1]:
                    piramidal = False
                    break

    if piramidal:
        print(len(paridade))
    else:
        print('nao')

    return piramidal

main(lista)
