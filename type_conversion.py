print(str(100)) # Convert Integer to String
print(int("200")) # Convert String to Integer
print(float("3.14")) # Convert String to Float
print(bool(1)) # Convert Integer to Boolean
print(list((1, 2, 3))) # Convert Tuple to List
print(tuple([4, 5, 6])) # Convert List to Tuple
print(set([1, 2, 2, 3])) # Convert List to Set
print(dict(a=1, b=2)) # Convert keyword arguments to Dictionary
print(complex(2, 3)) # Convert two Integers to Complex Number

# Demonstrating various type conversions in Python
a = 10
b = "10"
print(a + int(b)) # Convert String to Integer for addition
print(b) # type of variable b
print(type(b)) # Check type of variable
b = int(b) # Convert String to Integer
print(type(b)) # Check type of variable after conversion
print(a + b) # Now both are Integers
