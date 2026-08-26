"Structure de donnée: linked-list"

from typing import Any

# Les opérations de bases:

# Parcourir
# Insérer un noeud
# Supprimer un noeud
# Trier

# Liste simplement chaînée

class Node:
    "Classe d'objet de type Node"

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def traverse(head: Node) -> None:
    """
    Parcourir une liste simplement chaînée

    Args:
        head (Node): Le noeud de tête
    """
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

traverse(node1)


# Trouver la valeur minimal dans une liste chaînée
def find_min_value(head: Node) -> Any:
    """
    Trouver la valeur minimal d'une liste chaînée

    Args:
        head (Node): Le noeud de tête
    """

    min_value = head.data
    current_node = head.next

    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value

print("La valeur minimale dans la liste chaînée est:", find_min_value(node1))


# Supprimer un noeud de la liste chaînée
def remove_node(head: Node, node: Node) -> Node | None:
    """
    Supprimer un noeud de la liste chaînée

    Args:
        head (Node): Noeud de tête
        node (Node): Noeud à supprimer

    Returns:
        node (Node | None): Un noeud de la liste
    """

    if head == node:
        return head.next

    current_node = head

    while current_node.next and current_node.next != node:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next

    return head


print("Avant suppression")
traverse(node1)
remove_node(node1, node4)
print("Après suppression")
traverse(node1)


# Insérer un noeud dans la liste chaînée
def insert_node(head: Node, new_node: Node, position: int) -> Node:
    """
    Insére un nouveau noeud à une liste chaînée

    Args:
        head (Node): Noeud de tête
        new_node (Node): Noeud à insérer
        position (int): Postion de l'insertion

    Returns:
        Noeud inséré
    """
    if position == 1:
        new_node.next = head
        return new_node

    current_node = head

    for _ in range(position - 2):
        if current_node.next is None:
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node

    return head


node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("\nAvant insertion:")
traverse(node1)

# Inséer un nouveau noeud avec une valeur de 97 en position 2
new_node = Node(97)
node1 = insert_node(node1, new_node, 2)

print("Après insertion:")
traverse(node1)
