"""
Listas de Exercicios
"""

def buscaBinaria(seq, x, p = 0, r = 0): #pesquisa binaria
	if r == 0: r = len(seq)
	if len(seq[p:r]) == 1 and x != seq[p]: return None
	q = int((r + p) / 2)
	if x == seq[q]:
		return q
	if x < seq[q]:
		return buscaBinaria(seq, x, p, q)
	else: return buscaBinaria(seq, x, q, r)

def exercicio_2_3_5():
	from random import randint
	seq, x = [randint(0, 100) for i in range(100)], 0#randint(0, 100)
	seq.sort()
	print(seq, x, buscaBinaria(seq, x))
	
if __name__ == "__main__":
	exercicio_2_3_5()
	
	
