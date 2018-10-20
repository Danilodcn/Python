# considere as seguintes formulas de recorrencia:
#
# f(1) = 2, f(2) = 1, f(i) = 2 * f(i - 1) + g(i - 1) se i >= 1
# g(1) = 1, g(2) = 2, g(i) = g(i - 1) + 3 * f(i - 1) se i >= 1

# b) faca uma funcao valor que recebe um inteiro k>= 1 e devolve f(k) e g(k)
# c) faca um programa que leia um inteiro n>2 e imprime o valores de f(n - 2) + g(n + 200) e f(n + 200) - g(n - 2)


def valor(k):
    if k is 1:
        f, g = [2, 1]
    elif k is 2:
        f, g = [1, 2]
    elif k > 2:
        f = 2 * valor(k - 1)[0] + valor(k - 2)[1]
        g = valor(k - 1)[1] + 3 * valor(k - 2)[0]
    else: return 0, 0
    return f, g


if __name__ == '__main__':
    n = int(input('n = '))
    print(valor(n - 2)[0] + valor(n + 200)[1])
    print(valor(n + 200)[0] - valor(n - 2)[1])