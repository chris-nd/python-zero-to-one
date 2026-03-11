# Portée des Variables en Python

## 1. Variables Globales vs Locales

### Comportement par défaut

```python
a = 'a globale'  # variable globale

def f():
    a = 'a dans f'  # variable locale (nouvelle variable)
    print(a)

print(a)  # → a globale
f()       # → a dans f
print(a)  # → a globale
```

**Principe clé :** Par défaut, une assignation dans une fonction crée une **variable locale**, même si une variable globale du même nom existe.

## 2. L'instruction `global`

### Modifier une variable globale

```python
a = 'a globale'

def f():
    global a  # déclare qu'on utilise la variable globale
    a = 'a dans f'
    print(a)

print(a)  # → a globale
f()       # → a dans f
print(a)  # → a dans f (la variable globale a été modifiée)
```

### Exemple avec opération arithmétique

```python
a = 10

def f():
    global a
    a = a + 10  # modification de la variable globale

print(a)  # → 10
f()
print(a)  # → 20
```

**Attention :** L'utilisation de `global` crée des **effets de bord** (side effects).

## 3. Fonctions Pures (Bonne Pratique)

### Préférer les fonctions sans effets de bord

```python
note = 10

def add_10(n):
    return n + 10  # fonction pure : pas de modification globale

note = add_10(note)
print(note)  # → 20
```

**Avantages des fonctions pures :**

- Plus faciles à tester
- Plus prévisibles
- Pas d'effets de bord
- Meilleure lisibilité

## 4. Portées Imbriquées (Nested Scopes)

### Sans `nonlocal`

```python
a = 'a globale'

def f():
    a = 'a de f'

    def g():
        a = 'a de g'  # nouvelle variable locale à g
        print(a)

    g()
    print(a)

f()       # → a de g
          # → a de f
print(a)  # → a globale
```

**Résultat :** Chaque fonction a sa propre variable locale `a`.

## 5. L'instruction `nonlocal`

### Modifier une variable de la portée englobante

```python
a = 'a globale'

def f():
    a = 'a de f'

    def g():
        nonlocal a  # référence la variable de f (pas globale)
        a = 'a de g'
        print(a)

    g()
    print(a)

f()       # → a de g
          # → a de g (la variable de f a été modifiée)
print(a)  # → a globale (inchangée)
```

**Différence clé :**

- `global` → accède à la portée globale
- `nonlocal` → accède à la portée englobante (mais pas globale)

## Bonnes Pratiques

1. **Éviter `global`** autant que possible → préférer passer les valeurs en paramètres
2. **Utiliser des fonctions pures** → retourner des valeurs plutôt que modifier des variables externes
3. **`nonlocal` avec prudence** → utile pour les closures, mais peut rendre le code moins lisible
4. **Nommer clairement** → utiliser des noms différents pour éviter les confusions
