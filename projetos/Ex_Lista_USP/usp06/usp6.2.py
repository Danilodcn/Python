# Deseja-se publicar o numero de acertos de cada aluno de uma sala em uma prova em forma de testes.
# A prova consta de 30 questoes, cada uma com 5 alternativas identificadas como A, B, C, D e E.
# Para isso são dadas:
# - o cartão gabarito
# - o número de alunos na turma
# - o cartao resposta contendo seu numero e suas respostas

import random

def gabarito(n):    #n é o numero de questoes
    gabarito = []
    respostas = ['A', 'B', 'C', 'D', 'E']
    for i in range(n):
        gabarito.append(respostas[random.randrange(0, 5)])
    return gabarito


def cartaoResposta(nAlunos, n):    #n é o numero de questoes
    respostas = []
    for i in range(1, nAlunos + 1):
        respostas.append([i, gabarito(n)])
    return respostas

if __name__ == "__main__":
    while True:
        try:
            nAlunos = int(input('nAlunos = '))
            n = int(input('n = '))
            break
        except: print('Digite numeros inteiros')
    respostas = cartaoResposta(nAlunos, n)
    gabarito = gabarito(n)

    file = open('usp6.2.txt', 'w')

    for resposta in respostas:
        corretas = 0
        for i in range(len(resposta[1]) - 1):
            if resposta[1][i] == gabarito[i]:
                corretas += 1
        print(f'O aluno {resposta[0]} acertou {corretas} questoes')
        file.write(f'O aluno {resposta[0]} acertou {corretas} questoes\n')
    file.close()

