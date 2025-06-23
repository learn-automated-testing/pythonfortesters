"""
Python Functions - Variable Arguments
====================================

This script covers variable arguments (*args and **kwargs) in Python functions:
- *args for variable number of positional arguments
- **kwargs for variable number of keyword arguments
- Combining both in flexible functions
"""

print("=" * 50)
print("PYTHON FUNCTIONS - VARIABLE ARGUMENTS")
print("=" * 50)

# *args for variable number of positional arguments
def sum_all(*args):
    """Sum all provided arguments"""
    return sum(args)

print("\n1. *ARGS - VARIABLE POSITIONAL ARGUMENTS")
print("-" * 40)

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
print(f"Sum of 10, 20: {sum_all(10, 20)}")
print(f"Sum of single number 42: {sum_all(42)}")

# Function that finds the maximum of any number of arguments
def find_max(*args):
    """Find the maximum value from any number of arguments"""
    if not args:
        return None
    return max(args)

print(f"\nMaximum of 1, 5, 3, 9, 2: {find_max(1, 5, 3, 9, 2)}")
print(f"Maximum of 10, 20, 30: {find_max(10, 20, 30)}")

# **kwargs for variable number of keyword arguments
def print_info(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n2. **KWARGS - VARIABLE KEYWORD ARGUMENTS")
print("-" * 40)

print("Person info:")
print_info(name="Alice", age=25, city="New York")

print("\nEmployee info:")
print_info(title="Manager", department="Engineering", salary=75000, experience=5)

# Function that creates a dictionary from keyword arguments
def create_person(**kwargs):
    """Create a person dictionary from keyword arguments"""
    person = {
        "name": kwargs.get("name", "Unknown"),
        "age": kwargs.get("age", 0),
        "city": kwargs.get("city", "Unknown"),
        "occupation": kwargs.get("occupation", "Unknown")
    }
    # Add any additional fields
    for key, value in kwargs.items():
        if key not in person:
            person[key] = value
    return person

print("\n3. CREATING OBJECTS WITH KWARGS")
print("-" * 40)

person1 = create_person(name="Alice", age=25, city="New York")
person2 = create_person(name="Bob", age=30, occupation="Engineer", hobby="Reading")

print("Person 1:", person1)
print("Person 2:", person2)

# Combining both *args and **kwargs
def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("\n4. COMBINING *ARGS AND **KWARGS")
print("-" * 40)

flexible_function(1, 2, 3, name="Alice", age=25)
flexible_function("hello", "world", title="Greeting", count=2)
flexible_function(42, message="Answer to everything")

# Practical example: Calculator with variable arguments
def calculate(operation, *args, **kwargs):
    """Flexible calculator that can handle different operations"""
    if operation == "sum":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "average":
        return sum(args) / len(args) if args else 0
    elif operation == "info":
        return {
            "operation": operation,
            "arguments": args,
            "options": kwargs
        }
    else:
        return f"Unknown operation: {operation}"

print("\n5. PRACTICAL EXAMPLE - FLEXIBLE CALCULATOR")
print("-" * 40)

print(f"Sum of 1, 2, 3, 4: {calculate('sum', 1, 2, 3, 4)}")
print(f"Multiply 2, 3, 4: {calculate('multiply', 2, 3, 4)}")
print(f"Average of 10, 20, 30: {calculate('average', 10, 20, 30)}")
print(f"Info with options: {calculate('info', 1, 2, 3, precision=2, round_result=True)}")

# Function that processes both types of arguments
def process_data(*args, **kwargs):
    """Process both positional and keyword data"""
    result = {
        "numbers": [],
        "strings": [],
        "other": [],
        "metadata": kwargs
    }
    
    for arg in args:
        if isinstance(arg, (int, float)):
            result["numbers"].append(arg)
        elif isinstance(arg, str):
            result["strings"].append(arg)
        else:
            result["other"].append(arg)
    
    return result

print("\n6. DATA PROCESSING WITH VARIABLE ARGUMENTS")
print("-" * 40)

data = process_data(1, 2, "hello", 3.14, "world", True, 
                   source="user_input", timestamp="2024-01-01")
print("Processed data:", data)

print("\n" + "=" * 50)
print("VARIABLE ARGUMENTS COMPLETED!")
print("=" * 50) 