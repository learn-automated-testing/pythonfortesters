#!/usr/bin/env python3
"""
Python Boolean Examples
=======================

This file contains examples of Python's boolean data type:
- Boolean values (True/False)
- Boolean expressions
- Logical operators (and, or, not)
- Comparison operators
- Boolean conversion

Author: Python for Testers
Date: 2024
"""

def demonstrate_boolean_values():
    """Demonstrate basic boolean values"""
    print("=" * 50)
    print("BOOLEAN VALUES")
    print("=" * 50)
    
    # Basic boolean values
    is_valid = True
    is_complete = False
    
    print(f"is_valid: {is_valid}, Type: {type(is_valid)}")
    print(f"is_complete: {is_complete}, Type: {type(is_complete)}")
    
    # Boolean conversion
    print(f"\nBoolean Conversion:")
    print(f"bool(0): {bool(0)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool(42): {bool(42)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('hello'): {bool('hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2]): {bool([1, 2])}")
    print(f"bool(None): {bool(None)}")


def demonstrate_comparison_operators():
    """Demonstrate comparison operators"""
    print("\n" + "=" * 50)
    print("COMPARISON OPERATORS")
    print("=" * 50)
    
    x = 5
    y = 10
    
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")  # Equal to
    print(f"x != y: {x != y}")  # Not equal to
    print(f"x < y: {x < y}")    # Less than
    print(f"x > y: {x > y}")    # Greater than
    print(f"x <= y: {x <= y}")  # Less than or equal to
    print(f"x >= y: {x >= y}")  # Greater than or equal to
    
    # String comparisons
    name1 = "Alice"
    name2 = "Bob"
    print(f"\nString comparisons:")
    print(f"'{name1}' == '{name2}': {name1 == name2}")
    print(f"'{name1}' < '{name2}': {name1 < name2}")  # Lexicographic order
    
    # List comparisons
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    print(f"\nList comparisons:")
    print(f"{list1} == {list2}: {list1 == list2}")
    print(f"{list1} < {list2}: {list1 < list2}")


def demonstrate_logical_operators():
    """Demonstrate logical operators"""
    print("\n" + "=" * 50)
    print("LOGICAL OPERATORS")
    print("=" * 50)
    
    # AND operator
    print("AND Operator (and):")
    print(f"True and True: {True and True}")
    print(f"True and False: {True and False}")
    print(f"False and True: {False and True}")
    print(f"False and False: {False and False}")
    
    # OR operator
    print(f"\nOR Operator (or):")
    print(f"True or True: {True or True}")
    print(f"True or False: {True or False}")
    print(f"False or True: {False or True}")
    print(f"False or False: {False or False}")
    
    # NOT operator
    print(f"\nNOT Operator (not):")
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    
    # Short-circuit evaluation
    print(f"\nShort-circuit evaluation:")
    print(f"False and print('This won\'t print'): {False and print('This won\'t print')}")
    print(f"True or print('This won\'t print'): {True or print('This won\'t print')}")


def demonstrate_boolean_expressions():
    """Demonstrate complex boolean expressions"""
    print("\n" + "=" * 50)
    print("COMPLEX BOOLEAN EXPRESSIONS")
    print("=" * 50)
    
    age = 25
    has_license = True
    has_car = False
    
    # Complex conditions
    can_drive = age >= 18 and has_license
    needs_ride = not has_car
    is_young_driver = age < 25 and has_license
    
    print(f"Age: {age}")
    print(f"Has license: {has_license}")
    print(f"Has car: {has_car}")
    print(f"Can drive: {can_drive}")
    print(f"Needs ride: {needs_ride}")
    print(f"Is young driver: {is_young_driver}")
    
    # Multiple conditions
    score = 85
    attendance = 0.9
    homework_complete = True
    
    passed_course = (score >= 70 and attendance >= 0.8) or homework_complete
    print(f"\nCourse Results:")
    print(f"Score: {score}")
    print(f"Attendance: {attendance*100}%")
    print(f"Homework complete: {homework_complete}")
    print(f"Passed course: {passed_course}")


def demonstrate_boolean_in_control_flow():
    """Demonstrate boolean usage in control flow"""
    print("\n" + "=" * 50)
    print("BOOLEANS IN CONTROL FLOW")
    print("=" * 50)
    
    # Simple if-else
    user_age = 20
    is_adult = user_age >= 18
    
    if is_adult:
        print(f"User is {user_age} years old - Adult access granted")
    else:
        print(f"User is {user_age} years old - Adult access denied")
    
    # Multiple conditions
    username = "admin"
    password = "password123"
    is_authenticated = username == "admin" and password == "password123"
    
    if is_authenticated:
        print("Login successful!")
    else:
        print("Login failed!")
    
    # Boolean in loops
    print(f"\nBoolean in while loop:")
    count = 0
    should_continue = True
    
    while should_continue and count < 3:
        print(f"Count: {count}")
        count += 1
        if count >= 3:
            should_continue = False


def demonstrate_boolean_methods():
    """Demonstrate boolean methods and functions"""
    print("\n" + "=" * 50)
    print("BOOLEAN METHODS")
    print("=" * 50)
    
    # String boolean methods
    text = "Hello World"
    empty_string = ""
    
    print(f"Text: '{text}'")
    print(f"text.isalpha(): {text.isalpha()}")
    print(f"text.isdigit(): {text.isdigit()}")
    print(f"text.islower(): {text.islower()}")
    print(f"text.isupper(): {text.isupper()}")
    print(f"text.startswith('Hello'): {text.startswith('Hello')}")
    print(f"text.endswith('World'): {text.endswith('World')}")
    
    print(f"\nEmpty string: '{empty_string}'")
    print(f"empty_string.isalpha(): {empty_string.isalpha()}")
    print(f"empty_string.isdigit(): {empty_string.isdigit()}")
    
    # List boolean methods
    numbers = [1, 2, 3, 4, 5]
    empty_list = []
    
    print(f"\nNumbers list: {numbers}")
    print(f"5 in numbers: {5 in numbers}")
    print(f"10 in numbers: {10 in numbers}")
    print(f"numbers: {bool(numbers)}")
    print(f"empty_list: {bool(empty_list)}")


def practice_exercises():
    """Practice exercises for booleans"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Check if a number is even and positive")
    number = 8
    is_even = number % 2 == 0
    is_positive = number > 0
    is_even_and_positive = is_even and is_positive
    print(f"Number: {number}")
    print(f"Is even: {is_even}")
    print(f"Is positive: {is_positive}")
    print(f"Is even and positive: {is_even_and_positive}")
    
    print("\nExercise 2: Validate email format (simple check)")
    email = "user@example.com"
    has_at = "@" in email
    has_dot = "." in email
    is_valid_email = has_at and has_dot
    print(f"Email: {email}")
    print(f"Contains @: {has_at}")
    print(f"Contains .: {has_dot}")
    print(f"Is valid email: {is_valid_email}")
    
    print("\nExercise 3: Check if a year is a leap year")
    year = 2024
    is_divisible_by_4 = year % 4 == 0
    is_divisible_by_100 = year % 100 == 0
    is_divisible_by_400 = year % 400 == 0
    is_leap_year = is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)
    print(f"Year: {year}")
    print(f"Divisible by 4: {is_divisible_by_4}")
    print(f"Divisible by 100: {is_divisible_by_100}")
    print(f"Divisible by 400: {is_divisible_by_400}")
    print(f"Is leap year: {is_leap_year}")


if __name__ == "__main__":
    print("PYTHON BOOLEAN TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_boolean_values()
    demonstrate_comparison_operators()
    demonstrate_logical_operators()
    demonstrate_boolean_expressions()
    demonstrate_boolean_in_control_flow()
    demonstrate_boolean_methods()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 