# Functions

# def greet(name):
#     """Function to greet a person."""
#     print(f"Hello, {name}! Welcome to the program.")
# greet("Alice")
# print("\n")

# def add(a, b):
#     return a + b

# result = add(2, 5)
# print(result)
# print("\n")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
greet("Bob","Good morning")