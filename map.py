
map1 = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(map1)) # [1, 4, 9, 16, 25]

map2 = map(lambda x: x > 2, [1, 2, 3, 4, 5])
print(list(map2)) # [False, False, True, True, True]

print(type(map1)) # <class 'map'> qui est un itérateur
print(type(map2)) # <class 'map'> qui est un itérateur



