## Des méthodes de liste en Python

**Trouver l'information**

- Utilisez `help(list)` pour voir toutes les méthodes disponibles
- Ignorez les méthodes en `__nom__` (elles seront vues plus tard)

**Méthodes principales** (avec `liste = [0, 1, 2, 3]`)

### **`append(element)`**

Ajoute un élément à la fin

```python
liste.append('ap')  # → [0, 1, 2, 3, 'ap']
```

### **`extend(liste2)`**

Ajoute tous les éléments d'une autre liste

```python
liste.extend(['ex1', 'ex2'])  # → [0, 1, 2, 3, 'ap', 'ex1', 'ex2']
```

### **`insert(index, element)`**

Insère un élément à une position

```python
liste.insert(2, '1 bis')  # insère à l'index 2
# Alternative avec slice: liste[2:2] = ['1 bis']
```

### **`remove(element)`**

Supprime la première occurrence d'un élément

```python
liste.remove(3)  # supprime le premier 3 trouvé
```

### **`pop([index])`**

Extrait et retourne un élément

```python
element = liste.pop(0)  # extrait l'élément à l'index 0
element = liste.pop()   # sans argument : extrait le dernier

```

### **`reverse()`**

Inverse la liste (modifie l'original)

```python
liste.reverse()  # inverse la liste sur place
# Alternative avec slice (crée une copie): liste2 = liste[::-1]

```

### **Différence clé : mutabilité**

**`append`/`extend` vs `+` :**

- `liste1.extend(liste2)` : **modifie** `liste1` en place, retourne `None`
- `liste3 = liste1 + liste2` : **crée un nouvel objet**, laisse `liste1` et `liste2` intacts

**`reverse()` vs slicing `[::-1]` :**

- `liste.reverse()` : modifie la liste originale
- `liste2 = liste[::-1]` : crée une nouvelle liste inversée

**Règle générale :**

- Les méthodes de liste qui modifient l'objet retournent `None`
- Ces méthodes n'existent que sur les objets **mutables** (pas sur les strings par exemple)

**Astuces notebook**

- `help(list.pop)` ou `list.pop?` : afficher l'aide
- `%timeit` : mesurer le temps d'exécution
- Tab : autocomplétion

**Attention** : Les méthodes modifient la liste en place, donc l'ordre d'exécution des cellules compte !

## Objets mutables vs immuables

Python fait une distinction essentielle entre :

- **Objets immuables** : ne peuvent pas être modifiés après création
- **Objets mutables** : peuvent être modifiés en place

### Les chaînes sont IMMUABLES

**Exemple avec des chaînes :**

```python
s1 = 'abc'
s2 = s1      # s2 pointe vers le même objet
s1 += 'def'  # crée un NOUVEL objet 'abcdef'

print(s1)  # → 'abcdef' (pointe vers le nouvel objet)
print(s2)  # → 'abc' (pointe toujours vers l'ancien objet)

```

**Ce qui se passe :**

1. `s1` et `s2` pointent initialement vers le même objet `'abc'`
2. L'opération `+=` ne peut pas modifier l'objet original (immuable)
3. Python crée un **nouvel objet** `'abcdef'`
4. Seul `s1` pointe maintenant vers ce nouvel objet
5. `s2` reste inchangé, pointant vers l'objet original

### Les listes sont MUTABLES

**Même exemple avec des listes :**

```python
liste1 = ['a', 'b', 'c']
liste2 = liste1      # liste2 pointe vers le même objet
liste1 += ['d', 'e', 'f']  # modifie l'objet EN PLACE

print(liste1)  # → ['a', 'b', 'c', 'd', 'e', 'f']
print(liste2)  # → ['a', 'b', 'c', 'd', 'e', 'f'] (pareil !)

```

**Ce qui se passe :**

1. `liste1` et `liste2` pointent vers le même objet
2. L'opération `+=` **modifie directement** l'objet liste
3. Aucun nouvel objet n'est créé
4. `liste1` et `liste2` pointent toujours vers le **même objet modifié**
5. Les deux variables voient donc le changement

### Tableau récapitulatif

| Type | Mutable ? | Comportement avec `+=` | Exemple |
| --- | --- | --- | --- |
| **str** | ❌ Immuable | Crée un nouvel objet | `'abc'` |
| **int, float** | ❌ Immuable | Crée un nouvel objet | `42` |
| **tuple** | ❌ Immuable | Crée un nouvel objet | `(1, 2)` |
| **list** | ✅ Mutable | Modifie en place | `[1, 2]` |
| **dict** | ✅ Mutable | Modifie en place | `{'a': 1}` |
| **set** | ✅ Mutable | Modifie en place | `{1, 2}` |

### Points clés à retenir

1. **Les objets immuables sont "sûrs"** : si vous passez une chaîne à une fonction, elle ne peut pas être modifiée accidentellement
2. **Les objets mutables nécessitent plus d'attention** : si plusieurs variables pointent vers la même liste, la modifier via l'une affecte toutes les autres
3. **Ce comportement n'est pas spécifique à `+=`** : c'est une propriété fondamentale des types d'objets
4. **Conséquence importante** : pour éviter les effets de bord avec les mutables, il faut parfois créer des copies explicites

## Tris de listes en Python

### Méthode `sort()` — tri en place

- Modifie la liste directement (tri en place).
- Exemple : `liste.sort()` trie la liste par ordre croissant.

### Fonction `sorted()` — tri sur copie

- Retourne une nouvelle liste triée sans modifier l’originale.
- Exemple : `liste2 = sorted(liste1)`.

### Tri décroissant

- Utiliser `reverse=True` : `liste.sort(reverse=True)`.

### Tri de chaînes de caractères

- Tri lexicographique (ordre du dictionnaire).
- Points importants :
    - Les majuscules sont avant les minuscules : `'Z' < 'a'`.
    - Les espaces et la ponctuation influencent l’ordre.
    - L’ordre est déterministe mais peut sembler arbitraire.

### Note

- Fonctionne sur les types numériques (sauf les complexes) et les chaînes.
- Il est possible de définir un critère de tri personnalisé (à voir plus tard avec les fonctions).

En résumé : `sort()` modifie la liste, `sorted()` retourne une copie triée. Le tri des chaînes suit l’ordre lexicographique (majuscules avant minuscules).