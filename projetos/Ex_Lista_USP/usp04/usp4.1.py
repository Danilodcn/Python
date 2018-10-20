# Um numero a é dito permutação de um numero b se os numeros de a formam um permutação dos digitos de b.
# considere que o digito 0 não aparece nos numeros.
# 1. faça uma função contadigitos que, recebendo um inteiro n e um inteiro d, 0<d<=9,
# devolve quantas vezes o digito d aparece em n
# 2. faca um programa que le dois numeros, a e b, e responde se a é permutação de b


# Primeira parte
def contadigitos(n, d):
    n, con = [str(n), 0]
    for i in range(len(n)):
        if n[i] == str(d):
            con += 1
    return con



a = int(input('a = '))
b = int(input('b = '))

# fução principal
def main(a, b):
    for i in range(0, 10):
        permutacao = True
        if contadigitos(a, i) != contadigitos(b, i):
            permutacao = False
            break
    return permutacao

if main(a, b):
    print('{} é permutação de {}'.format(a, b))
else:
    print('{} não é permutação de {}'.format(a, b))