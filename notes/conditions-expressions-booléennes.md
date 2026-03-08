## Conditions & Expressions Booléennes

### Instructions conditionnelles

**Syntaxe de base :**

```python
if <expression>:
    <do_something>
```

**Important :** L'expression n'a pas besoin d'être un booléen !

### Valeurs considérées comme **fausses** (Falsy)

**Python évalue comme `False` :**

| Type | Valeur Falsy | Exemple |
| --- | --- | --- |
| **Nombres** | `0`, `0.0`, `0j` | `if 0:` → False |
| **Chaînes** | `""` (vide) | `if "":` → False |
| **Listes** | `[]` (vide) | `if []:` → False |
| **Tuples** | `()` (vide) | `if ():` → False |
| **Dicts** | `{}` (vide) | `if {}:` → False |
| **Sets** | `set()` (vide) | `if set():` → False |
| **None** | `None` | `if None:` → False |

**Exemples :**

```python
# Valeurs fausses
if 3 - 3:  # 0
    print("ne passera pas par là")

if "":  # chaîne vide
    print("ne passera pas par là")

if []:  # liste vide
    print("ne passera pas par là")

if None:  # None
    print("ne passera pas par là")
```

### Piège avec les flottants

```python
# Attention : différent de 0 à cause de la précision flottante
if 0.1 + 0.2 - 0.3:
    print("par contre on passe ici")  # True (petit nombre non-zéro)
```

### Valeurs considérées comme **vraies** (Truthy)

**Tout le reste est évalué comme `True` :**

```python
if 1:           # True
if "texte":     # True
if [1, 2]:      # True
if {'a': 1}:    # True
```

**Règle générale :**

- Collections **non vides** → True
- Nombres **différents de 0** → True
- Tout objet sauf `None` et les valeurs falsy → True

### Opérateurs d'égalité

**Égalité (`==`) et inégalité (`!=`) :**

```python
bas = 12
haut = 25.82

# Égalité
if bas == haut:
    print('==')

# Non-égalité
if bas != haut:
    print('!=')  # → Affiche !=
```

### Égalité entre types différents

**Règle générale : types différents ≠ égaux**

```python
# Liste vs Tuple : jamais égaux
if [1, 2] != (1, 2):
    print('!=')  # → Affiche !=
```

**Exception : types numériques**

```python
# int, float et complex peuvent être égaux
bas = 12
bas_reel = 12.0

if bas == bas_reel:
    print('int == float')  # → True

if (12 + 0j) == 12:
    print('int == complex')  # → True
```

### Opérateurs de comparaison

**Opérateurs classiques :**

```python
bas = 12
haut = 25.82

if bas <= haut:  # Inférieur ou égal
    print('<=')

if bas < haut:   # Strictement inférieur
    print('<')

if haut >= bas:  # Supérieur ou égal
    print('>=')

if haut > bas:   # Strictement supérieur
    print('>')
```

### Comparaisons chaînées (feature Python)

**Syntaxe élégante pour intervalles :**

```python
x = (bas + haut) / 2

# Deux tests en une expression !
if bas <= x <= haut:
    print("dans l'intervalle")

# Équivalent à (mais plus lisible que) :
if bas <= x and x <= haut:
    print("dans l'intervalle")
```

**Autres exemples :**

```python
if 1 < x < 10:
    print("x entre 1 et 10")

if a == b == c:
    print("Tous égaux")
```

### Comparaisons sur autres types

**Listes :**

```python
# Comparaison lexicographique
[1, 2] <= [2, 3]  # → True
```

**Sets (ensembles) :**

```python
# <= signifie "sous-ensemble"
{1, 2} <= {1, 2, 3}  # → True
```

### Attention : Nombres complexes

**Les complexes ne peuvent PAS être comparés avec `<`, `>`, `<=`, `>=` :**

```python
try:
    2j <= 3j
except TypeError as e:
    print("OOPS", e)
    # → TypeError: '<=' not supported between complex
```

**Seuls `==` et `!=` fonctionnent avec les complexes.**

### Connecteurs logiques

**Trois opérateurs : `and`, `or`, `not`**

```python
# AND : vrai si les deux conditions sont vraies
if x > 0 and x < 10:
    print("x entre 0 et 10")

# OR : vrai si au moins une condition est vraie
if x < 0 or x > 10:
    print("x hors de [0, 10]")

# NOT : inverse la condition
if not x == 0:
    print("x différent de 0")
```

### Priorité des opérateurs

**Ordre de priorité (du plus fort au plus faible) :**

1. **`not`** (le plus fort)
2. **`and`**
3. **`or`** (le plus faible)

**Exemple problématique (sans parenthèses) :**

```python
# ❌ Difficile à lire, priorités implicites
if 12 <= 25. or [1, 2] <= [2, 3] and not 12 <= 32:
    print("OK mais pourrait être mieux")
```

**Avec parenthèses (recommandé) :**

```python
# ✅ Clair et lisible
if 12 <= 25. or ([1, 2] <= [2, 3] and not 12 <= 32):
    print("OK, c'est équivalent et plus clair")

# ⚠️ Attention : parenthésage différent = sens différent !
if (12 <= 25. or [1, 2] <= [2, 3]) and not 12 <= 32:
    print("ce n'est pas équivalent")
```

## Évaluation des tests (lazy evaluation)

### Principe : Évaluation paresseuse

**Règle fondamentale :** Python évalue les conditions **jusqu'à obtenir un résultat vrai**, puis s'arrête.

**Exemple :**

```python
s = 'berlin'
if 'a' in s:
    print('avec a')
elif 'b' in s:
    print('avec b')          # ← Exécuté
elif 'c' in s:              # ← NON évalué !
    print('avec c')
else:
    print('sans a ni b ni c')
```

**Dans cet exemple :**

1. `'a' in s` → évalué → False
2. `'b' in s` → évalué → **True** → exécute le bloc
3. `'c' in s` → **NON évalué** (on a déjà trouvé une condition vraie)

**En termes savants :** **Évaluation paresseuse** (lazy evaluation)

### Pourquoi c'est important ?

**Deux raisons principales :**

**1. Performance**

- Évite d'évaluer des tests coûteux inutilement
- Permet d'optimiser l'ordre des tests

**2. Effets de bord**

- Certains tests peuvent **modifier des objets**
- Important de savoir quels tests sont réellement exécutés

### Effets de bord dans les conditions

**Rappel : méthode `pop()`**

```python
liste = ['premier', 'deuxieme', 'troisieme']
print(liste)  # → ['premier', 'deuxieme', 'troisieme']

element = liste.pop(0)  # Retire ET retourne le 1er élément
print(element)  # → 'premier'
print(liste)    # → ['deuxieme', 'troisieme'] (modifiée !)
```

**`pop()` a un effet de bord :** Elle **modifie** la liste en retirant un élément.

### Exemple avec effets de bord - Cas 1

**Entrée où première condition est vraie :**

```python
liste = list(range(5))  # [0, 1, 2, 3, 4]
print('liste en entree:', liste, 'de taille', len(liste))

if liste.pop(0) <= 0:     # pop() retourne 0, condition vraie
    print('cas 1')         # ← Exécuté
elif liste.pop(0) <= 1:   # ← NON évalué !
    print('cas 2')
elif liste.pop(0) <= 2:   # ← NON évalué !
    print('cas 3')
else:
    print('cas 4')

print('liste en sortie de taille', len(liste))
# → Taille = 4 (un seul pop() exécuté)
```

**Résultat :**

- `pop()` exécuté **1 fois** seulement
- Liste raccourcie de **1 élément**

### Exemple avec effets de bord - Cas 2

**Entrée où aucune condition n'est vraie :**

```python
liste = list(range(5, 10))  # [5, 6, 7, 8, 9]
print('en entree: liste=', liste, 'de taille', len(liste))

if liste.pop(0) <= 0:     # pop() retourne 5 → False
    print('cas 1')
elif liste.pop(0) <= 1:   # pop() retourne 6 → False
    print('cas 2')
elif liste.pop(0) <= 2:   # pop() retourne 7 → False
    print('cas 3')
else:
    print('cas 4')         # ← Exécuté

print('en sortie: liste=', liste, 'de taille', len(liste))
# → Taille = 6 (trois pop() exécutés)
```

**Résultat :**

- `pop()` exécuté **3 fois**
- Liste raccourcie de **3 éléments**

**Leçon :** Les effets de bord dépendent des valeurs testées !

### Court-circuit (Short-circuit) avec `and` et `or`

**Même logique avec opérateurs logiques :** Évaluation paresseuse.

**Fonctions de test :**

```python
def true():
    print('true')
    return True

def false():
    print('false')
    return False
```

### Short-circuit avec `and`

**Exemple 1 :**

```python
false() and true()
# Affiche : false
# Résultat : False
```

**Explication :**

1. Évalue `false()` → affiche "false", retourne False
2. **Ne évalue PAS `true()`** car premier terme est False
3. Résultat de `and` est forcément False

**Règle :** Avec `and`, si premier terme est False, second n'est pas évalué.

**Exemple 2 :**

```python
true() and false()
# Affiche : true
#           false
# Résultat : False
```

**Explication :**

1. Évalue `true()` → affiche "true", retourne True
2. **Doit évaluer `false()`** → affiche "false", retourne False
3. Résultat : True and False = False

### Short-circuit avec `or`

**Exemple 1 :**

```python
true() or false()
# Affiche : true
# Résultat : True
```

**Explication :**

1. Évalue `true()` → affiche "true", retourne True
2. **Ne évalue PAS `false()`** car premier terme est True
3. Résultat de `or` est forcément True

**Règle :** Avec `or`, si premier terme est True, second n'est pas évalué.

**Exemple 2 :**

```python
false() or true()
# Affiche : false
#           true
# Résultat : True
```

**Explication :**

1. Évalue `false()` → affiche "false", retourne False
2. **Doit évaluer `true()`** → affiche "true", retourne True
3. Résultat : False or True = True

## Résumé : Récapitulatif sur les conditions dans un `if`

### Toutes les expressions sont éligibles

**Règle :** On peut mettre **n'importe quelle expression** comme condition d'un `if`.

**Pas besoin de booléen explicite :**

```python
for n in (18, 19):
    # if n % 3: équivaut à if n % 3 != 0:
    if n % 3:
        print(f"{n} non divisible par trois")
    else:
        print(f"{n} divisible par trois")

# Résultat :
# 18 divisible par trois
# 19 non divisible par trois
```

### Qu'est-ce qui est considéré comme "vrai" ?

**Valeurs considérées comme FAUSSES (Falsy) :**

**1. Valeurs numériques nulles :**

- `0` (int)
- `0.0` (float)
- `0j` (complex)

**2. Objets vides :**

- `""` (chaîne vide)
- `[]` (liste vide)
- `()` (tuple vide)
- `{}` (dictionnaire vide)
- `set()` (ensemble vide)

**3. Valeur spéciale :**

- `None`

**Fonction `bool()` pour vérifier :**

```python
def show_bool(x):
    print(f"condition {repr(x):>10} considérée comme {bool(x)}")

for exp in [None, "", 'a', [], [1], (), (1, 2), {}, {'a': 1}, set(), {1}]:
    show_bool(exp)

# Résultat :
# condition       None considérée comme False
# condition         '' considérée comme False
# condition        'a' considérée comme True
# condition         [] considérée comme False
# condition        [1] considérée comme True
# condition         () considérée comme False
# condition     (1, 2) considérée comme True
# condition         {} considérée comme False
# condition  {'a': 1} considérée comme True
# condition     set() considérée comme False
# condition        {1} considérée comme True
```

### Exemples d'expressions comme conditions

**1. Référence à variable :**

```python
a = list(range(4))  # [0, 1, 2, 3]
print(a)

if a:  # Liste non vide → True
    print("a n'est pas vide")

if a[0]:  # a[0] = 0 → False
    print("on ne passe pas par ici")

if a[1]:  # a[1] = 1 → True
    print("a[1] n'est pas nul")
```

**2. Appels de fonction ou méthode :**

```python
chaine = "jean"

if chaine.upper():  # "JEAN" (non vide) → True
    print("la chaine mise en majuscule n'est pas vide")

# Fonction sans return retourne None
def procedure(a, b, c):
    pass

if procedure(1, 2, 3):  # None → False
    print("ne passe pas ici")
else:
    print("par contre on passe ici")
```

**3. Compréhensions :**

```python
inputs = [23, 65, 24]

# Y a-t-il au moins un nombre dont le carré finit par 5 ?
def condition(n):
    return (n * n) % 10 == 5

# Compréhension comme condition
if [value for value in inputs if condition(value)]:
    print("au moins une entrée convient")

# Résultat : [65] (65² = 4225) → True → affiche le message
```

**Pourquoi ça marche :**

- Si aucun élément ne convient : `[]` (vide) → False
- Si au moins un élément convient : `[...]` (non vide) → True

### Principaux opérateurs

**Tableau récapitulatif :**

| Famille | Opérateurs | Exemples |
| --- | --- | --- |
| **Égalité** | `==`, `!=`, `is`, `is not` | `a == b`, `x is None` |
| **Appartenance** | `in`, `not in` | `'a' in s`, `x not in liste` |
| **Comparaison** | `<`, `<=`, `>`, `>=` | `a < b`, `x >= 10` |
| **Logiques** | `and`, `or`, `not` | `a and b`, `not c` |

### Remarques importantes

**1. Opérateur `==` et types différents :**

```python
# Types différents généralement pas égaux
[] == ()         # → False (liste ≠ tuple)
[1, 2] == (1, 2) # → False

# Exception : types numériques
12 == 12.0       # → True (int == float)
```

---

**2. Priorité des opérateurs logiques :**

**Ordre de priorité (du plus fort au plus faible) :**

1. `not`
2. `and`
3. `or`

**Exemple :**

```python
# Sans parenthèses (déconseillé)
a and not b or c and d

# Équivalent à (selon priorités) :
(a and (not b)) or (c and d)
```

**Recommandation :** **Toujours parenthéser** pour clarté !

```python
# ✅ Clair et explicite
if (a and not b) or (c and d):
    pass
```

**3. Opérateurs logiques sur non-booléens :**

**Les opérateurs `and`/`or` fonctionnent sur n'importe quoi :**

```python
2 and [1, 2]           # → [1, 2]
None or "abcde"        # → "abcde"
```

**Règle d'évaluation paresseuse :**

- Retourne **le dernier élément évalué** si pas de court-circuit

```python
1 and 2 and 3                # → 3 (dernier évalué)
1 and 2 and 3 and '' and 4   # → '' (s'arrête à '')
[] or "" or {}               # → {} (dernier évalué)
[] or "" or {} or 4 or set() # → 4 (s'arrête à 4)
```

### Expression conditionnelle dans un if (à éviter !)

**Techniquement possible mais totalement illisible :**

```python
a = 1

# ❌ Franchement illisible (ne faites JAMAIS ça)
if 0 if not a else 2:
    print("une construction illisible")

# ❌ Encore pire !
if 0 if a else 3 if a + 1 else 2:
    print("encore pire")
```

**Message :** C'est **légal** mais **à proscrire absolument** !

### Types définis par l'utilisateur (avancé)

**Anticipation pour semaine 6 :**

Python permet de définir comment vos propres classes se comportent dans les conditions :

```python
# Exemple futur (semaine 6)
class MaClasse:
    def __bool__(self):
        # Définir quand l'objet est True/False
        return True

mon_objet = MaClasse()

if mon_objet:  # Utilisera __bool__()
    print("personnalisable")

for partie in mon_objet:  # Utilisera __iter__()
    # ...
```

**Note :** Détails en semaine 6 sur la programmation orientée objet.

### Bonnes pratiques résumées

**1. Utiliser expressions directement :**

```python
# ✅ Pythonique
if liste:
    pass

# ❌ Inutilement verbeux
if len(liste) > 0:
    pass
```

**2. Parenthéser les expressions complexes :**

```python
# ✅ Clair
if (a and b) or (c and d):
    pass

# ❌ Ambigu
if a and b or c and d:
    pass
```

**3. Utiliser `bool()` pour tester :**

```python
# Pour comprendre le comportement
print(bool(valeur))
```

**4. Tester avec `is None` :**

```python
# ✅ Recommandé
if x is None:
    pass

# ⚠️ Moins idiomatique
if x == None:
    pass
```