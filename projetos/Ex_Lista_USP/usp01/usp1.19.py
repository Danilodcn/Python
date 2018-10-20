"""Dados tres numeros, imprimi-lo em ordem crescente"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a > b:
    maior = a
    a = b
    b = maior
if a > c:
    maior = a
    a = c
    c = maior
if b > c:
    maior = b
    b = c
    c = maior

print(a, b, c)