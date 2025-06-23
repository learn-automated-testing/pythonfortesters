"""
Python Functions - Lambda Functions and Advanced Concepts
========================================================

This script covers advanced function concepts in Python:
- Lambda functions (anonymous functions)
- Functions as arguments
- Higher-order functions
- Practical applications
"""

print("=" * 50)
print("PYTHON FUNCTIONS - LAMBDA & ADVANCED CONCEPTS")
print("=" * 50)

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
add = lambda x, y: x + y
multiply = lambda x, y: x * y

print("\n1. BASIC LAMBDA FUNCTIONS")
print("-" * 40)

print(f"Square of 5: {square(5)}")
print(f"Sum of 3 and 7: {add(3, 7)}")
print(f"Multiply 4 and 6: {multiply(4, 6)}")

# Lambda with conditional logic
is_even = lambda x: x % 2 == 0
is_positive = lambda x: x > 0
get_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

print(f"\nIs 8 even? {is_even(8)}")
print(f"Is -5 positive? {is_positive(-5)}")
print(f"Grade for score 85: {get_grade(85)}")
print(f"Grade for score 95: {get_grade(95)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, numbers))
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("\n2. LAMBDA WITH BUILT-IN FUNCTIONS")
print("-" * 40)

print(f"Original numbers: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Doubled numbers: {doubled_numbers}")

# More complex lambda examples
words = ["hello", "world", "python", "programming", "lambda"]
long_words = list(filter(lambda word: len(word) > 5, words))
upper_words = list(map(lambda word: word.upper(), words))
word_lengths = list(map(lambda word: len(word), words))

print(f"\nOriginal words: {words}")
print(f"Long words (>5 chars): {long_words}")
print(f"Upper case words: {upper_words}")
print(f"Word lengths: {word_lengths}")

# Functions as arguments
def apply_operation(func, x, y):
    """Apply a function to two arguments"""
    return func(x, y)

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    return a / b if b != 0 else "Error: Division by zero"

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

print("\n3. FUNCTIONS AS ARGUMENTS")
print("-" * 40)

print(f"Apply multiply: {apply_operation(multiply, 4, 5)}")
print(f"Apply divide: {apply_operation(divide, 10, 2)}")
print(f"Apply lambda: {apply_operation(lambda x, y: x - y, 10, 3)}")
print(f"Apply power: {apply_operation(power, 2, 3)}")

# Higher-order functions
def create_operation(operation_type):
    """Create a function based on operation type"""
    if operation_type == "add":
        return lambda x, y: x + y
    elif operation_type == "subtract":
        return lambda x, y: x - y
    elif operation_type == "multiply":
        return lambda x, y: x * y
    elif operation_type == "divide":
        return lambda x, y: x / y if y != 0 else "Error: Division by zero"
    else:
        return lambda x, y: f"Unknown operation: {operation_type}"

print("\n4. HIGHER-ORDER FUNCTIONS")
print("-" * 40)

add_func = create_operation("add")
subtract_func = create_operation("subtract")
multiply_func = create_operation("multiply")

print(f"Add function: {add_func(5, 3)}")
print(f"Subtract function: {subtract_func(10, 4)}")
print(f"Multiply function: {multiply_func(6, 7)}")

# Sorting with lambda
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78},
    {"name": "Diana", "age": 21, "grade": 88}
]

print("\n5. SORTING WITH LAMBDA")
print("-" * 40)

# Sort by age
sorted_by_age = sorted(students, key=lambda student: student["age"])
print("Sorted by age:")
for student in sorted_by_age:
    print(f"  {student['name']}: {student['age']} years old")

# Sort by grade (descending)
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
print("\nSorted by grade (descending):")
for student in sorted_by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Sort by name
sorted_by_name = sorted(students, key=lambda student: student["name"])
print("\nSorted by name:")
for student in sorted_by_name:
    print(f"  {student['name']}: {student['grade']}")

# Practical examples with lambda
print("\n6. PRACTICAL LAMBDA EXAMPLES")
print("-" * 40)

# Data processing
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter and transform in one go
processed_data = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data)))
print(f"Even numbers squared: {processed_data}")

# String processing
sentences = [
    "Hello world",
    "Python is awesome",
    "Lambda functions are powerful",
    "Programming is fun"
]

# Count words in each sentence
word_counts = list(map(lambda sentence: len(sentence.split()), sentences))
print(f"Word counts: {word_counts}")

# Find sentences with more than 3 words
long_sentences = list(filter(lambda sentence: len(sentence.split()) > 3, sentences))
print(f"Long sentences: {long_sentences}")

# Mathematical operations
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Calculate distances from origin
distances = list(map(lambda point: (point[0] ** 2 + point[1] ** 2) ** 0.5, points))
print(f"Distances from origin: {distances}")

# Find points in first quadrant
first_quadrant = list(filter(lambda point: point[0] > 0 and point[1] > 0, points))
print(f"Points in first quadrant: {first_quadrant}")

# Advanced lambda examples
print("\n7. ADVANCED LAMBDA EXAMPLES")
print("-" * 40)

# Lambda with multiple conditions
classify_number = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

test_numbers = [-5, 0, 10, -3, 7]
classifications = list(map(classify_number, test_numbers))
print(f"Number classifications: {list(zip(test_numbers, classifications))}")

# Lambda with string operations
format_name = lambda first, last: f"{first.title()} {last.title()}"
names = [("john", "doe"), ("jane", "smith"), ("bob", "jones")]
formatted_names = list(map(lambda name: format_name(name[0], name[1]), names))
print(f"Formatted names: {formatted_names}")

# Lambda for data validation
validate_email = lambda email: '@' in email and '.' in email.split('@')[1]
emails = ["user@example.com", "invalid-email", "test@domain.org", "no-at-sign"]
valid_emails = list(filter(validate_email, emails))
print(f"Valid emails: {valid_emails}")

# Performance comparison
print("\n8. PERFORMANCE COMPARISON")
print("-" * 40)

import time

# Regular function
def square_regular(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

# Test performance
numbers = list(range(1000000))

# Test regular function
start_time = time.time()
result1 = list(map(square_regular, numbers[:1000]))
regular_time = time.time() - start_time

# Test lambda function
start_time = time.time()
result2 = list(map(square_lambda, numbers[:1000]))
lambda_time = time.time() - start_time

print(f"Regular function time: {regular_time:.6f} seconds")
print(f"Lambda function time: {lambda_time:.6f} seconds")
print(f"Results are equal: {result1 == result2}")

print("\n" + "=" * 50)
print("LAMBDA FUNCTIONS COMPLETED!")
print("=" * 50) 