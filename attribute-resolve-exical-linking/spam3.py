"Variables et attributs"

a = 1

class A:
    a = 2

    class B:
        a = 3

        def f(self):
            print(a)
            print(self.a)
            print(A.a)

ins = A.B()
ins.f()
