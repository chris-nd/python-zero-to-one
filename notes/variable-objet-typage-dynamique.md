## Les Noms de Variables

Imagine que les variables sont comme des **boîtes avec des étiquettes** où tu ranges tes affaires. L'étiquette, c'est le nom de ta variable !

Voici les règles pour nommer tes boîtes :

### ✅ Autorisé :

```python
age = 12                 # lettres minuscules
age_moyen = 13           # avec tiret du bas _
classe_6eme = "A"        # chiffres (mais pas au début!)

```

### ❌ Interdit :

```python
6eme_classe = "A"        # ❌ Ne commence JAMAIS par un chiffre
age-moyen = 13           # ❌ Pas de tiret normal -
mon age = 13             # ❌ Pas d'espace
__special__ = 10         # ❌ Réservé à Python

```

### 📌 Conseils :

- **Utilise les minuscules** pour les variables simples
- **Sépare les mots** avec `_` : `mon_age` plutôt que `monage`
- **Choisis des noms clairs** : `age` plutôt que `a`
- **Évite les accents** : `eleve` plutôt que `élève`

Choisis des noms **clairs et simples** pour que toi (et les autres) puissiez comprendre facilement ce qu'il y a dans chaque boîte ! 📦

## Les Mots-Clés de Python

### C'est quoi un mot-clé ?

Les **mots-clés** sont des mots **réservés par Python** pour des instructions spéciales. Tu **ne peux pas** les utiliser comme noms de variables.

### Exemple :

```python
if age <= 10:
    print("Tu es jeune")
else:
    print("Tu es plus grand")

```

Ici, `if` et `else` sont des mots-clés. Tu ne peux donc **PAS** faire :

```python
if = 12  # ❌ INTERDIT ! "if" est réservé par Python

```

### 📋 Liste des principaux mots-clés :

```python
if      else      for       while     def
True    False     None      and       or
not     in        is        return    break
continue pass     import    class     try
except  finally   with      as        from

```

## Types de données

les **types de données** décrivent la nature des valeurs que tu peux manipuler. Python est **dynamiquement typé** : tu n’as pas besoin de déclarer le type, il est déduit automatiquement.

## Types numériques

### `int` — nombres entiers

```python
x = 10
y = -3
```

### `float` — nombres décimaux

```python
pi = 3.14
```

### `complex` — nombres complexes

```python
z = 2 + 3j
```

## Type texte

### `str` — chaînes de caractères

```python
nom = "Python"
message = 'Bonjour'
```

📌 Les chaînes sont **immutables** (non modifiables).

## Type booléen

### `bool` — vrai ou faux

```python
is_valid = True
is_empty = False
```

## Types de collections

### `list` — liste (modifiable)

```python
fruits = ["pomme", "banane", "orange"]
```

### `tuple` — tuple (non modifiable)

```python
coord = (10, 20)
```

### `set` — ensemble (valeurs uniques)

```python
nombres = {1, 2, 3}
```

### `dict` — dictionnaire (clé → valeur)

```python
personne = {
    "nom": "Jean",
    "age": 30
}
```

## Type nul

### `NoneType`

```python
resultat = None
```

Représente **l’absence de valeur**.

## Types binaires

### `bytes`

```python
data = b"abc"
```

### `bytearray` (modifiable)

```python
data = bytearray(5)
```

### `memoryview`

```python
m = memoryview(bytes(5))
```

## Types avancés (orienté objet)

### Classes et objets

```python
class Voiture:
    pass

v = Voiture()
```

## La Gestion de la Mémoire

Imagine que tu gères une bibliothèque avec des livres (les données de ton programme).

### Dans les langages de bas niveau (comme C ou C++)

C'est comme si **tu devais faire tout le travail toi-même** :

1. **Réserver une étagère** : Quand tu veux ranger un nouveau livre, tu dois d'abord demander au bibliothécaire : "Est-ce que je peux avoir une étagère ?" (c'est `malloc` ou `new`)
2. **Ranger le livre** : Tu poses ton livre sur l'étagère
3. **Libérer l'étagère** : Quand tu n'as plus besoin du livre, tu dois penser à dire au bibliothécaire : "Tu peux reprendre cette étagère" (c'est `free` ou `delete`)

**Le problème ?**

- Si tu **oublies de rendre l'étagère**, la bibliothèque se remplit et il n'y a plus de place !
- Si tu **utilises une étagère que tu n'as pas demandée**, c'est le bazar et ça peut créer de gros problèmes !

### Dans les langages de haut niveau (comme Python)

C'est comme si **tu avais un assistant magique** qui fait tout à ta place !

- Tu poses simplement ton livre quelque part
- L'assistant surveille tous les livres
- Quand il voit qu'un livre n'est plus utilisé par personne, il le range automatiquement

**En Python :**

```python
message = "Bonjour !"  # Tu crées ton objet
# Python s'occupe de tout le reste automatiquement !

```

### Le petit « prix à payer »

Python utilise un peu plus de place parce que chaque objet contient des **informations supplémentaires** (comme une étiquette qui dit "je suis un texte" ou "3 personnes m'utilisent"). 

C'est comme si chaque livre avait une fiche collée dessus avec des infos - ça prend un peu plus de place, mais c'est beaucoup plus pratique !

## **Typages statique et dynamique**

### Typage statique (comme C ou C++)

Imagine que tu dois étiqueter chaque boîte dans ta chambre en disant ce qu'elle contient AVANT d'y mettre quoi que ce soit. Par exemple :

- Une boîte marquée "jouets" ne peut contenir QUE des jouets
- Une boîte marquée "livres" ne peut contenir QUE des livres

C'est pareil en programmation : chaque variable doit avoir un type défini à l'avance. Si tu essaies de mettre le mauvais type de donnée, le programme refuse même de démarrer.

**Avantage** : L'ordinateur peut vérifier les erreurs AVANT que le programme démarre (**Type checking ou vérification de type**).

**Inconvénient** : C'est plus de travail pour le programmeur.

### Typage dynamique (comme Python)

Avec Python, c'est différent : tu n'as pas besoin d'étiqueter tes boîtes à l'avance. Tu peux mettre ce que tu veux dedans, et Python s'adapte automatiquement.

Python suit la règle du "duck typing" : "Si ça ressemble à un canard et que ça fait coin-coin comme un canard, c'est un canard". En d'autres termes, peu importe le type exact, tant que ça fonctionne !

**Avantage** : C'est beaucoup plus rapide et simple à écrire.

**Inconvénient** : Les erreurs de type sont découvertes seulement quand le programme tourne.

## La fonction `type()`

Pour connaître **le type** d'une variable, utilise la fonction `type()` :

```python
type(15)           # → int (nombre entier)
type("bonjour")    # → str (texte)
type(3.14)         # → float (nombre décimal)
```

### Important : Le type est attaché à l'objet, pas à la variable !

Une **même variable** peut changer de type :

```python
x = 10          # x contient un nombre
type(x)         # → int

x = "salut"     # maintenant x contient du texte
type(x)         # → str
```

## La fonction `isinstance()`

Pour **vérifier** si une variable est d'un certain type :

```python
isinstance(23, int)        # → True (23 est bien un entier)
isinstance("hello", int)   # → False ("hello" n'est pas un entier)
```

**Pourquoi c'est utile ?** Parce que Python ne vérifie pas automatiquement les types. Tu peux vérifier toi-même qu'une variable contient bien ce que tu attends !