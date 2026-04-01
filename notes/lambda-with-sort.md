# Tri de listes : Critères personnalisés

## La question fondamentale

Comment trier des objets complexes (tuples, dictionnaires) qui n'ont pas d'ordre naturel évident ou lorsque l'on veut trier selon un champ spécifique ?

## 1. Le paramètre `key` : Personnaliser le tri

Pour trier selon un critère propre à l'application, on passe une **fonction** à l'argument `key`.

- **Principe :** La fonction est appliquée à chaque élément. Le résultat de cette fonction sert de "base" (valeur numérique ou textuelle) pour effectuer la comparaison.
- **Exemple :** Trier des tuples `(latitude, longitude)` par longitude (index 1).

### Trois manières d'implémenter la clé :

1. **Fonction nommée (`def`) :** Très lisible pour les tris complexes.
2. **Expression `lambda` :** La plus courante pour les tris simples et rapides.
3. **`operator.itemgetter` :** La plus performante (implémentée en C), idéale pour extraire des index ou des clés.

```python
import operator
coords = [(43, 7), (46, -7), (46, 0)]

# A. Via lambda
coords.sort(key=lambda x: x[1])

# B. Via itemgetter (plus rapide)
coords.sort(key=operator.itemgetter(1))

# Résultat : [(46, -7), (46, 0), (43, 7)]
```

## 2. `sort()` vs `sorted()` : "En place" ou "Copie"

| **Caractéristique** | **liste.sort()** | **sorted(itérable)** |
| --- | --- | --- |
| **Type** | Méthode de l'objet `list` | Fonction intégrée (*built-in*) |
| **Action** | **En place** (modifie l'original) | **Copie** (crée une nouvelle liste) |
| **Retour** | `None` | La **nouvelle liste triée** |
| **Flexibilité** | Uniquement sur les listes | **Tout itérable** (tuple, dict, set...) |

### Visualisation de la différence

```python
liste = [3, 1, 2]

# sorted() préserve l'original
triee = sorted(liste) 
# liste -> [3, 1, 2] | triee -> [1, 2, 3]

# sort() écrase l'original
liste.sort()
# liste -> [1, 2, 3]
```

## 3. Analyse mémoire et performance

- **Coût mémoire :** `sorted()` est qualifiée de "fonction de commodité". Bien qu'elle crée une nouvelle liste, son coût mémoire final est équivalent à celui d'une copie manuelle suivie d'un `sort()`.
- **Stabilité :** Le tri en Python est **stable**. Si deux éléments ont la même valeur de clé, leur ordre relatif d'origine est conservé.
- **Itérables :** `sorted()` est très puissant car il peut trier un dictionnaire ou un ensemble, mais il retournera **toujours une liste**.

---

## Synthèse : Ce qu'il faut retenir

- Utilisez `reverse=True` pour inverser l'ordre (croissant $\rightarrow$ décroissant).
- Le paramètre `key` attend une fonction qui ne prend **qu'un seul argument** (l'élément à évaluer).
- Privilégiez `sort()` pour économiser de la mémoire si vous n'avez plus besoin de la liste originale.