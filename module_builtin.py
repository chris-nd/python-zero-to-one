import builtins

dir(builtins)

print(1)
print = 10
print(1)

x = 1

print = builtins.print
print(1)