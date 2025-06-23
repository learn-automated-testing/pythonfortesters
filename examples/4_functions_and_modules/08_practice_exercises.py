"""
Python Functions and Modules - Practice Exercises
=================================================

This script contains practice exercises for Python functions and modules:
- Calculator function
- Scope understanding
- String utilities module
- Standard library usage
- Function decorators
"""

print("=" * 50)
print("PYTHON FUNCTIONS & MODULES - PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Create a Calculator Function
print("\nEXERCISE 1: CALCULATOR FUNCTION")
print("-" * 40)

def calculator(operation, a, b):
    """
    Perform basic arithmetic operations
    
    Args:
        operation (str): 'add', 'subtract', 'multiply', 'divide'
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Result of the operation
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Test the calculator
print(f"10 + 5 = {calculator('add', 10, 5)}")
print(f"10 - 5 = {calculator('subtract', 10, 5)}")
print(f"10 * 5 = {calculator('multiply', 10, 5)}")
print(f"10 / 5 = {calculator('divide', 10, 5)}")
print(f"10 / 0 = {calculator('divide', 10, 0)}")
print(f"10 ^ 5 = {calculator('power', 10, 5)}")

# Exercise 2: Scope Understanding
print("\nEXERCISE 2: SCOPE UNDERSTANDING")
print("-" * 40)

global_var = "I'm global"

def scope_demo():
    """Demonstrate local, global, and nonlocal scope"""
    local_var = "I'm local"
    
    def nested_function():
        nonlocal local_var
        local_var = "I'm modified by nested function"
        print(f"Inside nested: {local_var}")
    
    print(f"Before nested: {local_var}")
    nested_function()
    print(f"After nested: {local_var}")
    print(f"Global var: {global_var}")

print(f"Global var before: {global_var}")
scope_demo()
print(f"Global var after: {global_var}")

# Exercise 3: Create a String Utilities Module
print("\nEXERCISE 3: STRING UTILITIES MODULE")
print("-" * 40)

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

def count_words(text):
    """Count words in a string"""
    return len(text.split())

def remove_duplicates(text):
    """Remove duplicate characters from string"""
    seen = set()
    result = ""
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Test the string utilities
test_string = "Hello World"
print(f"Original: '{test_string}'")
print(f"Reversed: '{reverse_string(test_string)}'")
print(f"Vowel count: {count_vowels(test_string)}")
print(f"Is 'racecar' palindrome: {is_palindrome('racecar')}")
print(f"Is 'hello' palindrome: {is_palindrome('hello')}")
print(f"Title case: '{title_case(test_string)}'")
print(f"Word count: {count_words(test_string)}")
print(f"Remove duplicates from 'hello': '{remove_duplicates('hello')}'")

# Exercise 4: Using Standard Library Modules
print("\nEXERCISE 4: STANDARD LIBRARY USAGE")
print("-" * 40)

import datetime
import random
import json

def log_event(event_type, message):
    """Log an event with timestamp"""
    timestamp = datetime.datetime.now().isoformat()
    event_id = random.randint(1000, 9999)
    
    log_entry = {
        "id": event_id,
        "timestamp": timestamp,
        "type": event_type,
        "message": message
    }
    
    return log_entry

# Create some log entries
events = [
    log_event("INFO", "Application started"),
    log_event("WARNING", "High memory usage detected"),
    log_event("ERROR", "Database connection failed"),
    log_event("INFO", "User login successful"),
    log_event("INFO", "Data processing completed")
]

# Convert to JSON and display
log_json = json.dumps(events, indent=2)
print("Event Log:")
print(log_json)

# Filter events by type
info_events = [event for event in events if event["type"] == "INFO"]
error_events = [event for event in events if event["type"] == "ERROR"]

print(f"\nInfo events count: {len(info_events)}")
print(f"Error events count: {len(error_events)}")

# Exercise 5: Function Decorators
print("\nEXERCISE 5: FUNCTION DECORATORS")
print("-" * 40)

def log_function(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"\nCalling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"{func.__name__} raised exception: {e}")
            raise
    
    return wrapper

@log_function
def add_numbers(a, b):
    """Add two numbers"""
    return a + b

@log_function
def divide_numbers(a, b):
    """Divide two numbers"""
    return a / b

# Test the decorated functions
add_numbers(5, 3)
divide_numbers(10, 2)
try:
    divide_numbers(10, 0)  # This will raise an exception
except:
    pass

# Exercise 6: Advanced Calculator with History
print("\nEXERCISE 6: ADVANCED CALCULATOR WITH HISTORY")
print("-" * 40)

class AdvancedCalculator:
    """Advanced calculator with history and multiple operations"""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
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
    
    def power(self, x, y):
        """Raise x to the power of y"""
        result = x ** y
        self.history.append(f"{x} ^ {y} = {result}")
        return result
    
    def sqrt(self, x):
        """Calculate square root"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = x ** 0.5
        self.history.append(f"√{x} = {result}")
        return result
    
    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        self.history.append(f"Stored {value} in memory")
    
    def recall_memory(self):
        """Recall value from memory"""
        self.history.append(f"Recalled {self.memory} from memory")
        return self.memory
    
    def clear_memory(self):
        """Clear memory"""
        self.memory = 0
        self.history.append("Memory cleared")
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
    
    def get_statistics(self):
        """Get statistics about calculations"""
        if not self.history:
            return "No calculations performed"
        
        # Count operations
        operations = {}
        for entry in self.history:
            if " + " in entry:
                operations["addition"] = operations.get("addition", 0) + 1
            elif " - " in entry:
                operations["subtraction"] = operations.get("subtraction", 0) + 1
            elif " * " in entry:
                operations["multiplication"] = operations.get("multiplication", 0) + 1
            elif " / " in entry:
                operations["division"] = operations.get("division", 0) + 1
            elif " ^ " in entry:
                operations["power"] = operations.get("power", 0) + 1
            elif "√" in entry:
                operations["square_root"] = operations.get("square_root", 0) + 1
        
        return {
            "total_calculations": len(self.history),
            "operations": operations
        }

# Test the advanced calculator
calc = AdvancedCalculator()

print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"2 ^ 8 = {calc.power(2, 8)}")
print(f"√16 = {calc.sqrt(16)}")

calc.store_memory(100)
print(f"Memory value: {calc.recall_memory()}")

print(f"\nCalculation history:")
for entry in calc.get_history():
    print(f"  {entry}")

print(f"\nStatistics: {calc.get_statistics()}")

# Exercise 7: Data Processing Pipeline
print("\nEXERCISE 7: DATA PROCESSING PIPELINE")
print("-" * 40)

def process_data_pipeline(data, operations):
    """
    Process data through a series of operations
    
    Args:
        data: Input data
        operations: List of functions to apply
    
    Returns:
        Processed data
    """
    result = data
    for operation in operations:
        result = operation(result)
    return result

# Define some processing operations
def filter_even_numbers(numbers):
    """Filter even numbers"""
    return [num for num in numbers if num % 2 == 0]

def square_numbers(numbers):
    """Square all numbers"""
    return [num ** 2 for num in numbers]

def sum_numbers(numbers):
    """Sum all numbers"""
    return sum(numbers)

def filter_positive_numbers(numbers):
    """Filter positive numbers"""
    return [num for num in numbers if num > 0]

# Test the data processing pipeline
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pipeline 1: Filter even numbers, then square them
pipeline1 = [filter_even_numbers, square_numbers]
result1 = process_data_pipeline(test_data, pipeline1)
print(f"Pipeline 1 (even numbers squared): {result1}")

# Pipeline 2: Filter positive numbers, then sum them
pipeline2 = [filter_positive_numbers, sum_numbers]
result2 = process_data_pipeline(test_data, pipeline2)
print(f"Pipeline 2 (sum of positive numbers): {result2}")

# Pipeline 3: Filter even, square, then sum
pipeline3 = [filter_even_numbers, square_numbers, sum_numbers]
result3 = process_data_pipeline(test_data, pipeline3)
print(f"Pipeline 3 (sum of squared even numbers): {result3}")

# Exercise 8: Module Testing Framework
print("\nEXERCISE 8: MODULE TESTING FRAMEWORK")
print("-" * 40)

def run_tests():
    """Run all tests for the module"""
    tests = [
        test_calculator,
        test_string_utilities,
        test_scope,
        test_decorators
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__} passed")
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
    
    print(f"\nTest Results: {passed} passed, {failed} failed")
    return passed, failed

def test_calculator():
    """Test calculator function"""
    assert calculator('add', 2, 3) == 5
    assert calculator('subtract', 5, 2) == 3
    assert calculator('multiply', 4, 5) == 20
    assert calculator('divide', 10, 2) == 5
    assert calculator('divide', 10, 0) == "Error: Division by zero"

def test_string_utilities():
    """Test string utility functions"""
    assert reverse_string("hello") == "olleh"
    assert count_vowels("hello") == 2
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert title_case("hello world") == "Hello World"

def test_scope():
    """Test scope understanding"""
    global global_var
    assert global_var == "I'm global"

def test_decorators():
    """Test decorator functionality"""
    # This is a simple test - in practice you'd test more thoroughly
    result = add_numbers(2, 3)
    assert result == 5

# Run the tests
print("Running module tests...")
run_tests()

print("\n" + "=" * 50)
print("PRACTICE EXERCISES COMPLETED!")
print("=" * 50) 