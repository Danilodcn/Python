tree = [None]
def inserir(dado, tree):
	if tree[0] == None: tree[0] = [dado, [None], [None]]
	elif tree[0][0] > dado: inserir(dado, tree[0][1])
	else: inserir(dado, tree[0][2])
from random import randint as rint
lista = [rint(1, 101) for i in range(10)]
print(lista)
for i in lista:
	inserir(i, tree)

print(tree)
print(lista)

from pprint import pprint

print("\n" * 2)

pprint(tree)



#pagina 121 do livro Cormen
