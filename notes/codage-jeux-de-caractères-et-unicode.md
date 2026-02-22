# Caractères accentués

## Un caractère ≠ un octet

- Un ordinateur ne comprend que des **0 et des 1**.
- Un **caractère** (lettre, accent, symbole) est donc **codé** en nombres.
- Avant, on pensait :
    
    👉 *1 caractère = 1 octet*
    
- Aujourd’hui, avec **Unicode**, ce n’est **plus vrai**.

## En Python 3 : `str` et `bytes`

- **`str`** : sert à stocker du **texte lisible** (lettres, accents, emojis).
- **`bytes`** : sert à stocker des **données brutes** (fichiers, images…).

👉 Pour passer de l’un à l’autre :

- **encodage** : `str → bytes`
- **décodage** : `bytes → str`

⚠️ Pour que ça marche correctement, il faut **toujours connaître l’encodage**.

## UTF-8 : l’encodage à utiliser

- Il existe plusieurs encodages, mais **UTF-8 est le standard moderne**.
- En Python, il est **fortement conseillé d’utiliser UTF-8 partout**.
- Ne pas laisser l’ordinateur choisir tout seul.

👉 Règle simple :

**Quand tu vois “encoding”, mets UTF-8.**

## Accents en Python 3

- Python 3 gère **tous les caractères du monde** grâce à Unicode.
- Tu peux utiliser des accents :
    - ✅ dans les **chaînes de caractères** (textes affichés à l’utilisateur)
    - ✅ dans les **commentaires**
    - ⚠️ **pas recommandé** dans les **noms de variables**

👉 Bonne pratique :

- **Code** : en anglais, sans accents
- **Textes pour l’utilisateur** : avec accents

## Qu’est-ce qu’un encodage ?

- Un encodage est une **règle** qui dit :
    
    > “Quel nombre correspond à quel caractère ?”
    > 
- Exemple :
    - le caractère `A` → nombre 65
- Si on lit un fichier avec le **mauvais encodage**, les caractères deviennent faux (`€` → `¤`).

## Pourquoi les erreurs arrivent ?

- Si un fichier est écrit avec un encodage
- et lu avec un **autre encodage**
    
    👉 le texte devient illisible
    

💡 Sur le même ordinateur, ça marche souvent par hasard

💥 Sur un autre ordinateur, ça peut casser