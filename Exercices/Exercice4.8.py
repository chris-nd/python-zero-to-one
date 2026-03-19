# O(n²) - count() parcourt la chaîne à chaque fois
def anagramme(str):
    str_1, str_2 = str
    if len(str_1) == len(str_2):
        for c in str_1:
            if str_1.count(c) == str_2.count(c):
                pass
            else:
                return f"{str_1} et {str_2} ne sont pas des anagrammes"
        return f"{str_1} et {str_2} sont des anagrammes"
    
print(anagramme(("listen", "silent")))
print(anagramme(("hello", "world")))
print(anagramme(("triangle", "integral")))

# Alternative : O(n log n) - plus rapide pour grandes chaînes
# def anagramme(str_tuple):
#     str_1, str_2 = str_tuple
#     if sorted(str_1) == sorted(str_2):
#         return f"{str_1} et {str_2} sont des anagrammes"
#     return f"{str_1} et {str_2} ne sont pas des anagrammes"

# print(anagramme(("listen", "silent")))
# print(anagramme(("hello", "world")))
# print(anagramme(("triangle", "integral")))