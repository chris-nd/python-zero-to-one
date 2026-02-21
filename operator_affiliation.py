# Checking membership in a list
# Teste d'appartenance dans une liste
users = ["Alice", "Bob", "Charlie", "Frank"]
print("Bob" in users)  # Displaying the original list
print("bob" in users)  # Checking for an element in the list
print("Eve" in users)  # Checking for an element not in the list

#Teste de non-appartenance dans une liste
print("Alice" not in users)  # Checking for an element in the list
print("David" not in users)  # Checking for an element not in the list

# Removing an element if it exists
if "Franck" in users:
    users.remove("Franck")
    print("Franck removed from the list.")
else:
    print("Franck is not in the list.")

# Checking membership in a string
print("Java" in "JavaScript")  # Checking substring in a string
print("java" in "JavaScript")  # Checking substring in a string
print("Java" in "TypeScript")  # Checking substring not in a string
print("Script" not in "TypeScript")  # Checking substring in a string