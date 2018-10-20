class No:
	def __init__(self, dado, left = None, right = None):
		self._dado = dado
		self._left = left
		self._right = right
		self._pai = None
		
	def __str__(self): return f"No: {self.getDado()}"
	def getDado(self): return self._dado
	def setDado(self, novo): self._dado = novo
	def getLeft(self): return self._left
	def setLeft(self, novo): self._left = novo
	def getRight(self):	return self._right
	def setRight(self, novo): self._right = novo
	def getPai(self): return self._pai
	def setPai(self, novo): self._pai = novo

class Tree(No):
	def __init__(self, raiz = None):
		self._raiz = raiz
	def __str__(self): return f"{self.getRaiz()}"
		
	def getRaiz(self):return self._raiz
	def setRaiz(self, nova): self._raiz = nova
	
	def buscar(self, x, dado):
		if self.getRaiz == None or x.getDado() == dado:
			return x
		elif x < dado: return self.buscar(self.getLeft(), dado)
		else: return self.buscar(self.getRight(), dado)
		
	def minimo(self, x):
		while x.getLeft() is not None: x = getLeft()
		return x
	def maximo(self, x):
		while x.getRight() is not None: x = getRight()
		return x
	
	def sucessor(self, x):
		if x.getRight() != None: return self.minimo(x.getRight())
		y = x.getPai()
		while y != None and not x is y.getRight():
			x = y
			y = y.getPai()
		return y
	def predecessor(self, x):
		if x.getLeft() != None:
			return self.maximo(x.getLeft())
		y = x.getPai()
		while y != None and not x is y.getLeft():
			x = y
			y = y.getPai()
		return y
		
	def inserir(self, z):
		y  = None
		x = self.getRaiz()
		while x != None:
			y = x
			if z.getDado() < y.getDado(): x = x.getLeft()
			else: x = x.getRight()
		
		z.setPai(y)
		if y == None: self.getRaiz(z)
		else: 
			if z.getDado() < y.getDado(): y.setLeft(z)
			else: y.setRight(z)
			
	def remover(self, x):
		if x.getLeft() == None or x.getRight() == None: y = x
		else: y = self.sucessor(x)
		if y.getLeft() != None: z = y.getLeft()
		else: z = getRight()
		if z == None: z.setPai(y.getPai())
		if y.getPai() == None: self.getRaiz(z)
		else:
			if y == y.getPai().getLeft(): y.getPai().setLeft(z)
			else: y.getPai().setRight(z)
		
		if y != x: x.setDado(y.getDado) 
			
		
		
		
			
	

t = Tree(2)
n = No(4)
t.inserir(n)

print(t)
