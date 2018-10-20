def raiz(n):
    return lambda x: x ** (1 / n)
    
r = raiz(5)
print(r(32))
