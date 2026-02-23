int1 = 15
int2 = int1
int1 = 20

list1 = [15]
list2 = list1
list1.append(20)

print(id(int1))
print(id(int2))
print(int1 == int2)
print(id(list1))
print(id(list2))
print(list1 == list2)
print(list1)
print(list2)

