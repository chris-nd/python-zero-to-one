## 1. Concepts Clés : Itérable vs Itérateur

Bien que conceptuellement différents, ces deux types d'objets sont au cœur du fonctionnement des boucles en Python.

- **L'Itérable** : C'est un objet qui contient des données (comme une liste, un ensemble ou une chaîne de caractères) et qui peut être parcouru **plusieurs fois**. Pour être itérable, l'objet doit posséder une méthode spéciale `__iter__` qui, lorsqu'elle est appelée, renvoie un **nouvel itérateur**.
- **L'Itérateur** : C'est un objet simple et compact dont le rôle est de parcourir les données de l'itérable. Il possède une méthode `__next__` pour fournir l'élément suivant et une méthode `__iter__` qui renvoie l'itérateur lui-même. Un itérateur ne peut être parcouru **qu'une seule fois** : une fois épuisé, il lève une exception `StopIteration`.

## 2. Le Protocole d'Itération en Schéma

Lorsqu'une boucle `for` est utilisée, Python automatise le protocole d'itération sans que vous ayez à appeler manuellement les méthodes.

```
OBJET ITÉRABLE (ex: Liste)
      |
      | Appels de iter() ou .__iter__()
      v
   ITÉRATEUR (ex: list_iterator) <------------------+
      |                                             |
      | Appel de next() ou .__next__()       | Répétition
      v                                             |
[ Élément suivant ] --------------------------------+
      |
      | Si plus d'éléments...
      v
[ StopIteration ] (Fin du parcours)
```

## 3. Exemples de Code

### Fonctionnement manuel (déconstruction d'une boucle)

Voici comment Python interagit avec un ensemble (`set`) en coulisses :

```python
s = {1, 2, 'a'} # Un itérable (ensemble)
it = iter(s)    # On crée un itérateur (set_iterator)

print(next(it)) # Affiche le 1er élément
print(next(it)) # Affiche le 2ème élément
print(next(it)) # Affiche le 3ème élément
# print(next(it)) # Lèverait l'exception StopIteration
```

### Consommation d'un itérateur (exemple avec `zip`)

Certains objets, comme ceux produits par la fonction `zip`, sont directement des itérateurs pour économiser de la mémoire (évaluation paresseuse).

```python
a =
b =
z = zip(a, b) # z est son propre itérateur

# Premier parcours (compréhension de liste)
print([i for i in z]) # Affiche: [(1, 3), (2, 4)]

# Tentative de second parcours
print([i for i in z]) # Affiche: [] (la liste est vide car z est épuisé)
```

## 4. Pourquoi cette distinction ?

La séparation entre itérable et itérateur permet une gestion efficace de la mémoire :

- **Économie de mémoire** : Un fichier volumineux peut être lu ligne par ligne via un itérateur sans être chargé entièrement en mémoire vive.
- **Flexibilité** : Les mécanismes comme les boucles `for` ou les compréhensions peuvent accepter indifféremment un itérable ou un itérateur, car les deux implémentent la méthode `__iter__`.
- **Réutilisation** : Pour parcourir à nouveau des données épuisées dans un itérateur, il suffit d'en recréer un nouveau, ce qui est une opération très peu coûteuse.