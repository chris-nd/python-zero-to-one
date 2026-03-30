from functools import reduce
from operator import mul # mul(a, b) est l'équivalent fonctionnel de a * b

def factoriel(n):
    # 1 est l'élément neutre de la multiplication (retourné si liste vide)
    return reduce(mul, range(1, n+1), 1)

print(factoriel(5)) # 1 * 2 * 3 * 4 * 5 = 120