"""Dados n e uma sequencia de n numeros inteiros,
determinar a soma dos numeros pares."""

numero = int(input('Digite um numero NATURAL: '))
soma = 0
sequencia = 0
while True:
    sequencia = sequencia + 1
    if sequencia % 2 == 0:
        soma = soma + sequencia
    if sequencia == numero:
        break

print(soma)
