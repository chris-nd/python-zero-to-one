## Processus d'importation

Le passage de l'instruction `import` à l'obtention d'un objet module suit trois étapes majeures :

1. **Recherche du fichier sur le disque** :
L'interpréteur cherche le fichier correspondant au nom du module (par exemple `os.py`) dans un ordre précis :
    - Le **répertoire courant** où l'interpréteur a été lancé.
    - La variable d'environnement **`PYTHONPATH`**.
    - Les répertoires des **librairies standards**.
    Vous pouvez consulter la liste ordonnée de ces chemins via la variable `sys.path`.
2. **Pré-compilation en bytecode** :
Une fois le fichier trouvé, Python génère du **bytecode** (fichiers avec l'extension **`.pyc`**). Ces fichiers sont regroupés dans un dossier nommé **`__pycache__`**.
3. **Évaluation et exécution** :
L'interpréteur évalue le bytecode de manière **séquentielle**, de la première à la dernière ligne, pour créer l'objet module. Les fonctions sont définies lors de l'import, mais leur code interne n'est exécuté que lors de l'appel.

**Optimisation importante** : Comme l'importation est une opération coûteuse, l'interpréteur n'importe un module **qu'une seule fois**. Les imports suivants vers le même module utilisent des **références partagées** vers l'objet déjà existant en mémoire.

## Extraits de code utiles

Voici comment inspecter les chemins de recherche et l'environnement de votre système :

```python
import sys
import os

# Afficher la liste des répertoires où Python cherche les modules
print(sys.path)

# Accéder au dictionnaire des variables d'environnement, incluant PYTHONPATH
print(os.environ.get('PYTHONPATH'))

# Vérifier que le module est bien un objet référencé par une variable
import os
print(os) # <module 'os' from '...'>
```

Note : Bien que la plupart des modules soient des fichiers `.py`, certains modules de base sont directement écrits en C.

## Importation : Mécanismes et Rechargement

### La règle d'or

**Un module n'est chargé qu'une seule fois par session d'interpréteur.** Toute instruction `import` supplémentaire pour le même module ne fait que réaffecter une variable vers l'objet module déjà présent en mémoire.

---

### 1. Pourquoi ce choix ?

Le chargement unique répond à trois besoins majeurs :

- **Performance :** On ne paie le coût de lecture du fichier et d'exécution du code qu'une seule fois.
- **Cycles de dépendances :** Permet à deux modules de s'importer mutuellement sans créer de boucle infinie.
- **Stabilité :** Garantit que l'état interne d'un module reste cohérent durant toute l'exécution.

---

### 2. Le problème du développement : `reload`

En mode interactif, si vous modifiez le code source d'un module sur votre disque, un nouvel `import` ne prendra pas en compte vos changements.

### La solution : `importlib.reload`

Pour forcer Python à relire le fichier, il faut utiliser une fonction spécifique :

```java
import mon_module
# ... modifications du fichier mon_module.py ...

from importlib import reload
reload(mon_module) # Le code est ré-exécuté et mis à jour
```

### Cas particulier : Les Notebooks

Dans un environnement type Jupyter ou IPython, on peut automatiser ce processus pour ne pas avoir à appeler `reload` manuellement :

```java
%load_ext autoreload
%autoreload 2
```

### 3. Les coulisses de l'import (Niveau Avancé)

Python utilise des variables systèmes pour gérer ses modules :

### `sys.modules`

C'est un dictionnaire qui sert de **cache**. Avant chaque import, Python vérifie si le nom du module s'y trouve.

- **Astuce :** Supprimer un module de ce dictionnaire (`del sys.modules['nom']`) puis ré-importer le module est une alternative brutale au `reload`.

### `sys.builtin_module_names`

Contient la liste des modules "natifs" écrits en C et intégrés directement dans l'exécutable Python (comme `gc` pour le ramasse-miettes ou `sys`). Ils ne correspondent pas à des fichiers `.py` sur le disque.

## Synthèse : Ce qu'il faut retenir

- L'instruction `import` est **peu coûteuse** après le premier appel : on peut l'utiliser sans crainte à l'intérieur d'une fonction pour limiter les dépendances.
- **`import`** est une instruction, tandis que **`reload`** est une fonction du module `importlib`.
- En cas de comportement étrange après une modification de code, le premier réflexe doit être de vérifier si le module a bien été rechargé.

## **Où sont cherchés les modules ?**

### **Complément - niveau basique**

Pour les débutants en informatique, le plus simple est de se souvenir que si vous voulez uniquement charger vos propres modules ou packages, il suffit de les placer **dans le répertoire où se trouve le point d'entrée**. Pour rappel, le point d'entrée c'est le nom du fichier que vous passez à l'interpréteur lorsque vous démarrez votre programme.

Lorsque vous lancez l'interpréteur **en mode interactif** (sans lui donner de point d'entrée), c'est **le répertoire courant** qui sert alors d'emplacement par défaut pour votre code. Le répertoire courant, c'est celui où vous vous trouvez quand vous lancez la commande python. Si vous n'êtes pas sûr de cet emplacement vous pouvez le savoir en faisant :

```java
from pathlib import Path
Path.cwd()
```

### **Complément - niveau intermédiaire**

Dans ce complément nous allons voir, de manière générale, comment sont localisés (sur le disque dur) les modules que vous chargez dans python grâce à l'instruction `import` ; nous verrons aussi où placer vos propres fichiers pour qu'ils soient accessibles à Python.

[Comme expliqué ici](https://docs.python.org/3/tutorial/modules.html#the-module-search-path), lorsque vous importez le module `spam`, python cherche dans cet ordre :

- un module *built-in* de nom `spam` - possiblement/probablement écrit en C,
- ou sinon un fichier `spam.py` (ou un dossier `spam/` s'il s'agit d'un package, éventuellement assorti d'un `__init__.py`) ; pour le localiser on utilise la variable `sys.path` (c'est-à-dire l'attribut `path` dans le module `sys`), qui est une liste de répertoires, et qui est initialisée avec, dans cet ordre :
    - le répertoire où se trouve le point d'entrée ;
    - la variable d'environnement `PYTHONPATH` ;
    - un certain nombre d'emplacements définis au moment de la compilation de python.

Ainsi sans action particulière de l'utilisateur, Python trouve l'intégralité de la librairie standard, ainsi que les modules et packages installés dans le même répertoire que le fichier passé à l'interpréteur.

La façon dont cela se présente dans l'interpréteur des notebooks peut vous induire en erreur. Aussi je vous engage à exécuter plutôt, et sur votre machine, le programme suivant :

```java
#!/usr/bin/env python3

import sys
from pathlib import Path

def show_argv_and_path():
    print(f"le répertoire courant est {Path.cwd()}")
    print(f"le point d'entrée du programme est {sys.argv[0]}")
    print(f"la variable sys.path contient")
    for i, path in enumerate(sys.path, 1):
        print(f"{i}-ème chemin dans sys.path {path}")

show_argv_and_path()
```

En admettant que

- vous rangez ceci dans le fichier `/le/repertoire/du/script/run.py`
- et que vous lancez Python depuis un répertoire différent, disons `/le/repertoire/ou/vous/etes`
- et avec une variable `PYTHONPATH` vide;

```java
$ cd /le/repertoire/ou/vous/etes/
/le/repertoire/ou/vous/etes 
$ python3 /le/repertoire/du/script/run.py
```

alors vous devriez observer une sortie sur le terminal comme ceci :

```java
le répertoire courant est /le/repertoire/ou/vous/etes
le point d'entrée du programme est /le/repertoire/du/script/run.py
la variable sys.path contient
1-ème chemin dans sys.path /le/repertoire/du/script
... <snip> ... le reste dépend de votre installation*
```

C'est-à-dire que :

- la variable `sys.argv[0]` contient - en tous cas ici - le chemin complet `/le/repertoire/du/script/run.py`,
- et le premier terme dans `sys.path` contient `/le/repertoire/du/script/`.

(NB que [d'après cette documentation](https://docs.python.org/3/library/sys.html#sys.argv) `sys.argv[0]` peut contenir un chemin complet ou un simple nom de fichier, selon votre OS et comment vous invoquez Python)

La [variable d'environnement](http://en.wikipedia.org/wiki/Environment_variable) PYTHONPATH est définie de façon à donner la possibilité d'étendre ces listes depuis l'extérieur, et sans recompiler l'interpréteur, ni modifier les sources. Cette possibilité s'adresse donc à l'utilisateur final - ou à son administrateur système - plutôt qu'au programmeur. Je vous recommande du coup de **ne pas utiliser cette *feature***, qu'il faut réserver à des cas bien précis.

En tant que programmeur, vous avez aussi la possibilité d'étendre `sys.path` avant de faire vos `import`. Ici encore, ce n'est **pas une pratique** très courante, ni **très recommandée**.

### **Distribuer sa propre librairie avec `setuptools`**

On préfère en effet de beaucoup diffuser une application python, ou une librairie, sous forme de packaging en utilisant le [module setuptools](https://pypi.python.org/pypi/setuptools). Il s'agit d'un outil qui **ne fait pas partie de la librairie standard**, et qui supplante `distutils` qui lui, fait partie de la distribution standard mais qui est tombé en déshérence au fil du temps.

`setuptools` permet au programmeur d'écrire - dans un fichier qu'on appelle traditionnellement `setup.py` - le contenu de son application ; grâce à quoi on peut ensuite de manière unifiée :

- installer l'application sur une machine à partir des sources ;
- préparer un package de l'application ;
- diffuser le package dans [l'infrastructure PyPI](https://pypi.python.org/pypi) ;
- installer le package depuis PyPI en utilisant [`pip3`](http://pip.readthedocs.org/en/latest/installing.html).

Pour installer `setuptools`, comme d'habitude vous pouvez faire simplement :

`pip3 install setuptools`

On reviendra en Semaine 6 sur les bonnes pratiques pour organiser l'arborescence des sources de votre projet, et notamment sur les techniques qui permettent de manière sûre de se passer de tout tripotage intempestif de `PYTHONPATH` et/ou `sys.path`.