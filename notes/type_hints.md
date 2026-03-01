## Type Hints (annotations de types)

### Contexte : Langages compilés vs Python

**Langage compilé (ex: C) :**

→ Typage **obligatoire** et **statique**

```c
int factoriel(int n) {
  return (n<=1) ? 1 : n * factoriel(n-1);
}
```

**Python (avant 3.5) :**

→ Typage **dynamique**, pas d'annotations nécessaires

```python
def factoriel(n):
    return 1 if n <= 1 else n * factoriel(n-1)
```

### Type Hints : Typage optionnel (Python ≥ 3.5)

**Depuis Python 3.5 :** Possibilité d'annoter le code avec des informations de typage (totalement **optionnel**).

### Syntaxe de base

**1. Typer une variable :**

```python
nb_items: int = 0
```

**2. Typer une fonction (paramètres et retour) :**

```python
def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n-1)

result = fact(12)  # result est connu comme int
```

**Format général :**

```python
def fonction(param1: Type1, param2: Type2) -> TypeRetour:
    pass
```

### Usages et avantages

**1. Documentation du code :**

```python
def diviser(a: float, b: float) -> float:
    """Divise a par b."""
    return a / b
```

**2. Aide des IDE :**

- Complétion plus pertinente
- Détection d'erreurs potentielles
- IntelliSense amélioré

**3. Analyse statique précoce :**

- Outils comme `mypy` peuvent détecter erreurs avant exécution
- Validation du code sans l'exécuter

### IMPORTANT : Ignoré par l'interpréteur !

**Les type hints sont totalement ignorés à l'exécution :**

```python
# Déclaré pour des str
def fake_fact(n: str) -> str:
    return 1 if n <= 1 else n * fake_fact(n-1)

# ✅ Fonctionne quand même avec un int !
fake_fact(12)  # Pas d'erreur à l'exécution
```

**Point clé :** Python **ne valide PAS** les type hints à l'exécution.

**Solution :** Utiliser des outils externes comme **mypy** pour validation statique.

### Le module `typing`

**Import nécessaire pour types complexes :**

```python
from typing import List, Dict, Tuple, Optional, Any
```

### Types de base

**Types simples (built-in) :**

```python
def simple(a: int, b: str, c: float, d: bool) -> None:
    pass
```

**Types de collections :**

```python
from typing import List, Dict, Tuple, Set

def process(
    liste: List[int],           # Liste d'entiers
    dico: Dict[str, int],       # Dict avec clés str, valeurs int
    tuple_fixe: Tuple[int, str],  # Tuple de 2 éléments (int, str)
    ensemble: Set[str]          # Set de strings
) -> List[str]:
    pass
```

### `list` vs `List`

**Attention à la distinction :**

```python
# ❌ Ne fonctionne pas pour annotations
def bad(x: list[int]):  # Erreur en Python < 3.9
    pass

# ✅ Correct
from typing import List
def good(x: List[int]):
    pass

# ✅ Python ≥ 3.9 : les deux fonctionnent
def new_style(x: list[int]):  # OK depuis 3.9
    pass
```

**Raisons :**

- `list` = type **concret** (pour créer instances)
- `List` = type **abstrait** (pour annotations)
- Python 3.9+ : `list[int]` accepté pour annotations

### Exemple : Types abstraits

**`Iterable` = type abstrait (duck typing) :**

```python
from typing import Iterable

def lower_split(sep: str, inputs: Iterable[str]) -> str:
    return sep.join([x.lower() for x in inputs])

# Fonctionne avec tuple, list, set, etc.
lower_split('--', ('AB', 'CD', 'EF'))  # → 'ab--cd--ef'
```

**Avantage :** Accepte tout itérable de strings, pas juste `list`.

### Exemple complet

**Tiré de la documentation `typing` :**

```python
from typing import Dict, Tuple, List

# Définir des alias pour clarté
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: List[Server]) -> None:
    ...

# Équivalent sans alias (moins lisible)
def broadcast_message(
    message: str,
    servers: List[Tuple[Tuple[str, int], Dict[str, str]]]
) -> None:
    ...
```

**Note :** `...` (Ellipsis) est un objet Python réel, utilisé surtout pour numpy.

### Typage partiel

**Pas obligé de tout typer :**

```python
# Typage partiel : seulement n1 est typé
def partially_typed(n1: int, n2):
    return None
```

**Équivalent explicite avec `Any` :**

```python
from typing import Any

def partially_typed(n1: int, n2: Any) -> Any:
    return None
```

**`Any` :** Type qui accepte n'importe quoi (équivalent à pas de typage).

### Alias et types personnalisés

**Créer des alias pour clarté :**

```python
from typing import NewType

# Créer un type distinct basé sur int
UserId = NewType('UserId', int)

# ✅ Plus clair
user1_id: UserId = 0

# ❌ Moins parlant
user1_id: int = 0
```

**Différence :** `UserId` est sémantiquement distinct de `int`, aide les outils de validation.

### Types courants du module `typing`

| Type | Description | Exemple |
| --- | --- | --- |
| **`List[T]`** | Liste d'éléments de type T | `List[int]` |
| **`Dict[K, V]`** | Dict avec clés K et valeurs V | `Dict[str, int]` |
| **`Tuple[T1, T2]`** | Tuple avec types précis | `Tuple[int, str]` |
| **`Set[T]`** | Ensemble d'éléments de type T | `Set[str]` |
| **`Optional[T]`** | T ou None | `Optional[int]` |
| **`Union[T1, T2]`** | T1 ou T2 | `Union[int, str]` |
| **`Any`** | N'importe quel type | `Any` |
| **`Callable[[Args], Ret]`** | Fonction callable | `Callable[[int], str]` |
| **`Iterable[T]`** | Tout itérable de T | `Iterable[str]` |

### Exemples pratiques

**1. Optional (valeur ou None) :**

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    # Peut retourner str ou None
    if user_id > 0:
        return "Alice"
    return None
```

**2. Union (plusieurs types possibles) :**

```python
from typing import Union

def process(data: Union[int, str]) -> str:
    if isinstance(data, int):
        return str(data)
    return data
```

**3. Callable (fonctions comme paramètres) :**

```python
from typing import Callable

def apply_twice(func: Callable[[int], int], x: int) -> int:
    return func(func(x))

def double(n: int) -> int:
    return n * 2

result = apply_twice(double, 5)  # → 20
```

### Avancé : Generics

**Pour définir des classes génériques :**

```python
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')  # Variable de type

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
```

**Usage :** Permet de créer `LoggedVar[int]`, `LoggedVar[str]`, etc.

### Outils pour exploiter les type hints

**1. mypy :** Validateur statique de types

```bash
pip install mypy
mypy mon_script.py
```

**2. PyCharm :** IDE avec support intégré

**3. VS Code :** Avec Pylance

**4. Autres :** pyre, pytype, pyright

### Adoption

**État actuel (document écrit après 2015) :**

- Introduits en Python 3.5 (2015)
- Améliorés en 3.6 (typage variables)
- Pas encore très répandus à l'époque
- Usage grandissant avec le temps
- Outils se sont améliorés

**Aujourd'hui (2024+) :**

- Beaucoup plus courant
- Standard dans projets professionnels
- Fortement recommandé pour gros projets

### Bonnes pratiques

**1. Utiliser pour APIs publiques :**

```python
# ✅ Fonctions exposées : typer
def public_api(data: List[int]) -> Dict[str, int]:
    pass

# Fonctions internes : optionnel
def _internal_helper(x, y):
    pass
```

**2. Préférer types abstraits :**

```python
# ✅ Plus flexible
from typing import Sequence
def process(items: Sequence[int]):
    pass

# ❌ Trop restrictif
def process(items: List[int]):
    pass
```

**3. Documenter comportements spéciaux :**

```python
def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Divise a par b.

    Returns:
        float si b != 0, None si b == 0
    """
    return a / b if b != 0 else None Points clés à retenir
```