"""Dado um inteiro n, n >= 0, verificar se n é polídrome """

n = int(input('n = '))

n = str(n)

if (10 < len(n)) and (len(n) % 2 == 0):
    polidrome = True
    for i in range(0, int(len(n) / 2) - 1):
        if n[i] != n[len(n) - 1 -i]:
            polidrome = False
    if polidrome:
        print(n, 'é polidrome')
    else: print(n, 'não é polidrome')

else: print('Número inválido')