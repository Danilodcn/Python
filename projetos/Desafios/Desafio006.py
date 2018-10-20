#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero: '))
print('o dobro, o triplo e a raiz quadrada de {} sao {}, {} e {:.2f} respectivamente.'.format(n, 2*n, 3*n, n**(1/2)))
