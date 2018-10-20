"""Dado um numero na base binária, transformá-lo para a base decimal"""

def decimal_binario(binario):
    decimal, binario = [0, str(binario)]
    binario, tamanho = [binario[::-1], len(binario)]
    for i in range(tamanho):
        if binario[i] == "1":
            decimal = decimal + (2 ** i)
    return decimal

n = input('Digite: ')
print(decimal_binario(n))