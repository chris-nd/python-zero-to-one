"""
Structure de données : Graphe

- Les différents types de graphes:
    1- Graphe non orienté(bidirectionnel): 
        Un graphe dans lequel les arêtes 
        n'ont pas de direction.

    2- Graphe orienté (digraphe): 
        Un graphe dans lequel les arêtes 
        ont une direction.

    3- Graphe pondéré: 
        Un graphe dont les arêtes possèdent des valeurs 
        (poids, distances, capacités, temps ou probabilités).

    4- Graphe non pondéré: 
        Un graphe dont les arêtes n'ont pas de valeurs.

    5- Graphe connexe: 
        Un graphe dont tous les sommets sont reliés par des arêtes.

    6- Graphe non connexe: 
        Un graphe comportant des sous-graphes isolés (disjoints)
        ou des sommets isolés.

    7- Graphe cyclique: 
        Un graphe qui contient au moins un cycle, 
        dont les arêtes forment des boucles;

    8- Graphe acyclique
        Un graphe qui ne contient pas de cycle (boucle).

- Les différentes propriétés des graphes:
    - Pondéré
    - Orienté
    - Connexe
    - Cyclique
    - Boucle (boucle interne):
        Une boucle est un cycle constitué d'une seule arête.
"""

from typing import Any


# Liste des sommets du graphe selon la position
# des indices dans la matrice d'adjacence
vertex_data = ['A', 'B', 'C', 'D']

# Matrice d'adjacence du graphe
adjacenty_matrix = [
    [0, 1, 1, 1], # Le sommet A est connecté aux sommets B, C et D
    [1, 0, 1, 0], # Le sommet B est connecté aux sommets A et C
    [1, 1, 0, 0], # Le sommet C est connecté aux sommets A et B
    [1, 0, 0, 0]  # Le sommet D est connecté au sommet A
]

def display_connections(matrix: list[list[int]], vertices: list[str]) -> None:
    """
    Affiche les connexions pour chaque sommet du graphe.

    Args:
        matrix (list[list[int]]): La matrice d'adjacence du graphe.
        vertices (list[str]): La liste des sommets du graphe.
    """
    print("\nVoici les connexions pour chaqu'un des sommets:")
    for vertex, _ in enumerate(vertices):
        print(f"\n{vertices[vertex]}", end=" -> ")
        for connection, _ in enumerate(matrix[vertex]):
            if matrix[vertex][connection]:
                print(vertices[connection], end=" ")
    print()

display_connections(adjacenty_matrix, vertex_data)
