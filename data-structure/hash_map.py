"""
Structure de donnée: Hash Map

- La fonction de hachage

Il  existe de nombreuses façons de créer une fonction de hashage
"""

my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value: str) -> int:
    """
    Calcule et renvoie un code de hashage (hash code)

    Args:
        value (str): complément de la taille de la table de hash

    Returns:
        int: code de hashage
    """
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10


def add(value: str) -> None:
    """
    Ajoute un complément la table de hashage

    Args:
        value (str): complément de la table de hash
    """
    index = hash_function(value)
    my_list[index] = value


add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

print("'Bob' a un hash code (code de hashage) de:", hash_function('Bob'))
print("'Chris' a un hash code (code de hashage) de:", hash_function('Chris'))

