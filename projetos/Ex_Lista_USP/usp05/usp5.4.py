# a) escreva uma função que recebe tres bits, b1, b2 e vaiUm, e devolve um bit soma,
# representando a soma e o novo bit em vaiUm


def somaBits(b1, b2, vaiUm, soma):
    b1, b2, vaiUm, soma = [int(b1), int(b2), int(vaiUm), str(soma)]
    s, vaiUm= (b1 + b2 + vaiUm, 0)

    if s == 2: s = 0; vaiUm = 1

    elif s == 3: s = 1; vaiUm = 1

    soma = str(s) + soma

    return soma, vaiUm

def soma(m, n):
    m, n = [str(m), str(n)]
    if len(m) > len(n):
        m, n = (n, m)
    b1, b2, con = (m[len(m) - 1], n[len(n) - 1], 1)
    soma, vaiUm = somaBits(b1, b2, 0, '')
    while con < len(n) or vaiUm == 1:
        con += 1
        if len(m) - con < 0: b1 = 0
        else: b1 = m[len(m) - con]
        if len(n) - con < 0: b2 = 0
        else: b2 = n[len(n) - con]
        soma, vaiUm = somaBits(b1, b2, vaiUm, soma)
    return int(soma)


def possivel(m, n):
    m, n = [str(m), str(n)]
    for i in range(0, len(m) - 1):
        if m[i] not in ['0', '1']: return False

    for i in range(len(n)):
        if n[i] not in ['0', '1']: return False

    return True

def somaBinario(m, n):
    m, n = [str(m), str(n)]

    if possivel(m, n): s = soma(m, n); return s

    else: return SyntaxError

