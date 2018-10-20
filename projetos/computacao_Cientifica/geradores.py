def letras(st):
    for i in st:
        yield i
        
for l in letras("There was once a farmer and your wife."):
    print(l, end = "")
    
print("\n", end = "")
