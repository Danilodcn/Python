# a) escreva uma função que recebe um inteiro positivo e devolve 1 se m e primo e 0 caso contrario
# b) escreava um programa que recebe um inteiro nao negativo n e imprime a soma dos n primeiros primos

def primo(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return 0

    return 1


def soma(n):
    i = 1
    soma = 0
    con = 0

    while con < n:
        i += 1

        if primo(i):
            soma += i
            con += 1

    return soma


print(soma(n=int(input('n = '))))
