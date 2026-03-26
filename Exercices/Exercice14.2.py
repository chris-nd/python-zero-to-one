from collections import Counter

def counter(string):
    return {s: string.count(s) for s in string}

print(counter("hello"))
print(counter("programming"))

# 2ème approche de complexité O(n)
# def counter_efficient(string):
#     frequences = {}
#     for char in string:
#         frequences[char] = frequences.get(char, 0) + 1
#     return frequences

# print(counter("hello"))
# print(counter("programming"))

# 3ème approche avec la classe Counter du module collection
def counter_pro(string):
    return dict(Counter(string))

print(counter("hello"))
print(counter("programming"))