"""Simular a execução do programa destacando sua saida"""

a, b, total, soma= [int(input('Digite um numero: ')), int(input('Digite um numero: ')), 0, 0]

while a != 0:
    total = total + 1
    termo = 1
    for i in range(1, b + 1):
        termo = termo * a
    print('Resp = ', termo)
    soma = soma + termo
    print('Soma = ', soma)
    a, b = [int(input('Digite um numero: ')), int(input('Digite um numero: '))]
    print(a, b)
print('Total de pares: ', total)
