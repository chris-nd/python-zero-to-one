# Demonstrating basic list operations in Python

brother = ["chris",
        "richel",
        "nathan",
        "djessy"]

list1 = [1, 2, 3, 4, 5 ]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [True, False, True, False]

print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)

list1.append(6)
print("After appending 6 to List 1:", list1)
list1.extend([7, 8, 9])
print("After extending List 1 with [7, 8, 9]:", list1)
list2.remove('c')
print("After removing 'c' from List 2:", list2)

print(brother[2])  # Accessing the third element of list1
print(brother[-1]) # Accessing the last element of list1

print(brother[2:4])  # Slicing list to get elements from index 2 to 3
print(brother[:])  # Slicing list1 to get all elements
print(brother[:3])  # Slicing list1 to get the first three elements
print(brother[1:])  # Slicing list2 to get elements from index 1 to the end
print(brother[::2])  # Slicing list2 to get every second element
print(brother[1::2])  # Slicing list3 to get every second element starting from index 1
print(brother[::-1])  # Slicing list3 to get elements in reverse order

# Finding the index of an element in a list

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("Index color:", colors.index("blue"))  # Accessing element index of 'blue'

colors.append('red')
print(colors.count('red'))  # Counting occurrences of 'red' in the list
colors.remove('red') # Removing the first occurrence of 'red'

# Sorting a list
list_brother_sorted = sorted(brother)  # Sorting the list and storing in a new variable
print(list_brother_sorted) # Displaying the sorted list

colors.sort()
print(colors)  # Sorting the list in ascending order

# Sorting in descending order
colors.sort(reverse=True)
print(colors)  # Sorting the list in descending order

# Reversing a list
brother.reverse()
print(brother)  # Displaying the reversed list

# Copying a list
prenoms = brother.copy()  # Copying the list
print("Copied list:", prenoms)

# Popping an element from the list
prenom = prenoms.pop(-1) # Popping the last element from the list
print("Popped element:", prenom)
print("List after popping:", brother)

# Clearing a list
people = prenoms.clear()  # Clearing all elements from the list
print("Cleared list:", people)  # Displaying the cleared list

# Joining list elements into a string
join_list = " ".join(["python", "is", "fun"])  # Joining list elements into a string
print(join_list)  # Displaying the joined string
join_list = "\n".join(["python", "is", "fun"])  # Joining list elements into a string
print(join_list)  # Displaying the joined string
join_list = "\t".join(["python", "is", "fun"])  # Joining list elements into a string
print(join_list)  # Displaying the joined string

# Splitting a string into a list
split_list = "python is fun".split()  # Splitting a string into a list
print(split_list)  # Displaying the split list
split_list = "python is fun".split("-") # Splitting a string into a list
print(split_list)  # Displaying the split list

# Embedded lists (lists within lists)
embeded_list_languages = [
    ["python", "java", "c++"],
    ["html", "css", "js"],
    ["sql", "mongodb", "firebase"]
]

print(embeded_list_languages[0][1])  # Accessing 'java' from the embedded list
print(embeded_list_languages[1][2])  # Accessing 'js' from the embedded list
print(embeded_list_languages[2][0])  # Accessing 'sql' from the embedded list

list1[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)  # Resetting list1 to original values

del list1[-4:]
print(list1)  # Deleting the last four elements from list1

a1 = list(range(3))
print(a1)  # Creating a list using range

a2 = list(range(10, 13))
print(a2)

