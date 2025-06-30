#Lesson 5 Dictionaries
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are defined using curly braces with key-value pairs separated by a colon.
# Example of a dictionary

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("\n")  # Print a new line for better readability

#accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York
print("\n")  # Print a new line for better readability

# Adding a new key-value pair to the dictionary
my_dict["grade"] = "A"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'grade': 'A'}
print("\n")  # Print a new line for better readability

# modifying an existing key-value pair
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'grade': 'A'}
print("\n")  # Print a new line for better readability

# Deleting a key-value pair from the dictionary
del my_dict["grade"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
print("\n")  # Print a new line for better readability
