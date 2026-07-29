""" Fonctions de conversion de base """

def to_base36(value: int) -> str:
    """
    Convertit un entier en base 36.

    Args:
        value (int): L'entier à convertir

    Returns:
        str: La représentation de l'entier en base 36
    """
    if value == 0:
        return '0'
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'.upper()
    result = ''
    while value > 0:
        value, r = divmod(value, 36)
        result = alphabet[r] + result
    return result

def changement_de_base(rep_a: str, a: int, b: int)-> str:
    """
    Change la base d'un nombre representé par rep_a de base a à la base b

    Args:
        rep_a: le nombre representé dans la base a
        a: la base de depart
        b: la base d'arrivée

    Returns:
        le nombre representé dans la base b

    Example:
        >>> changement_de_base('10', 10, 2)
        '1010'
        >>> changement_de_base('A', 20, 8)
    """

    value = int(rep_a, a)
    result = ""

    if b == 2:
        result = bin(value)[2:]
    elif b == 8:
        result = oct(value)[2:]
    elif b == 10:
        result = str(value)
    elif b == 16:
        result = hex(value)[2:].upper()
    else:
        result = to_base36(value)

    return result

print(changement_de_base('10', 10, 2))
print(changement_de_base('A', 20, 8))
print(changement_de_base('101', 3, 10))
print(changement_de_base('101', 3, 16))
print(changement_de_base('143', 10, 36))
