"""
Module 1: Hello World Examples
==============================

This module covers basic Python programming concepts including:
- Writing your first Python program
- Using the print() function
- Working with variables
- Different ways to display output

Learning Objectives:
- Write your first Python program (Hello World)
- Understand different ways to use print() function
- Work with variables and string formatting
"""

print("=" * 50)
print("MODULE 1: HELLO WORLD EXAMPLES")
print("=" * 50)

# Basic Hello World
print("\n1. Basic Hello World:")
print("Hello, World!")

# Hello World with Variables
print("\n2. Hello World with Variables:")
message = "Hello, World!"
print(message)

# Multiple Ways to Print
print("\n3. Multiple Ways to Print:")

# Method 1: Multiple arguments
print("Method 1 - Multiple arguments:")
print("Hello", "World", "from", "Python")

# Method 2: String concatenation
print("\nMethod 2 - String concatenation:")
print("Hello" + " " + "World" + " " + "from" + " " + "Python")

# Method 3: .format() method
print("\nMethod 3 - .format() method:")
print("Hello {} from {}".format("World", "Python"))

# Method 4: f-strings (recommended)
print("\nMethod 4 - f-strings (recommended):")
print(f"Hello {'World'} from {'Python'}")

# Interactive Hello World
print("\n4. Interactive Hello World:")
print("This demonstrates getting user input and creating personalized output")

# Uncomment the lines below to make it interactive
# name = input("Enter your name: ")
# print(f"Hello, {name}! Welcome to Python programming!")

# Test Automation Example
print("\n5. Test Automation Example:")
test_name = "Login Test"
test_status = "PASSED"
test_duration = 2.5

print(f"Test: {test_name}")
print(f"Status: {test_status}")
print(f"Duration: {test_duration} seconds")

# Multiple test results
print("\n6. Multiple Test Results:")
test_results = [
    {"name": "Login Test", "status": "PASS", "duration": 2.5},
    {"name": "Search Test", "status": "PASS", "duration": 1.8},
    {"name": "Logout Test", "status": "FAIL", "duration": 1.2}
]

for result in test_results:
    status_icon = "✅" if result["status"] == "PASS" else "❌"
    print(f"{status_icon} {result['name']}: {result['duration']}s ({result['status']})")

print("\n" + "=" * 50)
print("MODULE 1 COMPLETED!")
print("=" * 50)

"""
Practice Exercise:
Try creating a program that asks for your name and prints a personalized greeting.
You can uncomment the interactive section above to see how it works.

Next Steps:
- Experiment with different print() methods
- Try creating variables with different types of data
- Practice string formatting with f-strings
""" 