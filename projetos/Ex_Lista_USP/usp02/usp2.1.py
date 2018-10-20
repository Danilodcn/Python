"""Dados um inteiro positivo n e n sequencias de numeros inteiros,
cada uma terminada por 0, calcular a soma dos numeros pares de cada sequencia"""

#estrutura para criar as listas.
lista2 = []
while True:
    lista = []
    while True:
        n = int(input('Digite um numero: '))
        lista.append(n)
        if n == 0: break
    lista2.append(lista)
    escolha = input('precione enter para continuar')
    if not (escolha == '') or not (escolha == ''): break

#Somar os numeros de cada saquencia em lista2
lista3 = []
for i in range(len(lista2)):
    soma = 0
    for j in range(len(lista2[i])):
        if lista2[i][j] % 2 == 0:
            soma = soma + lista2[i][j]
    print('A soma dos numeros pares da lista {} é {}'.format(lista2[i], soma))
    lista3.append(soma)
