from random import randint
from time import clock

l = [i for i in range(0, 5)]
n = len(l)

def aleatorio(seq):
	t = len(seq)
	for i in range(t):
		k = randint(0, t - 1)
		seq[i], seq[k] = seq[k], seq[i]
	return seq

def igual(seq1, seq2):
	for i, j in zip(seq1, seq2): 
		if i != j: return False
	else: return True
	
	
def main():
	t = clock()
	p = aleatorio(l.copy())
	m = 0
	n = 1000000

	for i in range(n):
		k = aleatorio(l)
		if igual(k, p): 
			print(k, p)
			m += 1

	print(m, m / n, clock() - t)
	
if __name__ == "__main__":
	main()
