## La fonction `isinstance`

### Utilité de `isinstance`

La fonction `isinstance` permet de :

1. **Vérifier** qu'un argument a le type attendu
2. **Traiter différemment** les entrées selon leur type

### Typage dynamique en Python

**Rappel :** Python utilise le **typage dynamique**, contrairement au typage statique d'autres langages.

`isinstance` facilite la gestion de types multiples dans les fonctions.

### Exemple pratique : Fonction flexible

**Fonction acceptant plusieurs types d'entrées :**

```python
def factoriel(argument):
    # Si on reçoit un entier
    if isinstance(argument, int):              # (*)
        return 1 if argument <= 1 else argument * factoriel(argument - 1)

    # Convertir si on reçoit une chaîne
    elif isinstance(argument, str):
        return factoriel(int(argument))

    # Liste des résultats si tuple ou liste
    elif isinstance(argument, (tuple, list)):  # (**)
        return [factoriel(i) for i in argument]

    # Sinon : erreur
    else:
        raise TypeError(argument)

# Utilisation
print("entier", factoriel(4))          # → entier 24
print("chaine", factoriel("8"))        # → chaine 40320
print("tuple", factoriel((4, 8)))      # → tuple [24, 40320]
```

### Syntaxe de `isinstance`

**Syntaxe de base :**

```python
isinstance(objet, Type)
# → True si objet est une instance de Type, False sinon
```

**Avec plusieurs types (tuple) :**

```python
isinstance(objet, (Type1, Type2, Type3))
# → True si objet est une instance de l'un des types
```

**Exemples :**

```python
# Un seul type
isinstance(42, int)           # → True
isinstance("hello", str)      # → True
isinstance([1, 2], list)      # → True

# Plusieurs types
isinstance(5, (int, float))   # → True (int dans le tuple)
isinstance("x", (int, str))   # → True (str dans le tuple)
isinstance([], (tuple, list)) # → True (list dans le tuple)
```

### Module `types`

**Utilité :** Définit des constantes pour types moins courants.

```python
from types import FunctionType

def ma_fonction():
    pass

isinstance(ma_fonction, FunctionType)  # → True
```

**Attention aux fonctions built-in :**

```python
from types import BuiltinFunctionType, FunctionType

isinstance(len, BuiltinFunctionType)  # → True
isinstance(len, FunctionType)         # → False (!)
```

**Types courants dans `types` :**

```python
import types

# Quelques constantes utiles
types.FunctionType           # Fonctions définies par l'utilisateur
types.BuiltinFunctionType    # Fonctions built-in (len, print, etc.)
types.MethodType             # Méthodes
types.LambdaType             # Fonctions lambda
types.GeneratorType          # Générateurs
types.ModuleType             # Modules
```

**Liste complète :**

```python
import types
dir(types)  # Affiche tous les attributs
```

### `isinstance` vs `type`

**Recommandation :** Préférer `isinstance` à `type`.

**Raison 1 : Plusieurs types**

```python
# ✅ Avec isinstance : simple
isinstance(x, (int, float))

# ❌ Avec type : verbeux
type(x) == int or type(x) == float
```

**Raison 2 : Support de l'héritage (POO)**

**Définition de classes avec héritage :**

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammifere(Animal):  # Mammifere hérite d'Animal
    def __init__(self, name):
        Animal.__init__(self, name)

# Créer des instances
requin = Animal('requin')
baleine = Mammifere('baleine')
```

**Test avec `isinstance` :**

```python
# Évident : baleine est un Mammifere
isinstance(baleine, Mammifere)  # → True

# Important : baleine est AUSSI un Animal (héritage)
isinstance(baleine, Animal)     # → True
```

**Test avec `type` (problème !) :**

```python
# Type exact
type(baleine) == Mammifere      # → True

# ❌ Ne reconnaît PAS l'héritage
type(baleine) == Animal         # → False (problème)
```

### Comparaison détaillée

| Aspect | `isinstance` | `type` |
| --- | --- | --- |
| **Test simple** | `isinstance(x, int)` | `type(x) == int` |
| **Plusieurs types** | ✅ `isinstance(x, (int, float))` | ❌ Verbeux |
| **Héritage** | ✅ Reconnaît classes parentes | ❌ Type exact seulement |
| **Recommandation** | ✅ **Préféré** | ⚠️ Cas spécifiques |

### Héritage : Concept clé

**Principe ensembliste :**

```
Animal
├── Mammifere
│   ├── Baleine
│   └── Dauphin
└── Poisson
    └── Requin
```

**Logique :**

- `Mammifere` ⊂ `Animal` (sous-ensemble)
- Tout ce qu'on peut faire sur `Animal`, on peut le faire sur `Mammifere`
- `isinstance` respecte cette hiérarchie

**Exemple :**

```python
baleine = Mammifere('baleine')

# Test avec isinstance (respecte héritage)
isinstance(baleine, Mammifere)  # → True
isinstance(baleine, Animal)     # → True (parent)
isinstance(baleine, object)     # → True (racine de tout)

# Test avec type (type exact uniquement)
type(baleine) == Mammifere      # → True
type(baleine) == Animal         # → False
```

### Cas d'usage pratiques

**1. Validation de paramètres**

```python
def diviser(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a doit être un nombre")
    if not isinstance(b, (int, float)):
        raise TypeError("b doit être un nombre")
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b
```

**2. Traitement polymorphe**

```python
def traiter(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, (list, tuple)):
        return [traiter(item) for item in data]
    elif isinstance(data, dict):
        return {k: traiter(v) for k, v in data.items()}
    else:
        return data

print(traiter("hello"))           # → "HELLO"
print(traiter(["a", "b"]))        # → ["A", "B"]
print(traiter({"x": "hello"}))    # → {"x": "HELLO"}
```

**3. Gestion d'API flexible**

```python
def envoyer_message(destinataires, message):
    # Accepte un string ou une liste
    if isinstance(destinataires, str):
        destinataires = [destinataires]

    for dest in destinataires:
        # envoyer à dest
        pass

# Les deux fonctionnent
envoyer_message("alice@example.com", "Bonjour")
envoyer_message(["alice@example.com", "bob@example.com"], "Bonjour")
```

**4. Duck typing avec vérification**

```python
def sauvegarder(fichier_ou_nom):
    # Accepte un nom de fichier ou un objet fichier
    if isinstance(fichier_ou_nom, str):
        with open(fichier_ou_nom, 'w') as f:
            f.write(data)
    else:
        # Assume que c'est un objet fichier
        fichier_ou_nom.write(data)
```

### Cas particuliers

**1. None**

```python
isinstance(None, type(None))  # → True

# Mais généralement on teste avec is
if x is None:  # Préféré
    pass
```

**2. Booléens sont des entiers**

```python
isinstance(True, bool)  # → True
isinstance(True, int)   # → True (bool hérite de int)
```

**3. Fonctions lambda**

```python
from types import LambdaType, FunctionType

f = lambda x: x * 2
isinstance(f, LambdaType)     # → True
isinstance(f, FunctionType)   # → True (aussi)
```

### Bonnes pratiques

**1. Utiliser `isinstance` pour vérifier types :**

```python
# ✅ Bon
if isinstance(x, int):
    pass

# ❌ Moins bon
if type(x) == int:
    pass
```

**2. Accepter plusieurs types avec tuple :**

```python
# ✅ Concis et clair
if isinstance(x, (int, float)):
    pass
```

**3. Respecter le duck typing Python :**

```python
# ✅ Pythonique : essayer puis gérer l'erreur
try:
    x.append(item)
except AttributeError:
    # pas une liste
    pass

# Plutôt que
if isinstance(x, list):
    x.append(item)
```

**4. Ne pas sur-vérifier :**

```python
# ❌ Trop restrictif
def process(data):
    if not isinstance(data, list):
        raise TypeError("Doit être une liste")
    # ...

# ✅ Plus flexible (accepte toute séquence)
def process(data):
    for item in data:  # Marche avec list, tuple, etc.
        # ...
```

### Points clés à retenir

1. **`isinstance(objet, Type)`** : vérifie le type d'un objet
2. **Plusieurs types** : `isinstance(x, (Type1, Type2))`
3. **Supporte l'héritage** : reconnaît les classes parentes
4. **Préférer à `type`** : plus flexible et pythonique
5. **Module `types`** : constantes pour types spéciaux
6. **Duck typing** : ne pas abuser de `isinstance`
7. **Héritage** : `isinstance(baleine, Animal)` → True