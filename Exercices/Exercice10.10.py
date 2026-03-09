import random
# import string

def generatePassword():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$@_:-%€"
    return "".join(random.choices(chars, k=12))

print(generatePassword())

# 2ème approche
# def generatePassword():
#     chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$@_:-%€"
#     return "".join(random.sample(chars, 12))

# print(generatePassword())

# 3ème approche avec le module string
# def generatePassword():
#     chars = string.ascii_letters + string.digits + string.punctuation
#     return random.sample(chars, 12)

# print(generatePassword())