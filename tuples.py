#lesson 3 tuples
# Tuples are immutable sequences in Python, meaning they cannot be changed after creation.
# They are defined using parentheses and can contain any type of data.
# Example of a tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
print("\n")  # Print a new line for better readability

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
print(my_tuple[2])  # Output: 3
print("\n")  # Print a new line for better readability

# Attempting to change an element in a tuple will raise an error
# Uncommenting the following line will raise a TypeError
# my_tuple[1] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment
# Tuples can be used to store multiple values together

# Tuples can be concatenated
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
print("\n")  # Print a new line for better readability

#repeating tuples
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)
