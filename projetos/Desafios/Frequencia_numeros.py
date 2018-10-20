# esse programa calcula a frequencia com que os digitos aparecem como primeiro
# digito em uma sequen de numeros de k digitos

import csv

# abrindo um arquivo
try:
    arq = open("Fibonacci.csv", "r")
except:
    print("Arquivo nao encontrado!!!")

f = {}

for x, y in tuple(csv.reader(arq)):
    f[x] = int(y)

arq.close()

ff = f.copy()

def fibonacci(n):
    if str(n) not in f.keys():
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            f[str(n)] = fibonacci(n - 1) + fibonacci(n - 2)
            return f[str(n)]
    else:
        return f[str(n)]


def n_fibonacci(n):
    lista = []
    for i in range(n):
        lista.append(fibonacci(i))
    return tuple(lista)



freq = {}
for i in range(10):
    freq[str(i)] = 0

def frequencia(n = 10):
    for i in n_fibonacci(n):
        i = str(i)
        try:
            freq[i[3]] += 1
        except:
            None
    print(freq)





#if f[list(f.keys())[len(f) - 1]] > ff[list(ff.keys())[len(ff) - 1]]:
 #   print("True")

arq = open("Fibonacci.csv", "a")

csv.writer(arq).writerows(f.items())

#arq.close()

#else: print(False, f[list(f.keys())[len(f) - 1]] > ff[list(ff.keys())[len(ff) - 1]], )

print(f)

import datetime


print("s" or "   ", 3, ord("s"), chr(115))
for i in range(100000):
    try:
        if chr(i) != chr(0):
            print(i, chr(i))
            arq.write(str(i) + ", " + chr(i))
    except:
        None




print(chr(960) + "=3,14")


