import math

def square(nb):
    try:
        return f"la racine carré de {nb} est {math.sqrt(nb)} et sa valeur absolue {math.fabs(nb)}"
    except Exception as e:
        return f"Il y'a eu une érreur: {e}"

print(square(16))
print(square(-25))
print(square(2.5))