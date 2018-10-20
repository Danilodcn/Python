def exercicio_01():
    "Usando o arquivo texto notas_estudantes.dat escreva um programa que imprime o nome dos alunos que têm mais de seis notas."

    try:
        notas = open("notas_estudantes.dat", "r")
        alunos = ""
        linhas = notas.readlines()
        for linha in linhas:
            linha = linha.split()
            if len(linha) > 7:
                alunos = alunos + linha[0] + ", "

        print(alunos[:len(alunos) - 2])

        notas.close()

    except: print("Arquivo não encontrado!!!")


def exercicio_02():
    "Usando o arquivo texto notas_estudantes.dat escreva um programa que calcula a média das notas de cada estudante e imprime o nome e a média de cada estudante."
    try:
        alunos = open("notas_estudantes.dat", "r")
        linhas = alunos.readlines()
        for linha in linhas:
            linha = linha.split()
            soma = 0
            for nota in linha[1:len(linha)]:
                soma += int(nota)
            print(f"{linha[0]} obteve média {soma / len(linha) - 1 :.2f}")

        alunos.close()

    except: print("Arquivo não encontrado!!")


def exercicio_03():
    "Usando o arquivo texto notas_estudantes.dat escreva um programa que calcula a nota mínima e máxima de cada estudante e imprima o nome de cada aluno junto com a suam notá máxima e mínima."
    alunos = open("notas_estudantes.dat", "r")
    linhas = alunos.readlines()
    for linha in linhas:
        linha = linha.split()
        max = min = int(linha[1])
        for nota in linha[1:len(linha)]:
            if int(nota) > max:
                max = int(nota)
            elif int(nota) < min:
                min = int(nota)
        print(f"{linha[0]}, nota maxima = {max} e nota minima = {min}")

def exercicio_04():

    def media(lista):
        s = 0
        for i in lista:
            s += i
        return s / len(lista)

    def soma(lista):
        s = 0
        for i in lista:
            s += i
        return s


    import turtle

    arq = open("lab.dat", "r")
    linhas = arq.readlines()

    wp = turtle.Screen()
    wp.title("Exercicio 04 files")
    wp.screensize(300, 300)

    alex = turtle.Turtle()
    alex.color("blue")
    alex.penup()

    mel = turtle.Turtle()
    mel.color("blue")
    mel.penup()

    x_valores = []
    y_valores = []
    n = 0

    for linha in linhas:
        n += 1
        linha = linha.split()
        x, y = (int(linha[0]), int(linha[1]))

        x_valores.append(x)
        y_valores.append(y)

        alex.goto(x, y)
        alex.stamp()





    arq.close()
    wp.exitonclick()


def exercicio_05():
    """A linhas do arquivo misterio.dat contém ou a palavra
    CIMA ou BAIXO ou um par de números. CIMA e BAIXO são instruções
    para a tartaruga colocar a sua cauda para cima ou para baixo.
    O par de números são coordenadas x,y.
    Escreva um programa que lê o arquivo misterio.dat
    e usa a tartaruga para desenhar a figura descrita
    pelos comandos e cojunto de pontos no arquivo."""

    import turtle

    arq = open("misterio.dat", "r")
    linhas = arq.readlines()

    canvas = turtle.Screen()
    canvas.title("misterio.dat")
    canvas.bgcolor("blue")

    mel = turtle.Turtle()

    cauda = ["CIMA\n", "BAIXO\n"]

    for linha in linhas:
        if linha in cauda:
            if linha == cauda[0]:
                mel.penup()
            else:
                mel.pendown()
        else:
            linha = linha.split()
            x, y = tuple(linha)
            x, y = (int(x), int(y))

            mel.goto(x, y)
    arq.close()
    canvas.exitonclick()


