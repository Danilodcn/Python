import time
def recursao(raio, k = 10):
    import turtle, math

    canvas = turtle.Screen()
    canvas.title("Visualizando recursao")
    ted = turtle.Turtle()

    # visualizando recursao
    def circulo(raio):
        def inicio():
            ted.penup()
            ted.goto(-raio, 0)
            ted.pendown()

        def semi(k = 1):
            try:
                for i in range(int(3 * raio)):
                    x = -raio + i
                    y = (raio ** 2 - x ** 2) ** (1 / 2)
                    ted.goto(x, k * y)
            except: None

        def semi_circunferencia(bool=True):
            if bool:
                semi()
            else:
                semi(-1)

        inicio()
        semi_circunferencia()
        inicio()
        semi_circunferencia(False)

    def teste(raio, k):
        if raio > 0:
            circulo(raio)
            teste(raio - k, k)
        ted.penup()
        ted.goto(0, 0)
        ted.pendown()

    teste(raio, k)


    ted.write(time.clock(), False, "left", ("Arial", 12, "normal"))
    canvas.exitonclick()




import csv

dados = {}
a = 0
for i in "abcdefghijklmnopqrstuvwxyz":
    dados[i] = a
    a += 1

print(dados)
file = open("dados.csv", "w")
out = csv.writer(file)
out.writerows(dados.items())

file.close()

file = open("dados.csv", "r")

inp = csv.reader(file)
dic = {}
dic2 = []
for reg in inp:
    dic2.append((reg[0], int(reg[1])))

dic = dict(dic2)
print(dic)

file.close()


for i in dir("a"):
    print(i)


