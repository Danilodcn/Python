# simule a execução do programa

def f1(x, y):
    if y != 0:
        res = x / y
    else: res = 1 / x
    while x > y:
        res += float(y / x)
        x -= 1
    return res

def main(a, b, c, d):
    print('Digite quetro numeros')
    a = int(input('a = '))
    b = int(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))
    print(f'a = {a}, b = {b}, c = {c}, d = {d}')
    while a < b:
        if c > d:
            d = f1(b, a)
            b -= 1
        else:
            c = 1 / f1(a, b)
            a += 1
        print(f'a = {a}, b = {b}, c = {c}, d = {d}')
    return 0

main(1, 1, 1, 1)