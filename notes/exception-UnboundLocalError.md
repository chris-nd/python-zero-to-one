# L'exception `UnboundLocalError` en Python

## Le Problème

`UnboundLocalError` survient quand on essaie d'utiliser une variable **à la fois comme globale et locale** dans une même fonction.

### Règle d'or

**Une variable dans une fonction ne peut être QUE locale OU globale, jamais les deux !**

## Les Cas de Portée de Variables

### Variable Locale

Une variable devient locale dès qu'on l'**affecte** dans la fonction :

```python
def ma_fonction():
    variable = "locale"  # Création d'une variable locale
    print(variable)      # ✅ Fonctionne
```

**Important** : Même si une variable globale du même nom existe, l'affectation crée une nouvelle variable locale.

```python
variable = "globale"

def ma_fonction():
    variable = "locale"  # Masque la globale
    print(variable)      # Affiche "locale"
```

### Variable Globale en Lecture

On peut **lire** une variable globale sans problème :

```python
variable = "globale"

def ma_fonction():
    print(variable)  # ✅ Accès en lecture OK
```

### Le Cas Problématique

**INTERDIT** : Lire d'abord comme globale, puis affecter comme locale :

```python
variable = "globale"

def ma_fonction():
    print(variable)      # ❌ Essaie de lire la globale
    variable = "locale"  # ❌ Mais elle devient locale !

# Résultat : UnboundLocalError
```

**Pourquoi ?** Python détecte l'affectation `variable = "locale"` et considère `variable` comme locale **dans toute la fonction**. Donc au moment du `print()`, la variable locale n'est pas encore définie.

## La Solution : Le mot-clé `global`

Pour **modifier** une variable globale depuis une fonction :

```python
variable = "globale"

def ma_fonction():
    global variable           # Déclare qu'on utilise la globale
    print(variable)           # ✅ Lecture OK
    variable = "modifiée"     # ✅ Modification OK

ma_fonction()
print(variable)  # Affiche "modifiée"
```

## Bonnes Pratiques

### À Éviter

- Modifier des variables globales avec `global`
- Mélanger variables locales et globales du même nom

### À Privilégier

1. **Passer des arguments** pour fournir le contexte
2. **Retourner des valeurs** au lieu de modifier des globales
3. Utiliser des objets de configuration pour les constantes

### Exemple recommandé

```python
# ❌ Mauvais
total = 0
def ajouter(x):
    global total
    total += x

# ✅ Bon
def ajouter(total, x):
    return total + x

total = 0
total = ajouter(total, 5)
```

## Diagnostic Rapide

- `UnboundLocalError` = signal que vous mélangez local/global
- **Solution immédiate** : `global variable_name`
- **Solution recommandée** : Repenser le code pour éviter les variables globales
