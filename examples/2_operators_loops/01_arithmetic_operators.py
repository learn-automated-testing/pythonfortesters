"""
Arithmetic Operators in Python
Examples and exercises for arithmetic operators: +, -, *, /, %, //, **
"""

print("=== Arithmetic Operators Examples ===")

# Basic arithmetic operations
x = 10
y = 3

print(f"x = {x}, y = {y}")
print(f"Addition: x + y = {x + y}")           # 13
print(f"Subtraction: x - y = {x - y}")        # 7
print(f"Multiplication: x * y = {x * y}")     # 30
print(f"Division: x / y = {x / y}")           # 3.333...
print(f"Modulus: x % y = {x % y}")            # 1
print(f"Floor Division: x // y = {x // y}")   # 3
print(f"Exponentiation: x ** y = {x ** y}")   # 1000

print("\n=== Practical Examples ===")

# Check even/odd numbers
print("Even/Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Pagination example
print("\nPagination example:")
total_items = 25
items_per_page = 5
total_pages = (total_items + items_per_page - 1) // items_per_page
print(f"Total items: {total_items}")
print(f"Items per page: {items_per_page}")
print(f"Total pages needed: {total_pages}")

# Calculate average
print("\nAverage calculation:")
scores = [85, 92, 78, 96, 88]
total = sum(scores)
count = len(scores)
average = total / count
print(f"Scores: {scores}")
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")

print("\n=== Practice Exercises ===")

# Exercise 1: Calculate area and perimeter of a rectangle
def calculate_rectangle(length, width):
    """Calculate area and perimeter of a rectangle"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Test the function
length = 5
width = 3
area, perimeter = calculate_rectangle(length, width)
print(f"Rectangle: {length} x {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Exercise 2: Convert temperature
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
celsius_temps = [0, 25, 100]
for temp in celsius_temps:
    fahr = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {fahr}°F")

# Exercise 3: Calculate compound interest
def compound_interest(principal, rate, time, compounds_per_year=1):
    """Calculate compound interest"""
    amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
    interest = amount - principal
    return interest, amount

# Test the function
principal = 1000
rate = 0.05  # 5%
time = 2     # 2 years
interest, total = compound_interest(principal, rate, time)
print(f"Principal: ${principal}")
print(f"Rate: {rate*100}%")
print(f"Time: {time} years")
print(f"Interest earned: ${interest:.2f}")
print(f"Total amount: ${total:.2f}") 