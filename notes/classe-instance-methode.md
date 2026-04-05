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