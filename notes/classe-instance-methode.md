# Introduction aux Classes

## La question fondamentale

Comment créer nos propres types de données complexes pour structurer nos applications, au-delà des types natifs (`list`, `dict`, etc.) ?

## 1. Structure d'une classe : Le "moule"

Une classe est une définition qui permet de créer des objets (instances). Chaque instance possède ses propres données (attributs) et ses propres comportements (méthodes).

### Exemple : `Matrix2`

```python
class Matrix2:
    """Une implémentation sommaire de matrice 2x2"""

    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        # ... mémorisation des attributs
        
    def determinant(self):
        return self.a11 * self.a22 - self.a12 * self.a21
```

## 2. Concepts clés de l'initialisation

### La méthode `__init__` (Le Constructeur)

- C'est une **méthode spéciale** appelée automatiquement à la création d'un objet.
- Elle initialise l'instance.
- **Attention :** Le premier argument est toujours `self`. Lors de l'appel `Matrix2(...)`, Python passe l'objet tout juste créé en tant que `self`. Vous ne le passez pas explicitement dans les parenthèses.

### Le rôle de `self`

- `self` est une **convention**, mais une convention universelle en Python.
- Il représente l'instance actuelle. Il permet à l'objet de modifier ou d'accéder à ses propres données (`self.a11`).
- Contrairement à d'autres langages (comme `this` en C++ ou Java), en Python, `self` **doit être explicitement** mentionné dans la signature de la méthode.

## 3. Pourquoi utiliser la POO ? (Les 3 piliers)

1. **Encapsulation :** Vous cachez la logique interne dans des méthodes. Si vous changez la façon de stocker les données (ex: passer de 4 variables individuelles à un seul tuple), le code utilisateur reste inchangé.
2. **Résolution dynamique de méthode :** Python appelle la méthode spécifique à l'objet au moment de l'exécution. C'est ce qui permet à `print()` d'appeler automatiquement votre méthode `__repr__` si elle est définie.
3. **Héritage :** La capacité de créer une nouvelle classe à partir d'une classe existante pour en réutiliser ou en spécialiser le comportement.

## 4. Surcharge des méthodes spéciales

Vous pouvez modifier le comportement par défaut de Python en définissant des méthodes commençant et finissant par `__` :

- `__init__(self, ...)` : Initialisation.
- `__repr__(self)` : Détermine comment l'objet est représenté sous forme de chaîne de caractères (idéal pour le débogage et `print()`).

```python
# Grâce à __repr__, print(matrice) devient lisible :
def __repr__(self):
    return f"<<mat-2x2 {self.a}>>"
```

## Synthèse : Ce qu'il faut retenir

- **Une classe** = Le plan (le moule).
- **Une instance** = L'objet concret fabriqué avec ce plan.
- **`self`** = Le moyen pour l'objet de parler de lui-même.
- **Encapsulation** = On change l'intérieur sans casser l'extérieur.

## Définition d'une Classe et création d'une Instance

Une **classe** agit comme un modèle ou une "usine à instances". On la définit avec le mot-clé `class` et on crée une **instance** en appelant la classe comme une fonction.

```python
# Définition de la classe (le modèle)
class Phrase:
    ma_phrase = "je fais un mooc sur python"

# Création d'une instance (l'objet produit)
p = Phrase()
```

## Espaces de nommage et héritage dynamique

Chaque objet (classe ou instance) possède son propre **espace de nommage**, consultable avec la fonction `vars()`. Python utilise un **arbre d'héritage** : s'il ne trouve pas un attribut dans l'instance, il le cherche dans la classe.

```python
# L'instance p est créée vide au départ
print(vars(p)) # {}

# On peut ajouter un attribut à la classe après coup
Phrase.mots = Phrase.ma_phrase.split()

# L'instance y accède dynamiquement par héritage
print(p.mots) # ['je', 'fais', 'un', 'mooc', 'sur', 'python']
```

## Les Méthodes et le paramètre `self`

Les méthodes sont des fonctions définies dans la classe pour implémenter des **comportements**. Le premier argument, **`self`**, est crucial car il reçoit automatiquement la référence de l'instance qui appelle la méthode.

```python
class Phrase:
    def initia(self, texte):
        # self.ma_phrase crée un attribut spécifique à l'instance
        self.ma_phrase = texte

p = Phrase()
p.initia("Nouvelle phrase")
print(p.ma_phrase) # L'instance a maintenant son propre attribut
```

## Le mécanisme des "Bound Methods" (Méthodes liées)

Lorsqu'une méthode est appelée depuis une instance, Python la transforme en **méthode liée**, ce qui lui permet de passer l'instance comme premier argument de manière invisible.

Les deux écritures suivantes sont **totalement équivalentes** pour Python :

```python
# Appel classique via l'instance
p.initia("Bonjour")

# Ce que Python fait réellement en arrière-plan
Phrase.initia(p, "Bonjour")
```