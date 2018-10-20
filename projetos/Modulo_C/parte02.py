#!/usr/bin/env python3

from tkinter import *


class Janela:
	def __init__(self, cont):
		self.fr1 = Frame(cont)
		self.fr1.pack()

		self.btn01 = Button(cont, text = "Boa Tarde!", bg = "blue")
		self.btn01["font"] = ("verdana", '14', 'italic', 'bold')
		self.btn01["width"] = 10
		self.btn01["height"] = 3
		self.btn01.pack()

		self.btn02 = Button(cont, text = "Meu nome: ", bg = "red")
		self.btn02["height"] = 3
		self.btn02["width"] = 10
		self.btn02["fg"] = "black"
		self.btn02["font"] = ("times", "10", "bold")
		self.btn02.pack()



wn = Tk()
Janela(wn)
wn.mainloop()

class a:
    def  __init__(self, n):
        self.n = n
    def __eq__(self, other):
        if self.n == other.n + 1:
            return True
        return False
    def __call__(self, *args, **kwargs):
        print()


