# Construction par compréhension

## La notion fondamentale

La compréhension est à l'instruction `for` ce que l'expression conditionnelle est au `if` : c'est une **expression** qui retourne une nouvelle collection de données en une seule ligne.

## 1. Compréhension de liste (List Comprehension)

C'est la forme la plus courante. Elle permet de transformer un itérable en une nouvelle liste.

### Structure de base : le "Map"

On applique une opération à chaque élément d'une source.

- **Analogie mathématique :** $f(x) \text{ pour tout } x \in E$.
- **Analogie fonctionnelle :** Équivalent à la fonction `map`.

```python
depart = (-5, -3, 0, 3, 5, 10)

# On calcule le carré de chaque élément
arrivee = [x**2 for x in depart] 
# -> [25, 9, 0, 9, 25, 100]
```

### Avec condition : le "Filter"

On peut filtrer les éléments de la source pour ne garder que ceux qui nous intéressent avant d'appliquer l'opération.

- **Analogie fonctionnelle :** Équivalent à la fonction `filter`.

```python
# Uniquement les carrés des nombres pairs
[x**2 for x in depart if x % 2 == 0]
# -> [0, 100] (0 et 10 étaient les seuls pairs)
```

## 2. Flexibilité des types

Bien que l'on parte de n'importe quel **itérable** (chaîne de caractères, tuple, range), le résultat dépend des délimiteurs utilisés :

### Production d'une Liste `[]`

```python
[ord(x) for x in 'abc'] # Transforme des caractères en codes ASCII
```

### Production d'un Ensemble `{}` (Set)

Élimine automatiquement les doublons et ne garantit pas l'ordre.

```python
{x**2 for x in (1, 2, -1, 2)} 
# -> {1, 4} (Les doublons sont supprimés)
```

### Production d'un Dictionnaire `{k: v}`

Nécessite la syntaxe `clé: valeur`.

```python
d = {x: ord(x) for x in 'abc'}
# -> {'a': 97, 'b': 98, 'c': 99}
```

## 3. Pourquoi privilégier la compréhension ?

1. **Lisibilité :** L'intention du code est claire immédiatement ("Je veux une liste de carrés").
2. **Performance :** Les compréhensions sont généralement plus rapides qu'une boucle `for` avec un `.append()` car elles sont optimisées au niveau de l'interpréteur Python.
3. **Concision :** Remplace avantageusement la combinaison complexe de `list(map(lambda...))`.

## Synthèse : Ce qu'il faut retenir

- La syntaxe suit l'ordre : `[expression for élément in itérable if condition]`.
- Elle crée toujours un **nouvel objet**, l'itérable de départ reste intact.
- C'est l'outil idéal pour le traitement de données simple (nettoyage, conversion, calcul mathématique).

# Compréhensions imbriquées

## La question fondamentale

Comment traiter des données à plusieurs niveaux (ex: une liste de listes) pour soit conserver la structure, soit l'aplatir en une seule liste ?

## 1. La compréhension "à plat" (`[... for ... for ...]`)

Elle permet de parcourir plusieurs itérables pour ne produire qu'**une seule liste simple** (profondeur 1).

- **Ordre de lecture :** L'ordre des `for` dans la compréhension est le même que dans des boucles imbriquées classiques.
- **Moyen mnémotechnique :** Écrivez mentalement les boucles `for` les unes sous les autres.

```python
# Compréhension :
[n + p for n in [2, 4] for p in [10, 20, 30]]

# Équivalent "bavard" :
resultat = []
for n in [2, 4]:          # 1er for
    for p in [10, 20, 30]: # 2ème for
        resultat.append(n + p)
# -> [12, 22, 32, 14, 24, 34]
```

## 2. La compréhension "de compréhension" (`[[... for ...] for ...]`)

Elle permet de créer ou de manipuler des **listes de listes** (profondeur 2).

- **Ordre de lecture :** On commence par l'extérieur (le `for` le plus à droite) pour créer les sous-listes, puis on traite l'intérieur.
- **Usage type :** Création de matrices ou de grilles.

```python
n = 3
matrix = [[(i, j) for i in range(1, j + 1)] for j in range(1, n + 1)]

# Équivalent "bavard" :
res_exterieur = []
for j in range(1, n + 1):     # On commence par le j (extérieur)
    res_interieur = []
    for i in range(1, j + 1): # Puis on remplit la sous-liste avec i
        res_interieur.append((i, j))
    res_exterieur.append(res_interieur)
```

## 3. Le piège de la variable non définie

Dans une compréhension **à plat**, vous ne pouvez pas utiliser une variable de boucle avant qu'elle ne soit déclarée dans l'ordre de lecture (de gauche à droite).

```python
# ❌ ERREUR : j est utilisé avant d'être défini par le second for
[ (i, j) for i in range(1, j + 1) for j in range(1, 4) ]

# ✅ CORRECT : j est défini d'abord
[ (i, j) for j in range(1, 4) for i in range(1, j + 1) ]
```

## 4. Combinaison avec des clauses `if`

Les conditions `if` se placent juste après le `for` qu'elles concernent.

```python
# Filtrage complexe :
[[(i, j) for i in range(1, j + 1) if (i+j)%2 == 0] # Filtre sur i
         for j in range(1, 5)     if j % 2 == 0]   # Filtre sur j
```

## Synthèse : Ce qu'il faut retenir

- **`[x for... for...]`** : Aplatit le résultat (1 liste). Utile pour combiner des éléments.
- **`[[x for...] for...]`** : Conserve/Crée une structure (liste de listes). Utile pour les matrices.
- **Zen de Python :** *"Flat is better than nested"* (Le plat est préférable à l'imbriqué). Si votre compréhension devient illisible sur une seule ligne, utilisez des boucles `for` classiques.