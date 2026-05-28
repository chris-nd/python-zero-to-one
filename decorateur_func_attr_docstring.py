from functools import wraps

def trace_call(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.called = wrapper.called + 1
        print(f'{wrapper.called} appels de {f.__name__}')
        return f(*args, **kwargs)
    wrapper.called = 0
    return wrapper

@trace_call
def my_func():
    "Documentation de my_func"
    pass

my_func()
my_func()

print(my_func.__doc__)
print(my_func.__name__)
print(my_func.__module__)
print(my_func.__dict__)
print(my_func.__closure__)
print(my_func.__globals__)
print(my_func.__dir__)
print(help(my_func))
