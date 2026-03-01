from typing import List
from typing import Iterable
from typing import Dict, Tuple, List
from typing import Any
from typing import NewType

# une fonction qui 
# attend un paramètre qui soit une liste d'entiers,
# et qui retourne une liste de chaînes
def foo(x: List[int]) -> List[str]:
    pass

def lower_split(sep: str, inputs : Iterable[str]) -> str:
    return sep.join([x.lower() for x in inputs])

print(lower_split('--', ('AB', 'CD', 'EF')))

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

# L'objet ... existe bel et bien en Python
# sert principalement pour le slicing multidimensionnel de numpy

el = ...
print(el)

def broadcast_message(message: str, servers: List[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
        message: str,
        servers: List[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    ...

# Typage partiel

# imaginez que vous ne typez pas n2, ni la valeur de retour
# c'est équivalent de dire ceci
def partially_typed(n1: int, n2):
    return None

# ou cela

def partially_typed(n1: int, n2: Any) -> Any:
    return None

# Alias

UserId = NewType('UserId', int)

user1_id : UserId = 0

# plutôt que ceci, qui est beaucoup moins parlant

user1_id : int = 0