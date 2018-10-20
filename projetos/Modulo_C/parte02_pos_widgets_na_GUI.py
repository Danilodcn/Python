#!/usr/bin/env python3


import tkinter as tk
import os


class janela:

	def f01(self, ins_tk):
		self.frame01 = tk.Frame(ins_tk)
		self.frame01.pack()

		tk.Button(self.frame01, text = "B1", bg = "blue").pack()

	def f02(self, ins_tk):
		self.frame02 = tk.Frame(ins_tk)
		self.frame02.pack(side = "top")

		tk.Button(self.frame02, text = "B2", bg = "red").pack(side = "left")
		tk.Button(self.frame02, text = "B3", bg = "red").pack(side = "left")

	def f03(self, ins_tk):
		self.frame03 = tk.Frame(ins_tk)
		self.frame03.pack()

		tk.Button(self.frame03, text = 'B3', bg = 'black', fg = "white").pack(side = "left")
		tk.Button(self.frame03, text = 'B4', bg = 'black', fg = 'white').pack(side = 'left')
		tk.Button(self.frame03, text = 'B5', bg = 'black', fg = 'white', command = self.destroy).pack(side = 'left')

	def destroy(self):
		a = os.getcwd()
		print(a)

wn = tk.Tk()

J = janela()
J.f01(wn)
J.f02(wn)
J.f03(wn)

wn.mainloop()