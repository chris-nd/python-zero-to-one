from collections import defaultdict

def notes(etudiants):
    groupe = defaultdict(list)
    
    for etudiant, note in etudiants:
        groupe[note].append(etudiant)

    return dict(groupe)

print(notes([("Alice", 15), ("Bob", 12), ("Charlie", 15), ("David", 18)]))