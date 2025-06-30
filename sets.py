#lesson 4 sets
# Sets are unordered collections of unique elements in Python.
# They are defined using curly braces or the set() constructor.
# Example of a set

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print("\n")  # Print a new line for better readability
# Accessing elements in a set is not possible by index since sets are unordered
# However, you can check for membership
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False
print("\n")  # Print a new line for better readability
# Adding an element to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
print("\n")  # Print a new line for better readability

# Removing an element from a set
my_set.remove(2)  # This will raise a KeyError if 2 is not present
print(my_set)  # Output: {1, 3, 4, 5, 6}
print("\n")  # Print a new line for better readability

# Discarding an element from a set (does not raise an error if the element is not present)
my_set.discard(3)  # This will not raise an error if 3 is not present
print(my_set)  # Output: {1, 4, 5, 6}
print("\n")  # Print a new line for better readability

# Clearing all elements from a set
my_set.clear()  # This will remove all elements from the set
print(my_set)  # Output: set()
print("\n")  # Print a new line for better readability

# Creating a new set from a list
my_list = [1, 2, 3, 4, 5]
my_new_set = set(my_list)  # This will remove duplicates
print(my_new_set)  # Output: {1, 2, 3, 4, 5}
print("\n")  # Print a new line for better readability

# Set operations
# Union of two sets

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_union = set_a | set_b  # Using the | operator
print(set_union)  # Output: {1, 2, 3, 4, 5}
print("\n")  # Print a new line for better readability

# Intersection of two sets
set_intersection = set_a & set_b  # Using the & operator
print(set_intersection)  # Output: {3}
print("\n")  # Print a new line for better readability

# Difference of two sets
set_difference = set_a - set_b  # Using the - operator
print(set_difference)  # Output: {1, 2}
print("\n")  # Print a new line for better readability

# Symmetric difference of two sets
set_symmetric_difference = set_a ^ set_b  # Using the ^ operator
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}
print("\n")  # Print a new line for better readability

# Checking if a set is a subset of another set
print(set_a.issubset(set_b))  # Output: False
print(set_a.issubset({1, 2, 3, 4, 5}))  # Output: True

# Checking if a set is a superset of another set
print(set_a.issuperset(set_b))  # Output: False
print(set_a.issuperset({1, 2}))  # Output: True

# Checking if two sets are disjoint
print(set_a.isdisjoint(set_b))  # Output: False
print(set_a.isdisjoint({6, 7}))  # Output: True

# Copying a set
set_copy = set_a.copy()  # Creates a shallow copy of set_a
print(set_copy)  # Output: {1, 2, 3}
print("\n")  # Print a new line for better readability
