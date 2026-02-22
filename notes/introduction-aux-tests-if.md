## Structure de base

**Exemple simple :**

```python
if 'g' in 'egg':
    print('OUI')      # indenté de 4 espaces
else:
    print('NON')      # indenté de 4 espaces

```

**Points importants :**

- Chaque début de bloc se termine par **deux-points `:`**
- Le bloc qui suit doit être indenté
- Pas besoin de marquer la fin du bloc (pas d'accolade fermante ni de `end`)

### Imbrications

```python
if 'a' in entree:
    if 'b' in entree:              # 4 espaces
        cas11 = True               # 8 espaces
        print('a et b')
    else:                          # 4 espaces
        cas12 = True               # 8 espaces
        print('a mais pas b')

```

Pour imbriquer des blocs, on ajoute simplement 4 espaces supplémentaires à chaque niveau.

### ⚠️ RÈGLE CRITIQUE : Jamais de tabulations !

**Message essentiel : N'UTILISEZ JAMAIS de caractères tabulation (`^I`) dans votre code Python.**

**Pourquoi ?**

Le problème vient de l'interprétation variable des tabulations :

- Vim peut afficher une tabulation comme 4 espaces
- Emacs peut l'afficher comme 8 espaces
- Résultat : le même fichier apparaît différemment selon l'éditeur

**Exemple de chaos :**

Ce que Bernard voit (Vim, tab=4) :

```python
if 'a' in entree:
    if 'b' in entree:
        cas11 = True
        print('a et b')

```

Fichier réel (avec `^I` = tabulation) :

```python
if 'a' in entree:
^Iif 'b' in entree:
^I^Icas11 = True
    ^Iprint('a et b')

```

Ce qu'Alice voit (Emacs, tab=8) :

```python
if 'a' in entree:
        if 'b' in entree:
                cas11 = True
            print('a et b')    # Incohérent !

```

**Solution :**

- Configurez votre éditeur pour convertir les tabulations en espaces
- Vous pouvez utiliser la touche Tab, mais elle doit insérer des espaces, pas un caractère tabulation

### Règles d'indentation en Python

**Règle 1 :** Toutes les lignes d'un même bloc doivent avoir la même indentation

**Code légal (mais pas recommandé) :**

```python
if 'a' in entree:
  print('OUI')        # 2 espaces
else:
      print('NON')    # 6 espaces (bloc différent, OK)

```

**Code ILLÉGAL :**

```python
if 'a' in entree:
    if 'b' in entree:
        cas11 = True
      else:           # ERREUR : pas la même indentation que le if
        cas12 = True

```

Les lignes `if 'b'` et `else` font partie du même bloc logique, elles doivent donc avoir exactement la même indentation.

### Avantages de cette syntaxe

1. **Code toujours bien formaté** : l'indentation fait partie de la syntaxe
2. **Pas d'accolades à gérer** : une fois la dernière ligne écrite, c'est fini
3. **Lisibilité maximale** : la structure visuelle = structure logique
4. **Évite les erreurs** : impossible d'avoir un code mal indenté qui compile

Voici un résumé de ce document sur les bonnes pratiques de présentation de code Python :

### Règles sur les espaces

**Affectations et opérateurs**

```python
# ✅ BON
x = y + z

# ❌ MAUVAIS
x=y+z
x = y+z
x=y + z

```

→ Toujours espacer de manière homogène pour faciliter la lecture

**Définition de fonction**

```python
# ✅ BON
def foo(x, y, z):
    pass

# ❌ MAUVAIS
def foo (x, y, z):     # espace avant (
def foo(x,y,z):        # pas d'espace entre paramètres

```

**Appel de fonction**

```python
# ✅ BON
foo(x, y, z)

# ❌ MAUVAIS
foo (x,y,z)
foo(x,y,z)

```

**Note importante :** Ces règles sont des **conventions d'usage**, pas des règles syntaxiques. Le code "incorrect" fonctionnera, mais ne respecte pas les standards Python.

### Coupures de ligne

**1. Sans backslash (parenthèses non fermées)**

Quand une parenthèse `(`, un crochet `[` ou une accolade `{` n'est pas fermée, pas besoin de backslash :

```python
# Listes
valeurs = [
    1,
    2,
    3,
    5,
    7,
]

# Appels de fonction
x = un_nom_de_fonction_tres_long(
    argument1, argument2,
    argument3, argument4,
)

# Définitions de fonction
def pprint(
    object, stream=None, indent=1,
    width=80, depth=None
):
    pass

```

**Chaînes multi-lignes :**

```python
texte = """Les sanglots longs
Des violons
De l'automne"""

```

**2. Avec backslash `\` (quand nécessaire)**

Obligatoire quand aucune parenthèse n'est ouverte :

```python
if (issubclass(typ, list) and \
    condition_2 and \
    condition_3):
    faire_quelque_chose()

```

**Règle générale :**

- On **peut** toujours mettre un backslash, même quand ce n'est pas nécessaire
- Mais on l'**évite** car cela nuit à la lisibilité

### Autres recommandations PEP-008

**Indentation**

- Toujours **4 espaces** par niveau
- Jamais de tabulations

**Largeur des lignes**

- Maximum **79 caractères** par ligne
- Permet une meilleure lisibilité et facilite les comparaisons côte à côte

**Commentaires**

- Clairs et à jour
- En anglais si le code est destiné à être partagé internationalement

**Docstrings**

- Documentation des modules, fonctions et classes
- Utilise `"""triple quotes"""`

### Outils d'aide

Disponibles via `pip` sur https://pypi.python.org :

**`pep8`** (ou `pycodestyle`) : Vérifier la conformité

```bash
pip install pycodestyle
pycodestyle mon_fichier.py

```

**`autopep8`** : Corriger automatiquement

```bash
pip install autopep8
autopep8 --in-place mon_fichier.py

```

## Rôle de `pass`

L'instruction `pass` **ne fait absolument rien**. Elle sert de placeholder (espace réservé) là où la syntaxe Python exige un bloc de code, mais où on ne veut rien exécuter.

## Cas d'utilisation

### **1. Fonction vide**

Comparaison avec le langage C :

```c
/* C : fonction vide */
void foo() {}

```

En Python :

```python
# Python : fonction vide
def foo():
    pass

```

Sans `pass`, on aurait une erreur de syntaxe car Python attend un bloc indenté après les `:`.

### **2. Boucle vide (pratique)**

Exemple : dépiler une liste jusqu'à une valeur spécifique

```python
liste = list(range(10))
print('avant', liste)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# On retire des éléments jusqu'à tomber sur 5
while liste.pop() != 5:
    pass

print('après', liste)  # [0, 1, 2, 3, 4]

```

Le corps de la boucle est vide (seule la condition compte), donc on utilise `pass`.

### **3. If sans then (modification de code)**

**Situation initiale :**

```python
if condition:
    print("non")
else:
    print("bingo")

```

**Si on commente le print, syntaxe invalide :**

```python
# ❌ ERREUR de syntaxe
if condition:
#    print("non")
else:
    print("bingo")

```

**Solution avec pass :**

```python
# ✅ Correct
if condition:
#    print("non")
    pass
else:
    print("bingo")

```

Utile quand on veut minimiser l'impact d'une modification sans réécrire toute la logique.

### **4. Classe vide**

```python
class Foo:
    pass

foo = Foo()  # On peut créer une instance

```

Utile pour :

- Définir une structure de base qu'on complétera plus tard
- Créer des exceptions personnalisées simples
- Faire du prototypage rapide

### Pourquoi `pass` existe ?

**Contrainte syntaxique de Python :**

- Après un `:` (if, for, while, def, class...), Python **exige** un bloc indenté
- Un bloc ne peut pas être complètement vide
- `pass` satisfait cette exigence sans rien exécuter

### Alternatives modernes

Dans certains cas, on peut utiliser :

**`...` (Ellipsis)** - équivalent plus moderne :

```python
def foo():
    ...

class Bar:
    ...

```

Mais `pass` reste le standard et est plus explicite sur l'intention.