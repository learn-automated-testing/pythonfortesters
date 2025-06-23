"""
Module 2: Data Types and Type Checking Examples
===============================================

This module covers Python's built-in data types and type checking:
- Understanding Python's built-in data types
- Using the type() function
- Working with different data structures
- Type checking at runtime

Learning Objectives:
- Understand different data types in Python
- Learn how to check data types at runtime
- Work with collections (lists, tuples, dictionaries, sets)
"""

print("=" * 50)
print("MODULE 2: DATA TYPES AND TYPE CHECKING")
print("=" * 50)

# Python Data Types Overview
print("\n1. Python Data Types Overview:")

# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String
name = "John"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# None
empty_value = None
print(f"Empty Value: {empty_value}, Type: {type(empty_value)}")

# Collections in Python
print("\n2. Collections in Python:")

# Lists (Mutable)
print("\nLists (Mutable):")
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}, Type: {type(fruits)}")
print(f"Numbers: {numbers}, Type: {type(numbers)}")
print(f"Mixed List: {mixed_list}, Type: {type(mixed_list)}")

# List operations
fruits.append("grape")
print(f"After append: {fruits}")

# Tuples (Immutable)
print("\nTuples (Immutable):")
coordinates = (10, 20)
person = ("John", 25, "Engineer")

print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print(f"Person: {person}, Type: {type(person)}")

# Dictionaries (Key-Value Pairs)
print("\nDictionaries (Key-Value Pairs):")
person_info = {
    "name": "John Doe",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Java", "SQL"]
}

print(f"Person Info: {person_info}, Type: {type(person_info)}")
print(f"Name: {person_info['name']}")
print(f"Skills: {person_info['skills']}")

# Sets (Unique Elements)
print("\nSets (Unique Elements):")
unique_numbers = {1, 2, 3, 4, 5}
unique_letters = {"a", "b", "c", "a", "b"}  # Duplicates removed

print(f"Unique Numbers: {unique_numbers}, Type: {type(unique_numbers)}")
print(f"Unique Letters: {unique_letters}, Type: {type(unique_letters)}")

# Type Checking Examples
print("\n3. Type Checking Examples:")

# Check types at runtime
test_data = [
    ("age", 25, int),
    ("name", "John", str),
    ("is_student", True, bool),
    ("height", 5.9, float),
    ("skills", ["Python", "Java"], list),
    ("coordinates", (10, 20), tuple),
    ("person_info", {"name": "John"}, dict),
    ("unique_items", {1, 2, 3}, set)
]

for field_name, value, expected_type in test_data:
    actual_type = type(value)
    is_correct = actual_type == expected_type
    status = "✅" if is_correct else "❌"
    print(f"{status} {field_name}: {value} ({actual_type.__name__})")

# Type Conversion Examples
print("\n4. Type Conversion Examples:")

# String to number
string_number = "123"
integer_number = int(string_number)
float_number = float(string_number)

print(f"String '{string_number}' -> int: {integer_number}, Type: {type(integer_number)}")
print(f"String '{string_number}' -> float: {float_number}, Type: {type(float_number)}")

# Number to string
number = 42
string_number = str(number)
print(f"Number {number} -> string: '{string_number}', Type: {type(string_number)}")

# List to tuple and vice versa
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
my_list_again = list(my_tuple)

print(f"List {my_list} -> tuple: {my_tuple}, Type: {type(my_tuple)}")
print(f"Tuple {my_tuple} -> list: {my_list_again}, Type: {type(my_list_again)}")

# Boolean Conversion
print("\n5. Boolean Conversion:")

# Truthy values (convert to True)
truthy_values = [1, 42, "hello", [1, 2, 3], {"key": "value"}]
print("Truthy values (convert to True):")
for value in truthy_values:
    print(f"  bool({value}) = {bool(value)}")

# Falsy values (convert to False)
falsy_values = [0, "", [], {}, None, False]
print("\nFalsy values (convert to False):")
for value in falsy_values:
    print(f"  bool({value}) = {bool(value)}")

# Test Automation Examples
print("\n6. Test Automation Examples:")

# Test configuration with different data types
test_config = {
    "base_url": "https://example.com",
    "timeout": 30,
    "browser": "chrome",
    "headless": True,
    "test_users": ["admin", "user1", "user2"],
    "retry_count": 3,
    "screenshot_on_failure": True
}

print("Test Configuration:")
for key, value in test_config.items():
    print(f"  {key}: {value} ({type(value).__name__})")

# Test data validation
def validate_test_data_types(data):
    """Validate that test data has correct types"""
    expected_types = {
        "username": str,
        "password": str,
        "age": int,
        "is_active": bool,
        "permissions": list
    }
    
    print("\nTest Data Type Validation:")
    for field, expected_type in expected_types.items():
        if field in data:
            actual_type = type(data[field])
            if actual_type == expected_type:
                print(f"  ✅ {field}: Correct type ({actual_type.__name__})")
            else:
                print(f"  ❌ {field}: Expected {expected_type.__name__}, got {actual_type.__name__}")
        else:
            print(f"  ⚠️  {field}: Missing field")

# Test the validation function
test_data = {
    "username": "testuser",
    "password": "testpass123",
    "age": 25,
    "is_active": True,
    "permissions": ["read", "write"]
}

validate_test_data_types(test_data)

print("\n" + "=" * 50)
print("MODULE 2 COMPLETED!")
print("=" * 50)

"""
Practice Exercise:
Create variables of different types and use type() to verify their types.
Try creating:
- A list of test case names
- A dictionary of test configurations
- A tuple of coordinates
- A set of unique test IDs

Next Steps:
- Practice with string manipulation
- Learn about operators and expressions
- Explore control flow statements
""" 