# Usages avancés de `import`

## Les attributs spéciaux du module

Tout objet de type module possède des attributs automatiques (entourés de doubles underscores `__`) qui décrivent son identité et sa source.

- **`__name__`** : Le nom complet du module (ex: `package.module`). Si le module est le point d'entrée exécuté, sa valeur devient `"__main__"`.
- **`__file__`** : Le chemin absolu vers le fichier physique sur le disque.
- **`__package__`** : Le nom du package parent (utilisé pour résoudre les imports relatifs).
- **`__all__`** : Une liste de chaînes de caractères définissant quels symboles sont exportés lors d'un `from module import *`.

## Import Absolu vs Relatif

Par défaut, Python utilise l'**import absolu** : il cherche toujours le module en partant des racines définies dans `sys.path`.

### L'import relatif (`.`)

Il permet d'importer un module voisin sans connaître le nom du package parent. Cela utilise une syntaxe à points :

- **`.`** : Le répertoire courant.
- **`..`** : Le répertoire parent.

**Exemple dans `package/main.py` :**

Python

```java
from . import random  # Importe le fichier random.py situé dans le MÊME dossier
from .. import utils  # Remonte d'un niveau pour chercher utils
```

## Le problème du point d'entrée (`__main__`)

C'est le piège classique : **l'import relatif ne fonctionne pas dans le script que vous lancez directement.**

**Pourquoi ?**

1. L'import relatif se base sur l'attribut `__name__`.
2. Pour le script lancé, `__name__` vaut `"__main__"`.
3. Python ne sait pas "où il est" dans la hiérarchie des packages car le nom `"__main__"` ne contient aucune information sur le parent.

### L'idiome de protection

Pour permettre à un fichier d'être à la fois un module importable et un script de test, on utilise :

Python

```java
if __name__ == "__main__":
    # Ce code ne s'exécute QUE si on lance le fichier directement
    print("Exécution des tests locaux...")
```

## Bonnes pratiques de structuration

Pour éviter les maux de tête liés aux imports :

1. **Séparez le code et le lancement** : Vos fichiers de bibliothèque doivent rester dans des packages. Vos scripts de lancement (points d'entrée) doivent être à la racine ou dans un dossier dédié, et n'utiliser que des **imports absolus**.
2. **Utilisez `unittest`** : Pour tester vos modules sans casser les imports, lancez vos tests avec l'option `m` (module) :
`python3 -m unittest tests.mon_test`
3. **Privilégiez l'absolu** : L'import relatif est pratique à l'intérieur d'une bibliothèque complexe pour rester "portable" (si on renomme le package), mais l'import absolu reste le plus lisible et le moins sujet aux erreurs.

## Synthèse : Ce qu'il faut retenir

- Un module exécuté directement s'appelle toujours **`__main__`**.
- Le point `.` dans un import signifie "cherche par rapport à mon nom actuel".
- Si vous avez une erreur `ImportError: attempted relative import with no known parent package`, c'est probablement que vous tentez de lancer un script contenant des imports relatifs comme s'il était à la racine.