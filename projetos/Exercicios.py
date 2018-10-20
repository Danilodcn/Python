# opcao 1: Calcula quadado de um numero n.
def quadrado():
    while True:  # (n!=0):
        n = int(input("Digite um Numero: "))
        if (n == 0):
            print("")
            break
        print(n * n)


# opcao 2: Calcula a soma dos n inteiros.
def soma_n_inteiros(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    print(s)


# opcao 3: imprime numeros impares menores que n.
def imprimir_impares(n):
    for i in range(1, n + 1):
        if (i % 2 == 1):
            print(i)


# opcao 4: calcular x potencia n.
def calcular_x_potencia_n(x, n):  # x e n nao inteiros
    p = 1
    for n in range(1, n + 1):
        p = p * x
    print(p)


# opcao 5: Sabendo a quantidade discos diareamente vendidos, determinar o dia e a quantidade de discos vendidos
def maior_numero_30():
    maior, dia, soma = (0, 0, 0)
    for i in range(1, 31):
        n_discos = int(input("Numero de discos vendidos no dia %d: " % i))
        soma = soma + n_discos
        if (n_discos > maior):
            maior = n_discos
            dia = i
    print("o maior numero de discos vendidos foi %d no dia %d" % (maior, dia))
    print("Foram vendidos %d discos esse mes" % soma)


def maior_nota_alunos_turma():
    maior_nota, melhor_aluno, numero, soma, nota = (0, 0, 0, 0, 0)
    while True:
        numero = numero + 1
        soma = soma + nota
        print("Digite qualquer numero maior que 100 para ver os resultados")
        nota = int(input("Nota do aluno %d: " % numero))
        if (nota > 100):
            break
        elif (maior_nota < nota):
            maior_nota = nota
            melhor_aluno = numero
    media = soma / (numero - 1)
    print("o numero, maior nota, e a media da turma sao respectivamente : %d, %d e %d" % (
    melhor_aluno, maior_nota, media))


# Comeco do programa.
while True:
    print("")
    print("RESPOSTA DOS EXERCICIOS")
    print("")
    # Escolhas
    print("0. Fecha o programa")
    print("1. Dada uma coleção de numeros inteiros terminada em 0, imprimir seus quadrados.")
    print("2. Calcular a soma dos n primeiros numeros inteiros.")
    print("3. Imprimir todos os numeros impares menosres que n dado.")
    print("4. Dado um inteiro n e um inteiro nao negativo n, calcular x potencia n.")
    print("5. Sabendo a quantidade discos diareamente vendidos, determinar o dia e a quantidade de discos vendidos")
    print("6. Dado o numero de alunos e suas notas, determinar a maior nota e o numero do aluno")
    print("")
    opcao = int(input("Escolha o numero do exercicio:"))

    # Condiçoes de execução do programa.
    if (opcao == 0):
        break
    elif (opcao == 1):
        print("Funcao quadrado de um numero")
        # n=int(input ("Digite um Numero: "))
        quadrado()
    elif (opcao == 2):
        print("Funcao soma de inteiros positivos")
        n = int(input("Digite um Numero: "))
        soma_n_inteiros(n)
    elif (opcao == 3):
        print("Funcao que imprime os mumeros menores que n")
        n = int(input("Digite um numero: "))
        imprimir_impares(n)
    elif (opcao == 4):
        print("Fução que calcula x potecia n")
        x = int(input("Valor de x: "))
        n = int(input("Valor de n: "))
        calcular_x_potencia_n(x, n)
    elif (opcao == 5):
        print("Funcao que encontra valor maior")
        maior_numero_30()
    elif (opcao == 6):
        maior_nota_alunos_turma()

    else:
        print("")
        print("Opção invalida")
