def check_char(char):

    consonant = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vowel = "AEIOUaeiou"

    if char in consonant:
        return "C'est une consonne"
    elif char in vowel:
        return "C'est une voyelle"
    else:
        return "Autre"
    
print(check_char("a"))
print(check_char("B"))
print(check_char("5"))