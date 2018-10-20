def selectionSort(seq):
	"""Funcao usa o metodo de ordenação por seleção"""
	for i in range(0, len(seq) - 1):
		for j in range(i, len(seq)):
			if seq[i] > seq[j]:
				seq[i], seq[j] = seq[j], seq[i]
	return seq
	
def insertSort(seq):
	for i in range(1, len(seq)):
		ch = seq[i]
		j = i - 1
		while j >= 0 and seq[j] > ch:
			seq[j + 1] = seq[j] 
			j -= 1
		
		seq[j + 1] = ch
	return seq

def merge(seq, p, q, r):
	a, b = seq[p:q] + [float("inf")], seq[q:r] + [float("inf")]
	i, j = 0, 0
	for k in range(p, r):
		if a[i] > b[j]:
			seq[k], j = b[j], j + 1
		else:
			seq[k], i = a[i], i + 1

def mergeSortAuxiliar(seq):
	p, r = 0, len(seq)
	if  r == 1: pass
	else:
		q = int((r + p)/2)
		a = mergeSortAuxiliar(seq[p:q])
		b = mergeSortAuxiliar(seq[q:r])
		seq = a + b
		merge(seq, p, q, r)
	return seq

def mergeSort(seq, p = 0, r = 0):
	if r == 0: r = len(seq)
	a, seq, b = seq[:p], seq[p:r], seq[r:]
	return a + mergeSortAuxiliar(seq) + b
	
if __name__ == "__main__":
	import random
	seq = [random.randint(0, 100) for i in range(10)]
	print(seq)
	print(mergeSort(seq))
	print(selectionSort(seq))
	print(insertSort(seq))
	
