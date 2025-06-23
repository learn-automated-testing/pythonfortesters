"""
Python Functions - Scope Examples
=================================

This script covers scope concepts in Python:
- Local vs Global scope
- Using global keyword
- Nested functions and nonlocal keyword
- LEGB rule demonstration
"""

print("=" * 50)
print("PYTHON FUNCTIONS - SCOPE EXAMPLES")
print("=" * 50)

# Global variable
x = "global"

def my_function():
    """Function demonstrating local vs global scope"""
    # Local variable (same name as global)
    x = "local"
    print("Inside function:", x)

print("\n1. LOCAL VS GLOBAL SCOPE")
print("-" * 40)

my_function()
print("Outside function:", x)

# Another example with different variable names
global_var = 100

def test_scope():
    """Function showing local and global variables"""
    local_var = 200
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

test_scope()
print(f"Outside function - global_var: {global_var}")
# print(f"Outside function - local_var: {local_var}")  # This would cause an error!

# Global keyword examples
counter = 0

def increment():
    """Function that modifies global variable"""
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")

def reset_counter():
    """Function that resets global variable"""
    global counter
    counter = 0
    print(f"Counter reset to: {counter}")

print("\n2. USING GLOBAL KEYWORD")
print("-" * 40)

print(f"Initial counter: {counter}")
increment()
increment()
increment()
reset_counter()

# Example with multiple global variables
name = "Unknown"
age = 0

def update_profile(new_name, new_age):
    """Function that updates multiple global variables"""
    global name, age
    name = new_name
    age = new_age
    print(f"Profile updated: {name}, {age} years old")

update_profile("Alice", 25)
print(f"Current profile: {name}, {age} years old")

# Nested functions and nonlocal
def outer():
    """Outer function with nested function"""
    x = "outer"
    
    def inner():
        """Inner function that modifies nonlocal variable"""
        nonlocal x
        x = "inner"
        print(f"Inside inner: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

print("\n3. NESTED FUNCTIONS AND NONLOCAL")
print("-" * 40)

outer()

# More complex nested function example
def calculator():
    """Function that returns nested functions with shared state"""
    result = 0
    
    def add(x):
        """Add to the shared result"""
        nonlocal result
        result += x
        return result
    
    def subtract(x):
        """Subtract from the shared result"""
        nonlocal result
        result -= x
        return result
    
    def get_result():
        """Get the current result"""
        return result
    
    def reset():
        """Reset the result to zero"""
        nonlocal result
        result = 0
        return result
    
    return add, subtract, get_result, reset

print("\n4. COMPLEX NESTED FUNCTION EXAMPLE")
print("-" * 40)

# Using the calculator
add_func, subtract_func, get_result_func, reset_func = calculator()

print(f"Initial result: {get_result_func()}")
print(f"After adding 5: {add_func(5)}")
print(f"After adding 3: {add_func(3)}")
print(f"After subtracting 2: {subtract_func(2)}")
print(f"Final result: {get_result_func()}")
print(f"After reset: {reset_func()}")

# LEGB Rule demonstration
def legb_demo():
    """Demonstrate LEGB (Local, Enclosing, Global, Built-in) rule"""
    
    # Local variable
    x = "local"
    
    def inner():
        # This will use the enclosing (nonlocal) x
        nonlocal x
        print(f"Enclosing x: {x}")
        
        def innermost():
            # This will also use the enclosing x
            nonlocal x
            x = "innermost"
            print(f"Innermost x: {x}")
        
        innermost()
        print(f"After innermost: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

print("\n5. LEGB RULE DEMONSTRATION")
print("-" * 40)

legb_demo()

# Practical example: Counter with different scopes
class Counter:
    """Class-based counter for comparison"""
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count

def create_function_counter():
    """Create a counter using function scope"""
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def reset():
        nonlocal count
        count = 0
        return count
    
    def get_count():
        return count
    
    return increment, reset, get_count

print("\n6. PRACTICAL EXAMPLE - COUNTER COMPARISON")
print("-" * 40)

# Class-based counter
class_counter = Counter()
print(f"Class counter - increment: {class_counter.increment()}")
print(f"Class counter - increment: {class_counter.increment()}")
print(f"Class counter - reset: {class_counter.reset()}")

# Function-based counter
func_increment, func_reset, func_get = create_function_counter()
print(f"Function counter - increment: {func_increment()}")
print(f"Function counter - increment: {func_increment()}")
print(f"Function counter - get count: {func_get()}")
print(f"Function counter - reset: {func_reset()}")

# Scope best practices
print("\n7. SCOPE BEST PRACTICES")
print("-" * 40)

# Good practice: Return values instead of modifying globals
def calculate_area(length, width):
    """Good: Returns a value instead of modifying global state"""
    return length * width

# Good practice: Pass data as parameters
def process_user_data(user_data):
    """Good: Takes data as parameter instead of accessing globals"""
    return {
        "name": user_data.get("name", "Unknown"),
        "age": user_data.get("age", 0),
        "processed": True
    }

# Example usage
area = calculate_area(10, 5)
print(f"Area: {area}")

user_data = {"name": "Alice", "age": 25}
processed = process_user_data(user_data)
print(f"Processed data: {processed}")

print("\n" + "=" * 50)
print("SCOPE EXAMPLES COMPLETED!")
print("=" * 50) 