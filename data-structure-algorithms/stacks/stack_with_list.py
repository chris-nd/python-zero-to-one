"Structure de données - Pile"

from typing import Any

# Basé sur le principe du LIFO"

# Les opérations de base
# Push
# Pop
# Peek
# isEmpty
# Size

# Les piles peuvent être implémentées à l'aide de
# tableaux ou de listes chaînées.

# Les listes python peuvent se comporter comme des
# des piles avec des méthodes comme: append(), pop()


class Stack:
    "Classe d'objet de type Stack"

    def __init__(self):
        self.__stack = []

    def _get_stack(self):
        return self.__stack

    def _set_stack(self):
        pass

    stack = property(_get_stack)

    def push(self, item: Any):
        """
        Ajoute un élement à la pile.

        Args:
            item (Any): L'élément à ajouter au dessus de la pile
        """

        if not isinstance(self.stack, list):
            return f"'{self.stack}' n'est pas une pile"

        self.stack.append(item)

    def pop(self) -> Any:
        """
        Retire et renvoie l'élément au dessus de la pile

        Returns:
            Any | int: L'élément renvoyé
        """

        if self.isEmpty():
            return "La pile est vide"

        return self.stack.pop()

    def peek(self) -> Any:
        """
        Renvoie l'élément au dessus de la pile

        Returns:
            Any: L'élément renvoyé
        """

        if self.isEmpty():
            return "La pile est vide"

        return self.stack[-1]

    def isEmpty(self) -> bool:
        """
        Vérifie si la pile est vide

        Returns:
            bool: True si la pile est vide, sinon False
        """

        return len(self.stack) == 0

    def size(self) -> int:
        """
        Renvoie la taille de la pile

        Returns:
            int: La taille de la pile
        """

        return len(self.stack)

    def __str__(self) -> str:

        return f"{self.stack}"


# Créer une stack (pile)
pile = Stack()
pile.push(5)
pile.push(1)
pile.push(6)

print("Pile: ", pile)
print("Pop: ", pile.pop())
print("Pile après Pop: ", pile)
print("Peek: ", pile.peek())
print("Pile après Peek: ", pile)
print("isEmpty: ", pile.isEmpty())
print("Size: ", pile.size())
