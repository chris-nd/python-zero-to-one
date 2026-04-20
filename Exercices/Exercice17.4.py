def error(liste, index):
    try:
        liste[index] = 4 / int(index)
        print(liste)
    except ValueError as e:
        print(f"Erreur 1 : {e}")
    except TypeError as e:
        print(f"Erreur 2 : {e}")
    except IndexError as e:
        print(f"Erreur 3 : {e}")

error([1, 2, 3], 2)
error([1, 2, 3], "abc")
error([1, 2, 3], "2")
error([1, 2, 3], 4)

