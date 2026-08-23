"Structure de donnée: Queue"

from typing import Any

# Basé sur le principe du FIFO"

# Les opérations de base:
# Enqueue
# Dequeue
# Peek
# isEmpty
# Size

# Les files d'attentes peuvent être implémentées à l'aide de
# tableaux ou de listes chaînées.

# Les listes python peuvent se comporter comme des
# files avec des méthodes comme: append(), pop()

class Queue:
    "Classe de type objet Queue"
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Any) -> str | None:
        """
        Ajoute un élément à la file d'attente

        Args:
            item (Any): l'élément à ajouter

        Returns:
            list : la file rétounée
        """

        if not isinstance(self.queue, list):
            return "L'objet n'est pas une file"

        self.queue.append(item)

    def dequeue(self) -> Any:
        "Retire et renvoie le premier élément de la file"

        if self.isEmpty():
            return "La file est vide"

        return self.queue.pop(0)

    def peek(self) -> str | Any:
        "Renvoie le premier élément de la file"

        if self.isEmpty():
            return "La file est vide"

        return self.queue[0]

    def isEmpty(self) -> bool:
        "Vérifier si la file est vite"

        return len(self.queue) == 0

    def size(self) -> int:
        "Renvoie la taille de la file"

        return len(self.queue)

    def __str__(self) -> str:
        return f"{self.queue}"


queue = Queue()

# Enqueue
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print("Queue: ", queue)

# Peek
frontElement = queue.peek()
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.dequeue()
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = queue.isEmpty()
print("isEmpty: ", isEmpty)

# Size
print("Size: ", queue.size())


