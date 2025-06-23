"""
Python Functions - Basic Concepts
================================

This script covers the fundamentals of Python functions including:
- Function definition and calling
- Parameters and return values
- Basic function examples
"""

print("=" * 50)
print("PYTHON FUNCTIONS - BASIC CONCEPTS")
print("=" * 50)

# Basic function definition
def greet(name):
    """Simple function that prints a greeting"""
    print(f"Hello, {name}!")

print("\n1. BASIC FUNCTION DEFINITION AND CALLING")
print("-" * 40)

# Calling the function
greet("Alice")
greet("Bob")
greet("Charlie")

# Function with return value
def add(a, b):
    """Function that returns the sum of two numbers"""
    return a + b

print("\n2. FUNCTIONS WITH RETURN VALUES")
print("-" * 40)

# Using the returned value
result = add(3, 5)
print(f"Result: {result}")

# Using the function in expressions
total = add(10, 20) + add(5, 15)
print(f"Total: {total}")

# Function that returns multiple values
def get_name_and_age():
    """Function that returns multiple values"""
    return "Alice", 25

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# Function with default parameters
def greet_person(name, greeting="Hello"):
    """Function with default parameter"""
    print(f"{greeting}, {name}!")

print("\n3. FUNCTIONS WITH DEFAULT PARAMETERS")
print("-" * 40)

greet_person("Alice")
greet_person("Bob", "Good morning")

# Multiple default parameters
def create_profile(name, age=25, city="Unknown", occupation="Student"):
    """Function with multiple default parameters"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation
    }

print("\n4. MULTIPLE DEFAULT PARAMETERS")
print("-" * 40)

# Using with different numbers of arguments
profile1 = create_profile("Alice")
profile2 = create_profile("Bob", 30)
profile3 = create_profile("Charlie", 35, "New York", "Engineer")

print("Profile 1:", profile1)
print("Profile 2:", profile2)
print("Profile 3:", profile3)

print("\n" + "=" * 50)
print("BASIC FUNCTIONS COMPLETED!")
print("=" * 50) 