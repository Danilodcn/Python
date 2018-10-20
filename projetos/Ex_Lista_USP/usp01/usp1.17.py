"""Dado um natural na base decimal, transforma-lo para binaria """
import math

math.pow(1,4)

def decimal_binario(decimal):
    decimal, binario = [int(decimal), '']
    while True:
        binario, decimal = [binario + str(decimal % 2), int(decimal / 2)]
        if decimal == 0: break
    binario = binario[::-1]
    binatio = int(binario)
    return binario
def binario_decimal(binario):
    binario, decimal = [str(binario), 0]
    binario = binario[::-1]
    tamanho = len(binario)

    for i in range(tamanho):
        if binario[i] == '1':
            decimal = decimal + (2 ** i)
    return decimal


n = input('n = ')
print(binario_decimal(n))



#m = input('m = ')
#print(decimal_binario(m))
#print("soma em binario: {}".format(decimal_binario(n) + decimal_binario(m)))
