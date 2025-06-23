"""
Module 4: Variable Assignment and Types Examples
===============================================

This module covers variable assignment and type handling in Python:
- Creating and assigning variables
- Variable naming conventions
- Dynamic typing in Python
- Type conversion and casting

Learning Objectives:
- Practice variable assignment and type conversion
- Learn variable naming conventions
- Understand dynamic typing in Python
- Apply type conversion in test automation
"""

print("=" * 50)
print("MODULE 4: VARIABLE ASSIGNMENT AND TYPES")
print("=" * 50)

# Basic Variable Assignment
print("\n1. Basic Variable Assignment:")

# Simple assignment
x = 10
y = 20
z = x + y

print(f"x = {x}")
print(f"y = {y}")
print(f"z = x + y = {z}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Unpacking from list
numbers = [10, 20, 30]
first, second, third = numbers
print(f"Unpacking from list: first={first}, second={second}, third={third}")

# Variable Naming Conventions
print("\n2. Variable Naming Conventions:")

# Good Variable Names
user_name = "John"
user_age = 25
is_active = True
total_count = 100
test_case_id = "TC_001"

print("Good variable names:")
print(f"  user_name: {user_name}")
print(f"  user_age: {user_age}")
print(f"  is_active: {is_active}")
print(f"  total_count: {total_count}")
print(f"  test_case_id: {test_case_id}")

# Examples of Valid Names
my_variable = "valid"
_private_var = "valid"
var123 = "valid"
test_user_1 = "valid"

print("\nValid variable names:")
print(f"  my_variable: {my_variable}")
print(f"  _private_var: {_private_var}")
print(f"  var123: {var123}")
print(f"  test_user_1: {test_user_1}")

# Variable Naming Rules
print("\n3. Variable Naming Rules:")
print("✅ Can contain letters, numbers, and underscores")
print("✅ Must start with a letter or underscore")
print("✅ Cannot use reserved keywords")
print("✅ Case sensitive")

# Examples of Invalid Names (commented out to avoid errors)
print("\nExamples of Invalid Names (avoid these):")
print("  # 123var = 'invalid'  # Can't start with number")
print("  # my-var = 'invalid'  # Can't use hyphens")
print("  # class = 'invalid'   # Can't use reserved keywords")
print("  # if = 'invalid'      # Can't use reserved keywords")

# Dynamic Typing
print("\n4. Dynamic Typing:")

variable = 42
print(f"Variable: {variable}, Type: {type(variable)}")

variable = "Hello"
print(f"Variable: {variable}, Type: {type(variable)}")

variable = [1, 2, 3]
print(f"Variable: {variable}, Type: {type(variable)}")

variable = True
print(f"Variable: {variable}, Type: {type(variable)}")

# Type Conversion (Casting)
print("\n5. Type Conversion (Casting):")

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
print("\n6. Boolean Conversion:")

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
print("\n7. Test Automation Examples:")

# Test data variables
test_url = "https://example.com"
expected_title = "Welcome Page"
timeout_seconds = 30.5
is_test_enabled = True
retry_count = 3

print("Test data variables:")
print(f"  test_url: {test_url} ({type(test_url).__name__})")
print(f"  expected_title: {expected_title} ({type(expected_title).__name__})")
print(f"  timeout_seconds: {timeout_seconds} ({type(timeout_seconds).__name__})")
print(f"  is_test_enabled: {is_test_enabled} ({type(is_test_enabled).__name__})")
print(f"  retry_count: {retry_count} ({type(retry_count).__name__})")

# Type conversion in test automation
print("\nType conversion in test automation:")
user_input = "123"
user_id = int(user_input)  # Convert string to integer
print(f"  User input: '{user_input}' ({type(user_input).__name__})")
print(f"  Converted to int: {user_id} ({type(user_id).__name__})")

# Test configuration with type conversion
test_config_raw = {
    "timeout": "30",
    "retry_count": "3",
    "headless": "true",
    "screenshot": "false"
}

test_config_processed = {
    "timeout": int(test_config_raw["timeout"]),
    "retry_count": int(test_config_raw["retry_count"]),
    "headless": test_config_raw["headless"].lower() == "true",
    "screenshot": test_config_raw["screenshot"].lower() == "true"
}

print("\nTest configuration processing:")
for key, value in test_config_raw.items():
    processed_value = test_config_processed[key]
    print(f"  {key}: '{value}' -> {processed_value} ({type(processed_value).__name__})")

# Environment-specific variables
environment = "staging"
if environment == "production":
    base_url = "https://app.production.com"
    debug_mode = False
elif environment == "staging":
    base_url = "https://app.staging.com"
    debug_mode = True
else:
    base_url = "http://localhost:3000"
    debug_mode = True

print(f"\nEnvironment configuration:")
print(f"  Environment: {environment}")
print(f"  Base URL: {base_url}")
print(f"  Debug Mode: {debug_mode}")

# Test data generation with variables
print("\n8. Test Data Generation with Variables:")

def generate_test_data(test_id, user_type="standard"):
    """Generate test data using variables and type conversion"""
    # Convert test_id to string with padding
    formatted_id = f"TC_{test_id:03d}"
    
    # Generate username based on user type
    if user_type == "admin":
        username = f"admin_{test_id:03d}"
        permissions = ["read", "write", "delete"]
    else:
        username = f"user_{test_id:03d}"
        permissions = ["read"]
    
    # Create test data dictionary
    test_data = {
        "test_id": formatted_id,
        "username": username,
        "email": f"{username}@example.com",
        "password": f"pass{test_id:03d}123",
        "permissions": permissions,
        "is_active": True,
        "created_date": "2024-01-15"
    }
    
    return test_data

# Generate test data for different scenarios
test_scenarios = [
    (1, "standard"),
    (2, "admin"),
    (3, "standard")
]

print("Generated test data:")
for test_id, user_type in test_scenarios:
    data = generate_test_data(test_id, user_type)
    print(f"  {data['test_id']}: {data['username']} ({user_type}) - {data['email']}")

# Variable scope example
print("\n9. Variable Scope Example:")

def test_function():
    """Demonstrate variable scope"""
    local_var = "I'm local to this function"
    print(f"  Inside function: {local_var}")
    return local_var

# Global variable
global_var = "I'm global"

print(f"Global variable: {global_var}")
result = test_function()
print(f"Function returned: {result}")

# Practice Exercise
print("\n10. Practice Exercise:")

# Exercise 1: Personal Information
print("Exercise 1: Personal Information")
person_name = "Alice Johnson"
person_age = 28
person_city = "San Francisco"
is_student = False

print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"City: {person_city}")
print(f"Student: {is_student}")

# Exercise 2: Type Conversion
print("\nExercise 2: Type Conversion")
mixed_data = ["42", 3.14, True, "Python"]

print("Original data with types:")
for item in mixed_data:
    print(f"  {item} ({type(item).__name__})")

print("\nConverted data:")
for item in mixed_data:
    if isinstance(item, str):
        # Try to convert string to number
        try:
            converted = int(item)
            print(f"  '{item}' -> {converted} (int)")
        except ValueError:
            try:
                converted = float(item)
                print(f"  '{item}' -> {converted} (float)")
            except ValueError:
                print(f"  '{item}' -> (cannot convert to number)")
    elif isinstance(item, (int, float)):
        converted = str(item)
        print(f"  {item} -> '{converted}' (str)")
    elif isinstance(item, bool):
        converted = int(item)
        print(f"  {item} -> {converted} (int)")

print("\n" + "=" * 50)
print("MODULE 4 COMPLETED!")
print("=" * 50)

"""
Practice Exercise:
Create variables of different types, then convert them to other types and verify the conversions.

Test Automation Applications:
- Storing test data and configurations
- Handling different data types from APIs
- Type-safe test assertions
- Environment-specific configurations
- Test data generation and validation

Next Steps:
- Learn about operators and expressions
- Explore control flow statements
- Practice with loops and iteration
""" 