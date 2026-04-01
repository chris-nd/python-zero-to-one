## 1. Concept des espaces de nommage

En Python, un **espace de nommage** (namespace) est un ensemble de variables appartenant à un objet spécifique, tel qu'un module, une fonction, une classe ou une instance. Ce mécanisme permet d'**isoler complètement les variables** : deux variables portant le même nom peuvent coexister sans se surcharger si elles appartiennent à des espaces de nommage différents.

## 2. Exemple de code : `spam.py` et `egg.py`

Pour illustrer l'isolation, considérons deux fichiers distincts :

**Fichier `spam.py` :**

```python
x = 1

def f():
    print(x)
```

**Fichier `egg.py` :**

```python
import spam

x = 2

def f():
    print(x)

# Appels et affichages
f()           # Affiche 2
spam.f()      # Affiche 1
print(spam.x) # Affiche 1
```

## 3. Schéma de visualisation (Mémoire et Espaces)

Lors de l'exécution de `python egg.py`, Python gère deux zones distinctes : l'**espace des objets** (la mémoire brute) et les **espaces de nommage** (les dictionnaires de variables).

```markdown
ESPACE DES OBJETS (Mémoire)        ESPACES DE NOMMAGE (Dictionnaires)
+-------------------------+        +---------------------------------+
| [ Entier : 1 ] <-----------+-----| x  (dans le module "spam")      |
|                         |  |     | f  (réf. fonction dans spam)    |
| [ Objet Fonction (f) ] <---+     +---------------------------------+
|        (de spam)        |
|                         |        +---------------------------------+
| [ Entier : 2 ] <-----------+-----| x  (dans le module "egg")       |
|                         |  |     | f  (réf. fonction dans egg)     |
| [ Objet Fonction (f) ] <---+     | spam (réf. vers l'objet module) |
|        (de egg)         |        +---------------------------------+
|                         |                   |
| [ Objet Module (spam) ] <-------------------+
+-------------------------+
```

## 4. Mécanismes clés

- **Règle LEGB :** Pour savoir dans quel espace de nommage une variable a été définie (Local, Enclosed, Global, Built-in), Python utilise la règle LEGB. Par exemple, dans `spam.f()`, Python cherche `x` dans l'espace de nommage global du module `spam`.
- **Accès explicite :** On accède à une variable d'un autre module via la notation **`objet.attribut`** (ex: `spam.x`). Cela rend le code plus maintenable et évite les collisions accidentelles.
- **Implémentation :** Techniquement, les espaces de nommage sont implémentés sous forme de **dictionnaires** où la clé est le nom de la variable et la valeur est la référence vers l'objet.
- **Objets partagés :** Si les espaces de nommage isolent les *variables*, ils n'isolent pas les *objets*. Deux variables dans des espaces différents peuvent référencer le même **objet mutable**. Si cet objet est modifié, le changement est visible partout (effet de bord).

En résumé, Python offre une isolation des variables "quasiment gratuitement" dès que l'on commence à écrire du code grâce aux modules, facilitant ainsi le développement et la maintenance.