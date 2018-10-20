#Dados n e uma sequencia n inteiros, determinar quantos segmentos de numeros iguais que compõe essa sequencia.


#Sequencia de numeros
lista = []
while True:
    n = int(input('Digite um numero: '))
    if n >= 0:
        lista.append(n)
    else: break

print('A lista é ', lista)
q, i= [1, 1]
while True:
    if lista[i] != lista[i + 1]:
        q = q + 1
    i = i + 1
    if i == len(lista) - 1: break
print('Existem ', q,' segmentos iguais')