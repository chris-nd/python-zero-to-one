int1 = 100
int2 = int1

list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

print(id(int1) == id(int2))
print(id(list1) == id(list2))
print(id(list1) == id(list3))