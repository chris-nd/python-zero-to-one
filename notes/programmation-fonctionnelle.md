# Programmation Fonctionnelle

## La notion fondamentale

Considérer les **fonctions comme des objets** à part entière. Cela signifie qu'on peut :

- Les stocker dans des variables.
- Les passer en argument à d'autres fonctions.
- Les retourner comme résultat d'une autre fonction.

---

## 1. Création de fonctions

Il existe deux manières principales de définir une fonction en Python :

| **Méthode** | **Caractéristiques** | **Usage type** |
| --- | --- | --- |
| **Instruction `def`** | Nommée, multi-lignes, puissante. | Fonctions complexes et réutilisables. |
| **Expression `lambda`** | Anonyme, une seule expression, concise. | Fonctions jetables ("one-liners"). |

## 2. Transformation de données : `map` & `filter`

Ces outils permettent de traiter des itérables de manière fonctionnelle.

- **`map(fonction, itérable)` :** Applique la fonction à chaque élément de l'itérable.
- **`filter(condition, itérable)` :** Ne garde que les éléments qui valident la condition.

**Note :** En Python moderne, on préfère souvent les **compréhensions de liste** (ex: `[f(x) for x in liste if condition]`) car elles sont plus lisibles et font le travail de `map` et `filter` simultanément.

## 3. L'agrégation : `reduce`

Disponible dans le module `functools`, `reduce` permet de "réduire" un itérable à une seule valeur en appliquant une opération binaire de manière cumulative.

### Exemple : Le factoriel

Pour calculer $n!$, on multiplie tous les nombres de $1$ à $n$ entre eux.

```python
from functools import reduce
from operator import mul # mul(a, b) est l'équivalent fonctionnel de a * b

def factoriel(n):
    # 1 est l'élément neutre de la multiplication (retourné si liste vide)
    return reduce(mul, range(1, n+1), 1)

print(factoriel(5)) # 1 * 2 * 3 * 4 * 5 = 120
```

## 4. Cas fréquents (Built-ins)

Python propose des fonctions natives qui sont en réalité des versions spécialisées et optimisées de `reduce` :

- **`sum()` :** Réduction par addition.
- **`min()` / `max()` :** Réduction par comparaison.
- **`any()` / `all()` :** Réduction par logique booléenne (OU / ET).

Python

```python
entrees = [8, 5, 12, 4]
print(sum(entrees)) # Équivalent à reduce(add, entrees)
```

## Synthèse : Ce qu'il faut retenir

- La programmation fonctionnelle favorise un code **déclaratif** (on dit *ce `qu'on veut`* plutôt que `*comment faire*` chaque étape).
- **`map`** transforme, **`filter`** nettoie, **`reduce`** résume.
- Utilisez les **compréhensions** pour la lecture/écriture simple, et `itertools`/`functools` pour les traitements de données plus complexes ou volumineux.