"""
Python Modules - Basic Concepts
===============================

This script covers basic module concepts in Python:
- Creating simple modules
- Different import methods
- Module-level variables and functions
- Basic module organization
"""

print("=" * 50)
print("PYTHON MODULES - BASIC CONCEPTS")
print("=" * 50)

# Creating a simple module (in a real file, this would be saved as mymodule.py)
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate area of rectangle"""
    return length * width

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

# Module-level variables
PI = 3.14159
VERSION = "1.0.0"
AUTHOR = "Python Developer"

# Module-level list
COLORS = ["red", "green", "blue", "yellow"]

# Module-level dictionary
CONFIG = {
    "debug": False,
    "timeout": 30,
    "max_retries": 3
}

print("\n1. CREATING A SIMPLE MODULE")
print("-" * 40)

print("Module created successfully!")
print(f"PI: {PI}")
print(f"Version: {VERSION}")
print(f"Author: {AUTHOR}")
print(f"Colors: {COLORS}")
print(f"Config: {CONFIG}")

# Testing module functions
print(f"\nGreeting: {greet('Alice')}")
print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")

# Different ways to import modules
print("\n2. DIFFERENT IMPORT METHODS")
print("-" * 40)

# Method 1: Import entire module
import math

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print(f"Ceiling of 3.7: {math.ceil(3.7)}")
print(f"Floor of 3.7: {math.floor(3.7)}")

# Method 2: Import specific items
from math import sqrt, pi, ceil, floor

print(f"\nSquare root of 25: {sqrt(25)}")
print(f"Value of pi: {pi}")
print(f"Ceiling of 4.2: {ceil(4.2)}")
print(f"Floor of 4.2: {floor(4.2)}")

# Method 3: Import with alias
import math as m

print(f"\nSquare root of 36: {m.sqrt(36)}")
print(f"Value of pi: {m.pi}")
print(f"Power of 2^3: {m.pow(2, 3)}")

# Method 4: Import specific items with alias
from math import sqrt as square_root, pi as PI_VALUE

print(f"\nSquare root of 49: {square_root(49)}")
print(f"Value of pi: {PI_VALUE}")

# Method 5: Import all (not recommended)
from math import *

print(f"\nFloor of 5.9: {floor(5.9)}")
print(f"Power of 3^2: {pow(3, 2)}")
print(f"Absolute value of -10: {fabs(-10)}")

# Creating a more complex module
print("\n3. CREATING A COMPLEX MODULE")
print("-" * 40)

# String utilities module
def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if string is palindrome"""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def title_case(text):
    """Convert string to title case"""
    return text.title()

# Test the string utilities
test_string = "Hello World"
print(f"Original: '{test_string}'")
print(f"Reversed: '{reverse_string(test_string)}'")
print(f"Vowel count: {count_vowels(test_string)}")
print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
print(f"Is 'hello' palindrome: {is_palindrome('hello')}")
print(f"Title case: '{title_case(test_string)}'")

# Module with classes
print("\n4. MODULE WITH CLASSES")
print("-" * 40)

class Calculator:
    """Simple calculator class"""
    def __init__(self):
        self.history = []
    
    def add(self, x, y):
        """Add two numbers"""
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result
    
    def subtract(self, x, y):
        """Subtract two numbers"""
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result
    
    def multiply(self, x, y):
        """Multiply two numbers"""
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result
    
    def divide(self, x, y):
        """Divide two numbers"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []

# Using the calculator class
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")

print(f"\nCalculation history: {calc.get_history()}")

# Module organization example
print("\n5. MODULE ORGANIZATION")
print("-" * 40)

# Constants section
DATABASE_URL = "postgresql://localhost:5432/mydb"
API_KEY = "your-api-key-here"
MAX_CONNECTIONS = 100

# Configuration section
DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "debug": False,
    "log_level": "INFO"
}

# Utility functions section
def validate_email(email):
    """Validate email format"""
    return '@' in email and '.' in email.split('@')[1]

def format_currency(amount, currency="USD"):
    """Format amount as currency"""
    return f"{currency} {amount:.2f}"

def generate_id(prefix="ID"):
    """Generate a unique ID"""
    import uuid
    return f"{prefix}_{str(uuid.uuid4())[:8]}"

# Main functionality section
def process_user_data(user_data):
    """Process user data with validation"""
    if not user_data.get("email"):
        raise ValueError("Email is required")
    
    if not validate_email(user_data["email"]):
        raise ValueError("Invalid email format")
    
    return {
        "id": generate_id("USER"),
        "email": user_data["email"],
        "name": user_data.get("name", "Unknown"),
        "processed": True
    }

# Test the organized module
print(f"Database URL: {DATABASE_URL}")
print(f"Default config: {DEFAULT_CONFIG}")
print(f"Email validation: {validate_email('user@example.com')}")
print(f"Currency format: {format_currency(123.45)}")
print(f"Generated ID: {generate_id()}")

user_data = {"email": "alice@example.com", "name": "Alice"}
processed_user = process_user_data(user_data)
print(f"Processed user: {processed_user}")

# Module documentation
print("\n6. MODULE DOCUMENTATION")
print("-" * 40)

"""
This module provides utility functions for common operations.

Functions:
    - validate_email: Check if email format is valid
    - format_currency: Format numbers as currency
    - generate_id: Create unique identifiers
    - process_user_data: Process and validate user data

Constants:
    - DATABASE_URL: Database connection string
    - API_KEY: API authentication key
    - MAX_CONNECTIONS: Maximum database connections

Classes:
    - Calculator: Simple calculator with history
"""

print("Module documentation example created!")

# Module testing section
print("\n7. MODULE TESTING")
print("-" * 40)

def test_module_functions():
    """Test all module functions"""
    # Test email validation
    assert validate_email("user@example.com") == True
    assert validate_email("invalid-email") == False
    
    # Test currency formatting
    assert format_currency(100) == "USD 100.00"
    assert format_currency(50.5, "EUR") == "EUR 50.50"
    
    # Test calculator
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.multiply(4, 5) == 20
    
    print("All tests passed!")

# Run tests
test_module_functions()

print("\n" + "=" * 50)
print("MODULES BASICS COMPLETED!")
print("=" * 50) 