def teste():
    teste = open('teste.txt', 'r')
    teste = teste.readlines()
    for i in teste:
        for j in range(len(i)):
            linha = i[:len(i)-1]
            print(linha)
            break


def tartaruga():
    import turtle, math, random


    wn = turtle.Screen()
    wn.title("Fução Seno")
    t = turtle.Turtle()
    t.forward(20)
    texto = wn.textinput('eu', 'prompt')
    t.write(texto, True, 'left', ("Arial", 12, "normal"))
    print()
    t.speed(1)
    for i in range(int(texto)):
        altrx, altry = (random.randrange(0, 200), random.randrange(0, 200))
        t.goto(altrx, altry)

    wn.exitonclick()

tartaruga()
