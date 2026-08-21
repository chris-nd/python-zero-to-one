"Structure de données : listes"

liste = [9, 5, 3, 8, 2, 7, 1, 6, 4]


def find_min_val(l: list) -> int:
    """
    Recherche la valeur minimale dans une liste.

    Keyword arguments:

    l -- La liste dans laquelle rechercher la valeur minimale(default: [])

    Args:
        l (list): La liste dans laquelle rechercher la valeur minimale.

    Returns:
        int: La valeur minimale dans la liste.
    """
    min_value = l[0]
    for i in l:
        min_value = min(min_value, i)
    return min_value


print(find_min_val(liste))
