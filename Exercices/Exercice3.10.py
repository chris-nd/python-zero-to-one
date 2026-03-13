# import unicodedata

def count_char_unicode(s: str):
    majuscule = 0
    miniscule = 0
    chiffre = 0
    symbole = 0
    for char in s:
        if char.isupper():
            majuscule += 1
        elif char.islower():
            miniscule +=1
        elif char.isdigit():
            chiffre += 1
        elif not char.isalnum():
            symbole += 1
    print(f"Majuscule = {majuscule}")
    print(f"Miniscule = {miniscule}")
    print(f"Chiffre = {chiffre}")
    print(f"Symbole = {symbole}")

count_char_unicode("Hello World 123!")
count_char_unicode("Café au lait")
count_char_unicode("Test_2024!")

# 2ème approche
# def count_char_unicode(s: str):
#     majuscule = sum(1 for c in s if c.isupper())
#     minuscule = sum(1 for c in s if c.islower())
#     chiffre = sum(1 for c in s if c.isdigit())
#     symbole = sum(1 for c in s if not c.isalnum())
    
#     return {
#         "majuscules": majuscule,
#         "minuscules": minuscule,
#         "chiffres": chiffre,
#         "symboles": symbole
#     }

# print(count_char_unicode("Hello World 123!"))
# print(count_char_unicode("Café au lait"))
# print(count_char_unicode("Test_2024!"))

# 3ème approche
# def count_char_unicode(s: str):
#     categories = {}
    
#     for char in s:
#         cat = unicodedata.category(char)
#         categories[cat] = categories.get(cat, 0) + 1
    
#     print("Catégories Unicode:")
#     for cat, count in categories.items():
#         print(f"  {cat}: {count}")

# count_char_unicode("Hello World 123!")
# count_char_unicode("Café au lait")
# count_char_unicode("Test_2024!")

