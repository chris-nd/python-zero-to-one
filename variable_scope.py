a, b, c = 1, 1, 1

def g():
     b, c = 2, 4
     b = b + 10
     def h():
         c = 5
         print(a, b, c)
     h()
g()

print(a, b, c)