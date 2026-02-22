## Slices (découpage de séquences)

Les slices permettent d'extraire une plage d'éléments d'une séquence (chaînes, listes, tuples, etc.) avec la syntaxe `sequence[debut:fin:pas]`.

**Slice simple : `[debut:fin]`**

```python
chaine = "abcdefghijklmnopqrstuvwxyz"
chaine[2:6]  # → "cdef"

```

### **Conventions importantes**

- Les indices commencent à 0
- `debut` est **inclus**
- `fin` est **exclu**
- On obtient `fin - debut` éléments
- Permet de juxtaposer facilement : `chaine[a:b] + chaine[b:c] == chaine[a:c]`

### **Bornes omises**

```python
chaine[:6]   # du début jusqu'à l'indice 6 (exclu)
chaine[24:]  # de l'indice 24 jusqu'à la fin
chaine[:]    # copie complète de la séquence

```

### **Indices négatifs**

Comptent à partir de la fin :

```python
chaine[3:-3]  # du 4ème élément jusqu'à l'avant-dernier (exclu)
chaine[-3:]   # les 3 derniers éléments

```

### **Slice avec pas : `[debut:fin:pas]`**

```python
chaine[3:-3:2]  # un élément sur 2 dans la plage [3:-3]

```

**Pas négatif (parcours inversé)**

```python
chaine[-3:3:-2]  # de la fin vers le début, un sur deux

```

⚠️ Attention : avec un pas négatif, `debut` doit être plus à droite que `fin`

### **Applications sur d'autres types**

*Listes :*

```python
liste = [1, 2, 4, 8, 16, 32]
liste[-1:1:-2]  # parcours inversé avec pas

# Modification par slice (change la taille !)
liste[2:4] = [10, 20, 30]  # remplace 2 éléments par 3

```

*Tableaux numpy (avancé) :*

```python
array[1:4, 1:4]   # sous-tableau 2D
array[::4, ::4]   # avec pas
array[::-1, :]    # inversion d'une dimension

```

**Point clé** : Les slices fonctionnent avec toutes les séquences Python et sont un outil très puissant pour manipuler les données.