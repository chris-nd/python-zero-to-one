# pour typer une variable avec les type hints
nb_items : int = 0

print(type(nb_items))
print(isinstance(nb_items, int))

# une fonction factorielle avec des type hints
def fact(n : int) -> int:
    return 1 if n <= 1 else n * fact(n-1)

print(fact(12))