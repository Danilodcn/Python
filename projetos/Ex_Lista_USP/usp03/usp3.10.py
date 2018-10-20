# Dado um inteiro positivo n, calcular e imprimir o valor da soma: (a soma está no livro-texto)

def main(n):
    soma = 0
    for i in range(1, n):
        soma = soma + i / (n - (i - 1))
    soma = int(soma * 1000)
    soma = soma / 1000
    return soma

n = int(input('n = '))
print(main(10))
