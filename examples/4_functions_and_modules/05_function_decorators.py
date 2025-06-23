"""
Python Functions - Function Decorators
======================================

This script covers function decorators in Python:
- Basic decorators
- Decorators with parameters
- Practical decorator examples
- Decorator best practices
"""

print("=" * 50)
print("PYTHON FUNCTIONS - FUNCTION DECORATORS")
print("=" * 50)

# Simple decorator
def timer_decorator(func):
    """Decorator that measures function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

# Using the decorator
@timer_decorator
def slow_function():
    """Function that takes time to execute"""
    import time
    time.sleep(1)
    return "Function completed"

@timer_decorator
def fast_function():
    """Function that executes quickly"""
    return "Function completed quickly"

print("\n1. BASIC DECORATOR")
print("-" * 40)

result1 = slow_function()
print(f"Result: {result1}")

result2 = fast_function()
print(f"Result: {result2}")

# Decorator with parameters
def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
                print(f"Execution {i+1}: {result}")
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Function that greets a person"""
    return f"Hello, {name}!"

print("\n2. DECORATOR WITH PARAMETERS")
print("-" * 40)

greet("Alice")

# Logging decorator
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

print("\n3. LOGGING DECORATOR")
print("-" * 40)

add_numbers(5, 3)
divide_numbers(10, 2)
try:
    divide_numbers(10, 0)  # This will raise an exception
except:
    pass

# Validation decorator
def validate_positive(func):
    """Decorator that validates arguments are positive"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Argument {arg} must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    """Calculate area of rectangle"""
    return length * width

print("\n4. VALIDATION DECORATOR")
print("-" * 40)

try:
    area = calculate_area(5, 3)
    print(f"Area: {area}")
    
    area = calculate_area(-5, 3)  # This will raise an exception
except ValueError as e:
    print(f"Validation error: {e}")

# Caching decorator
def cache_result(func):
    """Decorator that caches function results"""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create a key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"Using cached result for {func.__name__}")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"Calculated new result for {func.__name__}")
        return result
    
    return wrapper

@cache_result
def fibonacci(n):
    """Calculate Fibonacci number (inefficient implementation for demo)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n5. CACHING DECORATOR")
print("-" * 40)

print(f"Fibonacci(5): {fibonacci(5)}")
print(f"Fibonacci(5): {fibonacci(5)}")  # Uses cache
print(f"Fibonacci(3): {fibonacci(3)}")  # Uses cache

# Retry decorator
def retry(max_attempts=3, delay=1):
    """Decorator that retries function on failure"""
    import time
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        print(f"Function {func.__name__} failed after {max_attempts} attempts")
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    """Function that sometimes fails"""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("Random failure")
    return "Success!"

print("\n6. RETRY DECORATOR")
print("-" * 40)

for i in range(3):
    try:
        result = unreliable_function()
        print(f"Attempt {i+1}: {result}")
        break
    except Exception as e:
        print(f"Attempt {i+1}: {e}")

# Performance monitoring decorator
def monitor_performance(func):
    """Decorator that monitors function performance"""
    import time
    import functools
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = None
        
        try:
            import psutil
            process = psutil.Process()
            start_memory = process.memory_info().rss / 1024 / 1024  # MB
        except ImportError:
            pass
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"Function: {func.__name__}")
        print(f"Execution time: {execution_time:.4f} seconds")
        
        if start_memory is not None:
            try:
                end_memory = process.memory_info().rss / 1024 / 1024  # MB
                memory_used = end_memory - start_memory
                print(f"Memory usage: {memory_used:.2f} MB")
            except:
                pass
        
        return result
    
    return wrapper

@monitor_performance
def process_large_data():
    """Function that processes large amounts of data"""
    import time
    data = list(range(1000000))
    time.sleep(0.1)  # Simulate processing
    return len(data)

print("\n7. PERFORMANCE MONITORING DECORATOR")
print("-" * 40)

result = process_large_data()
print(f"Processed {result} items")

# Multiple decorators
def uppercase_result(func):
    """Decorator that converts result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

def add_prefix(prefix):
    """Decorator that adds prefix to result"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return f"{prefix}: {result}"
            return result
        return wrapper
    return decorator

@add_prefix("RESULT")
@uppercase_result
@log_function
def get_message(name):
    """Get a personalized message"""
    return f"Hello, {name}!"

print("\n8. MULTIPLE DECORATORS")
print("-" * 40)

message = get_message("Alice")
print(f"Final message: {message}")

# Decorator factory
def conditional_decorator(condition):
    """Decorator factory that applies decorator based on condition"""
    def decorator(func):
        if condition:
            # Apply logging decorator
            def wrapper(*args, **kwargs):
                print(f"DEBUG: Calling {func.__name__}")
                result = func(*args, **kwargs)
                print(f"DEBUG: {func.__name__} returned {result}")
                return result
            return wrapper
        else:
            # Return function unchanged
            return func
    return decorator

# Use environment variable or setting to control debugging
DEBUG_MODE = True

@conditional_decorator(DEBUG_MODE)
def production_function(x, y):
    """Function that runs in production"""
    return x * y

print("\n9. CONDITIONAL DECORATOR")
print("-" * 40)

result = production_function(5, 3)
print(f"Production result: {result}")

print("\n" + "=" * 50)
print("FUNCTION DECORATORS COMPLETED!")
print("=" * 50) 