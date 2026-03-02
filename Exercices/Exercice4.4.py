# def palindrome(s):
#     # Supprimer espaces et mettre en minuscules
#     s_clean = s.replace(" ", "").lower()
#     return s_clean == s_clean[::-1]

def palindrome(s):
    # Garder seulement les caractères alphanumériques en minuscules
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(palindrome("radar"))
print(palindrome("hello"))
print(palindrome("kayak"))
print(palindrome("A man a plan a canal Panama"))