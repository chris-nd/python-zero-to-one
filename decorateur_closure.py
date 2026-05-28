import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print('{:.2} s'.format(time.time() - start))
        return res
    return wrapper

@timer
def sum_poly5(n):
    return sum(i**5 for i in range(n))

sum_poly5(1_000_000)

# Limitation de la clôture de fonction
# Les closures en Python ont certaines limitations,
# notamment en ce qui concerne la modification des variables libres.

# nonlocal

def trace_call(f):
    called = 0
    def wrapper(*args, **kwargs):
        nonlocal called
        called += 1
        print(f'{called} appels de {f.__name__}')
        return f(*args, **kwargs)
    return wrapper

@trace_call
def my_func():
    pass

my_func()
my_func()

# attribut de fonction

def trace_call2(f):
    def wrapper(*args, **kwargs):
        wrapper.called = wrapper.called + 1
        print(f'{wrapper.called} appels de {f.__name__}')
        return f(*args, **kwargs)
    wrapper.called = 0
    return wrapper

@trace_call2
def my_func2():
    pass

my_func2()
my_func2()
