# Dado o numero de alunos de uma determinada classe e
# as tres notas das provas de cada aluno,
# calcular a média aritmética das provas de cada aluno,
# a média da classe, o numero de aprovados e o numero de reprovados

import random

#Cria uma lista com 3 notas de n alunos
def lista(n):
    lista = []
    for i in range(n):
        a = random.randrange(0, 20) / 2
        b = random.randrange(0, 20) / 2
        c = random.randrange(0, 20) / 2
        lista.append([a, b, c])
    return lista


#Calcula a media dos elementos de uma lista
def media(lista):
    s = 0
    for i in lista:
        s += i
    return s / len(lista)



def main(n):
    notas = lista(n)
    classe = []
    aprovados = 0
    for i in range(len(notas)):
        md = media(notas[i])
        classe.append(md)
        print('O aluno %d obteve média %.2f' %(i + 1, md))
        if md >= 5:
            aprovados += 1


    print('A media da classe foi %.2f' %media(classe))
    print('Numero de aprovados: {}. Reprovados {}'.format(aprovados, n - aprovados))



n = int(input('n = '))
main(n)
