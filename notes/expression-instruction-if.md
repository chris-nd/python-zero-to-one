## Expression conditionnelle (`if` ternaire)

### Expressions vs Instructions

**Deux familles de constructions Python :**

**1. Expressions**

- Retournent une **valeur**
- Peuvent être combinées entre elles
- **Test simple :** Peut-on l'utiliser à droite d'un `=` ?

```python
# Exemples d'expressions
x = 5 + 3        # 5 + 3 est une expression
y = max(1, 2)    # max(1, 2) est une expression
z = a * b + c    # toute cette partie droite est une expression
```

**2. Instructions**

- N'ont **pas** de valeur de retour
- Contrôlent le flux d'exécution
- Ne peuvent pas être combinées

```python
# Exemples d'instructions
if x > 0:        # if est une instruction
    print(x)
y = 10          # affectation est une instruction
```

### Problème : `if` classique est une instruction

**Le `if` traditionnel ne peut pas être utilisé dans une expression :**

```python
x = True

# ❌ On doit écrire ceci (verbeux)
if x:
    y = 12
else:
    y = 35

print(y)  # → 12
```

**Problème :** 4 lignes pour une simple affectation conditionnelle !

### Solution : Expression conditionnelle (if ternaire)

**Syntaxe :**

```python
<résultat_si_vrai> if <condition> else <résultat_si_faux>
```

**Exemple simple :**

```python
x = True
y = 12 if x else 35
print(y)  # → 12
```

**Équivalent en une ligne !**

### Comparaison : If classique vs Expression conditionnelle

**Situation :** Affecter une valeur selon condition

**Méthode 1 : If classique (instruction)**

```python
if score >= 50:
    resultat = "Réussi"
else:
    resultat = "Échoué"
```

**Méthode 2 : Expression conditionnelle**

```python
resultat = "Réussi" if score >= 50 else "Échoué"
```

**Avantages expression conditionnelle :**

- ✅ Plus concis
- ✅ Plus fonctionnel
- ✅ Peut être utilisé dans expressions plus complexes

### Imbrications (nesting)

**Puisque c'est une expression, on peut l'imbriquer :**

**Exemple : Classifier une valeur**

```python
x = 5

# Calculer :
# -1 si x < -10
#  0 si -10 <= x <= 10
#  1 si x > 10

# ✅ AVEC parenthèses (recommandé)
valeur = -1 if x < -10 else (0 if x <= 10 else 1)
print(valeur)  # → 0
```

**Variante SANS parenthèses (déconseillé) :**

```python
# ⚠️ Ambigu, difficile à lire
valeur = -1 if x < -10 else 0 if x <= 10 else 1
```

**Recommandation :** Toujours **parenthéser** les imbrications pour de la clarté !