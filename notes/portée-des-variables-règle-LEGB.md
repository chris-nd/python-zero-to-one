```python
a, b, c = 1, 1, 1
def g():
     b, c = 2, 4
     b = b + 10
     def h():
         c = 5
         print(a, b, c)
     h()
g()
print(a, b, c)
import builtins
dir(builtins)
print(1)
print = 10
print(1)
x = 1
print = builtins.print
print(1)
```

# Portée des variables - Règle LEGB

## Qu'est-ce que LEGB ?

Lorsque Python cherche une variable, il suit un ordre précis appelé **LEGB** :

**L** - **Local** : Variables définies dans la fonction actuelle

**E** - **Enclosing** : Variables des fonctions englobantes (fonctions imbriquées)

**G** - **Global** : Variables définies au niveau du module/fichier

**B** - **Built-in** : Noms prédéfinis de Python (`len`, `open`, etc.)

## Ordre de recherche

Python cherche dans cet ordre : **L → E → G → B**

Il s'arrête dès qu'il trouve le nom et utilise la première occurrence.

## Exemple illustratif

```python
x = "global"          # G - Global

def externe():
    x = "enclosing"   # E - Enclosing

    def interne():
        x = "local"   # L - Local
        print(x)      # Affiche "local"

    interne()

externe()
```