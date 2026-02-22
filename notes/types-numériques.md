## Les types numériques

| Types | Noms |
| --- | --- |
| `int` | Entier |
| `float` | Flottant / Décimal |
| `complex` | Complexe |
| `bool` | Booléen |

Les opérateurs arithmétiques pour effectuer des calculs mathématiques

| **code** | **opération** |
| --- | --- |
| `+` | Addition |
| `-` | Soustraction |
| `/` | Division |
| `//` | Division Entière |
| `%` | modulo |
| `**` | puissance |

Vous pouvez facilement faire aussi des calculs sur les complexes. Souvenez-vous seulement que la constante complexe que nous notons `i` se note `j` en Python:

```python
# multiplication de deux nombres complexes
(2 + 3j) * 2.5j
```

Aussi, pour entrer ce nombre complexe `j`, il faut toujours le faire précéder d'un nombre, donc ne pas entrer simplement `j` (qui serait compris comme un nom de variable) mais plutôt `1j` ou encore `1.j`, comme ceci : `1j * 1.j`

## **Conversions de types**

Il est parfois nécessaire de convertir une donnée d'un type dans un autre. 

| **Type** | **Fonction** |
| --- | --- |
| Entier | `int()` |
| Flottant | `float()` |
| Complexe | `complex()` |
| Booléen | `bool()` |

```python
# dans l'autre sens, si j'ai un entier
a = 2345

# je peux facilement le traduire en chaîne de caractères
str(2345) => "2345"

# ou en complexe
complex(2345) => 2345 + 0j
```

## **Grands nombres**

Comme les entiers sont de précision illimitée, on peut améliorer leur lisibilité en insérant des caractères `_` qui sont simplement ignorés à l'exécution.

```python
`tres_grand_nombre = 23_456_789_012_345

tres_grand_nombre`

`# ça marche aussi avec les flottants
123_456.789_012`
```

## **Entiers et bases**

En Python, on peut aussi entrer un entier sous forme binaire comme ceci :

```python
deux_cents = 0b11001000
print(deux_cents)
```

Ou encore sous forme octale (en base 8) comme ceci :

```python
deux_cents = 0o310
print(deux_cents)
```

Ou enfin encore en hexadécimal (base 16) comme ceci :

```python
deux_cents = 0xc8
print(deux_cents)
```

Pour d'autres bases, on peut utiliser la fonction de conversion `int` en lui passant un argument supplémentaire :

```python
deux_cents = int('3020', 4)
print(deux_cents)
```

## **Opérateurs d’affectation composée et Opérations (à la `+=`)**

### **Incrémentation**

On peut facilement augmenter la valeur d'une variable numérique comme ceci :

```python
entier = 10

entier += 2
print('entier', entier)
```

Comme on le devine peut-être, ceci est équivalent à :

```python
entier = 10

entier = entier + 2
print('entier', entier)
```

### **Autres opérateurs d’affectation composée**

Cette forme, qui combine opération sur une variable et réaffectation du résultat à la même variable, est disponible avec tous les opérateurs courants :

```python
entier -= 4
print('après décrément', entier)
entier *= 2
print('après doublement', entier)
entier /= 2
print('mis à moitié', entier)
```

### **Types non numériques**

En réalité cette construction est disponible sur tous les types qui supportent l'opérateur en question. Par exemple, les listes peuvent être additionnées entre elles :

```python
liste = [0, 3, 5]
print('liste', liste)

liste += ['a', 'b']
print('après ajout', liste)
```

Beaucoup de types supportent l'opérateur `+`, qui est sans doute de loin celui qui est le plus utilisé avec cette construction.

Signalons enfin que l'on trouve aussi cette construction avec d'autres opérateurs moins fréquents, par exemple :

```python
entier = 2
print('entier:', entier)
entier **= 10
print('à la puissance dix:', entier)
entier %= 5
print('modulo 5:', entier)
entier //= 2
print('le résultat de la division entière:', entier)
```

On peut même le faire avec des opérateurs de décalage, que nous verrons très bientôt :

```python
entier <<= 2
print('double décalage gauche:', entier)
```

## **Notions sur la précision des calculs flottants**

### **Le problème**

Comme pour les entiers, les calculs sur les flottants sont, naturellement, réalisés par le processeur. Cependant contrairement au cas des entiers où les calculs sont toujours exacts, les flottants posent un problème de précision. Cela n'est pas propre au langage Python, mais est dû à la technique de codage des nombres flottants sous forme binaire.

Voyons tout d'abord comment se matérialise le problème :

```python
0.2 + 0.4
```

Il faut retenir que lorsqu'on écrit un nombre flottant sous forme décimale, la valeur utilisée en mémoire pour représenter ce nombre ne représente **pas toujours exactement** le nombre entré.

```python
# du coup cette expression est fausse, à cause de l'erreur d'arrondi
0.3 - 0.1 == 0.2
```

De nouveau, ce problème n'est pas spécifique à Python, il existe pour tous les langages, et il est bien connu des numériciens.

Dans une grande majorité des cas, ces erreurs d'arrondi ne sont pas pénalisantes. Il faut toutefois en être conscient car cela peut expliquer des comportements curieux.

### **Une solution : penser en termes de nombres rationnels**

Tout d'abord si votre problème se pose bien en termes de nombres rationnels, il est alors tout à fait possible de le résoudre avec exactitude.

Alors qu'il n'est pas possible d'écrire exactement 3/10 en base 2, ni d'ailleurs 1/3 en base 10, on peut représenter **exactement** ces nombres dès lors qu'on les considère comme des fractions et qu'on les encode avec deux nombres entiers.

Python fournit en standard le module `fractions` qui permet de résoudre le problème.

```python
# on importe le module fractions, qui lui-même définit le symbole Fraction
from fractions import Fraction

# et cette fois, les calculs sont exacts, et l'expression retourne bien True
Fraction(3, 10) - Fraction(1, 10) == Fraction(2, 10)
```

Ou encore d'ailleurs, équivalent et plus lisible :

```python
Fraction('0.3') - Fraction('0.1') == Fraction('2/10')
```

### **Une autre solution : le module decimal**

Si par contre vous ne manipulez pas des nombres rationnels et que du coup la représentation sous forme de fractions ne peut pas convenir dans votre cas, il existe le module standard `decimal` qui offre des fonctionnalités très voisines du type `float`, tout en éliminant la plupart des inconvénients, au prix naturellement d'une consommation mémoire supérieure.

Pour reprendre l'exemple de départ, mais en utilisant le module decimal, on écrirait alors :

```python
from decimal import Decimal

Decimal('0.3') - Decimal('0.1') == Decimal('0.2')
```

## Les opérations bit à bit (bitwise)

### C’est quoi un bit ?

Un **bit**, c’est un petit interrupteur :

- **0** → éteint ❌
- **1** → allumé ✅

👉 Les nombres dans l’ordinateur sont écrits avec **des suites de 0 et de 1** (on appelle ça le **binaire**).

## Écrire un nombre en binaire

Par exemple :

- 49 = 32 + 16 + 1
- 81 = 64 + 16 + 1

👉 En binaire, ça devient une suite de 0 et de 1

## ET logique (`&`)

### Règle :

- **1 & 1 → 1**
- tous les autres cas → **0**

👉 C’est comme dire :

> les deux doivent être allumés pour que ça marche
> 

Exemple :

```python
49 & 81
```

➡️ Résultat : **17**

Pourquoi ?

- Les bits qui sont à **1 dans les deux nombres** restent à 1
- Les autres deviennent 0

## OU logique (`|`)

### Règle :

- **1 | 0 → 1**
- **0 | 1 → 1**
- **1 | 1 → 1**
- **0 | 0 → 0**

👉 C’est comme dire :

> au moins un des deux est allumé
> 

Exemple :

```python
49 | 81
```

➡️ Résultat : **113**

On garde **tous les bits allumés** dans l’un ou l’autre nombre.

## OU exclusif (`^`)

### Règle :

- **1 ^ 1 → 0**
- **0 ^ 0 → 0**
- **1 ^ 0 → 1**
- **0 ^ 1 → 1**

👉 Ça veut dire :

> un seul des deux, mais pas les deux en même temps
> 

C’est comme un interrupteur spécial ⚡

## Décalage à gauche (`<<`)

Décaler à gauche, c’est :

- **ajouter des 0 à droite**
- donc **multiplier par 2⁴**

Exemple :

```python
49 << 4
```

👉 C’est pareil que :

- multiplier par **2⁴ = 16, avec n=4**

➡️ Résultat : **784**

## Décalage à droite (`>>`)

Décaler à droite, c’est :

- **enlever des bits**
- donc **diviser par 2⁴, avec n=4**

Exemple :

```python
49 >> 4
```

👉 C’est comme :

- diviser par **16**

➡️ Résultat : **3**

## Astuce très pratique : `bin()`

Pour voir un nombre en binaire :

```python
bin(49)
```

➡️ Résultat :

```
0b110001
```

⚠️ Attention :

- c’est du **texte** (`str`), pas un nombre

## Écrire un nombre directement en binaire

```python
x = 0b110001
y = 49

x == y #True
```

👉 Python comprend que c’est un **nombre**

👉 Et ici, ça vaut bien **49**

## Les nombres flottants ont des limites

Un **flottant**, c’est un nombre avec une virgule :

- 1.5
- 0.0001
- 10.2

En Python, ce sont les nombres de type `float`.

👉 Problème : **l’ordinateur ne peut pas tout représenter**.

Il y a :

- un **plus petit nombre possible**
- un **plus grand nombre possible**

### Le plus petit flottant (très très petit)

Quand un nombre devient **trop petit**, Python :

👉 **ne sait plus le stocker**

👉 et le transforme en **0.0**

```python
1e-320   # fonctionne
1e-330   # devient 0.0 ❌

```

👉 Ça veut dire :

- `10⁻³²⁰` existe encore pour Python
- mais `10⁻³³⁰` est **trop petit**, donc Python dit :
    
    ➜ *« c’est zéro »*
    

🧠 Image :

> Imagine une goutte d’eau 💧
> 
> 
> Si elle devient trop petite… elle disparaît 👻
> 

### Comment trouver la limite ?

On essaie :

- des valeurs un peu plus petites
- jusqu’à ce que Python affiche **0.0**

👉 On s’approche petit à petit (comme un jeu de chaud/froid 🔥❄️)

### Le plus grand flottant (très très grand)

Même problème dans l’autre sens :

- si un nombre est **trop grand**
- Python **ne peut plus le représenter**

```python
10e450      # fonctionne → c’est un entier (int)
10e450.0    # erreur ❌ → Python essaie de faire un float

```

👉 Les **entiers (`int`) n’ont pas de limite**

👉 Les **flottants (`float`) ont une limite**

### Où est la limite ?

On observe que :

- `10e300.` fonctionne
- `10e310.` pose problème

👉 Donc le plus grand flottant est **quelque part entre 10³⁰⁰ et 10³¹⁰**

## Python connaît déjà ces limites

Python connaît exactement :

- le **plus petit**
- le **plus grand flottant**

```python
import sys
sys.float_info.min
sys.float_info.max
```

Mais :

- le **minimum observé à la main** peut sembler différent
- à cause de nombres spéciaux appelés **nombres dénormaux**