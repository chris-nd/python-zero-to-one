```python
s = set()
type(s)
s = {1, 2, 3, 'a', True}
a = [1, 2, 4, 1, 18, 30, 4, 1]
set(a)
len(s)
1 in s
'b' in s
s.add('alice')
s
s.update([1, 2, 3, 4, 5, 6, 7])
s
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 - s2
s1 | s2
s1 & s2
a = [0]
s = set(a)
%timeit -n 50 0 in a
%timeit -n 50 0 in s
```

## Les ensembles (type `set`)

**Rappel :** Le type `set` est un type **mutable**.

### Création d'ensembles

### **1. En extension (avec accolades) :**

```python
heteroclite = {'marc', 12, 'pierre', (1, 2, 3), 'pierre'}
print(heteroclite)
# → {'marc', 12, 'pierre', (1, 2, 3)}
# Note : 'pierre' en double est automatiquement dédupliqué
```

### **2. Avec le constructeur `set()` :**

```python
heteroclite2 = set(['marc', 12, 'pierre', (1, 2, 3), 'pierre'])
```

### **3. Ensemble vide :**

```python
# ⚠️ ATTENTION : {} crée un DICTIONNAIRE, pas un set !
type({})  # → <class 'dict'>

# ✅ Correct : utiliser set()
ensemble_vide = set()

# Ou (moins élégant, vieux code)
autre_ensemble_vide = set([])
```

**Raison historique :** Les ensembles sont apparus tardivement dans Python, `{}` était déjà réservé aux dictionnaires.

## Éléments globalement immuables

**Règle :** Comme pour les clés de dictionnaires, les éléments d'un ensemble doivent être **globalement immuables**.

**❌ Exemples invalides :**

```python
# Tuple contenant une liste (mutable)
ensemble = {(1, 2, [3, 4])}  # TypeError: unhashable type: 'list'

# Set contenant un set (mutable)
ensemble = {{1, 2}}  # TypeError: unhashable type: 'set'
```

**✅ Exemples valides :**

```python
ensemble = {1, 2, 'texte', (1, 2, 3)}  # OK
```

### Type `frozenset` (ensemble immuable)

**Pourquoi `frozenset` ?**

- Set immuable (ne peut pas être modifié)
- Peut servir de clé dans un dictionnaire
- Peut être inclus dans un autre ensemble

**Création :**

```python
# Pas de syntaxe {} pour frozenset
frozen = frozenset([1, 2, 3])
```

**Opérations exclues sur `frozenset` :**

- `update()`, `pop()`, `clear()`, `remove()`, `discard()`
- Toutes les opérations de modification

**Opérations permises :**

- Toutes les opérations en lecture seule (union, intersection, etc.)

## Opérations simples

### **Test d'appartenance :**

```python
(1, 2, 3) in heteroclite  # → True ou False
```

### **Taille :**

```python
len(heteroclite)  # Nombre d'éléments
```

## Manipulations (set mutable)

### **Vider un ensemble :**

```python
ensemble.clear()
```

### **Ajouter un élément :**

```python
ensemble.add(1)
```

### **Ajouter plusieurs éléments :**

```python
ensemble.update({2, (1, 2, 3), (1, 3, 5)})
```

### **Retirer un élément (qui ne génère pas d'erreur) :**

```python
ensemble.discard((1, 3, 5))  # OK même si absent
ensemble.discard('foo')       # Pas d'erreur si absent
```

### **Retirer un élément (génère erreur si absent) :**

```python
ensemble.remove((1, 2, 3))   # OK si présent

# Si absent → KeyError
try:
    ensemble.remove('foo')
except KeyError as e:
    print("Erreur:", e)
```

### **Retirer un élément arbitraire :**

```python
while ensemble:
    element = ensemble.pop()  # Pas d'ordre garanti !
    print(element)
```

⚠️ **Rappel :** Contrairement aux listes, les sets n'ont pas d'ordre.

## Opérations mathématiques sur les ensembles

**Données de test :**

```python
A2 = set([0, 2, 4, 6])
A3 = set([0, 6, 3])
```

### **1. Union (∪) :**

```python
A2 | A3  # → {0, 2, 3, 4, 6}
# Ou : A2.union(A3)
```

### **2. Intersection (∩) :**

```python
A2 & A3  # → {0, 6}
# Ou : A2.intersection(A3)
```

### **3. Différence (−) :**

```python
A2 - A3  # → {2, 4}  (éléments dans A2 mais pas dans A3)
A3 - A2  # → {3}     (éléments dans A3 mais pas dans A2)
# Ou : A2.difference(A3)
```

### **4. Différence symétrique (Δ) :**

```python
# (A - B) ∪ (B - A)
A2 ^ A3  # → {2, 3, 4}
# Ou : A2.symmetric_difference(A3)
```

## Comparaisons

**Données de test :**

```python
superset = {0, 1, 2, 3}
subset = {1, 3}
```

### **Égalité :**

```python
heteroclite == heteroclite2
```

### **Inclusion (sous-ensemble) :**

```python
subset <= superset  # → True (sous-ensemble ou égal)
subset < superset   # → True (sous-ensemble strict)
```

### **Ensembles disjoints (aucun élément commun) :**

```python
heteroclite.isdisjoint(A3)  # → True ou False
```

## Set vs Frozenset

| Caractéristique | `set` | `frozenset` |
| --- | --- | --- |
| **Mutable** | ✅ Oui | ❌ Non |
| **Peut être modifié** | ✅ Oui | ❌ Non |
| **Clé de dict** | ❌ Non | ✅ Oui |
| **Élément de set** | ❌ Non | ✅ Oui |
| **Hashable** | ❌ Non | ✅ Oui |
| **Syntaxe** | `{1, 2}` ou `set()` | `frozenset([1, 2])` |