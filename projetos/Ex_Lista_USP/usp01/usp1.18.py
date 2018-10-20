"""Dados tres numeros positivos, verificar se eles formam os lados de um triangulo"""

def teste_triangulo(lados):
    triangulo = True
    if (lados[0] > 0) and (lados[1] > 0) and (lados[2] > 0):
        if lados[0] > lados[1] + lados[2]:
            triangulo = False
        if lados[1] > lados[0] + lados[2]:
            triangulo = False
        if lados[2] > lados[0] + lados[1]:
            triangulo = False
    else:
        triangulo = False

    if triangulo == False: print('o triangulo nao existe')
    elif triangulo == True: print('O triangulo existe')




#Obter uma lista com 5 numeros
i = 0
a = []
while True:
    if i > 2: break
    n = float(input('Digite o {}o número: '.format(i + 1)))
    a.append(n)
    i += 1

teste_triangulo(a)