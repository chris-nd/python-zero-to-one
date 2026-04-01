# Le module `itertools` : L'art des itérateurs

## La question fondamentale

Comment manipuler, combiner ou parcourir de grands volumes de données sans saturer la mémoire vive (RAM) ?

## 1. Rappel : Pourquoi les itérateurs ?

L'intérêt premier est le **parcours paresseux** (*lazy evaluation*) :

- Les données sont produites **une par une**, à la demande.
- Aucune structure de données temporaire (comme une grande liste) n'est créée.
- **Coût mémoire :** Faible et constant, quelle que soit la taille des données.

## 2. Les 3 familles du module `itertools`

Le module `itertools` fournit des outils standardisés pour construire des itérateurs complexes.

### A. Les Itérateurs Infinis

Ils ne s'arrêtent jamais d'eux-mêmes (utiles avec un `break` ou un compteur).

- **`cycle` :** Répète indéfiniment un itérable (ex: `A, B, C, A, B, C...`).
- **`count` :** Génère une suite de nombres infinie.

### B. Les Combinatoires Mathématiques

Génèrent des arrangements complexes sans stocker toutes les possibilités.

- **`permutations` :** Toutes les façons d'ordonner des éléments.
- **`combinations` :** Groupes d'éléments sans répétition.
- **`product` :** Produit cartésien (équivalent à des boucles imbriquées).

### C. Les Utilitaires de Parcours

Versions optimisées de fonctions courantes.

## 3. Focus sur deux outils majeurs (Famille des Utilitaires de Parcours)

### `itertools.chain` : La concaténation "virtuelle"

Permet de lier plusieurs itérables (tuples, listes, ensembles) pour les parcourir comme s'ils n'en formaient qu'un seul, sans créer de nouvelle liste.

```python
import itertools

# On enchaîne un tuple et une liste sans les copier
for x in itertools.chain((1, 2), [3, 4]):
    print(x) # Affiche 1, 2, 3, 4
```

### `itertools.islice` : Le découpage intelligent

Permet de faire un "slice" (tranche) sur **n'importe quel itérable** (même ceux qui ne supportent pas l'indexation comme les fichiers ou les générateurs).

- **Différence avec `liste[start:stop]` :** `islice` ne crée pas de copie de la liste.
- **Analogie :** C'est un `range()` qui s'applique à des données existantes.

```python
import itertools
import string

support = string.ascii_lowercase # "abcdef..."

# On parcourt de l'indice 3 à 8 sans créer de sous-chaîne en mémoire
for x in itertools.islice(support, 3, 8):
    print(x) # Affiche d, e, f, g, h
```

## Synthèse : Quand utiliser `itertools` ?

- Dès que vous manipulez des **fichiers volumineux** ou des flux de données.
- Lorsque vous avez besoin de **performances optimales** (implémenté en C).
- Pour éviter de créer des **listes intermédiaires** inutiles qui ralentissent le programme.