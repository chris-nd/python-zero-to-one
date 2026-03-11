# Les fonctions `globals()` et `locals()` en Python

Les fonctions `globals()` et `locals()` permettent d'accéder à l'**environnement** d'exécution, c'est-à-dire aux variables visibles à un point donné du code.

## Concepts clés

### `globals()`

- Retourne un **dictionnaire** contenant toutes les variables définies au **niveau du module**
- Inclut tous les symboles du module (variables, fonctions, classes)
- S'applique au module où la fonction est **définie**, pas où elle est **appelée**

### `locals()`

- Retourne un **dictionnaire** des variables **locales** accessibles à ce point du code
- Change selon l'endroit où on l'appelle dans une fonction
- Inclut les paramètres et variables locales

## Exemples pratiques

### Exemple 1 : Visualiser l'environnement global

```python
# Variables globales
globale = "Je suis globale"

def ma_fonction():
    print(globals())
    # Affiche tous les symboles du module

ma_fonction()
```

### Exemple 2 : Variables locales

```python
def calcul(a, b):
    resultat = a + b
    print(locals())
    # Affiche: {'a': 10, 'b': 20, 'resultat': 30}
    return resultat

calcul(10, 20)
```

### Exemple 3 : Évolution de `locals()`

```python
def temoin(x):
    print("1. Au début:", locals())
    # {'x': 10}

    y = x * 2
    print("2. Après y:", locals())
    # {'x': 10, 'y': 20}

    z = y + 5
    print("3. Après z:", locals())
    # {'x': 10, 'y': 20, 'z': 25}
```

## Cas d'usage : Formatage de chaînes

### Note importante

Depuis Python 3.6, les **f-strings** sont la méthode recommandée. Les techniques ci-dessous sont devenues obsolètes mais restent utiles pour le code legacy.

### Avec `format()` et `locals()`

```python
def format_et_locals(nom, prenom, civilite, telephone):
    return "{civilite} {prenom} {nom} : Poste {telephone}".format(**locals())

format_et_locals('Dupont', 'Jean', 'Mr', '7748')
# → "Mr Jean Dupont : Poste 7748"
```

**Comment ça marche ?**

- `locals()` retourne `{'nom': 'Dupont', 'prenom': 'Jean', ...}`
- `*locals()` décompacte le dictionnaire en arguments nommés
- `format()` remplace les placeholders par les valeurs correspondantes

### Avec l'opérateur `%` (obsolète)

```python
def pourcent_et_locals(nom, prenom, civilite, telephone):
    return "%(civilite)s %(prenom)s %(nom)s : Poste %(telephone)s" % locals()

pourcent_et_locals('Dupont', 'Jean', 'Mr', '7748')
```

### ✅ Méthode moderne : f-strings (Python 3.6+)

```python
def avec_f_string(nom, prenom, civilite, telephone):
    return f"{civilite} {prenom} {nom} : Poste {telephone}"

avec_f_string('Dupont', 'Jean', 'Mr', '7748')
# Plus simple, plus lisible, plus performant !
```

## Points à retenir

| Fonction | Portée | Contenu | Usage |
| --- | --- | --- | --- |
| `globals()` | Module entier | Toutes les variables globales | Debugging, introspection |
| `locals()` | Fonction/bloc | Variables locales uniquement | Debugging, formatage |

### Bonnes pratiques

1. **Préférez les f-strings** pour le formatage de chaînes (Python 3.6+)
2. **Utilisez `globals()` et `locals()` principalement pour :**
    - Le debugging et l'introspection
    - Des outils de développement
    - Des cas très spécifiques d'injection de variables
3. **Évitez de modifier** directement ces dictionnaires (effets de bord complexes)

### Pièges courants

- `locals()` retourne une **copie** : modifier le dictionnaire ne change pas les variables
- `globals()` est **modifiable** mais c'est généralement une mauvaise idée
- La portée est toujours celle du **module de définition**, pas d'appel

## Cas d'usage réels

### Debugging avancé

```python
def debug_function():
    x = 10
    y = 20
    print("Variables locales:", locals())
    # Utile pour voir l'état complet sans print multiple
```

### Template dynamique

```python
def generer_message(**kwargs):
    # kwargs devient accessible via locals()
    template = "Bonjour {nom}, vous avez {nb_messages} messages"
    return template.format(**kwargs)

generer_message(nom="Alice", nb_messages=5)
```
