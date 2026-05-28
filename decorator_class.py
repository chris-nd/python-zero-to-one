class NbAppel:

    def __init__(self, f):
        self.appel = 0
        self.f = f

    def __call__(self, *args, **kwargs):
        self.appel += 1
        s = f"{self.f.__name__} a été appelé {self.appel} fois"
        print(s)
        return self.f(*args, **kwargs)


def f(a, b):
    print(a + b)

# f n'est plus une fonction normale 
# mais une instance de la classe NbAppel
f = NbAppel(f)
f(1, 2)
f(3, 4)
f(5, 6)

@NbAppel
def f2(a, b):
    print(a + b)



f2(1, 2)
f2(3, 4)
f2(5, 6)
