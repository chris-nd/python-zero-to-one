"Comprendre le module builtins"

import builtins

print(dir(builtins))

numb = 1

print(numb)
print = 10
try:
    print(1)
except TypeError as e:
    repr(e)

print = builtins.print
print(numb)
