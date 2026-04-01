# Contrôle des boucles : `break` et `continue`

## La question fondamentale

Comment modifier dynamiquement le comportement d'une boucle (`for` ou `while`) en fonction d'une condition rencontrée en cours de route ?

## 1. L'instruction `continue`

Permet de **sauter** l'itération actuelle pour passer immédiatement à la suivante.

- **Effet :** On abandonne le reste du bloc de code *dans* la boucle pour cette itération précise.
- **Résultat :** On reste **dans** la boucle.

## 2. L'instruction `break`

Permet d'**interrompre** et de quitter définitivement la boucle.

- **Effet :** On sort immédiatement de la structure de répétition, peu importe s'il restait des éléments à parcourir.
- **Résultat :** On passe à l'instruction qui suit la boucle.

## 3. Exemple combiné : Filtrage et Arrêt

Dans cet exemple, on parcourt une plage de nombres avec deux conditions de contrôle :

```python
for entier in range(1000):
    # 1. FILTRAGE : On ignore ce qui ne nous intéresse pas
    if entier % 10 != 0:
        continue  # On remonte directement au "for" suivant
    
    # Ce code n'est exécuté que si 'continue' n'a pas été activé
    print(f"On traite l'entier {entier}")
    
    # 2. ARRÊT : On définit une condition de sortie prématurée
    if entier >= 50:
        break     # On quitte la boucle définitivement

print("Fin de la boucle")
```

**Analyse du comportement :**

1. L'entier `1` ne passe pas le `if` → `continue` → on passe à `2`.
2. L'entier `10` passe le `if` → on affiche "On traite l'entier 10".
3. L'entier `50` passe le `if` → on affiche "On traite l'entier 50" → `break` → on sort de la boucle (on n'ira jamais jusqu'à 1000).

## Synthèse : Comparaison rapide

| **Instruction** | **Action** | **Destination** |
| --- | --- | --- |
| **`continue`** | "Saute ce tour-ci" | Retour au début de la boucle (itération suivante) |
| **`break`** | "J'arrête tout" | Sortie immédiate de la boucle |

## Pièges et bonnes pratiques

- **Utilisation abusive :** Trop de `break` et `continue` peuvent rendre le code difficile à lire (le fameux "code spaghetti"). Il est parfois préférable d'utiliser une condition plus précise dans le `while` ou le `if`.
- **Boucles imbriquées :** Attention, `break` et `continue` ne s'appliquent qu'à la boucle **la plus proche** (celle dans laquelle ils se trouvent directement). Ils ne font pas sortir de deux boucles à la fois.