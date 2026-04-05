import spam
from spam import y, z

x = 2

print(x) # 2
print(spam.x) # 1

print(y) # 5
y = 6
print(y) # 6
print(spam.y) # 5

z = 20

print(z) # 20
spam.z = 12
print(z) # 20
print(spam.z) # 12

print(vars()) # {'x': 2, 'y': 6, 'z': 20}
print(vars(spam)) # {'x': 1, 'y': 5, 'z': 12}
print(globals()) # {'x': 2, 'y': 6, 'z': 20, 'spam': <module 'spam' from '/path/to/spam.py'>}