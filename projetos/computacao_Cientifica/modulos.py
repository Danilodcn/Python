def f(n):
    a, b = 0, 1
    while b < n:
        print(b, end = " ")
        a, b = b, a + b

if __name__ == "__main__":
    import sys
    print(__name__)
    print(sys.argv)
    f(int(sys.argv[1]))
    print()
