
lbd = lambda x: x**2

print(lbd(5)) # 25

def function_with_lambda(lambda_func):
    return lambda_func(5)

print(function_with_lambda(lbd)) # 25

def image(func: callable):
    print(type(func))
    for x in range(10):
        print(f"{x}: {func(x)}")

def carre(x):
    return x**2

image(carre)

print(callable(carre))