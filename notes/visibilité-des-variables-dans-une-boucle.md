## Une variable de boucle reste visible après la boucle

En Python, la variable utilisée dans une boucle `for` **continue d’exister après la fin de la boucle**.

Exemple :

```python
for i in [0]:
    pass

print(i)  # i existe encore
```

On dit que la variable **“fuit” (leak)** : elle reste accessible **en dehors du bloc de la boucle**.

## Attention si la boucle est vide

Si la boucle **ne s’exécute jamais** (par exemple avec une liste vide), la variable de boucle **n’est jamais créée**.

Exemple :

```python
def length(l):
    for i, x in enumerate(l):
        pass
    return i + 1
```

- `length([1,2,3])` → fonctionne
- `length([])` → erreur `UnboundLocalError`

Pourquoi ?

Python considère **`i` comme une variable locale** parce qu’elle est utilisée dans la boucle.

Mais si la boucle ne tourne pas, **`i` n’a jamais reçu de valeur**.

## Pourquoi cette erreur arrive

Python décide qu’une variable est **locale dans une fonction** si elle est assignée dans la fonction (même dans une boucle).

Cette décision est faite **avant l’exécution du code** (pré-compilation).

Donc si la boucle ne tourne pas :

- `i` est considérée locale
- mais **elle n’a aucune valeur**
- → `UnboundLocalError`

## Bonnes pratiques pour éviter les erreurs

### Solution 1 — utiliser une variable externe

Au lieu d’utiliser directement la variable de boucle après la boucle :

Mauvaise pratique :

```python
for item in candidates:
    if checks(item):
        break

print(item)
```

Meilleure pratique :

```python
solution = None

for item in candidates:
    if checks(item):
        solution = item
        break

print(solution)
```

### Solution 2 — initialiser la variable avant la boucle

```python
def length2(l):
    i = -1
    for i, x in enumerate(l):
        pass
    return i + 1
```

Ainsi `i` **existe toujours**, même si la boucle est vide.

## Cas particulier : les compréhensions

En **Python 3**, les variables dans les compréhensions **ne fuient pas**.

Exemple :

```python
[i**2 for i in range(3)]
```

Après cela :

```python
print(i)
```

produit `NameError`

car **`i` n’existe pas en dehors de la compréhension**.