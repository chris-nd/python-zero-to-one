def agenda(nom, prenom, tel):
    return {'nom': nom, 'prenom': prenom, 'tel': tel}

# Arguments positionnels (ordre important)
agenda('idle', 'eric', '07070707')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}

# Arguments nommés (ordre non important)
agenda(tel='07070707', nom='idle', prenom='eric')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}

# Arguments par Défaut
def agenda(nom, prenom, tel='?'):
    return {'nom': nom, 'prenom': prenom, 'tel': tel}

# Sans fournir tel
agenda('idle', 'eric')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '?'}

# En fournissant tel
agenda('idle', 'eric', '07070707')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}

# Arguments Variables : args
def f(*t):
    print(t)

f() # → ()
f(1) # → (1,)
f(1, 2, 3, 4) # → (1, 2, 3, 4)

# Arguments Nommés Variables : *kwargs
def f(**d):
    print(d)

f() # → {}

f(nom='idle', prenom='eric') # → {'nom': 'idle', 'prenom': 'eric'}

# Exemple avec print()
# **kwargs : paramètres nommés (sep, end, etc.)
print(1, 2, sep=';', end='FIN') # → 1;2FIN

kwargs = {'sep': ';', 'end': 'FIN'}
print(1, 2, **kwargs) # → 1;2FIN

# Unpacking
def f(a, b):
    print(a, b)

# Unpacking avec une liste
L = [1, 2]
# Méthode manuelle, pas très pythonique 
# à cause de la manipulation d'indices
f(L[0], L[1]) # → 1 2
# Unpacking automatique
f(*L)# → 1 2

# Unpacking avec un dictionnaire
d = {'a': 1, 'b': 2}
# Déballage du dictionnaire
f(**d) # → 1 2
