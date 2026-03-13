import unicodedata

def replace_char(s: str):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")

print(replace_char("été"))
print(replace_char("naïveté"))
print(replace_char("coïncidence"))

# 2ème approche
# def replace_char(s: str):
#     accents = {
#         'à': 'a', 'á': 'a', 'â': 'a', 'ä': 'a',
#         'è': 'e', 'é': 'e', 'ê': 'e', 'ë': 'e',
#         'ì': 'i', 'í': 'i', 'î': 'i', 'ï': 'i',
#         'ò': 'o', 'ó': 'o', 'ô': 'o', 'ö': 'o',
#         'ù': 'u', 'ú': 'u', 'û': 'u', 'ü': 'u',
#         'ç': 'c', 'ñ': 'n'
#     }
#     result = ""
#     for char in s:
#         result += accents.get(char.lower(), char)
#     return result

# print(replace_char("été"))
# print(replace_char("naïveté"))
# print(replace_char("coïncidence"))