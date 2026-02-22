## Les méthodes principales sur les chaînes

### **Découpage et assemblage**

- `split()` : découpe une chaîne selon un séparateur et retourne une liste
- `join()` : reconstruit une chaîne à partir d'une liste avec un séparateur

### **Remplacement**

- `replace()` : remplace une sous-chaîne par une autre, avec possibilité de limiter le nombre de remplacements

### **Nettoyage**

- `strip()` : supprime les espaces, tabulations et retours à la ligne au début et à la fin d'une chaîne

### **Recherche de sous-chaînes**

- `find()` :  l'index de la première occurrence (ou -1 si absent)
- `rfind()` : comme find() mais en partant de la fin
- `index()` : comme find() mais lève une exception si absent
- `in` : teste simplement la présence d'une sous-chaîne
- `count()` : compte le nombre d'occurrences
- `startswith()` / `endswith()` : vérifient si la chaîne commence/finit par une sous-chaîne

### **Changement de casse**

- `upper()`, `lower()`, `swapcase()`, `capitalize()`, `title()` : diverses transformations majuscules/minuscules

Il est utile de consulter régulièrement la documentation (`help(str)`) car ces méthodes ont souvent des options supplémentaires.

## Formatage de chaînes en Python

### **La fonction `print()`**

- Affiche des valeurs en insérant automatiquement des espaces entre elles
- Ajoute un saut de ligne par défaut (modifiable avec `end=`)
- Peut imprimer n'importe quel type d'objet
- Limites : peu de contrôle sur la présentation finale

### **Les f-strings (recommandé depuis Python 3.6)**

- Syntaxe simple : commence par `f"..."`
- Les expressions entre `{}` sont évaluées et insérées dans la chaîne
- Permet d'effectuer des calculs et appels de fonctions directement : `f"dans 10 ans {age + 10} ans"`
- Formats avancés possibles avec `:` : `f"{pi:.2f}"` (2 décimales)

### **La méthode `format()` (avant les f-strings)**

- Syntaxe : `"texte {} {}".format(valeur1, valeur2)`
- Liaison par position : `"{1} {0}".format(a, b)`
- Liaison par nom : `"{nom} {prenom}".format(nom=n, prenom=p)`

### **L'opérateur `%` (obsolète)**

- Ancienne méthode, encore présente dans du vieux code
- Syntaxe : `"%s %s" % (val1, val2)`
- À ne plus utiliser dans du code moderne

### **Formats avancés** (avec f-strings ou format)

- Arrondis : `{valeur:.2f}` (2 chiffres après la virgule)
- Zéros de remplissage : `{x:04d}` (4 caractères avec des 0 à gauche)
- Largeur fixe : `{texte:<10}` (gauche), `{texte:^10}` (centre), `{texte:>10}` (droite)

Utiliser les f-strings pour du code moderne, c'est le plus simple et expressif.

## **Complément - niveau basique**

Occasionnellement, il peut être utile de poser une question à l'utilisateur.

### **La fonction `input`**

C'est le propos de la fonction `input`. Par exemple :

```python
nom_ville = "Nancy"`

nom_ville = input("Entrez le nom de la ville : ")

print(f"nom_ville={nom_ville}")
```

### **Attention à bien vérifier/convertir**

Notez bien que `input` renvoie **toujours une chaîne de caractères** (`str`). C'est assez évident, mais il est très facile de l'oublier et de passer cette chaîne directement à une fonction qui s'attend à recevoir, par exemple, un nombre entier, auquel cas les choses se passent mal :

```python
>>> input("nombre de lignes ? ") + 3
nombre de lignes ? 12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

Dans ce cas il faut appeler la fonction `int` pour convertir le résultat en un entier :

```python
int(input("Nombre de lignes ? ")) + 3
```

### **Limitations**

Cette fonction peut être utile pour vos premiers pas en Python.

En pratique toutefois, on utilise assez peu cette fonction, car les applications "réelles" viennent avec leur propre interface utilisateur, souvent graphique, et disposent donc d'autres moyens que celui-ci pour interagir avec l'utilisateur.

Les applications destinées à fonctionner dans un terminal, quant à elles, reçoivent traditionnellement leurs données de la ligne de commande. C'est le propos du module `argparse` que nous avons déjà rencontré en première semaine.

## Expressions régulières (module `re`)

**Concept de base**
Les expressions régulières (regex/regexp) permettent de décrire et filtrer des ensembles de textes ayant des propriétés communes. En Python, elles sont disponibles via le module `re`.

**Utilisation simple**

```python
import re
regexp = r"(.*)-(.*)\.txt"  # raw-string avec r
match = re.match(regexp, "abc-def.txt")

```

**Fonctions principales**

- `match()` : cherche au début de la chaîne
- `search()` : cherche n'importe où dans la chaîne
- `findall()` : trouve toutes les occurrences
- `split()` : découpe selon un pattern
- `sub()` : remplace les occurrences

**Syntaxe des patterns**

- `.` : n'importe quel caractère
- `\w` : caractère alphanumérique, `\W` : non-alphanumérique
- `\d` : chiffre, `\s` : espace/tabulation
- `[abc]` : ensemble de caractères, `[a-z]` : intervalle
- `[^abc]` : négation (tout sauf abc)
- `^` ou `\A` : début de chaîne, `$` ou `\Z` : fin de chaîne

**Répétitions**

- : 0 ou plusieurs occurrences
- `+` : 1 ou plusieurs occurrences
- `?` : 0 ou 1 occurrence
- `{n}` : exactement n occurrences
- `{m,n}` : entre m et n occurrences

**Groupes**

- `(...)` : groupe anonyme
- `(?P<name>...)` : groupe nommé
- `(?P=name)` : référence à un groupe précédent
- Accès : `match.group(1)` ou `match.group('name')`

**Bonnes pratiques**

- Utiliser des **raw-strings** (`r"..."`) pour éviter d'échapper les backslashes
- **Compiler** une fois avec `re.compile()` si réutilisation fréquente
- Flags utiles : `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`

**Greedy vs non-greedy**

- Par défaut : greedy (séquence la plus longue)
- `?`, `+?`, `??` : versions non-greedy (séquence la plus courte)

Les regex sont puissantes mais exigeantes à maîtriser. Sites recommandés pour tester : pythex.org, regex101.com.

## Exercices sur les expressions régulières

### **Exercice 1 : Identificateurs Python**

```python
regexp_pythonid = r"[a-zA-Z_][a-zA-Z0-9_]*\Z"

```

- `[a-zA-Z_]` : commence par une lettre ou underscore
- `[a-zA-Z0-9_]*` : suivi de 0 ou plusieurs lettres, chiffres ou underscores
- `\Z` : fin de chaîne

### **Exercice 2 : Nom et prénom**

```python
regexp_agenda = r"(?P<prenom>[\w-]*):(?P<nom>[\w-]+):?\Z"

```

- `(?P<prenom>[\w-]*)` : prénom (peut être vide), caractères alphanumériques ou tirets
- `:` : séparateur obligatoire
- `(?P<nom>[\w-]+)` : nom (non vide, au moins un caractère)
- `:?` : deuxième deux-points optionnel
- `\Z` : fin de chaîne

### **Exercice 3 : Numéros de téléphone**

```python
regexp_phone = r"(?:0(?P<number>\d{9})|(?:\+33)(?P<number2>\d{9}))\Z"

```

Ou plus simplement avec un seul groupe :

```python
regexp_phone = r"(?:0|\+33)(?P<number>\d{9})\Z"

```

- `(?:0|\+33)` : commence par 0 OU +33 (groupe non capturant)
- `(?P<number>\d{9})` : capture les 9 chiffres significatifs
- `\Z` : fin de chaîne

### **Exercice 4 : URL (avancé)**

```python
regexp_url = r"(?i)(?P<proto>https?|ftp|ssh)://(?:(?P<user>\w+)(?::(?P<password>[^:]+))?@)?(?P<hostname>[\w.]+)(?::(?P<port>\d+))?/(?P<path>.*)\Z"

```

Décomposition :

- `(?i)` : insensible à la casse
- `(?P<proto>https?|ftp|ssh)` : protocole (https? = http ou https)
- `://` : séparateur obligatoire
- `(?:(?P<user>\w+)(?::(?P<password>[^:]+))?@)?` : user optionnel avec password optionnel
- `(?P<hostname>[\w.]+)` : hostname obligatoire
- `(?::(?P<port>\d+))?` : port optionnel
- `/(?P<path>.*)` : path (peut être vide)
- `\Z` : fin de chaîne

Ces solutions respectent toutes les contraintes énoncées dans les exercices !