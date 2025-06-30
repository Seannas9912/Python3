#Lesson 1: Lists
# A list is a collection of items that can be of different types.
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry
print("\n")  # Print a new line for better readability

fruits[1] = "orange"  # Change the value of the second item
print(fruits)  # Output: ['apple', 'orange', 'cherry']
print("\n")  # Print a new line for better readability

#Lesson 2: List Methods
# List methods allow you to manipulate lists easily.
# Adding an item to the list
fruits.append("kiwi")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'kiwi']
print("\n")  # Print a new line for better readability

# Removing an item from the list
fruits.remove("orange")  # Correctly removing "orange"
print(fruits)  # Output: ['apple', 'cherry', 'kiwi']
print("\n")  # Print a new line for better readability

#inserting an item at a specific position
fruits.insert(1, "mango")  # Insert "mango" at index 1
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'kiwi']
print("\n")  # Print a new line for better readability

# Sorting the list
fruits.sort()  # Sort the list in alphabetical order
print(fruits)  # Output: ['apple', 'cherry', 'kiwi', 'mango']
print("\n")  # Print a new line for better readability

# Reversing the list
fruits.reverse()  # Reverse the order of the list
print(fruits)  # Output: ['mango', 'kiwi', 'cherry', 'apple']
print("\n")  # Print a new line for better readability
