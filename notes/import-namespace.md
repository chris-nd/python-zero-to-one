## Nature des Modules et Mémoire

- **Instance Unique :** Un module est un **objet mutable** chargé une seule fois en mémoire. Les imports suivants ne font que créer des références vers cet objet existant.
- **Coût Mémoire :** Que vous utilisiez `import spam` ou `from spam import x`, l'intégralité du module est chargée en mémoire. La différence n'est pas la consommation mémoire, mais la gestion de l'espace de nommage.

## Comparaison des méthodes d'importation

| **Méthode** | **Syntaxe** | **Accès** | **Risque** |
| --- | --- | --- | --- |
| **Module complet** | `import spam` | `spam.x` | Faible (Isolation parfaite) |
| **Symbole spécifique** | `from spam import x` | `x` | Moyen (Collisions de noms) |
| **Alias** | `import spam as s` | `s.x` | Faible (Pratique pour noms longs) |
| **Import global** | `from spam import *` | `x` | **Élevé** (Pollution, code illisible) |

## Espaces de Nommage (Namespaces)

Chaque module possède son propre dictionnaire d'attributs.

- **`vars(module)`** : Renvoie le dictionnaire (`__dict__`) de l'espace de nommage.
- **`dir(module)`** : Liste tous les attributs et méthodes disponibles (plus général).
- **`globals()`** : Équivaut à `vars()` pour le module courant.

---

## Concepts Avancés

### La Clause `import as` (Renommage)

Utile pour éviter les conflits avec des fonctions intégrées (ex: éviter qu'un module nommé `globals.py` n'écrase la fonction `globals()`) ou pour raccourcir les noms (ex: `import numpy as np`).

### Imports Dynamiques (`importlib`)

L'instruction `import` classique nécessite un nom fixe. Pour charger un module dont le nom est calculé (une chaîne de caractères), on utilise :

Python

```java
from importlib import import_module
name = "ma" + "th"
module = import_module(name) # Équivaut à import math
```

### Le danger du `import *`

À bannir (sauf en console interactive) car :

1. **Casse la liaison statique :** On ne sait plus d'où vient une variable à la lecture du code.
2. **Collisions invisibles :** Si deux modules importés avec  possèdent une variable `data`, le second écrasera silencieusement le premier.