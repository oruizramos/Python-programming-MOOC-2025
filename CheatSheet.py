"""
================================================================================
COMPREHENSIVE PYTHON CHEATSHEET FOR VS CODE
================================================================================
Visual learner-friendly | Syntax highlighted | Complete reference
================================================================================
"""

# ==============================================================================
# 1. BASICS & SYNTAX
# ==============================================================================

# Comments
# This is a single line comment

"""
This is a multi-line comment
or docstring
"""

# Variables - no declaration needed
name = "Alice"  # string
age = 25  # integer
height = 5.6  # float
is_student = True  # boolean

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Constants (by convention, use UPPERCASE)
PI = 3.14159
MAX_SIZE = 100


# ==============================================================================
# 2. DATA TYPES
# ==============================================================================

# Strings
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is a
multi-line string"""

# String methods
text = "  Python Programming  "
text.upper()  # "  PYTHON PROGRAMMING  "
text.lower()  # "  python programming  "
text.strip()  # "Python Programming"
text.replace("Python", "Java")  # "  Java Programming  "
text.split()  # ["Python", "Programming"]
"Hello".startswith("He")  # True
"Hello".endswith("lo")  # True
"Hello".find("ll")  # 2 (index)
len("Hello")  # 5

# String formatting
name = "Bob"
age = 30
f"My name is {name} and I'm {age}"  # f-strings (Python 3.6+)
"My name is {} and I'm {}".format(name, age)  # .format()
"My name is %s and I'm %d" % (name, age)  # old style

# Numbers
integer = 42
floating = 3.14
complex_num = 3 + 4j

# Number operations
10 + 3  # 13 (addition)
10 - 3  # 7 (subtraction)
10 * 3  # 30 (multiplication)
10 / 3  # 3.333... (division)
10 // 3  # 3 (floor division)
10 % 3  # 1 (modulus/remainder)
10 ** 3  # 1000 (exponentiation)

# Type conversion
int("42")  # 42
float("3.14")  # 3.14
str(42)  # "42"
bool(1)  # True
bool(0)  # False


# ==============================================================================
# 3. LISTS (Ordered, Mutable)
# ==============================================================================

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
nested = [[1, 2], [3, 4]]

# Accessing elements
numbers[0]  # 1 (first element)
numbers[-1]  # 5 (last element)
numbers[1:3]  # [2, 3] (slicing)
numbers[:3]  # [1, 2, 3] (first three)
numbers[2:]  # [3, 4, 5] (from index 2)
numbers[::2]  # [1, 3, 5] (every second)
numbers[::-1]  # [5, 4, 3, 2, 1] (reverse)

# List methods
fruits = ["apple", "banana"]
fruits.append("cherry")  # Add to end: ["apple", "banana", "cherry"]
fruits.insert(1, "orange")  # Insert at index: ["apple", "orange", "banana", "cherry"]
fruits.remove("banana")  # Remove first occurrence
popped = fruits.pop()  # Remove and return last item
popped_idx = fruits.pop(0)  # Remove and return item at index
fruits.clear()  # Remove all items

numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Sort in place: [1, 1, 3, 4, 5]
numbers.reverse()  # Reverse in place: [5, 4, 3, 1, 1]
sorted_nums = sorted(numbers)  # Return sorted copy (doesn't modify original)
numbers.count(1)  # 2 (count occurrences)
numbers.index(4)  # 2 (find index of first occurrence)
len(numbers)  # 5 (length)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


# ==============================================================================
# 4. TUPLES (Ordered, Immutable)
# ==============================================================================

# Creating tuples
empty_tuple = ()
single_item = (1,)  # Note the comma!
coordinates = (3, 4)
mixed_tuple = (1, "two", 3.0)

# Accessing (same as lists)
coordinates[0]  # 3
coordinates[-1]  # 4

# Tuple unpacking
x, y = coordinates  # x=3, y=4
a, b, c = (1, 2, 3)

# Tuple methods (limited because immutable)
numbers = (1, 2, 2, 3)
numbers.count(2)  # 2
numbers.index(3)  # 3


# ==============================================================================
# 5. SETS (Unordered, Unique, Mutable)
# ==============================================================================

# Creating sets
empty_set = set()  # Note: {} creates a dict, not a set!
numbers = {1, 2, 3, 4, 5}
mixed = {1, "two", 3.0}

# Set operations
numbers.add(6)  # Add element
numbers.remove(3)  # Remove (raises error if not found)
numbers.discard(3)  # Remove (no error if not found)
numbers.clear()  # Remove all

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b  # {1, 2, 3, 4, 5, 6} (union)
a & b  # {3, 4} (intersection)
a - b  # {1, 2} (difference)
a ^ b  # {1, 2, 5, 6} (symmetric difference)

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}


# ==============================================================================
# 6. DICTIONARIES (Key-Value Pairs, Unordered)
# ==============================================================================

# Creating dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "NYC"}
mixed_keys = {1: "one", "two": 2, (3, 4): "tuple key"}

# Accessing values
person["name"]  # "Alice"
person.get("age")  # 25
person.get("country", "USA")  # "USA" (default if key not found)

# Modifying
person["age"] = 26  # Update existing
person["job"] = "Engineer"  # Add new key-value pair
del person["city"]  # Delete key-value pair
removed = person.pop("job")  # Remove and return value

# Dictionary methods
person.keys()  # dict_keys(['name', 'age'])
person.values()  # dict_values(['Alice', 26])
person.items()  # dict_items([('name', 'Alice'), ('age', 26)])
person.update({"city": "LA", "country": "USA"})  # Merge dictionaries
person.clear()  # Remove all items

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Checking membership
"name" in person  # True (check if key exists)
"Alice" in person.values()  # True (check if value exists)


# ==============================================================================
# 7. CONDITIONAL STATEMENTS
# ==============================================================================

# if, elif, else
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Just turned adult")
else:
    print("Adult")

# Comparison operators
x == y  # Equal
x != y  # Not equal
x > y  # Greater than
x < y  # Less than
x >= y  # Greater than or equal
x <= y  # Less than or equal

# Logical operators
x > 5 and x < 10  # Both conditions true
x < 5 or x > 10  # At least one condition true
not x > 5  # Negation

# Membership operators
"a" in "apple"  # True
3 not in [1, 2, 4]  # True

# Ternary operator
result = "Even" if x % 2 == 0 else "Odd"


# ==============================================================================
# 8. LOOPS
# ==============================================================================

# for loop
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8 (start, stop, step)
    print(i)

# Iterating over lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterating over dictionaries
person = {"name": "Alice", "age": 25}
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue  # Skip rest of this iteration
    if i == 7:
        break  # Exit loop entirely
    print(i)

# else clause (executes if loop completes normally)
for i in range(5):
    print(i)
else:
    print("Loop completed")


# ==============================================================================
# 9. FUNCTIONS
# ==============================================================================

# Basic function
def greet():
    print("Hello!")

greet()  # Call function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with default parameters
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_person("Alice")  # Uses default greeting
greet_person("Bob", "Hi")  # Custom greeting

# Return values
def add(a, b):
    return a + b

result = add(3, 5)  # 8

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])

# *args (variable number of arguments)
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4)  # 10

# **kwargs (variable number of keyword arguments)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Lambda functions (anonymous)
square = lambda x: x**2
square(5)  # 25

add = lambda a, b: a + b
add(3, 5)  # 8

# Map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)  # 15


# ==============================================================================
# 10. CLASSES & OBJECTS (OOP)
# ==============================================================================

# Basic class
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Instance variable
        self.age = age
    
    def greet(self):  # Instance method
        return f"Hello, my name is {self.name}"
    
    def birthday(self):
        self.age += 1

# Creating objects
person1 = Person("Alice", 25)
person1.greet()  # "Hello, my name is Alice"
person1.birthday()

# Class variables (shared by all instances)
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
dog.speak()  # "Buddy says Woof!"

# Class methods and static methods
class MyClass:
    @classmethod
    def class_method(cls):
        return "This is a class method"
    
    @staticmethod
    def static_method():
        return "This is a static method"

# Special methods (magic methods)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):  # Called by str() and print()
        return f"{self.title} ({self.pages} pages)"
    
    def __len__(self):  # Called by len()
        return self.pages
    
    def __eq__(self, other):  # Called by ==
        return self.pages == other.pages


# ==============================================================================
# 11. FILE HANDLING
# ==============================================================================

# Reading files
with open("file.txt", "r") as file:
    content = file.read()  # Read entire file
    
with open("file.txt", "r") as file:
    line = file.readline()  # Read one line
    
with open("file.txt", "r") as file:
    lines = file.readlines()  # Read all lines as list
    
# Better way to read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Writing files
with open("file.txt", "w") as file:  # "w" = write (overwrites)
    file.write("Hello World\n")
    
with open("file.txt", "a") as file:  # "a" = append
    file.write("New line\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file.txt", "w") as file:
    file.writelines(lines)

# File modes
# "r" - Read (default)
# "w" - Write (overwrites)
# "a" - Append
# "r+" - Read and write
# "b" - Binary mode (e.g., "rb", "wb")

# Check if file exists
import os
if os.path.exists("file.txt"):
    print("File exists")

# Delete file
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")


# ==============================================================================
# 12. EXCEPTION HANDLING
# ==============================================================================

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Wrong type")

# Catch all exceptions (use sparingly)
try:
    # risky code
    pass
except Exception as e:
    print(f"Error: {e}")

# else clause (executes if no exception)
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success!")

# finally clause (always executes)
try:
    file = open("file.txt", "r")
    # process file
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always closes file

# Raising exceptions
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Custom exceptions
class CustomError(Exception):
    pass

raise CustomError("This is a custom error")


# ==============================================================================
# 13. MODULES & IMPORTS
# ==============================================================================

# Importing entire module
import math
math.sqrt(16)  # 4.0

# Import specific functions
from math import sqrt, pi
sqrt(16)  # 4.0

# Import with alias
import numpy as np
import pandas as pd

# Import all (not recommended)
from math import *

# Your own modules
# If you have a file mymodule.py:
# import mymodule
# mymodule.my_function()


# ==============================================================================
# 14. COMMON BUILT-IN FUNCTIONS
# ==============================================================================

# Type functions
type(42)  # <class 'int'>
isinstance(42, int)  # True

# Math functions
abs(-5)  # 5
min(1, 2, 3)  # 1
max(1, 2, 3)  # 3
sum([1, 2, 3])  # 6
round(3.14159, 2)  # 3.14
pow(2, 3)  # 8 (same as 2**3)

# Sequence functions
len([1, 2, 3])  # 3
sorted([3, 1, 2])  # [1, 2, 3]
reversed([1, 2, 3])  # reversed object (use list() to convert)
range(5)  # 0, 1, 2, 3, 4
enumerate(['a', 'b', 'c'])  # (0, 'a'), (1, 'b'), (2, 'c')
zip([1, 2], ['a', 'b'])  # (1, 'a'), (2, 'b')

# Type conversion
int(), float(), str(), list(), tuple(), set(), dict()

# Input/Output
input("Enter your name: ")  # Get user input (returns string)
print("Hello", "World", sep=", ", end="!\n")  # Custom separator and ending

# All/Any
all([True, True, False])  # False (all elements true?)
any([True, False, False])  # True (at least one true?)

# Others
dir(object)  # List attributes and methods
help(function)  # Get help on function
id(object)  # Get memory address


# ==============================================================================
# 15. LIST/DICT/SET COMPREHENSIONS (Advanced)
# ==============================================================================

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
matrix = [[i*j for j in range(3)] for i in range(3)]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
filtered_dict = {k: v for k, v in {'a': 1, 'b': 2, 'c': 3}.items() if v > 1}

# Set comprehension
unique_squares = {x**2 for x in [1, -1, 2, -2, 3]}

# Generator expression (memory efficient)
gen = (x**2 for x in range(1000000))  # Doesn't create list in memory
next(gen)  # Get next value


# ==============================================================================
# 16. COMMON STANDARD LIBRARY MODULES
# ==============================================================================

# math - Mathematical functions
import math
math.sqrt(16), math.pi, math.sin(math.pi/2), math.ceil(3.2), math.floor(3.8)

# random - Random number generation
import random
random.randint(1, 10)  # Random integer between 1 and 10
random.choice(['a', 'b', 'c'])  # Random element from sequence
random.shuffle([1, 2, 3])  # Shuffle list in place
random.random()  # Random float between 0 and 1

# datetime - Date and time
from datetime import datetime, date, time, timedelta
now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# os - Operating system interface
import os
os.getcwd()  # Current working directory
os.listdir('.')  # List files in directory
os.path.exists('file.txt')  # Check if file exists
os.mkdir('new_folder')  # Create directory

# sys - System-specific parameters
import sys
sys.argv  # Command line arguments
sys.exit()  # Exit program

# json - JSON encoding/decoding
import json
data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data)  # Python dict to JSON string
parsed = json.loads(json_string)  # JSON string to Python dict

# re - Regular expressions
import re
pattern = r'\d+'  # Match digits
re.findall(pattern, 'abc123def456')  # ['123', '456']
re.sub(r'\d+', 'X', 'abc123def456')  # 'abcXdefX'


# ==============================================================================
# 17. USEFUL TIPS & TRICKS
# ==============================================================================

# Unpacking
a, b = 1, 2
a, *rest = [1, 2, 3, 4]  # a=1, rest=[2, 3, 4]

# Swapping variables
a, b = b, a

# Multiple comparisons
1 < x < 10  # True if x between 1 and 10

# Check if string is digit/alpha
"123".isdigit()  # True
"abc".isalpha()  # True
"abc123".isalnum()  # True

# Join list into string
words = ["Hello", "World"]
" ".join(words)  # "Hello World"

# Split string into list
"Hello World".split()  # ["Hello", "World"]

# Get unique elements (preserve order)
seen = set()
unique = [x for x in [1, 2, 2, 3, 3, 4] if not (x in seen or seen.add(x))]

# Flatten list
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5]

# Count occurrences
from collections import Counter
Counter(['a', 'b', 'a', 'c', 'b', 'a'])  # Counter({'a': 3, 'b': 2, 'c': 1})

# Default dictionary
from collections import defaultdict
d = defaultdict(int)  # Default value is 0
d['key'] += 1  # No KeyError

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x, p.y  # 1, 2


# ==============================================================================
# 18. DECORATORS (Advanced)
# ==============================================================================

# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}")


# ==============================================================================
# 19. CONTEXT MANAGERS (with statement)
# ==============================================================================

# Files automatically close
with open('file.txt', 'r') as f:
    content = f.read()
# File is automatically closed here

# Custom context manager
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext() as ctx:
    print("Inside context")


# ==============================================================================
# 20. PYTHONIC IDIOMS
# ==============================================================================

# Check for empty sequences
if not my_list:  # Better than: if len(my_list) == 0:
    print("List is empty")

# Get from dict with default
value = my_dict.get('key', 'default')  # Better than try-except

# Use enumerate instead of range(len())
for i, item in enumerate(my_list):  # Better than: for i in range(len(my_list)):
    print(i, item)

# Use zip for parallel iteration
for name, age in zip(names, ages):  # Better than using indices
    print(name, age)

# Use any() and all()
if any(x > 10 for x in numbers):  # Better than loop with break
    print("At least one number > 10")

# Use dict.items() for iteration
for key, value in my_dict.items():  # Better than: for key in my_dict:
    print(key, value)


"""
================================================================================
END OF CHEATSHEET
================================================================================
Keep this file open in VS Code while learning Python!
Use Ctrl+F (Cmd+F on Mac) to search for specific topics.
================================================================================
"""