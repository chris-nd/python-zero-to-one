a = 'a globale' # variable globale
def f():
    a = 'a dans f' # variable locale
    print(a)

print(a) # a globale
f() # a dans f
print(a) # a globale

# L'instruction global
def f():
    global a # déclare a comme variable globale
    a = 'a dans f'
    print(a)

print(a) # a globale
f() # a dans f
print(a) # a dans f

a = 10
def f():
    global a
    a = a + 10

print(a) # 10
f()
print(a) # 20

# Préférences pour les fonctions pures 
# pour éviter les effets de bord
note = 10
def add_10(n):
    return n + 10

note = add_10(note) # note = 20
print(note) # 20

a = 'a globale'
def f():
    a = 'a de f'
    def g():
        a = 'a de g'
        print(a)
    g()
    print(a)

f() # (a de g) et ensuite (a de f)
print(a) # a globale

# L'instruction nonlocal
a = 'a globale'
def f():
    a = 'a de f'
    def g():
        nonlocal a
        a = 'a de g'
        print(a)
    g()
    print(a)

f() # (a de g) et ensuite (a de g)
print(a) # a globale