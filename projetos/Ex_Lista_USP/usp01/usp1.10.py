"""
Dizemos que um numero é triangular se ele é o produto de três números naturais consecutivos.
Dado um número não negativo n, verificar se n é triangular.
"""
#verifica se n é triangular.
def num_triangular(n: object) -> object:
    if n < 0:
        print('Numero inválido!')
    elif n > 0:
        for i in range(1, int(n**(1 / 3) + 1)):
            produto = i * (i + 1)*(i + 2)
            if produto == n:
                print('{} é triangular, pois {}={}*{}*{}!'.format(n, n, i, i + 1, i + 2))
            elif produto > n:
                print('O número {}, não é triangular!'.format(n))

n = int(input('Digite um número: '))
num_triangular(n)
