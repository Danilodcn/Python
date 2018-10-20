class ponto:
    "Classe que manipula cordenadas de pontos (x, y)"

    def __init__(self, cord_x = 0, cord_y = 0):
        "Cria um ponto na origem"
        self.x = cord_x
        self.y = cord_y

    def __str__(self):
        "Serve para imprimir na tela"
        return f"({self.x}, {self.y})"

    def getx(self):
        "Retorna a cordenada x"

        return self.x

    def gety(self):
        "Retorna a cornada y"

        return self.y

import tkinter

a = tkinter._test()
