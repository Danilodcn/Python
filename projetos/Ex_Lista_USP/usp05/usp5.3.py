# a) escreva uma função que recebe tres inteiros m, n e d,
# devolve 1 se d divide pelo menos um entre m e n, 0 caso contrário.
# Fora isso se d divide m, divide m por d e o mesmo para n


def divide(m, n, d):
    if m > n:
        maior = m
        m = n
        n = maior
        del maior
    meio = False
    for i in range(m + 1, n):
        if i % d == 0:
            meio = True
            break
    if m % d == 0:
        if n % d == 0:
            return meio, m / d, n / d
        return meio, m / d, 0
    elif n % d == 0:
        return meio, 0, n / d
    return meio, 0, 0


def mdc(m, n):
    menor = m
    if m > n:
        menor = n
    a = menor
    mdc = 1
    for d in range(1, menor + 1):
        lista = divide(m, n, d)
        if a > lista[1] and lista[1] != 0 and lista[2] != 0:
            a = lista[1]
            mdc = d
            print(d, lista[0])
"""m, n = [int(input('m = ')), int(input("n = "))]

mdc(m, n)"""

def somaBits(b1, b2, vaiUm, soma):
    b1, b2, vaiUm, soma = [int(b1), int(b2), int(vaiUm), str(soma)]
    s = b1 + b2 + vaiUm
    if s > 1:
        vaiUm = s - 1
        if s == 2:
            s = 0
        elif s == 3:
            s = 1
    else: vaiUm = 0
    soma = str(s) + soma
    return soma, vaiUm
# n = 111010
# m = 010101


soma = somaBits(0, 1, 0, '')[0]
vaiUm = somaBits(0, 1, 0, '')[1]
soma, vaiUm = [somaBits(1, 0, vaiUm, soma)[0], somaBits(1, 0, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(0, 1, vaiUm, soma)[0], somaBits(0, 1, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(1, 0, vaiUm, soma)[0], somaBits(1, 0, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(1, 1, vaiUm, soma)[0], somaBits(1, 1, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(1, 0, vaiUm, soma)[0], somaBits(1, 0, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(0, 0, vaiUm, soma)[0], somaBits(0, 0, vaiUm, soma)[1]]
soma, vaiUm = [somaBits(0, 0, vaiUm, soma)[0], somaBits(0, 0, vaiUm, soma)[1]]



print(soma, vaiUm)