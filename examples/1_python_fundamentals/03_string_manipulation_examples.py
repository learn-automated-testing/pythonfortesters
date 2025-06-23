"""
Module 3: String Manipulation Examples
======================================

This module covers string manipulation in Python:
- Creating and working with strings
- String formatting methods
- String methods and operations
- String slicing and indexing

Learning Objectives:
- Master string manipulation and formatting
- Understand different string formatting methods
- Practice string slicing and indexing
- Apply string operations in test automation
"""

print("=" * 50)
print("MODULE 3: STRING MANIPULATION")
print("=" * 50)

# String Creation
print("\n1. String Creation:")

# Different ways to create strings
single_quotes = 'This is a string'
double_quotes = "This is also a string"
triple_quotes = """This is a
multi-line string"""

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes: {triple_quotes}")

# String Formatting Methods
print("\n2. String Formatting Methods:")

name = "John"
age = 25
city = "New York"

# Method 1: f-strings (Recommended - Python 3.6+)
print("Method 1 - f-strings (Recommended):")
print(f"Name: {name}, Age: {age}, City: {city}")

# Method 2: .format() method
print("\nMethod 2 - .format() method:")
print("Name: {}, Age: {}, City: {}".format(name, age, city))
print("Name: {0}, Age: {1}, City: {2}".format(name, age, city))
print("Name: {name}, Age: {age}, City: {city}".format(name=name, age=age, city=city))

# Method 3: % Operator (Old Style)
print("\nMethod 3 - % Operator (Old Style):")
print("Name: %s, Age: %d, City: %s" % (name, age, city))

# String Methods
print("\n3. String Methods:")

text = "  Hello World  "

# Case methods
print("Original text:", repr(text))
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"capitalize(): {text.capitalize()}")

# Whitespace methods
print(f"\nWhitespace methods:")
print(f"strip(): {text.strip()}")
print(f"lstrip(): {text.lstrip()}")
print(f"rstrip(): {text.rstrip()}")

# Search and replace
sample_text = "Hello World, Hello Python"
print(f"\nSearch and replace:")
print(f"Original: {sample_text}")
print(f"find('World'): {sample_text.find('World')}")
print(f"count('Hello'): {sample_text.count('Hello')}")
print(f"replace('Hello', 'Hi'): {sample_text.replace('Hello', 'Hi')}")

# String Slicing
print("\n4. String Slicing:")

text = "Python Programming"
print(f"Original text: {text}")
print(f"text[0]: {text[0]}")
print(f"text[-1]: {text[-1]}")
print(f"text[:6]: {text[:6]}")
print(f"text[-6:]: {text[-6:]}")
print(f"text[7:12]: {text[7:12]}")
print(f"text[::2]: {text[::2]}")
print(f"text[::-1]: {text[::-1]}")

# String Testing Methods
print("\n5. String Testing Methods:")

test_string = "Hello123"
print(f"Test string: {test_string}")
print(f"isalpha(): {test_string.isalpha()}")
print(f"isnumeric(): {test_string.isnumeric()}")
print(f"isalnum(): {test_string.isalnum()}")
print(f"startswith('Hello'): {test_string.startswith('Hello')}")
print(f"endswith('123'): {test_string.endswith('123')}")

# Test Automation Examples
print("\n6. Test Automation Examples:")

# URL construction
base_url = "https://practiceautomatedtesting.com"
endpoints = ["login", "dashboard", "profile", "settings"]

print("Generated test URLs:")
for endpoint in endpoints:
    full_url = f"{base_url}/{endpoint}"
    print(f"  {full_url}")

# Test data generation
def generate_test_user(user_id):
    """Generate test user data with formatted strings"""
    return {
        "id": user_id,
        "username": f"user{user_id:03d}",
        "email": f"user{user_id:03d}@example.com",
        "password": f"pass{user_id:03d}123",
        "is_active": True
    }

print("\nGenerated test users:")
for i in range(1, 4):
    user = generate_test_user(i)
    print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")

# String validation for test automation
def validate_email(email):
    """Simple email validation using string methods"""
    if "@" in email and "." in email:
        # Basic validation: check if email has proper format
        parts = email.split("@")
        if len(parts) == 2 and "." in parts[1]:
            return True
    return False

test_emails = [
    "user@example.com",
    "invalid-email",
    "user@.com",
    "user@domain.org",
    "test.user@company.co.uk"
]

print("\nEmail validation:")
for email in test_emails:
    is_valid = validate_email(email)
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"  '{email}': {status}")

# Test result formatting
test_results = [
    {"name": "Login Test", "status": "PASS", "duration": 2.5},
    {"name": "Search Test", "status": "FAIL", "duration": 1.8},
    {"name": "Logout Test", "status": "PASS", "duration": 1.2}
]

print("\nTest Results:")
for result in test_results:
    status_icon = "✅" if result["status"] == "PASS" else "❌"
    print(f"  {status_icon} {result['name']}: {result['duration']}s ({result['status']})")

# String manipulation for test data
print("\n7. String Manipulation for Test Data:")

# Clean and format test data
raw_test_data = "  Test User Name  "
cleaned_name = raw_test_data.strip().title()
print(f"Raw data: '{raw_test_data}'")
print(f"Cleaned data: '{cleaned_name}'")

# Extract information from test strings
test_log_entry = "2024-01-15 10:30:45 [INFO] Test 'Login Test' completed successfully"
parts = test_log_entry.split()
date = parts[0]
time = parts[1]
level = parts[2].strip("[]")
test_name = parts[4].strip("'")
status = " ".join(parts[5:])

print(f"\nParsed test log:")
print(f"  Date: {date}")
print(f"  Time: {time}")
print(f"  Level: {level}")
print(f"  Test: {test_name}")
print(f"  Status: {status}")

# Practice Exercise
print("\n8. Practice Exercise:")
print("Given the string: '  Python Programming  '")
original = "  Python Programming  "

# 1. Remove extra spaces
step1 = original.strip()
print(f"1. Remove extra spaces: '{step1}'")

# 2. Convert to title case
step2 = step1.title()
print(f"2. Convert to title case: '{step2}'")

# 3. Replace "Programming" with "Basics"
step3 = step2.replace("Programming", "Basics")
print(f"3. Replace 'Programming' with 'Basics': '{step3}'")

# 4. Count words
word_count = len(step3.split())
print(f"4. Count words: {word_count}")

# 5. Reverse the string
reversed_string = step3[::-1]
print(f"5. Reverse the string: '{reversed_string}'")

print("\n" + "=" * 50)
print("MODULE 3 COMPLETED!")
print("=" * 50)

"""
Practice Exercise:
Create a program that takes a sentence and:
1. Converts it to title case
2. Replaces a specific word
3. Counts the number of words
4. Reverses the sentence

Test Automation Applications:
- URL construction and manipulation
- Test data generation and formatting
- Log parsing and analysis
- Input validation and cleaning
- Test result formatting and reporting

Next Steps:
- Learn about variable assignment and types
- Explore operators and expressions
- Practice control flow statements
""" 