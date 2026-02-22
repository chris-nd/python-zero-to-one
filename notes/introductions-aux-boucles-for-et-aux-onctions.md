## Deux styles de programmation

### **1. Style procédural (sans retour explicite)**

Une procédure exécute des instructions sans retourner de valeur utile :

```python
def affiche_carre(n):
    print("le carre de", n, "vaut", n*n)

affiche_carre(12)  # Affiche mais ne retourne rien d'utile

```

### **2. Style fonctionnel (avec retour)**

Une fonction calcule et retourne une valeur :

```python
def carre(n):
    return n*n

surface = carre(15)  # Retourne 225
if carre(8) <= 100:
    print('petit appartement')

```

**Avantage du style fonctionnel :** La valeur peut être réutilisée, stockée, testée, etc.

## L'instruction `return`

**Comportement :**

- **Termine immédiatement** l'exécution de la fonction
- **Retourne** l'objet spécifié à l'appelant
- Peut être utilisée plusieurs fois dans une fonction (conditions différentes)

```python
def exemple(x):
    if x < 0:
        return "négatif"
    elif x == 0:
        return "zéro"
    else:
        return "positif"

```

### Le singleton `None`

**Règle fondamentale :** Toutes les fonctions Python retournent **quelque chose**.

Si aucun `return` n'est spécifié (ou `return` sans valeur), Python retourne automatiquement `None`.

```python
def affiche_carre(n):
    print("le carre de", n, "vaut", n*n)
    # pas de return explicite

retour = affiche_carre(15)
print('retour =', retour)  # → retour = None

```

**`None` est :**

- Un singleton prédéfini (comme `True` et `False`)
- **Pas** une valeur booléenne
- Utilisé pour signaler l'absence de valeur

### Exemple réaliste : tester si un nombre est premier

```python
def premier(n):
    """
    Retourne un booléen selon que n est premier ou non
    Retourne None pour les entrées négatives ou nulles
    """
    # Entrées invalides
    if n <= 0:
        return  # retourne None

    # Cas particulier
    elif n == 1:
        return False

    # Recherche d'un diviseur
    else:
        for i in range(2, n):
            if n % i == 0:
                return False  # Diviseur trouvé, pas premier

    # Aucun diviseur trouvé
    return True

```

**Test :**

```python
for test in [-2, 1, 2, 4, 19, 35]:
    print(f"premier({test:2d}) = {premier(test)}")

# Résultat :
# premier(-2) = None
# premier( 1) = False
# premier( 2) = True
# premier( 4) = False
# premier(19) = True
# premier(35) = False

```

### `return` interrompt la fonction

**Point clé :** Dès qu'un `return` est exécuté, la fonction s'arrête **immédiatement**.

Cela permet d'optimiser le code en évitant des `else` superflus :

**Version avec `else` :**

```python
def premier(n):
    if n <= 0:
        return
    elif n == 1:
        return False
    else:  # Ce else est nécessaire
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

```

**Version sans `else` (équivalente) :**

```python
def premier_sans_else(n):
    if n <= 0:
        return
    if n == 1:
        return False
    # Pas besoin de else: si on arrive ici,
    # c'est que les conditions précédentes sont fausses
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

```

Les deux versions sont **strictement équivalentes**. C'est une question de style.

### Bonnes pratiques

**1. Préférer le style fonctionnel**

```python
# ❌ Moins flexible
def affiche_resultat(x):
    print(x * 2)

# ✅ Plus flexible
def calcule_resultat(x):
    return x * 2

```

**2. `return` sans valeur pour signaler une erreur**

```python
def diviser(a, b):
    if b == 0:
        return  # ou return None
    return a / b

```

**3. Documenter ce que retourne la fonction**

```python
def ma_fonction(x):
    """
    Fait quelque chose avec x.

    Args:
        x: un nombre

    Returns:
        Le résultat du calcul, ou None si invalide
    """
    if x < 0:
        return None
    return x * 2

```

### Concaténation de chaînes

Python concatène automatiquement les chaînes littérales adjacentes :

```python
# Ces deux chaînes sont automatiquement concaténées
message = "abc" "def"
print(message)  # → "abcdef"

# Utile pour formatter du code long
long_message = (
    "Première partie "
    "Deuxième partie "
    "Troisième partie"
)

```

### Tableau récapitulatif

| Concept | Description | Exemple |
| --- | --- | --- |
| **Style procédural** | Exécute des actions, pas de retour utile | `def affiche(): print("ok")` |
| **Style fonctionnel** | Calcule et retourne une valeur | `def calcule(): return 42` |
| **`return valeur`** | Termine la fonction et retourne `valeur` | `return x * 2` |
| **`return`** | Termine la fonction et retourne `None` | `if erreur: return` |
| **`None`** | Valeur par défaut si pas de `return` | Singleton prédéfini |
| **Interruption** | `return` arrête immédiatement la fonction | Ignore le code suivant |