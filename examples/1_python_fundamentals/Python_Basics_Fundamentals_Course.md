# Python Basics Fundamentals Course

## Course Overview

This course covers the fundamental concepts of Python programming essential for test automation and software development. The course is designed to be hands-on with practical examples and exercises.

**📚 Course Materials:** Use the accompanying Colab notebook: `Python_Basics_Fundamentals.ipynb`

**⏱️ Estimated Duration:** 4-6 hours

**🎯 Prerequisites:** None - This is a beginner-friendly course

---

## Learning Objectives

By the end of this course, you will be able to:

- ✅ Write your first Python program (Hello World)
- ✅ Understand different data types in Python
- ✅ Learn how to check data types at runtime
- ✅ Master string manipulation and formatting
- ✅ Practice variable assignment and type conversion
- ✅ Apply concepts to test automation scenarios

---

## Module 1: Hello World

### What You'll Learn
- Writing your first Python program
- Using the `print()` function
- Working with variables
- Different ways to display output

### Key Concepts

#### Basic Hello World
```python
print("Hello, World!")
```

#### Hello World with Variables
```python
message = "Hello, World!"
print(message)
```

#### Multiple Ways to Print
```python
# Method 1: Multiple arguments
print("Hello", "World", "from", "Python")

# Method 2: String concatenation
print("Hello" + " " + "World" + " " + "from" + " " + "Python")

# Method 3: .format() method
print("Hello {} from {}".format("World", "Python"))

# Method 4: f-strings (recommended)
print(f"Hello {'World'} from {'Python'}")
```

### Practice Exercise
Try creating a program that asks for your name and prints a personalized greeting.

**💡 Tip:** Use the Colab notebook for hands-on practice with these examples.

---

## Module 2: Data Types and Type Checking

### What You'll Learn
- Understanding Python's built-in data types
- Using the `type()` function
- Working with different data structures
- Type checking at runtime

### Python Data Types Overview

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer numbers | `42`, `-17`, `0` |
| `float` | Decimal numbers | `3.14`, `-2.5`, `0.0` |
| `str` | Text strings | `"Hello"`, `'Python'` |
| `bool` | True/False values | `True`, `False` |
| `list` | Mutable sequences | `[1, 2, 3]`, `["a", "b"]` |
| `tuple` | Immutable sequences | `(1, 2, 3)`, `("x", "y")` |
| `dict` | Key-value pairs | `{"name": "John", "age": 25}` |
| `set` | Unique collections | `{1, 2, 3}`, `{"a", "b"}` |
| `None` | Absence of value | `None` |

### Type Checking Examples

```python
# Check types at runtime
age = 25
name = "John"
is_student = True

print(f"Age: {age}, Type: {type(age)}")
print(f"Name: {name}, Type: {type(name)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
```

### Collections in Python

#### Lists (Mutable)
```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
```

#### Tuples (Immutable)
```python
coordinates = (10, 20)
person = ("John", 25, "Engineer")
```

#### Dictionaries (Key-Value Pairs)
```python
person_info = {
    "name": "John Doe",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Java", "SQL"]
}
```

#### Sets (Unique Elements)
```python
unique_numbers = {1, 2, 3, 4, 5}
unique_letters = {"a", "b", "c", "a", "b"}  # Duplicates removed
```

### Practice Exercise
Create variables of different types and use `type()` to verify their types.

---

## Module 3: String Manipulation

### What You'll Learn
- Creating and working with strings
- String formatting methods
- String methods and operations
- String slicing and indexing

### String Creation

```python
# Different ways to create strings
single_quotes = 'This is a string'
double_quotes = "This is also a string"
triple_quotes = """This is a
multi-line string"""
```

### String Formatting Methods

#### 1. f-strings (Recommended - Python 3.6+)
```python
name = "John"
age = 25
city = "New York"

print(f"Name: {name}, Age: {age}, City: {city}")
```

#### 2. .format() Method
```python
print("Name: {}, Age: {}, City: {}".format(name, age, city))
print("Name: {0}, Age: {1}, City: {2}".format(name, age, city))
print("Name: {name}, Age: {age}, City: {city}".format(name=name, age=age, city=city))
```

#### 3. % Operator (Old Style)
```python
print("Name: %s, Age: %d, City: %s" % (name, age, city))
```

### String Methods

```python
text = "  Hello World  "

# Case methods
print(text.upper())      # "  HELLO WORLD  "
print(text.lower())      # "  hello world  "
print(text.title())      # "  Hello World  "
print(text.capitalize()) # "  hello world  "

# Whitespace methods
print(text.strip())      # "Hello World"
print(text.lstrip())     # "Hello World  "
print(text.rstrip())     # "  Hello World"

# Search and replace
sample_text = "Hello World, Hello Python"
print(sample_text.find('World'))           # 6
print(sample_text.count('Hello'))          # 2
print(sample_text.replace('Hello', 'Hi'))  # "Hi World, Hi Python"
```

### String Slicing

```python
text = "Python Programming"

print(text[0])      # 'P'
print(text[-1])     # 'g'
print(text[:6])     # 'Python'
print(text[-6:])    # 'amming'
print(text[7:12])   # 'Progr'
print(text[::2])    # 'Pto rgamn'
print(text[::-1])   # 'gnimmargorP nohtyP'
```

### String Testing Methods

```python
test_string = "Hello123"

print(test_string.isalpha())      # False
print(test_string.isnumeric())    # False
print(test_string.isalnum())      # True
print(test_string.startswith('Hello'))  # True
print(test_string.endswith('123'))      # True
```

### Practice Exercise
Create a program that takes a sentence and:
1. Converts it to title case
2. Replaces a specific word
3. Counts the number of words
4. Reverses the sentence

---

## Module 4: Variable Assignment and Types

### What You'll Learn
- Creating and assigning variables
- Variable naming conventions
- Dynamic typing in Python
- Type conversion and casting

### Basic Variable Assignment

```python
# Simple assignment
x = 10
y = 20
z = x + y

# Multiple assignment
a, b, c = 1, 2, 3

# Unpacking from list
numbers = [10, 20, 30]
first, second, third = numbers
```

### Variable Naming Conventions

#### Good Variable Names
```python
user_name = "John"
user_age = 25
is_active = True
total_count = 100
```

#### Variable Naming Rules
- ✅ Can contain letters, numbers, and underscores
- ✅ Must start with a letter or underscore
- ✅ Cannot use reserved keywords
- ✅ Case sensitive

#### Examples of Valid Names
```python
my_variable = "valid"
_private_var = "valid"
var123 = "valid"
```

#### Examples of Invalid Names (Avoid These)
```python
# 123var = "invalid"  # Can't start with number
# my-var = "invalid"  # Can't use hyphens
# class = "invalid"   # Can't use reserved keywords
```

### Dynamic Typing

Python is dynamically typed, meaning variables can change type:

```python
variable = 42
print(f"Variable: {variable}, Type: {type(variable)}")

variable = "Hello"
print(f"Variable: {variable}, Type: {type(variable)}")

variable = [1, 2, 3]
print(f"Variable: {variable}, Type: {type(variable)}")

variable = True
print(f"Variable: {variable}, Type: {type(variable)}")
```

### Type Conversion (Casting)

```python
# String to number
string_number = "123"
integer_number = int(string_number)
float_number = float(string_number)

# Number to string
number = 42
string_number = str(number)

# List to tuple and vice versa
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
my_list_again = list(my_tuple)
```

### Boolean Conversion

```python
# Truthy values (convert to True)
print(bool(1))        # True
print(bool(42))       # True
print(bool("hello"))  # True
print(bool([1, 2, 3])) # True

# Falsy values (convert to False)
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False
```

### Practice Exercise
Create variables of different types, then convert them to other types and verify the conversions.

---

## Module 5: Practical Examples for Test Automation

### What You'll Learn
- Applying Python basics to test automation
- Generating test data
- Working with URLs and test results
- Data validation

### Test Data Generation

```python
def generate_test_user(user_id):
    """Generate test user data"""
    return {
        "id": user_id,
        "username": f"user{user_id:03d}",
        "email": f"user{user_id:03d}@example.com",
        "password": f"pass{user_id:03d}123",
        "is_active": True
    }

# Generate test users
test_users = []
for i in range(1, 4):
    user = generate_test_user(i)
    test_users.append(user)

print("Generated test users:")
for user in test_users:
    print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
```

### URL Construction

```python
base_url = "https://practiceautomatedtesting.com"
endpoints = ["login", "dashboard", "profile", "settings"]

print("Generated test URLs:")
for endpoint in endpoints:
    full_url = f"{base_url}/{endpoint}"
    print(f"  {full_url}")
```

### Test Result Formatting

```python
test_results = [
    {"name": "Login Test", "status": "PASS", "duration": 2.5},
    {"name": "Search Test", "status": "FAIL", "duration": 1.8},
    {"name": "Logout Test", "status": "PASS", "duration": 1.2}
]

print("Test Results:")
for result in test_results:
    status_icon = "✅" if result["status"] == "PASS" else "❌"
    print(f"  {status_icon} {result['name']}: {result['duration']}s ({result['status']})")
```

### String Validation

```python
def validate_email(email):
    """Simple email validation"""
    if "@" in email and "." in email:
        return True
    return False

test_emails = [
    "user@example.com",
    "invalid-email",
    "user@.com",
    "user@domain.org"
]

print("Email validation:")
for email in test_emails:
    is_valid = validate_email(email)
    print(f"  '{email}': {'Valid' if is_valid else 'Invalid'}")
```

### Data Type Validation

```python
def validate_test_data(data):
    """Validate test data types"""
    expected_types = {
        "username": str,
        "password": str,
        "age": int,
        "is_active": bool
    }
    
    print("Test data validation:")
    for field, expected_type in expected_types.items():
        if field in data:
            actual_type = type(data[field])
            if actual_type != expected_type:
                print(f"  ❌ {field}: Expected {expected_type.__name__}, got {actual_type.__name__}")
            else:
                print(f"  ✅ {field}: Correct type ({actual_type.__name__})")

test_data = {
    "username": "testuser",
    "password": "testpass123",
    "age": 25,
    "is_active": True
}

validate_test_data(test_data)
```

---

## Practice Exercises

### Exercise 1: Personal Information
Create variables for a person's information and print them using f-strings:
- Name
- Age
- City
- Student status

### Exercise 2: String Manipulation
Given the string: `"  Python Programming  "`
1. Remove extra spaces
2. Convert to title case
3. Replace "Programming" with "Basics"
4. Print the result

### Exercise 3: Type Conversion
Create a list with different data types: `["42", 3.14, True, "Python"]`
For each item, print its value, current type, and convert it to a different type.

---

## Course Completion Checklist

- [ ] Completed Hello World examples
- [ ] Understood all Python data types
- [ ] Practiced type checking with `type()` function
- [ ] Mastered string manipulation techniques
- [ ] Learned variable assignment and naming conventions
- [ ] Practiced type conversion and casting
- [ ] Completed all practice exercises
- [ ] Applied concepts to test automation scenarios

---

## Next Steps

Congratulations on completing the Python Basics Fundamentals course! Here's what to explore next:

### Recommended Next Topics:
1. **Operators and Control Statements** - Making decisions in your code
2. **Loops** - Repeating actions with for and while loops
3. **Functions** - Organizing and reusing code
4. **Data Structures** - Advanced work with lists, dictionaries, sets, and tuples
5. **Error Handling** - Dealing with exceptions using try-except blocks
6. **File Operations** - Reading and writing files
7. **Object-Oriented Programming** - Classes and objects

### Additional Resources:
- **Python Official Documentation**: https://docs.python.org/
- **Python Tutorial**: https://docs.python.org/3/tutorial/
- **Real Python**: https://realpython.com/
- **Python for Testers**: Practice with test automation frameworks

### Practice Projects:
- Build a simple calculator
- Create a text-based game
- Develop a test data generator
- Build a simple web scraper
- Create a file organizer

---

## Course Materials

**📓 Colab Notebook:** `Python_Basics_Fundamentals.ipynb`
**📖 This Course Guide:** `Python_Basics_Fundamentals_Course.md`

**💡 Tip:** Use the Colab notebook for hands-on practice and experimentation. The notebook contains all the code examples and interactive exercises mentioned in this course.

---

*Happy coding! 🐍✨* 