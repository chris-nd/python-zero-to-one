# Print "Hello, World!" five times

for i in range(5):
    print("Hello, World!")

# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# Print each character in the string "Python"

for char in "Python":
    print(char)

# Print each item in the list
for item in [10, 20, 30, 40, 50]:
    print(item)

# Using a while loop to print "Hello, World!" five times
    
i = 0
while i < 5:
    print("While Loop")
    i += 1

liste = ["5", "10", "15", "Paul", "20", "Pierre", "25"]
for element in liste:
    if element.isdigit():
        continue
    print(element)

liste = ["5", "10", "15", "Paul", "20", "Pierre", "25"]
for element in liste:
    if element.isdigit():
        break
    print(element)