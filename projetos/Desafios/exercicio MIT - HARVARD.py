 # Sendo x # y = sqrt(x * x + 3 * x * y + y * y - 2 * y - 2 * x + 4) / (x * y + 4)
 # ache o valor de ((...((2007 # 2006) # 2005) # ...) # 1)

from math import sqrt

def calculo(x, y):
    res = sqrt(x * x + 3 * x * y + y * y - 2 * y - 2 * x + 4) / (x * y + 4)
    return res

x = 2007
y = x - 1
x = calculo(x, y)
print(x, y)
for i in range(2005):
    y = 2005 - i
    print(calculo(x, y), y)
