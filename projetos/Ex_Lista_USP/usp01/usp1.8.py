#Dado um inteiro n nao-negativo, determinar n!

numero=int(input('Digite um numero nao negativo: '))
resposta=1
if numero<0:
    print('O número {} é negativo!'.format(numero))
elif numero==0:
    print('0! é igual a 1')
else:
    for i in range(1 , numero+1):
        resposta=resposta*i

print(resposta)

con = 0
while resposta > 10:
    resposta = resposta / 10
    con += 1
print(f'{resposta:.3f}e{con:d}')