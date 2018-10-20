"""Dado dois números interios positivos,
determinar o maximo divisor entre eles usando o algoritimo de Euclides"""


# metodo de teste de todos os numeros nemores que o menor n e m
def teste():
    n, m = [int(input('n = ')), int(input('m = '))]
    maior, mdc = (n, 1)
    if n < m:
        maior = m
    for i in range(1, maior + 1):
        if (n % i == 0) and (m % i == 0):
            mdc1 = i
            if mdc1 > mdc:
                mdc = mdc1
    print(mdc)


# Algoritimo de Euclides
def teste2():
    n, m, mdc, resto = [int(input('n = ')), int(input('m = ')), 1, 1]
    if m <= 0 or n <= 0:
        print('Números inválidos')
    else:
        maior = n if n > m else m
        menor = m if n > m else n
    while resto > 0:
        resto = maior % menor
        maior = menor
        menor = resto

    print('mdc({},{}) = {}'.format(n, m, maior))


print('USANDO TESTES SUCESSIVOS')
teste()
print('USANDO O ALGORITIMO DE EUCLIDES')
teste2()
