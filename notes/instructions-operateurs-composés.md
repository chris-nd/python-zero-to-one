## Les instructions `+=` et dérivées (`=`, `*=`, etc.)

### Le problème : Géométrie variable

**Différence fondamentale :** Le comportement de `+=` change selon que l'objet est **mutable** ou **immuable**.

### Contexte historique

**En C :**

- `+=` et `++` modifient la mémoire **en place**
- Optimisation pour utiliser instructions assembleur efficaces

**En Python :**

- Inspiré de C, mais adapté au modèle d'objets mutables/immuables
- Comportement **différent** selon le type !

### Exemple 1 : Type immuable (entier)

```python
# Référence partagée
a = b = 3
print(a is b)  # → True

# Utiliser += sur a
a += 1

# Résultat
print(a)       # → 4
print(b)       # → 3
print(a is b)  # → False
```

**Explication :**

- Les entiers sont **immuables**
- `a += 1` crée un **nouvel objet** (4)
- `a` pointe vers ce nouvel objet
- `b` reste inchangé (pointe toujours vers 3)

**Schéma :**

```
Avant :  a → 3 ← b

Après :  a → 4
         b → 3
```

### Exemple 2 : Type mutable (liste)

```python
# Référence partagée
a = b = []
print(a is b)  # → True

# Utiliser += sur a
a += [1]

# Résultat
print(a)       # → [1]
print(b)       # → [1]  ⚠️ b est aussi modifié !
print(a is b)  # → True  ⚠️ Toujours le même objet
```

**Explication :**

- Les listes sont **mutables**
- `a += [1]` modifie la liste **en place**
- `a` et `b` pointent toujours vers le **même objet**
- Les deux voient la modification

**Schéma :**

```
Avant :  a → [ ] ← b

Après :  a → [1] ← b
         (même objet modifié)
```

### Différence `+=` vs `= +`

**Avec une liste :**

**Version 1 : `+=` (modification en place)**

```python
a = []
print("avant", id(a))  # ex: 140234567890
a += [1]
print("après", id(a))  # ex: 140234567890 (même ID)
```

**Version 2 : `= +` (création nouvel objet)**

```python
a = []
print("avant", id(a))  # ex: 140234567920
a = a + [1]
print("après", id(a))  # ex: 140234568000 (ID différent)
```

### 🔍 Précision sur la définition

**On dit souvent (première approximation) :**

```python
x += y  ≈  x = x + y
```

**Mais c'est inexact !** Le comportement diffère selon mutabilité :

**Pour types immuables :**

```python
x += y  ==  x = x + y  # Équivalent
```

**Pour types mutables :**

```python
x += y  !=  x = x + y  # Différent !

# x += y  ≈  x.__iadd__(y)  (modification en place)
# x = x + y  ≈  x = x.__add__(y)  (nouvel objet)
```

### Impact sur références partagées

**Exemple complet du danger :**

```python
# Cas 1 : Avec += (mutable)
list1 = list2 = []
list1 += [1, 2]
print(list2)  # → [1, 2]  ⚠️ Modifié aussi !

# Cas 2 : Avec = + (mutable)
list1 = list2 = []
list1 = list1 + [1, 2]
print(list2)  # → []  ✅ Pas modifié
```

### Exemples par type

**Types immuables (créent nouvel objet) :**

```python
# Entiers
a = 5
a += 3  # a = 8 (nouvel objet)

# Strings
s = "hello"
s += " world"  # s = "hello world" (nouvelle string)

# Tuples
t = (1, 2)
t += (3, 4)  # t = (1, 2, 3, 4) (nouveau tuple)
```

**Types mutables (modifient en place) :**

```python
# Listes
l = [1, 2]
l += [3, 4]  # Modifie l en place

# Sets
s = {1, 2}
s |= {3, 4}  # Modifie s en place

# Dictionnaires
d = {'a': 1}
d.update({'b': 2})  # Modifie d en place (pas +=, mais même idée)
```

### 🎓 Recommandation de l'auteur

**Opinion personnelle :** Cette famille d'instructions n'est pas le trait le plus réussi dans le langage. **Je ne recommande pas de l'utiliser.**

**Raisons :**

- Comportement ambigu selon contexte
- Source de bugs avec références partagées
- Confusion pour les débutants

### Alternatives recommandées

**Pour types immuables :**

```python
# ✅ Clair et explicite
x = x + y
```

**Pour types mutables (listes) :**

```python
# ✅ Explicite sur l'intention
liste.extend([1, 2, 3])  # Modification en place
liste.append(1)           # Ajout d'un élément

# Ou si nouvelle liste voulue
nouvelle_liste = liste + [1, 2, 3]
```

**Pour sets :**

```python
# ✅ Explicite
ensemble.update({1, 2, 3})  # Modification en place
nouveau_set = ensemble | {1, 2, 3}  # Nouvel objet
```

### Détecter le comportement

**Tester si modification en place :**

```python
original_id = id(x)
x += y
if id(x) == original_id:
    print("Modification en place (mutable)")
else:
    print("Nouvel objet créé (immuable)")
```

### Checklist de sécurité

Avant d'utiliser `+=`, demandez-vous :

- [ ]  Le type est-il mutable ou immuable ?
- [ ]  Y a-t-il des références partagées ?
- [ ]  Est-ce que je veux modifier en place ?
- [ ]  Mon intention est-elle claire pour un lecteur ?

**Si doute → Utilisez la forme explicite** (`x = x + y` ou `liste.extend()`)

### ⚠️ Pièges courants

**Piège 1 : Références partagées avec listes**

```python
def ajouter_element(liste=[]):  # Valeur par défaut mutable !
    liste += [1]  # Modifie la liste partagée
    return liste

print(ajouter_element())  # → [1]
print(ajouter_element())  # → [1, 1]  Oups !
```

**Piège 2 : Tuples contenant mutables**

```python
t = ([1, 2], 3)
t[0] += [3]  # Erreur ! tuple immuable
# Mais la liste interne est quand même modifiée !
```

**Piège 3 : Confusion dans boucles**

```python
a = [1, 2, 3]
b = a
for _ in range(3):
    a += [0]  # Modifie aussi b !

print(b)  # → [1, 2, 3, 0, 0, 0]
```