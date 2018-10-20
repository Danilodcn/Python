from math import cos, sin, pi, asin


n = 100000
dx = pi / n
menor = 10
res = 0

for i in range(int(n / 2), n):
    s = i * dx
    a = cos(s) + s * sin(s) - 1

    if menor > abs(a):
        menor = abs(a)
        res = s

print(res, sin(res), pi-res)

r = pi - res
k = asin(r)
A1 = r * k + cos(r) - 1
A2 = cos(r) - cos(res) - k * res + k * r

print(A1, A2, k, r)