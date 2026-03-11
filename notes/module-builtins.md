## Le module `builtins` en Python

C'est le module qui contient toutes les fonctions disponibles "par défaut" en Python sans import (`open`, `len`, `zip`, etc.). Python fait implicitement `from builtins import *` au démarrage.

**Points clés :**

- **On peut redéfinir un built-in** (ex: créer sa propre fonction `open`), mais c'est fortement déconseillé. Les bons éditeurs les signalent avec une couleur spécifique pour éviter les erreurs.
- **Les mots-clés, c'est différent** — `if`, `def`, `for`, `lambda`… eux, ne peuvent *pas* être redéfinis (SyntaxError immédiate).
- **Retrouver un built-in écrasé** : si on a redéfini `open` par exemple, on peut toujours récupérer l'original via :
    
    ```python
    import builtins
    builtins.open(...)
    # ou
    from builtins import open as builtins_open
    ```
    
- **Lister tous les built-ins** : `dir(builtins)` — on y trouve les fonctions *et* les exceptions (qui commencent par une majuscule et représentent une bonne partie de l'espace de noms).

**En résumé** : les built-ins sont pratiques mais fragiles — on peut les écraser par accident, contrairement aux mots-clés qui sont protégés par le langage lui-même.