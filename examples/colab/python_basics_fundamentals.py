#!/usr/bin/env python3
"""
Python Basics Fundamentals
==========================

This file covers the fundamental concepts of Python programming:
1. Hello World
2. Data Types and Type Checking
3. String Manipulation
4. Variable Assignment and Types

Author: Python for Testers Course
"""

# ============================================================================
# 1. HELLO WORLD
# ============================================================================

print("=" * 50)
print("1. HELLO WORLD")
print("=" * 50)

# Basic Hello World
print("Hello, World!")

# Hello World with variables
message = "Hello, World!"
print(message)

# Hello World with user input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Hello World in different ways
print("Hello", "World", "from", "Python")
print("Hello" + " " + "World" + " " + "from" + " " + "Python")
print("Hello {} from {}".format("World", "Python"))

# ============================================================================
# 2. DATA TYPES IN PYTHON AND HOW TO GET THE TYPE AT RUNTIME
# ============================================================================

print("\n" + "=" * 50)
print("2. DATA TYPES AND TYPE CHECKING")
print("=" * 50)

# Integer (int)
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float (float)
height = 5.9
pi = 3.14159
print(f"Height: {height}, Type: {type(height)}")
print(f"Pi: {pi}, Type: {type(pi)}")

# String (str)
name = "John Doe"
email = 'john@example.com'
print(f"Name: {name}, Type: {type(name)}")
print(f"Email: {email}, Type: {type(email)}")

# Boolean (bool)
is_student = True
is_working = False
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Is Working: {is_working}, Type: {type(is_working)}")

# List (list) - Mutable, ordered collection
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
print(f"Fruits: {fruits}, Type: {type(fruits)}")
print(f"Numbers: {numbers}, Type: {type(numbers)}")
print(f"Mixed List: {mixed_list}, Type: {type(mixed_list)}")

# Tuple (tuple) - Immutable, ordered collection
coordinates = (10, 20)
person = ("John", 25, "Engineer")
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print(f"Person: {person}, Type: {type(person)}")

# Dictionary (dict) - Key-value pairs
person_info = {
    "name": "John Doe",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Java", "SQL"]
}
print(f"Person Info: {person_info}, Type: {type(person_info)}")

# Set (set) - Unordered collection of unique elements
unique_numbers = {1, 2, 3, 4, 5}
unique_letters = {"a", "b", "c", "a", "b"}  # Duplicates are removed
print(f"Unique Numbers: {unique_numbers}, Type: {type(unique_numbers)}")
print(f"Unique Letters: {unique_letters}, Type: {type(unique_letters)}")

# None (NoneType) - Represents absence of value
empty_value = None
print(f"Empty Value: {empty_value}, Type: {type(empty_value)}")

# Complex number (complex)
complex_num = 3 + 4j
print(f"Complex Number: {complex_num}, Type: {type(complex_num)}")

# ============================================================================
# 3. UNDERSTAND HOW TO MANIPULATE STRINGS AND PRINT THEM
# ============================================================================

print("\n" + "=" * 50)
print("3. STRING MANIPULATION")
print("=" * 50)

# String creation
single_quotes = 'This is a string'
double_quotes = "This is also a string"
triple_quotes = """This is a
multi-line string"""
print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes: {triple_quotes}")

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String formatting methods
age = 25
city = "New York"

# f-strings (recommended - Python 3.6+)
print(f"Name: {full_name}, Age: {age}, City: {city}")

# .format() method
print("Name: {}, Age: {}, City: {}".format(full_name, age, city))
print("Name: {0}, Age: {1}, City: {2}".format(full_name, age, city))
print("Name: {name}, Age: {age}, City: {city}".format(name=full_name, age=age, city=city))

# % operator (old style)
print("Name: %s, Age: %d, City: %s" % (full_name, age, city))

# String methods
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Length: {len(text)}")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Strip: '{text.strip()}'")
print(f"Lstrip: '{text.lstrip()}'")
print(f"Rstrip: '{text.rstrip()}'")

# String searching and replacing
sample_text = "Hello World, Hello Python"
print(f"\nSample text: {sample_text}")
print(f"Contains 'World': {sample_text.find('World')}")
print(f"Contains 'Python': {sample_text.find('Python')}")
print(f"Count 'Hello': {sample_text.count('Hello')}")
print(f"Replace 'Hello' with 'Hi': {sample_text.replace('Hello', 'Hi')}")

# String splitting and joining
csv_data = "apple,banana,orange,grape"
fruits_list = csv_data.split(",")
print(f"\nCSV data: {csv_data}")
print(f"Split into list: {fruits_list}")
print(f"Joined with ' | ': {' | '.join(fruits_list)}")

# String slicing
text = "Python Programming"
print(f"\nString: {text}")
print(f"Length: {len(text)}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[:6]}")
print(f"Last 6 characters: {text[-6:]}")
print(f"Characters 7-11: {text[7:12]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse: {text[::-1]}")

# String testing methods
test_string = "Hello123"
print(f"\nTest string: {test_string}")
print(f"Is alpha: {test_string.isalpha()}")
print(f"Is numeric: {test_string.isnumeric()}")
print(f"Is alphanumeric: {test_string.isalnum()}")
print(f"Starts with 'Hello': {test_string.startswith('Hello')}")
print(f"Ends with '123': {test_string.endswith('123')}")

# ============================================================================
# 4. VARIABLE ASSIGNMENT AND TYPES
# ============================================================================

print("\n" + "=" * 50)
print("4. VARIABLE ASSIGNMENT AND TYPES")
print("=" * 50)

# Basic variable assignment
x = 10
y = 20
z = x + y
print(f"x = {x}, y = {y}, z = x + y = {z}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Unpacking from list
numbers = [10, 20, 30]
first, second, third = numbers
print(f"Unpacking: first={first}, second={second}, third={third}")

# Variable naming conventions
# Good variable names
user_name = "John"
user_age = 25
is_active = True
total_count = 100

# Bad variable names (avoid these)
# user-name = "John"  # Can't use hyphens
# 1name = "John"      # Can't start with number
# class = "Python"    # Can't use reserved keywords

print(f"Good variable names: {user_name}, {user_age}, {is_active}, {total_count}")

# Dynamic typing
variable = 42
print(f"Variable: {variable}, Type: {type(variable)}")

variable = "Hello"
print(f"Variable: {variable}, Type: {type(variable)}")

variable = [1, 2, 3]
print(f"Variable: {variable}, Type: {type(variable)}")

# Type conversion
# String to number
string_number = "123"
integer_number = int(string_number)
float_number = float(string_number)
print(f"String '{string_number}' to int: {integer_number}, Type: {type(integer_number)}")
print(f"String '{string_number}' to float: {float_number}, Type: {type(float_number)}")

# Number to string
number = 42
string_number = str(number)
print(f"Number {number} to string: '{string_number}', Type: {type(string_number)}")

# Boolean conversion
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

# ============================================================================
# PRACTICAL EXAMPLES FOR TEST AUTOMATION
# ============================================================================

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES FOR TEST AUTOMATION")
print("=" * 50)

# Test data generation
def generate_test_user(user_id):
    """Generate test user data"""
    return {
        "id": user_id,
        "username": f"user{user_id:03d}",
        "email": f"user{user_id:03d}@example.com",
        "password": f"pass{user_id:03d}123",
        "is_active": True
    }

# Generate test users
test_users = []
for i in range(1, 4):
    user = generate_test_user(i)
    test_users.append(user)

print("Generated test users:")
for user in test_users:
    print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")

# URL construction
base_url = "https://practiceautomatedtesting.com"
endpoints = ["login", "dashboard", "profile", "settings"]

print(f"\nGenerated test URLs:")
for endpoint in endpoints:
    full_url = f"{base_url}/{endpoint}"
    print(f"  {full_url}")

# Test result formatting
test_results = [
    {"name": "Login Test", "status": "PASS", "duration": 2.5},
    {"name": "Search Test", "status": "FAIL", "duration": 1.8},
    {"name": "Logout Test", "status": "PASS", "duration": 1.2}
]

print(f"\nTest Results:")
for result in test_results:
    status_icon = "✅" if result["status"] == "PASS" else "❌"
    print(f"  {status_icon} {result['name']}: {result['duration']}s ({result['status']})")

# String validation
def validate_email(email):
    """Simple email validation"""
    if "@" in email and "." in email:
        return True
    return False

test_emails = [
    "user@example.com",
    "invalid-email",
    "user@.com",
    "user@domain.org"
]

print(f"\nEmail validation:")
for email in test_emails:
    is_valid = validate_email(email)
    print(f"  '{email}': {'Valid' if is_valid else 'Invalid'}")

# Data type checking in test automation
def validate_test_data(data):
    """Validate test data types"""
    expected_types = {
        "username": str,
        "password": str,
        "age": int,
        "is_active": bool
    }
    
    for field, expected_type in expected_types.items():
        if field in data:
            actual_type = type(data[field])
            if actual_type != expected_type:
                print(f"  ❌ {field}: Expected {expected_type.__name__}, got {actual_type.__name__}")
            else:
                print(f"  ✅ {field}: Correct type ({actual_type.__name__})")

test_data = {
    "username": "testuser",
    "password": "testpass123",
    "age": 25,
    "is_active": True
}

print(f"\nTest data validation:")
validate_test_data(test_data)

print("\n" + "=" * 50)
print("END OF PYTHON BASICS FUNDAMENTALS")
print("=" * 50) 