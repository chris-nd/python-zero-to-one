def nb_vowel(s):
    vowels = "AEIOUaeiou"
    counter = 0

    for char in s:
        if char in vowels:
            counter += 1

    return counter

# Alternative plus pythonique
# def nb_vowel(s):
#     vowels = "AEIOUaeiou"
#     return sum(1 for char in s if char in vowels)

print(nb_vowel("Hello"))
print(nb_vowel("Programming"))
print(nb_vowel("AEIUO"))