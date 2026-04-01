## 1. Les Fonctions Lambda

Les fonctions lambda sont des **fonctions anonymes** définies comme des **expressions**. Bien qu'elles ne soient pas indispensables (une fonction classique `def` peut toujours les remplacer), elles offrent une syntaxe plus concise et expressive.

- **Syntaxe :** `lambda paramètres: expression`.
- **Usage :** Elles sont idéales pour être passées directement en argument à une autre fonction sans avoir à les nommer.

**Extrait de code :**

```python
# Définition d'une fonction lambda simple
carre = lambda x: x**2 - 1  #
print(carre(5)) # Utilisation comme une fonction normale
```

**Schéma du flux d'une lambda :**

```python
**Entrée (x)**  ───>  **[ Expression : x² - 1 ]**  ───>  **Résultat**
```

## 2. Les Fonctions comme Objets

En Python, les fonctions sont des objets normaux. Cela signifie qu'une fonction peut être **passée comme argument** à une autre fonction.

**Extrait de code :**

```python
def image_de_f(f):
    for x in range(10):
        print(f"f({x}) = {f(x)}") # f est appelée ici

# On passe une lambda directement en argument
image_de_f(lambda x: x**2 - 1)
```

## 3. Les primitives `map` et `filter`

Ce sont deux outils issus de la programmation fonctionnelle pour manipuler des itérables (listes, ranges, etc.).

### A. La fonction `map`

Elle **applique une fonction** à chaque élément d'un itérable.

**Schéma de `map` :**

```python
Liste : [a, b, c]
↓ (Applique f)
Résultat : [f(a), f(b), f(c)]
```

### B. La fonction `filter`

Elle **filtre les éléments** d'un itérable selon un test logique (vrai ou faux).

**Schéma de `filter` :**

```python
Liste : ↓ (Test: est-ce pair ?) Résultat :
```

**Extrait de code :**

```python
# Utilisation de map
m = map(lambda x: x**2 - 1, range(10))

# Utilisation de filter (garde uniquement les nombres pairs)
f = filter(lambda x: x % 2 == 0, range(10))
```

## 4. Itérateurs vs Compréhensions de liste

Un point crucial est que `map` et `filter` produisent des **itérateurs**.

- **Avantage :** Ils sont très **compacts en mémoire** car ils ne créent pas de liste temporaire.
- **Inconvénient :** On ne peut les parcourir qu'**une seule fois**.
- **Alternative moderne :** En Python moderne, on préfère souvent les **compréhensions de liste** pour leur lisibilité, bien qu'elles occupent plus de mémoire.

**Comparaison visuelle :**

| Caractéristique | `map`/`filter` | Compréhension de liste |
| --- | --- | --- |
| **Type de retour** | Itérateur (objet compact) | Nouvelle liste en mémoire |
| **Usage** | Parcours unique | Multiples utilisations possibles |
| **Style** | Programmation fonctionnelle | Style "Pythonique" |

En résumé, Python utilise ces outils pour rester un langage **simple, puissant et flexible**, s'adaptant aux besoins du développeur sans dogmatisme.