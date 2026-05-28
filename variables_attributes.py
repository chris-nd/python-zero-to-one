# La résolution d'Attribut repose:
# sur l'arbre d'héritage et la MRO (Method Resolution Order)

# La résolution de variable repose:
# sur la règle LEGB et la liaison lexicale

a = 1

class C:
    a = 2
    def f(self):
        # a = 3
        # print(a) # 3
        print(a) # 1
        print(self.a) # 2
        print(C.a) # 2

c = C()
# c.f() # 3 2 2
c.f() # 1 2 2
print(a) # 1
print(c.a) # 2
print(C.a) # 2

class A:
    a = 2
    class B:
        def f(self):
            print(a) # 1
            print(A.a) # 2

ins = A.B()
ins.f() # 1 2