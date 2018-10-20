"""Verificar de um dado número inteiro é perfeito, ou seja, é igual a soma de seus divisores positivos"""


def perfeito():
    m, soma = [int(input('numero = ')), 0]
    for i in range(1, m):
        if m % i == 0:
            soma = soma + i
    if soma == m:
        print('o número {} é perfeito '.format(m))
    else: print('O número {} não é perfeito'.format(m))
perfeito()