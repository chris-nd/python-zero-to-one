"""
Structure de données : Arbre binaire de recherche (BST)

Permet de stocker et de rechercher efficacement 
des éléments dans un ordre spécifique.

- Les opérations de bases:
  - Insertion
  - Suppression
  - Recherche
  - Parcours
"""

from typing import Any


# Créer un noeud de la l'arbre
class TreeNode:
    "Représente un noeud dans l'arbre binaire de recherche."
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)