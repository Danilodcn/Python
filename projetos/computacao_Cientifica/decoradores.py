def fazNada(f):
    def novaf(*args, **kargs):
        print("chamando ...", args, kargs)
        s =  f(*args, **kargs)
        return s
        
    novaf.__name__ = f.__name__
    novaf.__doc__ = f.__doc__
    novaf.__dict__.update(f.__dict__)
    return novaf
    
@fazNada
def soma(a,b):
    return a + b
print(soma(1,2))


