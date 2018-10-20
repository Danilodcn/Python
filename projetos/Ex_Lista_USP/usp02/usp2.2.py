"""Dado uminteiro n, mostrar todos os inteiros entre 1 e n tais que
podem ser comprimentos de hipotenusa de um triangulo de lados inteiros"""

n = 200000 # Exemplo
"""lista = []
for i in range(1, n + 1):  # i é o comprimento da hipotenusa

    for j in range(1, i):  # j é o comprimento dos catetos
        if i ** 2 == 2 * (j ** 2):
            lista.append(i)

print(lista)
"""
lista = []

for hip in range(1, n + 1):
    achou = False
    cateto = 1
    while (cateto < hip) and not achou and (2 * (cateto *cateto) < hip * hip):
        cateto = cateto + 1
        print(2 * cateto * cateto, 'e', hip * hip )
        if 2 * (cateto * cateto) == hip * hip:
            print('Hipotenusa = {}, catetos = {}'.format(hip, cateto))
            achou = True
            lista.append(hip)
print(lista)