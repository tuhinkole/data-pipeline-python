# Basic Python Script
# This script demonstrates basic Python concepts including variables, data types, control flow, and functions.


# variable
name = "John Doe"
age = 30
is_Active = False
pi = 3.14
# Printing variables
print("Name:", name)
print("Age:", age)
print("Is Active:", is_Active)
print("Value of Pi:", pi)

# Printing types of variables
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(is_Active))  # <class 'bool'>
print(type(pi))    # <class 'float'>

multiline_string = """This is a
multiline string.
It can span multiple lines."""
print(multiline_string)


# Conditional_statements
if age > 18:
    if is_Active:
        print("You are an active adult.")
    else:
        print("You are an inactive adult.")
else:
    print("You are a minor.")

# For Loops
for i in range(5):
    # print(f"Iteration {i}")
    print(i)

# While Loops
count = 0
while count < 5:
    print(f'count is {count}')
    count += 1;


# functions
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
print(greet(name))  # Output: Hello, John Doe!

# Data Structures

# List
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
# Adding an item to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# Removing an item from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']
print(fruits[0])

# Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "is_active": True
}

print(person)  # Output: {'name': 'Alice', 'age': 25, 'is_active': True}

# Accessing dictionary values
print(person["name"])  # Output: Alice
# Adding a new key-value pair
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'is_active': True, 'city': 'New York'}
# Removing a key-value pair
del person["age"]
print(person)  # Output: {'name': 'Alice', 'is_active': True, 'city': 'New York'}

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
# Accessing tuple elements
print(my_tuple[1])  # Output: 2

# Set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Adding an item to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Removing an item from the set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
# Accessing set elements (Note: Sets are unordered)
for item in my_set:
    print(f'element list',item)  # Output: 1, 2, 4, 5, 6 (order may vary)


# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful, result is:", result)
finally:
    print("This block always executes, regardless of an error.")


# Importing modules
import math
# Using the math module
print("Square root of 16 is:", math.sqrt(16))  # Output: 4.0
# Using the random module
import random
# Generating a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)
# Using the datetime module
import datetime
# Getting the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)  # Output: Current date and time: YYYY-MM-DD HH:MM:SS.ssssss
# Using the time module
import time
# Pausing execution for 2 seconds
time.sleep(2)
print("Execution resumed after 2 seconds.")