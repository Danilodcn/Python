"""Dado os numeros inteiros j, m e n, imprimir o n pprimeiros naturais congruentes a j modulo m """


def congruente1():
    j, m, n, soma1, soma2 = [int(input('j = ')), int(input('m = ')), int(input('n = ')), 0, 0]
    if n <= 0:
        print('Número Inválido')
    else:
        while soma2 != n:
            soma1 = soma1 + 1
            if (soma1 % j) == (m % j):
                soma2 = soma2 + 1
                print('{} é congruente módulo {} a {}'.format(soma1, j, m))


def congruente2():
    j, m, n = [int(input('j = ')), int(input('m = ')), int(input('n = '))]
    resto = m % j
    for i in range(1, n+1):
        k = resto + j * (i - 1)
        print('{} é congruente módulo {} a {}'.format(k, j, m))


congruente1()

congruente2()