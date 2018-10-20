"""Dados um numero positivo n e um asequencia de n inteiros positivos,
determinar o comprimento de um segmento de comprimento maximo"""


lista = []
while True:
    n = int(input('Digite um numero: '))
    if n < 0: break
    lista.append(n)



print('A sequencia é {}'.format(lista))


con, qt, maior = [0, 1, 1]
while True:
    if con == len(lista) - 2: break
    if lista[con] < lista[con + 1]:
        qt = qt + 1
        if qt > maior:
            maior = qt
    else: qt = 1

    con = con + 1
print('O segmento maximo é ', maior)