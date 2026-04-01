carre = [x**2 for x in range(1000)]
print(sum(carre))

# Expréssion génératrice

# Création d'un générateur
carre = (x**2 for x in range(1000))
print(carre) # <generator object <genexpr> at 0x...>

print(sum(carre)) # 333333000
print(sum(carre)) # 0 parce que le générateur, qui est un itérateur, est épuisé
print(next(carre)) # Lève une exception StopIteration

# Générateur de nombres palindromes
gen_carre = (x**2 for x in range(1_000))
palin = (x for x in gen_carre if str(x) == str(x)[::-1])
print(palin) # <generator object <genexpr> at 0x...>
print(list(palin)) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Fonction génératrice
def gen(): 
    yield 10

print(gen) # <function gen at 0x...>
print(gen()) # <generator object gen at 0x...>

g = gen() 
print(next(g)) # 10
print(next(g)) # Lève une exception StopIteration

def gen(x): 
    yield x 
    x = x + 1 
    yield x

g = gen(15) 
print(next(g)) # 15
print(next(g)) # 16
print(next(g)) # Lève une exception StopIteration

# Fonction génératrice pour les carrés
def carre(a, b): 
    for i in range(a, b): 
        yield i ** 2

c = carre(1, 10) # Création d'un générateur
print(list(c)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Fonction génératrice pour les nombres palindromes
def palin(it): 
    for i in it: 
        if (isinstance(i, (str, int)) and
            str(i) == str(i)[::-1]): 
            yield i

p = palin([121, 10, 12321, 'abc', 'abba']) # Création d'un générateur
print(list(p)) # [121, 12321, 'abba']
print(list(palin(x**2 for x in range(1000)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]