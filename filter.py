
filter1 = filter(lambda x: x > 2, [1, 2, 3, 4, 5])
print(list(filter1)) # [3, 4, 5]

filter2 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(filter2)) # [2, 4]

print(type(filter1)) # <class 'filter'> qui est un itérateur
print(type(filter2)) # <class 'filter'> qui est un itérateur