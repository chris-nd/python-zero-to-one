# The len() function returns the number of items in an object.

length = len("Hello, World!")  # Calculate the length of the string
print(length)  # Output: 13
length = len([1, 2, 3, 4, 5])  # Calculate the length of the list
print(length)  # Output: 5

# The round() function rounds a number to a specified number of decimal places.

rounded = round(3.14159, 2)  # Round the number to 2 decimal places
print(rounded)  # Output: 3.14
rounded = round(2.1828)  # Round the number to the nearest integer
print(rounded)  # Output: 2
rounded = round(2.71828)  # Round the number to the nearest integer
print(rounded)  # Output: 3

# The min() and max() functions return the smallest and largest items in an iterable or among multiple arguments.

min_value = min(5, 10, 2, 8)  # Find the minimum value among the numbers
print(min_value)  # Output: 2
max_value = max(5, 10, 2, 8)  # Find the maximum value among the numbers
print(max_value)  # Output: 10

# Example with a list of characters

min_value = min(["a", "b", "c"])  # Find the minimum value in the list
print(min_value)  # Output: a
max_value = max(["a", "b", "c"])  # Find the maximum value in the list
print(max_value)  # Output: c

# The sum() function returns the sum of all items in an iterable.

sum_value = sum([1, 2, 3, 4, 5])  # Calculate the sum of the list
print(sum_value)  # Output: 15

range_item = range(5)  # Create a range object
print(range_item)  # Output: range(0, 5)
range_item = range(2, 5)  # Create a range object with start, stop, and step
print(range_item)  # Output: range(2, 10, 2)
# Create a range object with start, stop, and step
range_item = range(2, 10, 2)
print(range_item)  # Output: range(2, 10, 2)
