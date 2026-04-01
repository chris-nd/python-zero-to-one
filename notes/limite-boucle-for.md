# Boucles `for` : La règle de non-modification du sujet

## La règle d'or

**Il ne faut jamais modifier la structure (ajouter ou supprimer des éléments) de l'objet sur lequel on est en train d'itérer.**

---

## 1. Le problème : Instabilité de l'itérable

Si vous modifiez un objet (liste, ensemble, dictionnaire) pendant que vous le parcourez, Python perd le fil de l'itération.

### Cas A : L'erreur explicite (Ensembles/Dicts)

Python détecte souvent la modification et stoppe le programme avec une erreur.

```python
ensemble = {'marc', 'albert'}
for valeur in ensemble:
    if 'bert' not in valeur:
        ensemble.discard(valeur) 
# -> RuntimeError: Set changed size during iteration
```

### Cas B : Le comportement imprévisible (Listes)

Sur une liste, Python peut ne pas déclencher d'erreur mais produire un résultat aberrant ou une **boucle infinie**.

```python
# ATTENTION : Boucle infinie théorique
liste = [1, 2, 3]
for c in liste:
    if c == 3:
        liste.append(c) # On ajoute un élément, donc la boucle ne finit jamais
```

---

## 2. Solutions : Comment contourner la limite ?

### Solution 1 : La Compréhension (Recommandé)

Au lieu de modifier l'original, on crée un nouvel objet filtré. C'est la méthode la plus propre et la plus "Pythonique".

```python
ensemble = {'marc', 'albert'}
# On ne garde que ce qui nous intéresse
ensemble = {v for v in ensemble if 'bert' in v}
```

### Solution 2 : Itérer sur une copie (`shallow copy`)

Si vous devez absolument modifier l'objet original, faites la boucle sur une **copie** de l'objet. Ainsi, vous parcourez la copie pendant que vous 

```python
from copy import copy
ensemble = {'marc', 'albert'}

for valeur in copy(ensemble): # On itère sur la COPIE
    if 'bert' not in valeur:
        ensemble.discard(valeur) # On modifie l'ORIGINAL : OK !
```

---

## 3. Précision : Modification de contenu vs Structure

Il est crucial de distinguer la **structure** de l'itérable et le **contenu** de ses éléments.

- **Interdit :** Ajouter/Supprimer des éléments de la liste elle-même.
- **Autorisé :** Modifier un objet à l'intérieur de la liste (ex: ajouter une valeur à une sous-liste).

```python
# CECI EST VALIDE
liste = [[1], [2], [3]]
for sous_liste in liste:
    sous_liste.append(100) # On modifie l'objet CONTENU, pas la liste elle-même.
```

## Synthèse : Pourquoi est-ce si strict ?

1. **Difficulté sémantique :** Si on supprime l'élément 8 pendant qu'on traite l'élément 5, est-ce que le 9 devient le nouveau 8 ? Le comportement devient vite ambigu.
2. **Difficulté d'implémentation :** Pour des raisons de performance, l'itérateur de Python suit des adresses mémoire. Si la taille change, l'itérateur peut sauter des éléments ou pointer vers du vide.