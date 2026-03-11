# Arguments de Fonctions en Python

## Arguments Nommés(Positionnels)

### Définition de base

```python
def agenda(nom, prenom, tel):
    return {'nom': nom, 'prenom': prenom, 'tel': tel}
```

### Appels possibles

```python
# Arguments positionnels (ordre important)
agenda('idle', 'eric', '07070707')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}

# Arguments nommés (ordre non important)
agenda(tel='07070707', nom='idle', prenom='eric')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}
```

**Avantage des arguments nommés :** Plus lisible et ordre flexible.

## Arguments par Défaut

### Définition avec valeur par défaut

```python
def agenda(nom, prenom, tel='?'):
    return {'nom': nom, 'prenom': prenom, 'tel': tel}
```

### Utilisation

```python
# Sans fournir tel
agenda('idle', 'eric')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '?'}

# En fournissant tel
agenda('idle', 'eric', '07070707')
# → {'nom': 'idle', 'prenom': 'eric', 'tel': '07070707'}
```

**Règle :** Les arguments avec valeur par défaut doivent venir **après** les arguments obligatoires.

## Arguments Variables : `args`

### Syntaxe avec

```python
def f(*t):
    print(t)
```

Le `*t` permet de recevoir un **nombre variable d'arguments** qui seront stockés dans un **tuple**.

### Exemples d'utilisation

```python
f()
# → ()

f(1)
# → (1,)

f(1, 2, 3, 4)
# → (1, 2, 3, 4)
```

**Usage typique :** Fonctions qui acceptent un nombre arbitraire d'arguments (comme `print()`).

## Arguments Nommés Variables : `*kwargs`

### Syntaxe avec `*`

```python
def f(**d):
    print(d)
```

Le `**d` permet de recevoir un **nombre variable d'arguments nommés** qui seront stockés dans un **dictionnaire**.

### Exemples d'utilisation

```python
f()
# → {}

f(nom='idle', prenom='eric')
# → {'nom': 'idle', 'prenom': 'eric'}
```

**Usage typique :** Fonctions qui acceptent des options configurables.

## Comparaison avec `print()`

La fonction `print()` utilise ces deux mécanismes :

```python
# *args : nombre variable d'arguments
print(1)              # → 1
print(1, 2, 3, 4)     # → 1 2 3 4

# **kwargs : paramètres nommés (sep, end, etc.)
print(1, 2, sep=';', end='FIN')
# → 1;2FIN
```

## Déballage (Unpacking)

### Déballage de liste avec

```python
def f(a, b):
    print(a, b)

L = [1, 2]

# Méthode manuelle
f(L[0], L[1])
# → 1 2

# Déballage automatique
f(*L)
# → 1 2
```

Le `*L` **déplie** la liste en arguments séparés.

### Déballage de dictionnaire avec `*`

```python
def f(a, b):
    print(a, b)

d = {'a': 1, 'b': 2}

# Déballage du dictionnaire
f(**d)
# → 1 2
```

Le `**d` transforme les **clés en noms de paramètres** et les **valeurs en arguments**.

## Exemple Pratique avec `print()`

### Configuration des paramètres

```python
# Méthode directe
print(1, 2, sep=';', end='FIN')
# → 1;2FIN

# Avec un dictionnaire de paramètres
pp = {'sep': ';', 'end': 'FIN'}
print(1, 2, **pp)
# → 1;2FIN
```

**Avantage :** Réutiliser facilement des configurations.

## Exemples d'Utilisation Courante

### Fonction flexible

```python
def creer_profil(nom, prenom, age=None, **infos):
    profil = {'nom': nom, 'prenom': prenom}
    if age:
        profil['age'] = age
    profil.update(infos)
    return profil

# Utilisation
creer_profil('Idle', 'Eric', ville='Paris', tel='070707')
# → {'nom': 'Idle', 'prenom': 'Eric', 'ville': 'Paris', 'tel': '070707'}
```

### Wrapper de fonction

```python
def log_function(*args, **kwargs):
    print(f"Arguments: {args}")
    print(f"Keywords: {kwargs}")
    # Appeler une autre fonction avec tous les arguments
    autre_fonction(*args, **kwargs)
```

## Points Clés à Retenir

1. **Arguments nommés** rendent le code plus lisible
2. **Valeurs par défaut** rendent les fonctions plus flexibles
3. **`args`** pour un nombre variable d'arguments positionnels (→ tuple)
4. **`*kwargs`** pour un nombre variable d'arguments nommés (→ dict)
5. **`*` dans l'appel** déplie une séquence(tuple)
6. **`**` dans l'appel** déplie un dictionnaire
7. **Ordre important** dans la définition de fonction
