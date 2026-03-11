def merge_sort(list_1, list_2):
    liste = list_1.copy()
    liste.extend(list_2)
    return sorted(liste)

print(merge_sort([1, 3, 5, 7], [2, 4, 6, 8]))