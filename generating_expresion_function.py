carre = [x**2 for x in range(1000)]
print(sum(carre))

# Expréssion génératrice

# Création d'un générateur
carre = (x**2 for x in range(1000))
print(carre) # <generator object <genexpr> at 0x...>

print(sum(carre)) # 333333000
print(sum(carre)) # 0 parce que le générateur, qui est un itérateur, est épuisé

try:
    print(next(carre)) # Lève une exception StopIteration
except StopIteration as e:
    print("Le générateur est épuisé", e)

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

try:
    print(next(g)) # Lève une exception StopIteration
except StopIteration as e:
    print("Le générateur est épuisé", e)

def generator(x): 
    yield x 
    x = x + 1 
    yield x

g = generator(15) 
print(next(g)) # 15
print(next(g)) # 16

try:
    print(next(g)) # Lève une exception StopIteration
except StopIteration as e:
    print("Le générateur est épuisé", e)

# Fonction génératrice pour les carrés
def square(a, b):
    for i in range(a, b):
        yield i ** 2

c = square(1, 10) # Création d'un générateur
print(list(c)) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Fonction génératrice pour les nombres palindromes
def palindrome(it): 
    for i in it: 
        if (isinstance(i, (str, int)) and
            str(i) == str(i)[::-1]): 
            yield i

p = palindrome([121, 10, 12321, 'abc', 'abba']) # Création d'un générateur
print(list(p)) # [121, 12321, 'abba']
print(list(palindrome(x**2 for x in range(1000)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Générateur de diviseurs

def divs(n):
    for i in range(2, n):
        if n % i == 0: yield i # 

# Générateur de diviseurs de diviseurs

def divdivs_ko(n):
    for i in divs(n):
        yield divs(i)

print(divs(12)) # <generator object <genexpr> at 0x...>
print(list(divs(12))) # [2, 3, 4, 6]
print(divdivs_ko(12)) # <generator object <genexpr> at 0x...>
print(list(divdivs_ko(12))) # [<generator object divs at 0x10bf32500>, <generator object divs at 0x10bf320a0>, <generator object divs at 0x10bf32340>, <generator object divs at 0x10bf32420>]

def divdivs_ok_2(n):
    for i in divs(n):
        # ✅ "Extraie chaque valeur de divs(i) et yield-les une par une"
        yield from divs(i)

print(divdivs_ok_2(12))
print(list(divdivs_ok_2(12)))

round