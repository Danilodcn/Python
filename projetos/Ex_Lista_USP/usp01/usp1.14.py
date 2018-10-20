"""Mostrar o n-ésimo termo da sequencia de Fibonacci"""

def fibonacci():
    n= int(input('Digite um número natural maior que 2: '))
    if n <= 2: print('Número Inválido')
    else:
        #f1 e f2 representam o ultimo e o penultimo termo da sequencia
        f1 = 1
        f2 = 1
        fn = 0
        print(f1)
        print(f2)
        for i in range(1, n-1):
            fn = f2 + f1
            f1 = f2
            f2 = fn
        print('O termo F{} da sequencia de Fibonacci é {}'.format(n, fn))
fibonacci()

