def index_list(liste, index):
    try:
        print(liste[index])
    except IndexError as e:
        print(f"Erreur : {e}")

index_list([1, 2, 3], 1)
index_list([1, 2, 3], 10)

