# Expressions génératrices : L'alternative "Légère"

## La question fondamentale

Comment bénéficier de la puissance des compréhensions (syntaxe concise) sans subir leur coût mémoire (stockage de tous les éléments) ?

---

## 1. De la Liste à l'Itérateur

Une **compréhension de liste** crée immédiatement tous ses éléments en mémoire vive (RAM). Une **expression génératrice**, elle, crée un **itérateur** qui calculera les éléments un par un, uniquement à la demande (*Lazy Evaluation*).

### Syntaxe : Le changement de parenthèses

- **Compréhension de liste :** Utilise des crochets `[]`.
- **Expression génératrice :** Utilise des parenthèses `()`.

```python
# Gourmand en mémoire (crée une liste de 100 éléments)
comprehension = [x**2 for x in range(100) if x%17 == 0] 

# Économe en mémoire (crée un objet capable de calculer ces carrés)
generateur = (x**2 for x in range(100) if x%17 == 0)
```

## 2. L'avantage de l'infini (ou du "très grand")

Le générateur permet de manipuler des volumes de données virtuellement infinis que la mémoire de votre ordinateur ne pourrait pas supporter sous forme de liste.

```python
# Impossible à stocker en liste (10^18 éléments !)
# Mais le générateur se crée instantanément sans saturer la RAM.
generator = (x**2 for x in range(10**18) if x%17 == 0)

for x in generator:
    if x > 10**10:
        break # On s'arrête quand on veut, sans avoir tout calculé
    print(x)
```

## 3. Comparaison : Compréhension vs Génératrice

| **Caractéristique** | **Compréhension []** | **Expression Génératrice ()** |
| --- | --- | --- |
| **Type d'objet** | `list` (Itérable) | `generator` (Itérateur) |
| **Occupation RAM** | Proportionnelle au nombre d'éléments | **Constante** (très faible) |
| **Accès aux données** | Immédiat (indexation possible) | Séquentiel uniquement (`next()` ou `for`) |
| **Réutilisabilité** | Multiple (la liste reste en mémoire) | **Unique** (le générateur s'épuise) |

## 4. Le piège de l'épuisement

C'est la caractéristique principale des itérateurs : une fois qu'on a fini de parcourir une expression génératrice, elle est **vide**.

```python
depart = (1, 2, 3)
gen = (x**2 for x in depart)

# Premier passage : affiche 1, 4, 9
for val in gen:
    print(val)

# Second passage : n'affiche RIEN
for val in gen:
    print(val) # Le générateur est déjà épuisé
```

## Synthèse : Quand choisir quoi ?

- **Utilisez la compréhension `[]`** si vous avez besoin de réutiliser les données plusieurs fois, de les trier, ou d'accéder à un index précis (ex: `liste[5]`).
- **Utilisez l'expression génératrice `()`** si vous ne faites qu'un seul parcours (boucle `for`, passage à `sum()`, `max()`, etc.) ou si le volume de données est incertain/très grand.

# Délégation de générateurs : `yield from`

## La question fondamentale

Comment permettre à une fonction génératrice d'appeler une autre fonction génératrice et de transmettre ses résultats directement, sans avoir à écrire des boucles imbriquées lourdes ?

## 1. Le problème : L'appel naïf

Si une fonction génératrice se contente d'appeler une autre fonction génératrice, elle ne récupère qu'un **objet générateur** sans l'itérer.

### Échec du `yield` simple

```python
def divs(n):
    for i in range(2, n):
        if n % i == 0: yield i

def divdivs_ko(n):
    for i in divs(n):
        yield divs(i) # ❌ ERREUR : retourne l'objet générateur, pas ses valeurs
```

- **Résultat :** Au lieu de recevoir des nombres, l'appelant reçoit des objets `<generator object divs at ...>`.

## 2. La solution : `yield from`

L'instruction `yield from` (introduite pour déléguer le travail à un sous-générateur) permet de "brancher" la sortie d'un générateur secondaire directement sur la sortie du générateur principal.

### Syntaxe et fonctionnement

```python
def divdivs_ok(n):
    for i in divs(n):
        # ✅ "Extraie chaque valeur de divs(i) et yield-les une par une"
        yield from divs(i)
```

### Équivalence logique

L'instruction `yield from <iterable>` est une version courte et optimisée de :

```python
for item in <iterable>:
    yield item
```

## 3. Pourquoi utiliser `yield from` ?

1. **Concision :** Réduit le nombre de lignes de code et évite l'accumulation de boucles `for` imbriquées.
2. **Performance :** C'est un mécanisme interne de Python plus efficace qu'une boucle `for` manuelle avec un `yield` à chaque étape.
3. **Communication bidirectionnelle :** (Niveau expert) `yield from` permet aussi de transmettre des valeurs *vers* le sous-générateur via `.send()`, ce qui est crucial pour les coroutines.

## Synthèse : Ce qu'il faut retenir

- **`yield`** : Renvoie **une seule** valeur.
- **`yield from`** : Renvoie **toutes les valeurs** d'un itérable (liste, générateur, etc.) les unes après les autres.
- **Usage type :** Parcourir des structures récursives (comme des arbres de dossiers) ou cascader plusieurs étapes de filtrage/génération.