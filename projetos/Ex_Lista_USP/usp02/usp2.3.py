"""Dados dois inteiros positivos m e n, determinar, entre todos os pares de numeros inteiros (x, y)
tais que 0<= x <= m e 0 <= y  <= m, um par para qual o valor da expressao x*y - x*x + y seja maxima e
calcular tambem esse maximo."""

m, n, maior = [10, 10, 0]     #exemplo
par = [0, 0]
for x in range(m + 1):

    for y in range(n + 1):

        valor = x * (x - y) + y
        if maior < valor:
            maior = valor
            par[0] = x
            par[1] = y

print(maior, par)


