## Les dictionnaires (type `dict`)

**Rappel :** Le type `dict` est un type **mutable**.

### Création de dictionnaires

**1. En extension (directe) :**

```python
annuaire = {'marc': 35, 'alice': 30, 'eric': 38}
```

**2. Avec le constructeur `dict()` :**

```python
# À partir d'une liste de tuples (clé, valeur)
annuaire = dict([('marc', 35), ('alice', 30), ('eric', 38)])

# Avec arguments nommés (clés sans quotes)
annuaire = dict(marc=35, alice=30, eric=38)
```

### Accès aux valeurs

**Accès direct avec `[]` :**

```python
annuaire['marc']  # → 35
# ⚠️ Lève KeyError si la clé n'existe pas
```

**Accès sûr avec `get()` :**

```python
annuaire.get('marc', 0)      # → 35
annuaire.get('inconnu', 0)   # → 0 (valeur par défaut)
```

### Modification (dictionnaire mutable)

**Modifier une valeur :**

```python
annuaire['eric'] = 39
```

**Ajouter une entrée :**

```python
annuaire['bob'] = 42
```

**Supprimer une entrée :**

```python
del annuaire['marc']
```

**Tester l'existence d'une clé :**

```python
'john' in annuaire  # → True ou False (recommandé)
```

### Parcourir un dictionnaire

**Parcourir clés et valeurs (recommandé) :**

```python
for nom, age in annuaire.items():
    print(f"{nom}, age {age}")
```

**Parcourir seulement les clés :**

```python
for cle in annuaire.keys():
    print(cle)
```

**Parcourir seulement les valeurs :**

```python
for valeur in annuaire.values():
    print(valeur)
```

**Taille du dictionnaire :**

```python
len(annuaire)  # Nombre d'entrées
```

### Méthode `update()`

**Fusionner avec un autre dictionnaire :**

```python
annuaire.update({'jean': 25, 'eric': 70})
# eric est modifié, jean est ajouté
```

### Ordre d'insertion (Python ≥ 3.7)

**Important :** Depuis Python 3.7, les dictionnaires **se souviennent de l'ordre d'insertion**.

```python
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4

for k, v in d.items():
    print(k, v)
# Affiche dans l'ordre : 
#a 1 
#b 2
#c 3
#d 4
```

**Note historique :** `collections.OrderedDict` existe pour compatibilité avec Python < 3.7. 

### `collections.defaultdict` - Initialisation automatique

**Problème :** Valeurs qui sont des listes/compteurs nécessitent vérification avant ajout.

**Solution classique (verbeux) :**

```python
tuples = [
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 4),
]

resultat = {}
for x, y in tuples:
    if x not in resultat:
        resultat[x] = []  # Initialisation manuelle
    resultat[x].append(y)
```

**Solution avec `defaultdict` (élégant) :**

```python
from collections import defaultdict

# Initialisation automatique avec list()
resultat = defaultdict(list)

for x, y in tuples:
    resultat[x].append(y)  # Pas besoin de vérifier !
```

**Exemple avec compteurs :**

```python
compteurs = defaultdict(int)  # Valeur par défaut = 0

phrase = "hello"
for c in phrase:
    compteurs[c] += 1  # Pas besoin d'initialiser à 0 !

# Résultat : {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Méthode `setdefault()`

**Alternative moins élégante à `defaultdict` :**

```python
annuaire = {'eric': 35}

# N'a pas d'effet (eric existe déjà)
annuaire.setdefault('eric', 50)  # → 35

# Crée l'entrée si elle n'existe pas
annuaire.setdefault('inconnu', 50)  # → 50

# annuaire = {'eric': 35, 'inconnu': 50}
```

**Règle :** `setdefault()` **crée** si absent, mais **ne modifie jamais** une clé existante.

### Vues de dictionnaires (avancé)

**Les méthodes `keys()`, `values()`, `items()` retournent des VUES, pas des listes.**

**Différences :**

**Ce sont des itérables :**

```python
keys = d.keys()
for k in keys:  # ✅ Fonctionne
    print(k)

'a' in keys  # ✅ Fonctionne
```

**Ce ne sont PAS des listes :**

```python
isinstance(keys, list)  # → False
```

**Très rapide à créer :**

```python
big_keys = big_dict.keys()  # Instantané, pas d'allocation mémoire
big_list = list(big_keys)   # Beaucoup plus lent
```

**Ce sont des vues dynamiques :**

```python
d = {'a': 1, 'b': 2}
keys = d.keys()

for k in keys:
    print(k)  # → a, b

# Modifier le dictionnaire
d['c'] = 3

# La vue voit le changement !
for k in keys:
    print(k)  # → a, b, c
```

**Avantage :** Les vues reflètent l'état actuel du dictionnaire, même après leur création.

## Clés immuables

**Règle :** Une clé de dictionnaire doit être **immuable** (et globalement immuable).

### Pourquoi cette contrainte ?

**Mécanisme interne (table de hash) :**

1. Pour localiser une clé, Python calcule : `f(clé) = hash`
2. Utilise `hash` comme indice dans le tableau des couples (clé, valeur)
3. Permet des opérations en **temps constant** (O(1))

**Problème si la clé change :**

```
Scénario catastrophe :
1. On stocke (clé, valeur) à l'indice hash1 = f(clé)
2. La clé change → clé devient clé'
3. On cherche à l'indice hash2 = f(clé') ≠ hash1
4. On ne retrouve plus la valeur ! 💥
```

**Conclusion :** La clé doit rester **inchangée** pendant toute la durée de vie du dictionnaire.

### Types mutables vs immuables (rappel)

| Type | Mutable ? |
| --- | --- |
| `int`, `float` | ❌ Immuable |
| `complex`, `bool` | ❌ Immuable |
| `str` | ❌ Immuable |
| `tuple` | ❌ Immuable |
| `frozenset` | ❌ Immuable |
| `list` | ✅ Mutable |
| `dict` | ✅ Mutable |
| `set` | ✅ Mutable |

### Immuable ne suffit pas : notion de "globalement immuable"

**Point clé :** Une clé doit être immuable **de haut en bas** de sa structure.

**Exemple 1 : Clé valide ✅**

```python
d = {}
bonne_cle = (1, 2)  # Tuple d'entiers

# ✅ OK : tuple immuable contenant des entiers immuables
d[bonne_cle] = "pas de problème ici"
print(d)  # → {(1, 2): 'pas de problème ici'}
```

**Exemple 2 : Clé invalide ❌**

```python
mauvaise_cle = (1, [1, 2])  # Tuple contenant une LISTE

# Le tuple est immuable, MAIS il contient une liste mutable
mauvaise_cle[1].append(3)
print(mauvaise_cle)  # → (1, [1, 2, 3])  Modifié indirectement !

# ❌ ERREUR : TypeError: unhashable type: 'list'
d[mauvaise_cle] = 'on ne peut pas faire ceci'
```

**Pourquoi ça échoue ?**

- Le tuple lui-même est immuable
- **MAIS** il contient une liste qui, elle, est mutable
- On peut modifier indirectement le contenu via `mauvaise_cle[1].append()`
- La clé n'est donc pas **globalement** immuable

### Règle complète

**Pour être une clé valide, un objet doit :**

1. Être de type immuable
2. Contenir uniquement des objets immuables
3. Et ce récursivement à tous les niveaux

**Exemples :**

```python
# ✅ VALIDES (globalement immuables)
cle1 = 42                          # int
cle2 = "hello"                     # str
cle3 = (1, 2, 3)                   # tuple d'entiers
cle4 = (1, "a", (2, 3))           # tuple de (int, str, tuple)
cle5 = frozenset([1, 2, 3])       # frozenset

# ❌ INVALIDES (mutables ou contiennent du mutable)
cle_bad1 = [1, 2, 3]              # liste (mutable)
cle_bad2 = {1, 2, 3}              # set (mutable)
cle_bad3 = {'a': 1}               # dict (mutable)
cle_bad4 = (1, [2, 3])            # tuple contenant une liste
cle_bad5 = (1, {2, 3})            # tuple contenant un set
```

### Raison d'être de `tuple` et `frozenset`

**Objectif principal :** Créer des objets **globalement immuables** pour servir de clés.

**`tuple` :**

```python
# Créer une clé composée de plusieurs valeurs
coordonnees = (x, y, z)
donnees[coordonnees] = valeur
```

**`frozenset` :**

```python
# Version immuable d'un set
tags = frozenset(['python', 'data', 'science'])
articles[tags] = liste_articles
```

### En pratique

**Types couramment utilisés comme clés :**

1. **Nombres :** `int`, `float`, `complex`
    
    ```python
    d[42] = "valeur"
    ```
    
2. **Chaînes :** `str` (très courant)
    
    ```python
    d['nom'] = "Alice"
    ```
    
3. **Tuples :** pour clés composées
    
    ```python
    # Coordonnées (x, y)
    positions[(3, 5)] = "trésor"
    
    # Date (année, mois, jour)
    agenda[(2024, 2, 12)] = "événement"
    ```
    
4. **Frozensets :** pour ensembles immuables
    
    ```python
    d[frozenset([1, 2, 3])] = "valeur"
    ```
    

### Erreurs courantes

**Erreur 1 : Utiliser une liste comme clé**

```python
# ❌ TypeError: unhashable type: 'list'
d[[1, 2, 3]] = "erreur"

# ✅ Utiliser un tuple à la place
d[(1, 2, 3)] = "correct"
```

**Erreur 2 : Tuple contenant du mutable**

```python
# ❌ TypeError: unhashable type: 'list'
d[(1, [2, 3])] = "erreur"

# ✅ Tout immuable
d[(1, (2, 3))] = "correct"
```

**Erreur 3 : Utiliser un dict ou set comme clé**

```python
# ❌ TypeError: unhashable type: 'dict'
d[{'a': 1}] = "erreur"

# ❌ TypeError: unhashable type: 'set'
d[{1, 2, 3}] = "erreur"

# ✅ Utiliser frozenset
d[frozenset([1, 2, 3])] = "correct"
```

## Gérer des enregistrements

### Concept d'enregistrement

Un enregistrement (record/struct) est une donnée composite contenant plusieurs champs.

**Exemple :** Une personne avec nom, âge et email.

### Méthode 1 : Liste de dictionnaires

**Modéliser des enregistrements avec des dictionnaires :**

```python
personnes = [
    {'nom': 'Pierre',  'age': 25, 'email': 'pierre@example.com'},
    {'nom': 'Paul',    'age': 18, 'email': 'paul@example.com'},
    {'nom': 'Jacques', 'age': 52, 'email': 'jacques@example.com'},
]
```

**Utilisation :**

```python
# Modifier un champ (anniversaire de Pierre)
personnes[0]['age'] += 1

# Parcourir
for personne in personnes:
    for info, valeur in personne.items():
        print(f"{info} -> {valeur}")
```

**Problème :** On doit connaître l'indice (Pierre = `personnes[0]`), pas pratique !

### Méthode 2 : Dictionnaire de dictionnaires (avec index)

**Solution : Créer un index pour accès rapide par nom**

```python
# Dictionnaire par compréhension (détails en semaine 5)
index_par_nom = {personne['nom']: personne for personne in personnes}

# Résultat :
# {
#   'Pierre': {'nom': 'Pierre', 'age': 25, 'email': '...'},
#   'Paul': {'nom': 'Paul', 'age': 18, 'email': '...'},
#   'Jacques': {'nom': 'Jacques', 'age': 52, 'email': '...'}
# }
```

**Utilisation :**

```python
# ✅ Accès direct par nom
index_par_nom['Pierre']
# → {'nom': 'Pierre', 'age': 25, 'email': 'pierre@example.com'}

# Modifier l'âge de Pierre
index_par_nom['Pierre']['age'] += 1
```

**Parcourir l'index :**

```python
for nom, record in index_par_nom.items():
    print(f"Nom : {nom} -> enregistrement : {record}")
```

Deux niveaux d'utilisation du dictionnaire

**Dans cette approche, le dictionnaire sert à deux choses différentes :**

1. **Premier niveau (index)** : Trouver rapidement un objet par son nom
    - `index_par_nom['Pierre']` → accès rapide
2. **Second niveau (enregistrement)** : Stocker les données d'une personne
    - `{'nom': 'Pierre', 'age': 25, 'email': '...'}`
    - Équivalent d'un `struct` en C

### Méthode 3 : Utiliser des classes (avancé)

**Alternative plus élégante : définir une classe `Personne`**

```python
class Personne:
    # Constructeur (self sera expliqué en semaine 6)
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    # Méthode pour affichage lisible
    def __repr__(self):
        return f"{self.nom} ({self.age} ans) sur {self.email}"
```

**Créer des instances :**

```python
personnes2 = [
    Personne('Pierre',  25, 'pierre@example.com'),
    Personne('Paul',    18, 'paul@example.com'),
    Personne('Jacques', 52, 'jacques@example.com'),
]

# Afficher un élément
print(personnes2[0])
# → Pierre (25 ans) sur pierre@example.com
```

**Créer un index :**

```python
# Noter : personne.nom au lieu de personne['nom']
index2 = {personne.nom: personne for personne in personnes2}

# Utilisation
print(index2['Pierre'])
# → Pierre (25 ans) sur pierre@example.com

# Modifier l'âge
index2['Pierre'].age += 1
```