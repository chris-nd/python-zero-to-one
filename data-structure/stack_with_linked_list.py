"Structure de données: Pile avec liste chaînée"

class Node:
    "Classe représentant un nœud dans la liste chaînée"
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    "Classe représentant une pile"
    def __init__(self) -> None:
        self.head = None
        self.stack_size = 0

    def push(self, value):
        """
        Ajoute un élément au sommet de la pile.

        Args:
            value: La valeur à ajouter à la pile.
        """
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.stack_size += 1

    def pop(self):
        """
        Retire l'élément du sommet de la pile.

        Returns:
            La valeur retirée du sommet de la pile.
        """
        if self.isEmpty():
            return "La pile est vide"
        popped_node = self.head
        self.head = self.head.next
        self.stack_size -= 1
        return popped_node.value

    def peek(self):
        """
        Retourne l'élément du sommet de la pile sans le retirer.

        Returns:
            La valeur du sommet de la pile.
        """
        if self.isEmpty():
            return "La pile est vide"
        return self.head.value

    def isEmpty(self) -> bool:
        """
        Vérifie si la pile est vide.

        Returns:
            True si la pile est vide, False sinon.
        """
        return self.stack_size == 0

    def size(self) -> int:
        """
        Retourne le taille de la pile.

        Returns:
            Le nombre d'éléments dans la pile.
        """
        return self.stack_size
<<<<<<< HEAD

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print()

my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print("Liste chaînée: ", end="")
my_stack.traverse()
print("Peek: ", my_stack.peek())
print("Pop: ", my_stack.pop())
print("Liste chaînée après Pop: ", end="")
my_stack.traverse()
print("isEmpty: ", my_stack.isEmpty())
print("Size: ", my_stack.size())
=======
>>>>>>> refs/remotes/origin/main
