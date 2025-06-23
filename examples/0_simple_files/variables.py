# Variables and Basic Output - Foundation for Test Automation
# This file teaches you how to store and use data in Python

# ============================================================================
# 1. BASIC VARIABLE ASSIGNMENT
# ============================================================================

# Variables are like containers that store data
# You can think of them as labeled boxes

# String variables (text)
first_name = "John"
last_name = "Doe"
email = "john.doe@example.com"

# Numeric variables
age = 25
salary = 50000.50
test_score = 95

# Boolean variables (True/False)
is_student = True
is_employed = False
test_passed = True

# ============================================================================
# 2. PRINTING VARIABLES
# ============================================================================

print("=== Basic Variable Printing ===")
print("First Name:", first_name)
print("Age:", age)
print("Is Student:", is_student)
print()

# ============================================================================
# 3. STRING FORMATTING (IMPORTANT FOR TEST REPORTS)
# ============================================================================

print("=== String Formatting Examples ===")

# Method 1: Using f-strings (recommended for Python 3.6+)
print(f"User: {first_name} {last_name}")
print(f"Age: {age} years old")
print(f"Email: {email}")

# Method 2: Using .format()
print("User: {} {}".format(first_name, last_name))
print("Salary: ${:,.2f}".format(salary))

# Method 3: Using % operator (older style)
print("Test Score: %d%%" % test_score)
print()

# ============================================================================
# 4. VARIABLE NAMING CONVENTIONS
# ============================================================================

print("=== Variable Naming Examples ===")

# Good variable names (descriptive and clear)
user_id = "12345"
test_case_name = "login_functionality"
expected_result = "success"
actual_result = "success"

# Bad variable names (avoid these)
x = "something"  # Too vague
a = 123          # Not descriptive
test1 = "data"   # Not clear what it contains

print(f"User ID: {user_id}")
print(f"Test Case: {test_case_name}")
print(f"Expected: {expected_result}, Actual: {actual_result}")
print()

# ============================================================================
# 5. VARIABLE TYPES AND TYPE CHECKING
# ============================================================================

print("=== Variable Types ===")

# Check the type of variables
print(f"Type of first_name: {type(first_name)}")
print(f"Type of age: {type(age)}")
print(f"Type of salary: {type(salary)}")
print(f"Type of is_student: {type(is_student)}")
print()

# ============================================================================
# 6. VARIABLE OPERATIONS
# ============================================================================

print("=== Variable Operations ===")

# String concatenation
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# Numeric operations
years_experience = 3
total_salary = salary * (1 + years_experience * 0.1)
print(f"Total Salary with experience: ${total_salary:,.2f}")

# Boolean operations
can_drive = age >= 18 and is_student
print(f"Can drive: {can_drive}")
print()

# ============================================================================
# 7. PRACTICAL EXAMPLES FOR TEST AUTOMATION
# ============================================================================

print("=== Test Automation Examples ===")

# Test data variables
test_username = "testuser"
test_password = "testpass123"
base_url = "https://example.com"
timeout = 30

# Test status variables
test_status = "PASSED"
error_message = ""
test_duration = 2.5

# Test configuration
browser_name = "Chrome"
headless_mode = True
screenshot_on_failure = True

# Print test information
print(f"Test Configuration:")
print(f"  Browser: {browser_name}")
print(f"  Headless: {headless_mode}")
print(f"  Timeout: {timeout} seconds")
print(f"  Base URL: {base_url}")
print()

print(f"Test Results:")
print(f"  Status: {test_status}")
print(f"  Duration: {test_duration} seconds")
if error_message:
    print(f"  Error: {error_message}")
print()

# ============================================================================
# 8. VARIABLE SCOPE AND REASSIGNMENT
# ============================================================================

print("=== Variable Reassignment ===")

# Variables can be changed
counter = 1
print(f"Initial counter: {counter}")

counter = counter + 1
print(f"After increment: {counter}")

counter += 1  # Shorthand for counter = counter + 1
print(f"After shorthand increment: {counter}")

# String variables can be updated
status = "running"
print(f"Status: {status}")

status = "completed"
print(f"Updated status: {status}")
print()

# ============================================================================
# 9. CONSTANTS (CONVENTION)
# ============================================================================

print("=== Constants (Convention) ===")

# In Python, we use UPPERCASE for constants (convention, not enforced)
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT = 30
SUCCESS_STATUS = "PASSED"
FAILURE_STATUS = "FAILED"

print(f"Max retry attempts: {MAX_RETRY_ATTEMPTS}")
print(f"Default timeout: {DEFAULT_TIMEOUT} seconds")
print(f"Success status: {SUCCESS_STATUS}")
print(f"Failure status: {FAILURE_STATUS}")
print()

# ============================================================================
# 10. PRACTICAL EXERCISES
# ============================================================================

print("=== Practice Exercises ===")
print("Try these exercises to reinforce your learning:")
print()
print("1. Create variables for a test case:")
print("   - test_name = 'your test name'")
print("   - expected_result = 'expected outcome'")
print("   - actual_result = 'actual outcome'")
print()
print("2. Create variables for a user:")
print("   - username, password, email, role")
print()
print("3. Create variables for test configuration:")
print("   - browser, url, timeout, headless_mode")
print()
print("4. Use f-strings to print a test report:")
print("   - Test name, status, duration, and any errors")
print()

# ============================================================================
# 11. SUMMARY
# ============================================================================

print("=== Summary ===")
print("✓ Variables store data with descriptive names")
print("✓ Use f-strings for easy string formatting")
print("✓ Choose clear, descriptive variable names")
print("✓ Variables can be reassigned")
print("✓ Use UPPERCASE for constants (convention)")
print("✓ Variables are essential for test automation")
print()

print("🎉 You've learned the basics of variables!")
print("Next: Learn about data types in datatype.py")