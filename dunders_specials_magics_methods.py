"Méthodes spéciales (dunders)"

class Phrase:
    "Implémentation des méthodes spéciales"
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def nb_lettres(self):
        "Renvoie le nombre de lettres dans la phrase"
        return len(self.ma_phrase)

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):
        return mot in self.mots

    def __str__(self):
        return self.ma_phrase


p = Phrase("Bonjour, le monde!")
print(len(p)) # 3
print("monde" in p) # True
print(p) # Bonjour, le monde!


# Hachage par défaut: basé sur id() si aucune fonction de hachage n'est définie
class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pt[{self.x}, {self.y}]"

# Ces instances de Point1 sont mutables
p1 = Point1(2, 2)
p2 = Point1(2, 3)
# objets mutables
p1.y = 3

# les instances p1 et p2 ont des id différents, donc ils sont différent
s = {p1, p2}

print(len(s)) # 2
print(p1 in s) # True
print(p2 in s) # True

p3 = Point1(2, 3)
print(p3 in s) # False

# Le protocole hashable
# Il faut implémenter __hash__ pour rendre un objet hashable
# et __eq__ pour vérifier l'égalité
class Point2(Point1):
    "Implémentation d'une fonction hashable"
    # l'égalité va se baser naturellement sur x et y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # du coup la fonction de hachage
    # dépend aussi de x et de y
    def __hash__(self):
        return hash((self.x, self.y))

# Nos instances q1 et q2 sont différents au travers
# de la foncton builtin id() et de l'opérateur is
q1 = Point2(2, 3)
q2 = Point2(2, 3)

print(id(q1) == id(q2))  # False
print(q1 is q2)  # False
print(hash(q1) == hash(q2))  # True

s = {q1, q2}
print(len(s)) # 1
print(repr(q1)) # Pt[2, 3]
print(repr(q2)) # Pt[2, 3]

q3 = Point2(2, 3)
print(q3 in s) # True

d = {}
d[q1] = 1
print(d[q2]) # 1

d[q3] = 10000
print(d[q1]) # 10000
print(d) # {Pt[2, 3]: 10000}

class Matrix2:
    "Implémentation d'une matrice 2x2 avec des surcharges de méthodes built-in"

    def __init__(self, *args):
        """
        le constructeur accepte 
        (*) soit les 4 coefficients individuellement
        (*) soit une liste - ou + généralement une séquence - des mêmes
        """

        if len(args) == 4:
            self.coefs = args
        elif len(args) == 1:
            self.coefs = tuple(*args)

    def __repr__(self):
        "l'affichage"
        return "[" + ", ".join([str(c) for c in self.coefs]) + "]"

    def __add__(self, other):
        """
        l'addition de deux matrices retourne un nouvel objet
        la possibilité de créer une matrice à partir
        d'une liste rend ce code beaucoup plus facile à écrire
        """
        return Matrix2([a + b for a, b in zip(self.coefs, other.coefs)])

    def __bool__(self):
        """
        on considère que la matrice est non nulle 
        si un au moins de ses coefficients est non nul
        """
        # ATTENTION le retour doit être un booléen
        # ou à la rigueur 0 ou 1
        for c in self.coefs:
            if c:
                return True
        return False


zero = Matrix2 ([0,0,0,0])

matrice1 = Matrix2 (1,2,3,4)
matrice2 = Matrix2 (list(range(10,50,10)))

print('avant matrice1', matrice1)
print('avant matrice2', matrice2)

print('somme', matrice1 + matrice2)

print('après matrice1', matrice1)
print('après matrice2', matrice2)

if matrice1:
    print(matrice1,"n'est pas nulle")
if not zero:
    print(zero,"est nulle")

# Certaines des méthodes dunders pour le calcul arthimétique

def __add__(self, other):
    pass

def __sub__(self, other):
    pass

def __mul__(self, other):
    pass

def __div__(self, other):
    pass

# Certaines des méthodes dunders pour les bitwise

def __or__(self, other):
    pass

def __and__(self, other):
    pass

def __xor__(self, other):
    pass

def __invert__(self):
    pass

def __lshift__(self, other):
    pass

def __rshift__(self, other):
    pass

# Certaines des méthodes dunders pour les opérateur logique de comparaison

def __eq__(self, other):
    pass

def __ne__(self, other):
    pass

def __lt__(self, other):
    pass

def __le__(self, other):
    pass

def __gt__(self, other):
    pass

def __ge__(self, other):
    pass

# Implémentation du produit d'une matrice avec un scalaire

def multiplication_scalaire(self, alpha):
    "Renvoie une nouvelle matrice qui est le produit de la matrice actuelle par un scalaire"
    return Matrix2([alpha * coef for coef in self.coefs])

# on ajoute la méthode spéciale __rmul__
Matrix2.__rmul__ = multiplication_scalaire

# Certaines des méthodes dunders pour les fonctions built-in

def __len__(self):
    pass

def __contains__(self, item):
    pass

def __getitem__(self, index):
    pass

def __setitem__(self, index, value):
    pass

def __iter__(self):
    pass

def __call__(self):
    pass

class PlusClosure:
    """Une classe callable qui permet de faire un peu comme la 
    fonction built-in sum mais en ajoutant une valeur initiale"""
    def __init__(self, initial):
        self.initial = initial
    def __repr__(self):
        return f"{self.initial}"
    def __call__(self, *args):
        return self.initial + sum(args)

# on crée une instance avec une valeur initiale 2 pour la somme
plus2 = PlusClosure (2)

print(plus2())
print(plus2(1, 2, 3))


# __getattr__

class RPCProxy:
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
        
    def __getattr__(self, function):
        """
        Crée à la volée une méthode sur RPCProxy qui correspond
        à la fonction distante 'function'
        """
        def forwarder(*args):
            print(f"Envoi à {self.url}...")
            print(f"de la fonction {function} -- args= {args}")
            return "retour de la fonction " + function
        return forwarder

rpc_proxy = RPCProxy (url='http://cloud.provider.com/JSONAPI', 
                      login='dupont',
                      password='***')

nodes_list = rpc_proxy.GetNodes ( [ ('phy_mem', '>=', '32G') ] )
node_lease = rpc_proxy.BookNode ( { 'id' : 1002, 'phy_mem' : '32G' } )
