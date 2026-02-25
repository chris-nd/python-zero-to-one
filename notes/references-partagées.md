## L'opérateur `is`

### Deux opérateurs de comparaison

**Python propose deux opérateurs de comparaison distincts :**

| Opérateur | Compare | Utilisation |
| --- | --- | --- |
| **`==`** | Les **valeurs** | Égalité de contenu |
| **`is`** | L'**identité** (même objet en mémoire) | Même référence mémoire |

### Scénario 1 : Deux objets différents avec même valeur

```python
# Deux listes identiques en valeur
a = [1, 2]
b = [1, 2]

# Les valeurs sont égales
print('==', a == b)  # → True

# Mais ce sont des objets différents en mémoire
print('is', a is b)  # → False
```

**Explication :** Deux listes distinctes sont créées en mémoire, même si leur contenu est identique.

### Scénario 2 : Deux variables, un seul objet

```python
# Une seule liste
a = [1, 2]

# b référence le même objet que a
b = a

# Les valeurs sont égales
print('==', a == b)  # → True

# ET c'est le même objet
print('is', a is b)  # → True
```

**Syntaxe équivalente :**

```python
# Forme compacte
a = b = [1, 2]
# a et b pointent vers le MÊME objet
```

### Bonne pratique : Préférer `is` avec les singletons

**Règle :** Utiliser `is` lors de comparaison avec des **singletons** (objets uniques).

**Exemple avec `None` :**

```python
undef = None

# ✅ RECOMMANDÉ : pythonique et efficace
if undef is None:
    print('indéfini')

# ❌ MOINS BON : fonctionne mais moins idiomatique
if undef == None:
    print('indéfini')
```

**Pourquoi `is` est préférable ?**

1. **Plus lisible** : intention claire (tester l'identité)
2. **Plus pythonique** : convention établie
3. **Plus efficace** : comparaison en temps constant O(1)

### Performance : `is` vs `==`

**Différence de complexité :**

| Opérateur | Complexité | Raison |
| --- | --- | --- |
| **`is`** | ✅ O(1) - Temps constant | Compare deux adresses mémoire |
| **`==`** | ⚠️ O(n) - Peut être linéaire | Peut parcourir toute la structure |

**Exemple avec structures complexes :**

```python
# Liste gigantesque
huge_list = list(range(1_000_000))

# is : instantané (compare adresses)
huge_list is huge_list  # O(1)

# == : doit parcourir toute la liste
huge_list == huge_list  # O(n)
```

### La fonction `id()`

**Définition :** Retourne un identificateur unique pour chaque objet (modèle mental : adresse mémoire).

```python
a = [1, 2]
b = [1, 2]
c = a

print(id(a))  # ex: 140234567890
print(id(b))  # ex: 140234567920 (différent de a)
print(id(c))  # ex: 140234567890 (même que a)
```

**Relation formelle :**

```
(a is b) ⟺ (id(a) == id(b))
```

### Singletons : Optimisation pour types de base

**Définition :** Un singleton est un objet qui n'existe qu'en **un seul exemplaire** en mémoire.

**Objectif :** Optimiser la mémoire pour objets immuables fréquents.

**Exemples :**

**1. Petits entiers :**

```python
a = 3
b = 3

print(id(a))  # → Même ID
print(id(b))  # → Même ID

a is b  # → True (singleton !)
```

**2. Chaînes vides :**

```python
a = ""
b = ""

a is b  # → True
```

**3. Chaînes courtes :**

```python
a = "foo"
b = "foo"

a is b  # → True (optimisation)
```

**⚠️ Attention :** Cette optimisation ne s'applique **que** aux types **immuables**.

### Quand utiliser `is` vs `==`

**Utilisez `is` pour :**

- ✅ Comparer avec `None` : `if x is None:`
- ✅ Comparer avec `True`/`False` : `if flag is True:`
- ✅ Vérifier l'identité d'objets : `if obj1 is obj2:`
- ✅ Singletons personnalisés

**Utilisez `==` pour :**

- ✅ Comparer des valeurs : `if x == 5:`
- ✅ Comparer des contenus : `if list1 == list2:`
- ✅ Comparaisons générales d'égalité

## Listes infinies & références circulaires

### Construction d'une liste "infinie"

**Exemple basique :**

```python
# Créer une liste à un élément
infini_1 = [None]

# Remplacer cet élément par... la liste elle-même !
infini_1[0] = infini_1

print(infini_1)
# → [[...]]
```

**Résultat :** Une liste de taille 1 et de profondeur "infinie" qui se référence elle-même.

### Affichage avec ellipse `...`

**Problème :** Comment imprimer un objet qui se référence lui-même sans boucle infinie ?

**Solution Python :** Utiliser l'**ellipse** `...` pour indiquer une **référence circulaire**.

```python
print(infini_1)
# → [[...]]
# Au lieu de [[[[[[... infiniment ]]]]]]
```

**Signification de `...` :** "Cet objet a déjà été affiché, il y a une référence circulaire ici."

### Visualisation

**Sous PythonTutor :**
On peut voir graphiquement la cellule de la liste se référencer elle-même :

```python
infini_1 = [None]
infini_1[0] = infini_1
# La flèche de l'élément pointe vers la liste elle-même
```

### Comparaisons avec références circulaires

**Comparaison avec soi-même : ✅ Fonctionne**

```python
infini_1 == infini_1  # → True
```

**Comparaison avec objet similaire : ❌ Erreur !**

```python
infini_2 = [None]
infini_2[0] = infini_2

# ⚠️ Provoque une erreur
infini_1 == infini_2
# → RecursionError: maximum recursion depth exceeded in comparison
```

**Raison :** Python entre dans une boucle infinie en essayant de comparer les deux structures.

### Généralisation : Références circulaires dans structures complexes

**Exemple pratique avec dictionnaires :**

```python
# Collection de points
collection_de_points = [
    {'x': 10, 'y': 20},
    {'x': 30, 'y': 50},
]

# Ajouter une référence circulaire
for point in collection_de_points:
    point['points'] = collection_de_points
    # Chaque point référence maintenant toute la collection !

print(collection_de_points)
# → [{'x': 10, 'y': 20, 'points': [...]},
#    {'x': 30, 'y': 50, 'points': [...]}]
```

**Résultat :** Chaque dictionnaire contient une clé `'points'` qui référence la liste complète.

**Ellipse `...` :** Indique que l'objet `points` a déjà été affiché (référence circulaire).

### Utilité pratique

**Cette technique est très utilisée pour :**

1. **Navigation bidirectionnelle** dans des structures de données
2. **Graphes** et structures complexes
3. **Arbres** avec références parents ↔ enfants
4. **Objets liés** qui doivent se connaître mutuellement

**Exemple d'usage :**

```python
# Depuis un point, accéder à tous les autres points
point = collection_de_points[0]

# Accéder à tous les points de la collection
tous_les_points = point['points']

# Accéder à un autre point spécifique
autre_point = point['points'][1]
```

### Cas d'usage réels

**1. Structure parent-enfant :**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self  # Référence circulaire
        self.children.append(child)

root = Node("root")
child = Node("child")
root.add_child(child)

# Maintenant : child.parent → root et root.children[0] → child
```

**2. Graphe avec nœuds liés :**

```python
# Chaque nœud connaît ses voisins
graph = {
    'A': {'neighbors': []},
    'B': {'neighbors': []},
}

# Créer des liens bidirectionnels
graph['A']['neighbors'].append(graph['B'])
graph['B']['neighbors'].append(graph['A'])
```

**3. Base de données relationnelle (ORM) :**

```python
class Article:
    def __init__(self, title):
        self.title = title
        self.author = None

class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

author = Author("Alice")
article = Article("Python Tips")

# Références circulaires
article.author = author
author.articles.append(article)
```

### Précautions et pièges

**1. Comparaisons peuvent échouer :**

```python
# ❌ Peut causer RecursionError
structure1 == structure2  # Si références circulaires
```

**2. Sérialisation compliquée :**

```python
import json

# ❌ Erreur avec JSON
json.dumps(infini_1)
# → ValueError: Circular reference detected
```

**3. Garbage collection :**

Les références circulaires peuvent compliquer le ramasse-miettes (garbage collector), bien que Python le gère généralement bien.

### Détecter les références circulaires

**Utiliser PythonTutor :**

- Visualiser graphiquement les références
- Voir les flèches qui bouclent sur elles-mêmes

**Utiliser `id()` :**

```python
obj = [None]
obj[0] = obj

# Vérifier l'identité
obj is obj[0]  # → True
id(obj) == id(obj[0])  # → True
```

### Visualisation de la structure

**Liste infinie simple :**

```
infini_1 → [  •  ]
            ↑  |
            └──┘
```

**Collection de points :**

```
collection → [ {point1}, {point2} ]
               ↑           ↑
               |           |
         points|     points|
               └───────────┘
```

### Résumé en une phrase

Les **références circulaires** permettent à un objet de se référencer lui-même (directement ou indirectement), affichées avec `...` par Python, très utiles pour naviguer dans des structures complexes comme des graphes, mais nécessitent des précautions lors des comparaisons et sérialisations.

## Les différentes copies (shallow vs deep)

### Deux types de copie

| Type | Anglais | Français | Profondeur |
| --- | --- | --- | --- |
| **Shallow copy** | Superficial | Copie superficielle | 1er niveau seulement |
| **Deep copy** | Profound | Copie profonde | Tous les niveaux |

### Le module `copy`

**Méthode universelle pour copier :**

```python
import copy

# Copie superficielle
shallow_copy = copy.copy(objet)

# Copie profonde
deep_copy = copy.deepcopy(objet)
```

**Avantage :** Fonctionne avec **tous les types** de manière identique.

### Exemple de départ

```python
import copy

source = [
    [1, 2, 3],   # une liste (mutable)
    {1, 2, 3},   # un ensemble (mutable)
    (1, 2, 3),   # un tuple (immuable)
    '123',       # un string (immuable)
    123,         # un entier (immuable)
]
```

### Copie superficielle (Shallow Copy)

**Syntaxe :**

```python
shallow_copy = copy.copy(source)

# Équivalent pour une liste :
shallow_copy = source[:]
```

**Comportement :**

```
source        → [ •, •, •, •, • ]
                  ↓  ↓  ↓  ↓  ↓
shallow_copy  → [ •, •, •, •, • ]
                  ↓  ↓  ↓  ↓  ↓
               [1,2,3] {1,2,3} (1,2,3) '123' 123
```

**Caractéristiques :**

- ✅ Crée une **nouvelle liste** de premier niveau
- ❌ **Partage** tous les sous-éléments avec l'original
- ⚠️ Modifier `source[0]` modifiera aussi `shallow_copy[0]`

**Exemple :**

```python
source[0].append(4)
# Modifie AUSSI shallow_copy[0] car c'est le même objet !

print(source)        # → [[1, 2, 3, 4], ...]
print(shallow_copy)  # → [[1, 2, 3, 4], ...]
```

### Copie profonde (Deep Copy)

**Syntaxe :**

```python
deep_copy = copy.deepcopy(source)
```

**Comportement :**

```
source     → [ •, •, •, •, • ]
               ↓  ↓  ↓  ↓  ↓
            [1,2,3] ... objets originaux

deep_copy  → [ •, •, •, •, • ]
               ↓  ↓  ↓  ↓  ↓
            [1,2,3] ... nouveaux objets (pour mutables)
                    ... mêmes objets (pour immuables)
```

**Caractéristiques :**

- ✅ Duplique **tous les objets mutables** à tous les niveaux
- ✅ Partage seulement les objets **immuables** (optimisation)
- ✅ Source et copie **indépendantes** : modifier l'une n'affecte pas l'autre

**Exemple :**

```python
source[0].append(4)
# N'affecte PAS deep_copy[0] car c'est un objet différent

print(source)     # → [[1, 2, 3, 4], ...]
print(deep_copy)  # → [[1, 2, 3], ...]  (inchangé)
```

### Inspection détaillée

**Égalité logique (`==`) :**

```python
source == shallow_copy  # → True
source == deep_copy     # → True
```

**Identité des éléments (`is`) :**

**Shallow copy :**

```python
for i in range(len(source)):
    print(f"source[{i}] is shallow_copy[{i}] → {source[i] is shallow_copy[i]}")

# Résultat :
# source[0] is shallow_copy[0] → True  (même liste)
# source[1] is shallow_copy[1] → True  (même set)
# source[2] is shallow_copy[2] → True  (même tuple)
# source[3] is shallow_copy[3] → True  (même string)
# source[4] is shallow_copy[4] → True  (même entier)
```

**Deep copy :**

```python
for i in range(len(source)):
    print(f"source[{i}] is deep_copy[{i}] → {source[i] is deep_copy[i]}")

# Résultat :
# source[0] is deep_copy[0] → False (liste dupliquée)
# source[1] is deep_copy[1] → False (set dupliqué)
# source[2] is deep_copy[2] → True  (tuple partagé - immuable)
# source[3] is deep_copy[3] → True  (string partagé - immuable)
# source[4] is deep_copy[4] → True  (entier partagé - immuable)
```

### Comportements détaillés

**1. Modification d'un sous-élément (shallow) :**

```python
source = [[1, 2, 3], {1, 2, 3}]
shallow_copy = copy.copy(source)

# Modifier un élément DANS la liste
source[0].append(4)

print(source)        # → [[1, 2, 3, 4], {1, 2, 3}]
print(shallow_copy)  # → [[1, 2, 3, 4], {1, 2, 3}]  ⚠️ Modifié !
```

**2. Remplacement complet d'un élément (shallow) :**

```python
# Remplacer complètement l'élément
source[0] = 'remplacement'

print(source)        # → ['remplacement', {1, 2, 3}]
print(shallow_copy)  # → [[1, 2, 3, 4], {1, 2, 3}]  ✅ Pas modifié
```

**Explication :** On crée un **nouveau** lien, sans affecter l'ancien objet partagé.

### Copie et références circulaires

**Le module `copy` gère les références circulaires :**

```python
# Créer une référence circulaire
l = [None]
l[0] = l  # l se contient elle-même

print(l)  # → [[...]]

# Copie superficielle : fonctionne
copy.copy(l)  # → OK

# Copie profonde : fonctionne aussi
copy.deepcopy(l)  # → OK
```

### 🔧 Exemples pratiques

**1. Copie de configuration :**

```python
config_template = {
    'server': {'host': 'localhost', 'port': 8080},
    'database': {'host': 'db.server', 'port': 5432}
}

# ❌ Shallow : modification affectera le template
config1 = copy.copy(config_template)
config1['server']['port'] = 9000  # Modifie aussi config_template !

# ✅ Deep : indépendance totale
config2 = copy.deepcopy(config_template)
config2['server']['port'] = 9000  # N'affecte PAS config_template
```

**2. Sauvegarde d'état :**

```python
# État du jeu
game_state = {
    'player': {'x': 10, 'y': 20, 'inventory': ['sword', 'shield']},
    'enemies': [{'x': 50, 'y': 50, 'hp': 100}]
}

# Sauvegarder pour rollback
saved_state = copy.deepcopy(game_state)

# Modifier le jeu
game_state['player']['x'] = 15
game_state['enemies'][0]['hp'] = 50

# Restaurer si besoin
game_state = saved_state  # État original préservé
```

**3. Liste de listes :**

```python
# Créer une matrice
matrix = [[1, 2], [3, 4]]

# ❌ Shallow : lignes partagées
copy1 = copy.copy(matrix)
copy1[0][0] = 99
# matrix AUSSI modifié !

# ✅ Deep : lignes indépendantes
copy2 = copy.deepcopy(matrix)
copy2[0][0] = 99
# matrix NON modifié
```

## L'instruction `del`

### Rôle de `del`

L'instruction `del` permet de **supprimer** des références à des objets selon le contexte.

### Sur une variable

**Utilisation :** Annuler la définition d'une variable.

**Exemple complet :**

```python
# Variable non définie
try:
    print('a=', a)
except NameError:
    print("a n'est pas définie")  # → a n'est pas définie

# Définir la variable
a = 10
print('a=', a)  # → a= 10

# Supprimer la variable
del a

# La variable n'existe plus
try:
    print('a=', a)
except NameError:
    print("a n'est pas définie")  # → a n'est pas définie
```

**Effet :** Après `del a`, c'est **comme si la variable n'avait jamais été définie**.

### Sur une liste (élément ou slice)

**Utilisation :** Enlever des éléments d'une liste.

**1. Supprimer un élément par indice :**

```python
l = [0, 1, 2, 3, 4]
del l[2]
print(l)  # → [0, 1, 3, 4]
```

**2. Supprimer une slice :**

```python
l = list(range(12))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print('slice=', l[2:10:3])  # → [2, 5, 8]

# Supprimer cette slice
del l[2:10:3]
print("après del", l)  # → [0, 1, 3, 4, 6, 7, 9, 10, 11]
```

**Règle :** `del` supprime les éléments aux indices spécifiés par la slice.

### Sur un dictionnaire (clé)

**Utilisation :** Enlever une clé (et sa valeur associée).

```python
# Dictionnaire initial
d = dict(foo='bar', spam='eggs', a='b')
print(d)  # → {'foo': 'bar', 'spam': 'eggs', 'a': 'b'}

# Supprimer une clé
del d['a']
print(d)  # → {'foo': 'bar', 'spam': 'eggs'}
```

**Effet :** La clé `'a'` et sa valeur disparaissent du dictionnaire.

### Plusieurs arguments

**`del` accepte plusieurs expressions séparées par des virgules :**

```python
l = [0, 1, 2, 3, 4, 5]
d = {'foo': 'bar', 'spam': 'eggs'}

# État initial
print('l', l)  # → [0, 1, 2, 3, 4, 5]
print('d', d)  # → {'foo': 'bar', 'spam': 'eggs'}

# Supprimer plusieurs éléments en une seule instruction
del l[3:], d['spam']

print('l', l)  # → [0, 1, 2]
print('d', d)  # → {'foo': 'bar'}
```

**Syntaxe :** `del expr1, expr2, expr3`

### ⚠️ Points importants

**1. `del` vs réaffectation :**

```python
# ❌ Réaffectation : la variable existe toujours
a = None  # a existe et vaut None

# ✅ del : la variable n'existe plus
del a  # a n'existe plus du tout
```

**2. `del` sur dictionnaire vs `pop()` :**

```python
d = {'a': 1, 'b': 2}

# del : pas de valeur de retour
del d['a']

# pop : retourne la valeur supprimée
valeur = d.pop('b')  # → 2
```

**3. Erreur si clé/indice inexistant :**

```python
d = {'a': 1}

# ❌ KeyError
del d['inexistant']

# ❌ IndexError
l = [1, 2]
del l[10]
```

### Cas d'usage pratiques

**1. Nettoyer des variables temporaires :**

```python
# Calcul avec variables temporaires
temp1 = heavy_computation()
temp2 = another_computation()
result = combine(temp1, temp2)

# Libérer la mémoire
del temp1, temp2
```

**2. Supprimer des éléments de liste par condition :**

```python
# ⚠️ Attention : ne PAS modifier pendant l'itération
# ❌ Mauvais
for i, item in enumerate(liste):
    if condition(item):
        del liste[i]  # Problème !

# ✅ Correct : utiliser compréhension de liste
liste = [item for item in liste if not condition(item)]
```

**3. Nettoyer un dictionnaire :**

```python
config = {
    'temp_file': '/tmp/file',
    'important': 'data',
    'cache': 'old_data'
}

# Supprimer les données temporaires
del config['temp_file'], config['cache']
```

### Différences avec autres méthodes

**Sur les listes :**

| Méthode | Syntaxe | Retour | Usage |
| --- | --- | --- | --- |
| **`del`** | `del l[i]` | None | Supprimer par indice/slice |
| **`remove()`** | `l.remove(val)` | None | Supprimer par valeur (1ère occurrence) |
| **`pop()`** | `l.pop(i)` | Élément | Supprimer et récupérer |
| **`clear()`** | `l.clear()` | None | Vider toute la liste |

**Sur les dictionnaires :**

| Méthode | Syntaxe | Retour | Gère absence ? |
| --- | --- | --- | --- |
| **`del`** | `del d[k]` | None | ❌ KeyError |
| **`pop()`** | `d.pop(k)` | Valeur | ❌ KeyError (sauf défaut) |
| **`pop()`** | `d.pop(k, default)` | Valeur/défaut | ✅ Oui |
| **`clear()`** | `d.clear()` | None | - |

### ✅ Bonnes pratiques

**1. Préférer les méthodes spécifiques :**

```python
# ❌ Moins clair
del liste[-1]

# ✅ Plus explicite
liste.pop()  # Retourne aussi la valeur
```

**2. Utiliser `pop()` si besoin de la valeur :**

```python
# Si on a besoin de la valeur
valeur = d.pop('key')

# Sinon, del est acceptable
del d['key']
```

**3. Gérer les erreurs avec dictionnaires :**

```python
# ❌ Peut lever KeyError
del d['key']

# ✅ Sûr avec pop
d.pop('key', None)

# ✅ Sûr avec vérification
if 'key' in d:
    del d['key']
```

**4. Ne pas modifier une liste pendant itération :**

```python
# ❌ Comportement imprévisible
for i in range(len(liste)):
    if condition(liste[i]):
        del liste[i]

# ✅ Créer nouvelle liste
liste = [x for x in liste if not condition(x)]
```