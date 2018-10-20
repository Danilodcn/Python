# Dado uma sequencia de n numeros, imprimi-la na ordem inversa a da leitura

import random

def sequencia(n):
    sequencia = []
    for i in range(n):
        sequencia.append(int(100 * random.random()))
    return sequencia


def imprimir(sequencia):
    invertida = []
    for i in range(1, len(sequencia) + 1):
        invertida.append(sequencia[len(sequencia) - i])
    return invertida

if __name__ == '__main__':
    n = int(input('n = '))
    lista = sequencia(n)
    print(f'Sequencia original: {lista}\nSequencia invertida: {imprimir(lista)}')