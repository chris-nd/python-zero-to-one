## La boucle `while`...`else`

### Boucle `while` : Usage général

**Quand utiliser `while` vs `for` ?**

| `for` | `while` |
| --- | --- |
| Boucles **finies** et **déterministes** | Boucles **indéfinies** ou **conditionnelles** |
| Itérables / itérateurs | Condition quelconque |
| `for item in liste:` | `while condition:` |

**Tendance Python :** Privilégier `for` avec itérables quand possible.

### Boucles infinies avec `while True`

**Pattern courant : Boucle infinie avec `break`**

```python
while True:
    # Code répété indéfiniment
    if condition_sortie:
        break
```

**Exemple réel - Interpréteur Python (simplifié) :**

```python
while True:
    print(eval(read()))
```

### `break` et `continue` dans `while`

**Fonctionnent exactement comme dans `for` :**

**1. `continue` :**

- Termine l'itération **courante**
- Reste dans la boucle
- Passe à l'itération suivante

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Saute l'affichage de 3
    print(i)

# Affiche : 1, 2, 4, 5
```

**2. `break` :**

- Termine l'itération **courante**
- **Sort** de la boucle immédiatement

```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        break  # Sort de la boucle
    print(i)

# Affiche : 1, 2, 3, 4
```

### Conditions non-booléennes

**Rappel :** Comme pour `if`, condition peut être n'importe quelle expression.

**Exemple : Parcourir une liste avec `while` :**

```python
liste = ['a', 'b', 'c']

while liste:  # Vrai tant que liste non vide
    element = liste.pop()
    print(element)

# Affiche :
# c
# b
# a
```

**Explication :**

- `while liste:` équivaut à `while len(liste) > 0:`
- Liste vide `[]` évaluée comme False
- Boucle s'arrête quand liste devient vide

### La clause `else` (rarement utilisée)

**Syntaxe :**

```python
while condition:
    # corps de la boucle
    if sortie_anticipée:
        break
else:
    # Exécuté si sortie NORMALE (pas de break)
    print("Boucle terminée normalement")
```

**Règle :**

- `else` **exécuté** si boucle se termine normalement
- `else` **NON exécuté** si sortie par `break`

### Exemple complet avec `else`

```python
def scan(liste, break_mode):
    message = "avec break" if break_mode else "sans break"
    print(message)

    while liste:
        print(liste.pop())
        if break_mode:
            break
    else:
        print('else...')

# Test 1 : Sans break (sortie normale)
scan(['a'], False)
# Affiche :
# sans break
# a
# else...

# Test 2 : Avec break (sortie anticipée)
scan(['a'], True)
# Affiche :
# avec break
# a
# (pas de else)
```

### Décomposition du comportement `else`

**Cas 1 : Sortie normale (condition devient False)**

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Terminé normalement")

# Affiche :
# 0
# 1
# 2
# Terminé normalement
```

**Cas 2 : Sortie par `break`**

```python
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("Terminé normalement")

# Affiche :
# 0
# 1
# 2
# (pas de "Terminé normalement")
```

### Cas d'usage de `while`...`else`

**Exemple pratique : Recherche dans une liste**

```python
def chercher(liste, valeur):
    i = 0
    while i < len(liste):
        if liste[i] == valeur:
            print(f"Trouvé à l'index {i}")
            break
        i += 1
    else:
        print("Non trouvé")

chercher([1, 2, 3, 4], 3)  # → Trouvé à l'index 2
chercher([1, 2, 3, 4], 5)  # → Non trouvé
```

**Équivalent sans `else` (moins élégant) :**

```python
def chercher(liste, valeur):
    trouve = False
    i = 0
    while i < len(liste):
        if liste[i] == valeur:
            print(f"Trouvé à l'index {i}")
            trouve = True
            break
        i += 1

    if not trouve:
        print("Non trouvé")
```

### Comparaison `for`...`else` vs `while`...`else`

**Même comportement pour `else` :**

```python
# for...else
for item in liste:
    if condition:
        break
else:
    print("Pas de break")

# while...else (équivalent)
while liste:
    item = liste.pop(0)
    if condition:
        break
else:
    print("Pas de break")
```

**Dans les deux cas :** `else` exécuté seulement si pas de `break`.