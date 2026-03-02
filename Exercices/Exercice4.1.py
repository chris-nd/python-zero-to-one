# Avec le slicing

def reverse_string(s):
    return s[::-1]

# Avec une boucle
# def reverse_string(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result

# # Avec reversed()
# def reverse_string(s):
#     return "".join(reversed(s))

print(reverse_string("Python"))
print(reverse_string("Hello World"))