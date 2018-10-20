
#Dado um inteiro positivo n e uma sequencia com n inteiros,
#verificar de existe um inteiro k tal que a sequencia e k-alternante e mostre esse valor#

lista = [1, 7, 2, 8, 5, 7, 2, 4]
pares = []
impares = []
for i in range(len(lista)):

    if lista[i] % 2 != 0:
        impares = impares + [lista[i]]
        print(impares)
    else:
        pares = pares + [lista[i]]
        print(pares)