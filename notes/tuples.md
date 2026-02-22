## La construction de tuples

### Quatre façons de créer un tuple

```python
# 1. Sans parenthèse ni virgule terminale
couple1 = 1, 2

# 2. Avec parenthèses
couple2 = (1, 2)

# 3. Avec virgule terminale
couple3 = 1, 2,

# 4. Avec parenthèses ET virgule terminale
couple4 = (1, 2,)

# Toutes sont équivalentes
couple1 == couple2 == couple3 == couple4  # → True
```

**Points clés :**

- Les parenthèses sont **souvent optionnelles** (mais améliorent la lisibilité)
- La virgule terminale est **optionnelle** (pour tuples ≥ 2 éléments)

### Conseil : présentation sur plusieurs lignes

**Forme recommandée :** parenthèses + virgule terminale

```python
mon_tuple = ([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
            )  # ← virgule terminale
```

**Avantages :**

1. **Pas de backslash nécessaire** : à l'intérieur des parenthèses, Python sait que l'instruction continue
2. **Modification facile** : pour ajouter/retirer un élément, il suffit d'ajouter/retirer une ligne entière
3. **Meilleur suivi dans Git** : les différences sont plus claires

**Applicable aussi à :**

- Listes : `[1, 2, 3,]`
- Dictionnaires : `{'a': 1, 'b': 2,}`
- Ensembles : `{1, 2, 3,}`

### Cas particulier : tuple à 1 élément

**Attention aux pièges :**

```python
# ❌ NE créent PAS de tuple
simple1 = 1       # → entier
simple2 = (1)     # → entier (parenthèses = expression)

# ✅ Créent bien un tuple
simple3 = 1,      # → tuple
simple4 = (1,)    # → tuple (RECOMMANDÉ)

type(simple2)  # → <class 'int'>
type(simple3)  # → <class 'tuple'>
```

**Règle :** Pour un tuple à un élément, **la virgule est OBLIGATOIRE**.

### Quand les parenthèses sont OBLIGATOIRES

**Cas où la parenthèse est nécessaire :**

```python
# ✅ Avec parenthèses : OK
x = (1,)
(1,) == x  # → True

# ❌ Sans parenthèses : SyntaxError
1, == x  # → SyntaxError
```

**Autres cas :**

- Dans les appels de fonction : `fonction((1, 2))`
- Dans les expressions : `resultat = (1, 2) + (3, 4)`
- Pour désambiguïser : `return (a, b)`

### Addition de tuples

**Les tuples sont immuables, MAIS on peut les additionner :**

```python
tuple1 = (1, 2,)
tuple2 = (3, 4,)

# Addition crée un NOUVEAU tuple
resultat = tuple1 + tuple2
print(resultat)  # → (1, 2, 3, 4)
```

**Opérateur `+=` :**

```python
tuple1 = (1, 2,)
tuple1 += (3, 4,)  # Crée un NOUVEAU tuple
print(tuple1)  # → (1, 2, 3, 4)
```

⚠️ **Important :** L'addition crée un nouvel objet, ne modifie pas l'original (car immuable).

### Construire des tuples élaborés

**Astuce : convertir depuis une liste**

Plutôt que d'additionner successivement, construire une liste puis convertir :

```python
# 1. Construire une liste pas à pas
liste = list(range(10))    # [0, 1, 2, ..., 9]
liste[9] = 'Inconnu'       # Modifier
del liste[2:5]             # Supprimer des éléments

# 2. Convertir en tuple
mon_tuple = tuple(liste)
print(mon_tuple)  # → (0, 1, 5, 6, 7, 8, 'Inconnu')
```

**Avantage :** Les listes sont mutables, donc plus faciles à construire.

### Attention : ne pas écraser les noms prédéfinis

**Mauvaise pratique :**

```python
liste = range(10)

# ❌ ERREUR : écrase la fonction tuple()
tuple = tuple(liste)  # tuple est maintenant un objet, pas une fonction

# Plus tard...
autre_tuple = tuple(range(100))  # TypeError: 'tuple' object is not callable
```

**Le problème :**

- Ligne 2 : `tuple` devient l'objet tuple au lieu de la fonction
- Ligne 5 : on essaie d'appeler un tuple comme une fonction → erreur

**Bonne pratique :**

```python
# ✅ Utiliser un nom différent
mon_tuple = tuple(liste)
autre_tuple = tuple(autre_liste)  # Fonctionne !
```

## Sequence Unpacking

### **Définition**

Le sequence unpacking (ou tuple unpacking) permet d'affecter plusieurs variables en une seule instruction.

**Déjà rencontré :**

```python
# Dans la suite de Fibonacci
for i in range(2, n + 1):
    f2, f1 = f1, f1 + f2
```

### Exemple simple avec un tuple

**Méthode non-pythonique (avec indices) :**

```python
couple = (100, 'spam')

# ❌ Pas pythonique
gauche = couple[0]
droite = couple[1]
```

**Méthode pythonique (unpacking) :**

```python
couple = (100, 'spam')

# ✅ Pythonique - avec parenthèses
(gauche, droite) = couple

# ✅ Pythonique - sans parenthèses (plus courant)
gauche, droite = couple

print('gauche', gauche, 'droite', droite)
# → gauche 100 droite spam
```

**Avantages :**

- Code plus expressif et auto-documenté
- Évite la manipulation d'indices
- Variables nommées selon leur signification

### Fonctionne avec tous les types

**Avec des listes :**

```python
liste = [1, 2, 3]

# Syntaxe liste à gauche
[gauche, milieu, droit] = liste

# Ou syntaxe tuple à gauche (plus courant)
gauche, milieu, droit = liste
```

**Mélange de types :**

```python
# Droite : liste, Gauche : tuple
liste = [1, 2, 3]
gauche, milieu, droit = liste  # Fonctionne !
```

**Contraintes :**

1. **Droite** : doit être un **itérable** (tuple, liste, string, etc.)
2. **Gauche** : écrit comme tuple ou liste (tuple recommandé)
3. **Même longueur** des deux côtés (sauf avec extended unpacking)

### Échanger deux variables (idiome pythonique)

**La façon pythonique :**

```python
a = 1
b = 2

# ✅ Échange sûr et élégant
a, b = b, a

print('a', a, 'b', b)  # → a 2 b 1
```

**Pourquoi c'est sûr ?**
Toutes les valeurs à droite sont évaluées **avant** l'affectation, pas besoin de variable temporaire.

### Extended Unpacking (Python 3+)

**Syntaxe avec `*` :**

```python
reference = [1, 2, 3, 4, 5]

# *b capture tout ce qui est entre a et c
a, *b, c = reference
print(f"a={a} b={b} c={c}")
# → a=1 b=[2, 3, 4] c=5
```

**Règle :** Une seule variable avec `*` par niveau d'unpacking.

**Cas d'usage pratique - ignorer le reste :**

```python
reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")
# → a=0 b=[1, 2, ..., 18] c=19
```

**Extraire seulement les premiers éléments :**

```python
data = ['Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ']

# On ne s'intéresse qu'aux deux premiers
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")
# → prenom=Jean nom=Dupont
```

**Convention :** `*_` indique qu'on ignore le reste.

### Plusieurs occurrences d'une même variable

**Techniquement légal mais peu utile :**

```python
entree = [1, 2, 3]

# La dernière affectation gagne
a, a, a = entree
print(f"a = {a}")  # → a = 3
```

Équivalent à : `a = 1; a = 2; a = 3`

**Usage pratique - ignorer des valeurs :**

```python
entree = [1, 2, 3]

# Ignore premier et dernier éléments
_, milieu, _ = entree
print('milieu', milieu)  # → milieu 2

# Ou avec un nom plus explicite
ignored, ignored, right = entree
print('right', right)  # → right 3
```

### Unpacking en profondeur

**Structures imbriquées :**

```python
structure = ['abc', [(1, 2), ([3], 4)], 5]

# Extraire le 3 situé en profondeur
(a, (b, ((trois,), c)), d) = structure
print('trois', trois)  # → trois 3

# Ou plus lisible
(a, (b, ([trois], c)), d) = structure
print('trois', trois)  # → trois 3
```

**Alternative (moins pythonique) :**

```python
trois = structure[1][1][0][0]
```

**⚠️ Attention :** Rappel du Zen de Python :

> "Flat is better than nested"
>

Évitez les structures trop imbriquées, cela nuit à la lisibilité.

### Extended unpacking en profondeur

**Combinaison avec imbrication :**

```python
tree = [1, 2, [(3, 33, 'three', 'thirty-three')],
        ([4, 44, ('forty', 'forty-four')])]

# Extended unpacking à plusieurs niveaux
*_, ((_, *x3, _),), (*_, x4) = tree
print(f"x3={x3}, x4={x4}")
# → x3=['three'], x4=('forty', 'forty-four')
```

**Règle :** Une seule `*variable` par niveau d'imbrication.

## Plusieurs variables dans une boucle `for`

### Principe de base : Unpacking dans `for`

**Rappel du sequence unpacking :**

```python
item = (1, 2)
a, b = item
print(f"a={a} b={b}")  # → a=1 b=2
```

**Application dans une boucle `for` :**

```python
entrees = [(1, 2), (3, 4), (5, 6)]

for a, b in entrees:
    print(f"a={a} b={b}")

# Sortie :
# a=1 b=2
# a=3 b=4
# a=5 b=6
```

**Mécanisme :**

- À chaque itération, `entrees` fournit un tuple
- Ce tuple est automatiquement "dépaqueté" dans les variables `a` et `b`
- Très utilisé en Python, rend le code plus lisible

### La fonction `zip()` - Associer plusieurs listes

**Problème :** Parcourir deux (ou plus) listes en parallèle

**Exemple :**

```python
villes = ["Paris", "Nice", "Lyon"]
populations = [2*10**6, 4*10**5, 10**6]
```

**Solution avec `zip()` :**

```python
# zip() crée des tuples à partir de listes parallèles
list(zip(villes, populations))
# → [('Paris', 2000000), ('Nice', 400000), ('Lyon', 1000000)]
```

**Utilisation dans une boucle :**

```python
for ville, population in zip(villes, populations):
    print(population, "habitants à", ville)

# Sortie :
# 2000000 habitants à Paris
# 400000 habitants à Nice
# 1000000 habitants à Lyon
```

**Avantages :**

- Beaucoup plus lisible que des indices
- Pythonique et élégant
- Code auto-documenté

### `zip()` avec plus de deux listes

**Généralisation à n listes :**

```python
for i, j, k in zip(range(3), range(100, 103), range(200, 203)):
    print(f"i={i} j={j} k={k}")

# Sortie :
# i=0 j=100 k=200
# i=1 j=101 k=201
# i=2 j=102 k=202
```

### `zip()` avec listes de tailles différentes

**Comportement :** Le résultat est tronqué à la plus petite liste

```python
# Premier argument : 2 éléments
# Deuxième argument : 4 éléments
for units, tens in zip([1, 2], [10, 20, 30, 40]):
    print(units, tens)

# Sortie (seulement 2 itérations) :
# 1 10
# 2 20
```

**Règle :** `zip()` s'arrête quand la **plus courte** liste est épuisée.

### La fonction `enumerate()` - Itérer avec l'indice

**Besoin :** Parcourir une liste en ayant aussi l'indice de chaque élément

**Méthode pythonique avec `enumerate()` :**

```python
villes = ["Paris", "Nice", "Lyon"]

for i, ville in enumerate(villes):
    print(i, ville)

# Sortie :
# 0 Paris
# 1 Nice
# 2 Lyon
```

**Méthodes NON pythoniques (à éviter) :**

```python
# Mauvais : manipulation d'indices
for i in range(len(villes)):
    print(i, villes[i])

# Mauvais : utilisation détournée de zip
for i, ville in zip(range(len(villes)), villes):
    print(i, ville)
```

**Pourquoi `enumerate()` est mieux ?**

- Plus simple et direct
- Plus lisible
- Évite les erreurs d'indices
- Pythonique !

## la bibliothèque `chardet`

<aside>

Pour écrire une fonction `comptage` qui devine l’encodage, c’est-à-dire qui fonctionne correctement avec des entrées indifféremment en Unicode ou Latin, sans que cet encodage soit passé en paramètre à `comptage`.
C’est d’ailleurs le propos de la bibliothèque `chardet` qui s’efforce de déterminer l’encodage de fichiers d’entrée, sur la base de modèles statistiques.

</aside>
