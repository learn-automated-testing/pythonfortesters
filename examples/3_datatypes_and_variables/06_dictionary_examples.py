#!/usr/bin/env python3
"""
Python Dictionary Examples
==========================

This file contains examples of Python's dictionary data type:
- Dictionary creation and basic operations
- Dictionary methods and manipulation
- Dictionary comprehension
- Nested dictionaries
- Dictionary merging and updating
- Dictionary views and iteration

Author: Python for Testers
Date: 2024
"""

def demonstrate_dictionary_creation():
    """Demonstrate different ways to create dictionaries"""
    print("=" * 50)
    print("DICTIONARY CREATION")
    print("=" * 50)
    
    # Empty dictionary
    empty_dict = {}
    print(f"Empty dictionary: {empty_dict}, Type: {type(empty_dict)}")
    
    # Dictionary with key-value pairs
    person = {"name": "Alice", "age": 25, "city": "New York"}
    print(f"Person dictionary: {person}")
    
    # Dictionary with different data types
    mixed_dict = {
        "string": "hello",
        "number": 42,
        "float": 3.14,
        "boolean": True,
        "list": [1, 2, 3],
        "tuple": (1, 2, 3)
    }
    print(f"Mixed dictionary: {mixed_dict}")
    
    # Dictionary using dict() constructor
    dict_from_list = dict([("a", 1), ("b", 2), ("c", 3)])
    print(f"Dictionary from list of tuples: {dict_from_list}")
    
    # Dictionary using keyword arguments
    dict_from_kwargs = dict(name="Bob", age=30, city="Los Angeles")
    print(f"Dictionary from kwargs: {dict_from_kwargs}")
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}
    print(f"Dictionary comprehension: {squares}")
    
    # Nested dictionary
    nested_dict = {
        "person1": {"name": "Alice", "age": 25},
        "person2": {"name": "Bob", "age": 30}
    }
    print(f"Nested dictionary: {nested_dict}")


def demonstrate_dictionary_operations():
    """Demonstrate basic dictionary operations"""
    print("\n" + "=" * 50)
    print("DICTIONARY OPERATIONS")
    print("=" * 50)
    
    person = {"name": "Alice", "age": 25, "city": "New York"}
    
    # Length
    print(f"Dictionary: {person}")
    print(f"Length: {len(person)}")
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    
    # Using get() method (safer)
    print(f"Name (get): {person.get('name')}")
    print(f"Country (get with default): {person.get('country', 'Unknown')}")
    print(f"Non-existent key (get): {person.get('height')}")
    
    # Checking if key exists
    print(f"'name' in person: {'name' in person}")
    print(f"'height' in person: {'height' in person}")
    
    # Adding new key-value pairs
    person["occupation"] = "Engineer"
    print(f"After adding occupation: {person}")
    
    # Updating values
    person["age"] = 26
    print(f"After updating age: {person}")
    
    # Removing items
    removed_city = person.pop("city")
    print(f"Removed city: {removed_city}")
    print(f"After removing city: {person}")
    
    # Using del
    del person["age"]
    print(f"After del age: {person}")


def demonstrate_dictionary_methods():
    """Demonstrate dictionary methods"""
    print("\n" + "=" * 50)
    print("DICTIONARY METHODS")
    print("=" * 50)
    
    person = {"name": "Alice", "age": 25, "city": "New York"}
    
    # Keys, values, and items
    print(f"Dictionary: {person}")
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    print(f"Items: {list(person.items())}")
    
    # Copying dictionaries
    shallow_copy = person.copy()
    print(f"Shallow copy: {shallow_copy}")
    
    # Updating dictionary
    updates = {"age": 26, "occupation": "Engineer"}
    person.update(updates)
    print(f"After update: {person}")
    
    # Setdefault method
    person.setdefault("country", "USA")
    print(f"After setdefault: {person}")
    
    # Pop with default
    height = person.pop("height", 170)  # Default value if key doesn't exist
    print(f"Popped height: {height}")
    
    # Clear dictionary
    temp_dict = {"a": 1, "b": 2}
    temp_dict.clear()
    print(f"After clear: {temp_dict}")


def demonstrate_dictionary_comprehension():
    """Demonstrate dictionary comprehension"""
    print("\n" + "=" * 50)
    print("DICTIONARY COMPREHENSION")
    print("=" * 50)
    
    # Basic dictionary comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = {x: x**2 for x in numbers}
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    
    # Dictionary comprehension with condition
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    
    # Dictionary comprehension with conditional expression
    numbers = [1, 2, 3, 4, 5]
    even_odd = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
    print(f"Even/Odd mapping: {even_odd}")
    
    # Dictionary comprehension with string operations
    words = ["hello", "world", "python"]
    word_lengths = {word: len(word) for word in words}
    print(f"Words: {words}")
    print(f"Word lengths: {word_lengths}")
    
    # Dictionary comprehension from existing dictionary
    original = {"a": 1, "b": 2, "c": 3}
    doubled = {k: v * 2 for k, v in original.items()}
    print(f"Original: {original}")
    print(f"Doubled: {doubled}")


def demonstrate_nested_dictionaries():
    """Demonstrate nested dictionaries"""
    print("\n" + "=" * 50)
    print("NESTED DICTIONARIES")
    print("=" * 50)
    
    # Simple nested dictionary
    students = {
        "student1": {
            "name": "Alice",
            "age": 20,
            "grades": [85, 92, 78]
        },
        "student2": {
            "name": "Bob",
            "age": 22,
            "grades": [90, 88, 95]
        }
    }
    
    print(f"Students: {students}")
    print(f"Student1 name: {students['student1']['name']}")
    print(f"Student1 grades: {students['student1']['grades']}")
    
    # Accessing nested values safely
    try:
        grade = students['student1']['grades'][1]
        print(f"Student1 second grade: {grade}")
    except (KeyError, IndexError) as e:
        print(f"Error accessing grade: {e}")
    
    # Updating nested values
    students['student1']['age'] = 21
    students['student2']['grades'].append(87)
    print(f"After updates: {students}")
    
    # Complex nested structure
    company = {
        "name": "TechCorp",
        "departments": {
            "engineering": {
                "manager": "John Doe",
                "employees": ["Alice", "Bob", "Charlie"],
                "budget": 1000000
            },
            "marketing": {
                "manager": "Jane Smith",
                "employees": ["David", "Eve"],
                "budget": 500000
            }
        }
    }
    
    print(f"\nCompany: {company}")
    print(f"Engineering manager: {company['departments']['engineering']['manager']}")
    print(f"Marketing employees: {company['departments']['marketing']['employees']}")


def demonstrate_dictionary_views():
    """Demonstrate dictionary views"""
    print("\n" + "=" * 50)
    print("DICTIONARY VIEWS")
    print("=" * 50)
    
    person = {"name": "Alice", "age": 25, "city": "New York"}
    
    # Dictionary views
    keys_view = person.keys()
    values_view = person.values()
    items_view = person.items()
    
    print(f"Dictionary: {person}")
    print(f"Keys view: {keys_view}")
    print(f"Values view: {values_view}")
    print(f"Items view: {items_view}")
    
    # Views are dynamic
    person["occupation"] = "Engineer"
    print(f"After adding occupation:")
    print(f"Keys view: {keys_view}")
    print(f"Values view: {values_view}")
    print(f"Items view: {items_view}")
    
    # Iterating over views
    print("\nIterating over keys:")
    for key in person.keys():
        print(f"  {key}")
    
    print("\nIterating over values:")
    for value in person.values():
        print(f"  {value}")
    
    print("\nIterating over items:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    
    # Converting views to lists
    keys_list = list(person.keys())
    values_list = list(person.values())
    items_list = list(person.items())
    
    print(f"\nKeys as list: {keys_list}")
    print(f"Values as list: {values_list}")
    print(f"Items as list: {items_list}")


def demonstrate_dictionary_merging():
    """Demonstrate dictionary merging techniques"""
    print("\n" + "=" * 50)
    print("DICTIONARY MERGING")
    print("=" * 50)
    
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 5, "e": 6}  # Note: 'b' conflicts with dict1
    
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Dict3: {dict3}")
    
    # Method 1: Using update()
    merged1 = dict1.copy()
    merged1.update(dict2)
    merged1.update(dict3)
    print(f"Merged using update(): {merged1}")
    
    # Method 2: Using | operator (Python 3.9+)
    try:
        merged2 = dict1 | dict2 | dict3
        print(f"Merged using | operator: {merged2}")
    except TypeError:
        print("| operator not available in this Python version")
    
    # Method 3: Using ** unpacking
    merged3 = {**dict1, **dict2, **dict3}
    print(f"Merged using ** unpacking: {merged3}")
    
    # Method 4: Using dict() constructor
    merged4 = dict(dict1)
    merged4.update(dict2)
    merged4.update(dict3)
    print(f"Merged using dict() constructor: {merged4}")


def demonstrate_dictionary_advanced_operations():
    """Demonstrate advanced dictionary operations"""
    print("\n" + "=" * 50)
    print("ADVANCED DICTIONARY OPERATIONS")
    print("=" * 50)
    
    # Default dictionaries
    from collections import defaultdict
    
    # Count occurrences
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_count = defaultdict(int)
    
    for word in words:
        word_count[word] += 1
    
    print(f"Words: {words}")
    print(f"Word count: {dict(word_count)}")
    
    # Grouping by category
    items = [
        ("fruit", "apple"),
        ("vegetable", "carrot"),
        ("fruit", "banana"),
        ("vegetable", "broccoli"),
        ("fruit", "cherry")
    ]
    
    grouped = defaultdict(list)
    for category, item in items:
        grouped[category].append(item)
    
    print(f"Items: {items}")
    print(f"Grouped: {dict(grouped)}")
    
    # Dictionary as switch/case
    def operation_switch(operation, a, b):
        operations = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "multiply": lambda x, y: x * y,
            "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
        }
        return operations.get(operation, lambda x, y: "Error: Unknown operation")(a, b)
    
    print(f"\nOperation switch:")
    print(f"add(5, 3): {operation_switch('add', 5, 3)}")
    print(f"multiply(4, 6): {operation_switch('multiply', 4, 6)}")
    print(f"divide(10, 2): {operation_switch('divide', 10, 2)}")
    print(f"unknown(1, 2): {operation_switch('unknown', 1, 2)}")
    
    # Dictionary for configuration
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "api": {
            "base_url": "https://api.example.com",
            "timeout": 30
        }
    }
    
    print(f"\nConfiguration: {config}")
    print(f"Database host: {config['database']['host']}")
    print(f"API timeout: {config['api']['timeout']}")


def practice_exercises():
    """Practice exercises for dictionaries"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Count character frequency in a string")
    text = "hello world"
    char_count = {}
    for char in text:
        if char != ' ':  # Skip spaces
            char_count[char] = char_count.get(char, 0) + 1
    print(f"Text: '{text}'")
    print(f"Character count: {char_count}")
    
    print("\nExercise 2: Create a phone book")
    phone_book = {
        "Alice": "555-0101",
        "Bob": "555-0102",
        "Charlie": "555-0103"
    }
    print(f"Phone book: {phone_book}")
    
    # Add new contact
    phone_book["David"] = "555-0104"
    print(f"After adding David: {phone_book}")
    
    # Look up contact
    alice_phone = phone_book.get("Alice", "Not found")
    print(f"Alice's phone: {alice_phone}")
    
    print("\nExercise 3: Convert two lists to a dictionary")
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "New York"]
    person_dict = dict(zip(keys, values))
    print(f"Keys: {keys}")
    print(f"Values: {values}")
    print(f"Combined dictionary: {person_dict}")
    
    print("\nExercise 4: Find the most common word in a list")
    words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    most_common = max(word_freq, key=word_freq.get)
    print(f"Words: {words}")
    print(f"Word frequencies: {word_freq}")
    print(f"Most common word: '{most_common}' (appears {word_freq[most_common]} times)")
    
    print("\nExercise 5: Create a nested dictionary for a library")
    library = {
        "books": {
            "fiction": {
                "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925},
                "1984": {"author": "George Orwell", "year": 1949}
            },
            "non_fiction": {
                "Python Programming": {"author": "John Doe", "year": 2023}
            }
        }
    }
    print(f"Library: {library}")
    
    # Add a new book
    library["books"]["fiction"]["To Kill a Mockingbird"] = {
        "author": "Harper Lee",
        "year": 1960
    }
    print(f"After adding new book: {library}")
    
    print("\nExercise 6: Merge dictionaries with conflict resolution")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 4, "d": 5}  # 'b' conflicts
    
    # Merge with dict2 taking precedence
    merged = {**dict1, **dict2}
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Merged (dict2 precedence): {merged}")


if __name__ == "__main__":
    print("PYTHON DICTIONARY TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_dictionary_creation()
    demonstrate_dictionary_operations()
    demonstrate_dictionary_methods()
    demonstrate_dictionary_comprehension()
    demonstrate_nested_dictionaries()
    demonstrate_dictionary_views()
    demonstrate_dictionary_merging()
    demonstrate_dictionary_advanced_operations()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 