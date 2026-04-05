# La notion de Package

## Module vs Package : La hiérarchie

Alors que le **module** correspond à un **fichier** (`.py`), le **package** correspond à un **répertoire** (dossier).

### Structure type d'un package

Pour que Python reconnaisse un dossier comme un package, il ressemble généralement à ceci :

Plaintext

```java
mon_projet/
└── package_jouet/          <-- Le répertoire du package
    ├── __init__.py         <-- Le fichier d'initialisation (souvent vide)
    └── module_jouet.py     <-- Un module à l'intérieur du package
```

## Le rôle du fichier `__init__.py`

C'est le "cerveau" du répertoire. Lorsqu'on fait `import package_jouet`, c'est le code contenu dans `__init__.py` qui est exécuté.

### À quoi sert-il ?

1. **Initialisation :** Exécuter du code nécessaire au bon fonctionnement de la bibliothèque.
2. **Exposition (Façade) :** Permettre à l'utilisateur d'accéder à des fonctions sans connaître l'organisation interne des dossiers.

**Exemple d'exposition :**
Si dans `__init__.py` vous écrivez `from .module_jouet import ma_fonction`, l'utilisateur pourra faire : `import package_jouet`  et `package_jouet.ma_fonction()`  *(au lieu de package_jouet.module_jouet.ma_fonction())*

**Note historique :** Depuis Python 3.3, ce fichier n'est plus strictement obligatoire pour créer un package (on parle de *Namespace Packages*), mais il reste fortement recommandé pour contrôler ce que le package expose.

## Avantages des Packages

- **Encapsulation :** On cache la complexité. L'utilisateur interagit avec le nom du package, peu importe si celui-ci contient 10 ou 100 fichiers derrière.
- **Maintenance :** Le développeur peut renommer ou diviser ses modules internes sans casser le code des utilisateurs, tant qu'il met à jour les liens dans `__init__.py`.
- **Espaces de noms imbriqués :** Vous pouvez avoir `package.sous_package.module`. Cela évite toute collision de noms avec d'autres bibliothèques.

```java
import package_jouet

# Accès au module interne
print(package_jouet.module_jouet.spam)

# Accès direct si exposé dans __init__.py
print(package_jouet.jouet)
```

## Analogie pour mémoriser

- **Variable :** Une donnée unique.
- **Fonction :** Un carton contenant des variables et des instructions.
- **Module (`.py`) :** Une étagère contenant plusieurs fonctions.
- **Package (Dossier) :** Une pièce entière contenant plusieurs étagères (modules).

## Synthèse : Ce qu'il faut retenir

- Un **Package** est un répertoire qui contient des modules.
- L'import d'un package charge en priorité son fichier **`__init__.py`**.
- En termes de type Python, un package et un module sont de même nature : ce sont des objets de type `module`.
- Utilisez les packages pour structurer vos projets dès qu'ils dépassent quelques centaines de lignes de code.