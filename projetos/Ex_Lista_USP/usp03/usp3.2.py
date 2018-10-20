#Dado um inteiro positivo n, calcular o numero Harmoico H definido por:
# SOMA(1/k) quando k varia de 1 a n


n = int(input('n = '))

soma = 0
for k in range(1, n + 1):
    soma = soma + 1 / k
print(soma)