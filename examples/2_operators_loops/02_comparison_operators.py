"""
Comparison Operators in Python
Examples and exercises for comparison operators: ==, !=, >, <, >=, <=
"""

print("=== Comparison Operators Examples ===")

# Basic comparison operations
a = 5
b = 3
c = 5

print(f"a = {a}, b = {b}, c = {c}")
print(f"a == b: {a == b}")    # False
print(f"a == c: {a == c}")    # True
print(f"a != b: {a != b}")    # True
print(f"a > b: {a > b}")      # True
print(f"a < b: {a < b}")      # False
print(f"a >= b: {a >= b}")    # True
print(f"a <= b: {a <= b}")    # False

print("\n=== String Comparisons ===")

# String comparisons
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"name1 = '{name1}', name2 = '{name2}', name3 = '{name3}'")
print(f"name1 == name2: {name1 == name2}")    # False
print(f"name1 == name3: {name1 == name3}")    # True
print(f"name1 < name2: {name1 < name2}")      # True (alphabetical)
print(f"name1 > name2: {name1 > name2}")      # False

print("\n=== Practical Examples ===")

# Age verification
age = 20
print(f"Age: {age}")
if age >= 18:
    print("✅ Eligible to vote")
else:
    print("❌ Not eligible to vote")

# Grade checking
score = 85
print(f"\nScore: {score}")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Number validation
numbers = [5, -1, 0, 10, 100]
print(f"\nValidating numbers: {numbers}")
for num in numbers:
    if 0 < num < 50:
        print(f"{num}: Valid (between 0 and 50)")
    else:
        print(f"{num}: Invalid")

print("\n=== Practice Exercises ===")

# Exercise 1: Password strength checker
def check_password_strength(password):
    """Check if password meets strength requirements"""
    is_long_enough = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    if is_long_enough and has_uppercase and has_lowercase and has_digit:
        return "Strong"
    elif is_long_enough and (has_uppercase or has_lowercase):
        return "Medium"
    else:
        return "Weak"

# Test the function
passwords = ["abc123", "Password123", "weak", "STRONG123"]
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password '{pwd}': {strength}")

# Exercise 2: Temperature converter with validation
def convert_temperature(temp, unit):
    """Convert temperature between Celsius and Fahrenheit with validation"""
    if unit.upper() == 'C':
        if temp >= -273.15:  # Absolute zero
            fahrenheit = (temp * 9/5) + 32
            return f"{temp}°C = {fahrenheit}°F"
        else:
            return "Invalid temperature (below absolute zero)"
    elif unit.upper() == 'F':
        if temp >= -459.67:  # Absolute zero in Fahrenheit
            celsius = (temp - 32) * 5/9
            return f"{temp}°F = {celsius}°C"
        else:
            return "Invalid temperature (below absolute zero)"
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit"

# Test the function
test_temps = [(25, 'C'), (77, 'F'), (-300, 'C'), (100, 'X')]
for temp, unit in test_temps:
    result = convert_temperature(temp, unit)
    print(result)

# Exercise 3: Number range validator
def validate_number_range(number, min_val, max_val):
    """Validate if a number is within a specified range"""
    if min_val <= number <= max_val:
        return f"{number} is within range [{min_val}, {max_val}]"
    elif number < min_val:
        return f"{number} is below minimum ({min_val})"
    else:
        return f"{number} is above maximum ({max_val})"

# Test the function
test_numbers = [5, 15, 25, 35]
min_val = 10
max_val = 30
print(f"\nValidating numbers in range [{min_val}, {max_val}]:")
for num in test_numbers:
    result = validate_number_range(num, min_val, max_val)
    print(result) 