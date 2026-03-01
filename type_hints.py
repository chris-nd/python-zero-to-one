# pour typer une variable avec les type hints
nb_items : int = 0

print(type(nb_items))
print(isinstance(nb_items, int))

# une fonction factorielle avec des type hints
def fact(n : int) -> int:
    return 1 if n <= 1 else n * fact(n-1)

print(fact(12))

# vérification du typafe statique avec mypy
# pip install mypy
# mypy [file].py

# l'interpréteur ignore totalement ces informations
def fake_fact(n : str) -> str:
    return 1 if n <= 1 else n * fake_fact(n-1)

# on peut appeler fake_fact avec un int alors 
# que c'est déclaré pour des str
fake_fact(12)