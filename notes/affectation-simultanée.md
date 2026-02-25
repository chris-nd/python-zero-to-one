## Affectation simultanée

### Concept de base

**Définition :** Affecter le **même objet** à plusieurs variables en une seule instruction.

**Syntaxe :**

```python
a = b = valeur
# a et b pointent vers le MÊME objet
```

### Différence avec sequence unpacking

**Rappel du sequence unpacking (semaine 3) :**

```python
# Unpacking : distribue les éléments
x, y = ['spam', 'egg']
# x = 'spam', y = 'egg'
```

**Affectation simultanée :**

```python
# Affectation simultanée : même objet pour tous
a = b = 1
# a et b pointent vers le même 1
```

### Exemple simple (immuable)

```python
a = b = 1
print('a', a, 'b', b)  # → a 1 b 1

# Avec des immuables, pas de problème visible
a = 2
print('a', a, 'b', b)  # → a 2 b 1
# b n'est pas affecté car on crée un NOUVEAU lien
```

### Cas critique : Objets mutables

**Le piège des références partagées :**

```python
# Affectation simultanée d'une liste vide
a = b = []

# a et b pointent vers la MÊME liste
print(id(a) == id(b))  # → True

# Modifier a modifie aussi b !
a.append(1)
print('a', a, 'b', b)  # → a [1] b [1]
```

**Pourquoi ?** `a` et `b` sont des **références partagées** vers le même objet.

### Solution : Affectations séparées

```python
# Deux affectations différentes
a = []
b = []

# a et b pointent vers des objets DIFFÉRENTS
print(id(a) == id(b))  # → False

# Modifier a n'affecte PAS b
a.append(1)
print('a', a, 'b', b)  # → a [1] b []
```

**Résultat :** Chaque affectation crée une **nouvelle liste vide**.

### Visualisation

**Affectation simultanée (référence partagée) :**

```
a = b = []

a → [ ]  ← b
   (même objet)
```

**Affectations séparées (objets distincts) :**

```
a = []
b = []

a → [ ]
b → [ ]
   (objets différents)
```

### Comparaison détaillée

| Aspect | Affectation simultanée | Affectations séparées |
| --- | --- | --- |
| **Syntaxe** | `a = b = []` | `a = []; b = []` |
| **Nombre d'objets** | 1 (partagé) | 2 (distincts) |
| **Identité** | `a is b` → True | `a is b` → False |
| **Modification** | Affecte les deux | Indépendantes |
| **Usage** | Rare avec mutables | Recommandé |

### Impact sur les types

**Avec types immuables (int, str, tuple) :**

```python
# Pas de problème avec immuables
a = b = 5
a = 10  # Crée nouveau lien, b inchangé
print(b)  # → 5
```

**Avec types mutables (list, dict, set) :**

```python
# ⚠️ DANGER : références partagées
a = b = []
a.append(1)  # Modifie aussi b !
print(b)  # → [1]
```

### Cas d'usage et pièges

**Piège 1 : Liste de listes**

```python
# ❌ PIÈGE : toutes les lignes partagent la même liste !
matrix = [[]] * 3  # Équivalent à : row = []; matrix = [row, row, row]
matrix[0].append(1)
print(matrix)  # → [[1], [1], [1]]  Toutes modifiées !

# ✅ CORRECT : chaque ligne est distincte
matrix = [[] for _ in range(3)]
matrix[0].append(1)
print(matrix)  # → [[1], [], []]
```

**Piège 2 : Valeurs par défaut mutables**

```python
# ❌ Valeur par défaut partagée entre tous les appels
def ajouter(item, liste=[]):  # Danger !
    liste.append(item)
    return liste

print(ajouter(1))  # → [1]
print(ajouter(2))  # → [1, 2]  Oups !

# ✅ Correct
def ajouter(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

**Usage légitime : Constantes ou immuables**

```python
# ✅ OK avec immuables
EMPTY_TUPLE = ()
a = b = c = EMPTY_TUPLE  # Pas de problème

# ✅ OK pour initialisation simple
x = y = z = 0
```

### Exemples pratiques

**Exemple 1 : Initialisation multiple**

```python
# ✅ OK pour types immuables
count1 = count2 = count3 = 0

# ❌ Dangereux pour mutables
liste1 = liste2 = []  # Références partagées !
```

**Exemple 2 : Chaînage d'affectations**

```python
# On peut chaîner plusieurs variables
a = b = c = d = 42
print(a, b, c, d)  # → 42 42 42 42

# Avec mutables : attention !
list1 = list2 = list3 = []
list1.append(1)
print(list2, list3)  # → [1] [1]  Toutes affectées !
```

**Exemple 3 : Confusion courante**

```python
# Ce qu'on pense faire
a = b = []  # "Créer deux listes vides"
a.append(1)
# Résultat attendu : a=[1], b=[]
# Résultat réel : a=[1], b=[1]  ⚠️

# Ce qu'il faut faire
a = []
b = []
a.append(1)
# Résultat : a=[1], b=[]  ✅
```

### Détecter le problème

**Utiliser `is` pour vérifier :**

```python
# Affectation simultanée
a = b = []
print(a is b)  # → True (même objet)

# Affectations séparées
a = []
b = []
print(a is b)  # → False (objets différents)
```

**Utiliser `id()` :**

```python
a = b = [1, 2, 3]
print(id(a), id(b))  # → Même ID

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))  # → IDs différents
```

### ⚠️ Règle d'or

> **Avec des objets mutables, l'affectation simultanée crée mécaniquement des références partagées. Vérifiez bien que c'est votre intention !**
> 

### ✅ Bonnes pratiques

**1. Éviter avec mutables :**

```python
# ❌ À éviter
a = b = []
a = b = {}
a = b = set()

# ✅ Préférer
a = []
b = []
```

**2. OK avec immuables :**

```python
# ✅ Pas de problème
a = b = 0
a = b = "texte"
a = b = (1, 2, 3)
```

**3. Documenter si intentionnel :**

```python
# Si vraiment voulu, commenter
shared_cache = cache1 = cache2 = {}  # Partage intentionnel
```

**4. Utiliser pour constantes :**

```python
# ✅ Usage légitime
DEFAULT_X = DEFAULT_Y = 0
MAX_WIDTH = MAX_HEIGHT = 100
```