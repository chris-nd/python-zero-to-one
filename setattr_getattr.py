class Temperature:
    def __get__(self, inst, instype):
        print("desc __get__")
        return inst._temperature

    def __set__(self, inst, t):
        print(f"desc __set__ {t}")
        inst._temperature = t

class Maison:

    def __init__(self, t):
        self.temperature = t

    def __getattribute__(self, a):
        print(f"__getattribute__: {a}")
        return object.__getattribute__(self, a)

    def __setattr__(self, a, v):
        print(f"__setattr__: {a} {v}")
        object.__setattr__(self, a, v)

    temperature = Temperature()

maison = Maison(18)
print(maison.temperature)
maison.temperature = 22
print(maison.temperature)
