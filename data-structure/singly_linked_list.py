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
