def flatten(containers):
    "returns a list of the elements of the elements in containers"
    return [element for container in containers for element in container]

print(help(flatten))

print(flatten.__doc__)

# un style de docstring multi-lignes
def flatten(containers):
    """
provided that containers is a list (or more generally an iterable)
of elements that are themselves iterables, this function
returns a list of the items in these elements
    """
    return [element for container in containers for element in container]

print(help(flatten))

# un autre style, qui donne le même résultat
def flatten(containers):
    """
    provided that containers is a list (or more generally an iterable)
    of elements that are themselves iterables, this function
    returns a list of the items in these elements
    """
    return [element for container in containers for element in container]

print(help(flatten))