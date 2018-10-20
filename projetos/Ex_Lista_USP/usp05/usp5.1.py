# escreva uma função que recebe um inteiro n e devolve o numero de digitos de n e o primeiro digito de n


def digitos(n):
    n = str(n)
    return len(n), int(n[0])

print(digitos(12334))

def ler(n):
    for i in range(n):
        n = input('Digite um numero: ')
        print(f'o numero de digitos de {n} é {digitos(n)[0]} e o primeiro digito é {digitos(n)[1]}')
ler(5)