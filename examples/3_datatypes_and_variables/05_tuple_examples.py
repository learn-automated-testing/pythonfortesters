#!/usr/bin/env python3
"""
Python Tuple Examples
=====================

This file contains examples of Python's tuple data type:
- Tuple creation and basic operations
- Tuple methods and properties
- Tuple unpacking
- Tuple immutability
- Named tuples
- Tuple vs list comparison

Author: Python for Testers
Date: 2024
"""

def demonstrate_tuple_creation():
    """Demonstrate different ways to create tuples"""
    print("=" * 50)
    print("TUPLE CREATION")
    print("=" * 50)
    
    # Empty tuple
    empty_tuple = ()
    print(f"Empty tuple: {empty_tuple}, Type: {type(empty_tuple)}")
    
    # Tuple with elements
    fruits = ("apple", "banana", "cherry")
    print(f"Fruits tuple: {fruits}")
    
    # Tuple with different data types
    mixed_tuple = (1, "hello", 3.14, True)
    print(f"Mixed tuple: {mixed_tuple}")
    
    # Single element tuple (note the comma)
    single_element = (42,)
    print(f"Single element tuple: {single_element}")
    
    # Tuple without parentheses (tuple packing)
    packed_tuple = 1, 2, 3
    print(f"Packed tuple: {packed_tuple}")
    
    # Tuple from list
    list_to_tuple = tuple([1, 2, 3, 4, 5])
    print(f"Tuple from list: {list_to_tuple}")
    
    # Tuple from string
    string_to_tuple = tuple("Python")
    print(f"Tuple from string: {string_to_tuple}")
    
    # Nested tuples
    nested_tuple = ((1, 2), (3, 4), (5, 6))
    print(f"Nested tuple: {nested_tuple}")


def demonstrate_tuple_operations():
    """Demonstrate basic tuple operations"""
    print("\n" + "=" * 50)
    print("TUPLE OPERATIONS")
    print("=" * 50)
    
    numbers = (1, 2, 3, 4, 5)
    
    # Length
    print(f"Tuple: {numbers}")
    print(f"Length: {len(numbers)}")
    
    # Indexing
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Third element: {numbers[2]}")
    
    # Slicing
    print(f"First 3 elements: {numbers[0:3]}")
    print(f"Last 3 elements: {numbers[-3:]}")
    print(f"Every second element: {numbers[::2]}")
    print(f"Reverse tuple: {numbers[::-1]}")
    
    # Concatenation
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    combined = tuple1 + tuple2
    print(f"Concatenation: {tuple1} + {tuple2} = {combined}")
    
    # Repetition
    repeated = (1, 2) * 3
    print(f"Repetition: {repeated}")
    
    # Membership
    print(f"3 in numbers: {3 in numbers}")
    print(f"10 in numbers: {10 in numbers}")
    
    # Iteration
    print("Iterating through tuple:")
    for item in numbers:
        print(f"  {item}")


def demonstrate_tuple_methods():
    """Demonstrate tuple methods"""
    print("\n" + "=" * 50)
    print("TUPLE METHODS")
    print("=" * 50)
    
    # Count method
    numbers = (1, 2, 2, 3, 2, 4, 2)
    print(f"Tuple: {numbers}")
    print(f"Count of 2: {numbers.count(2)}")
    print(f"Count of 5: {numbers.count(5)}")
    
    # Index method
    print(f"Index of 3: {numbers.index(3)}")
    print(f"Index of 2: {numbers.index(2)}")  # Returns first occurrence
    
    # Note: Tuples don't have methods like append, insert, remove, etc.
    # because they are immutable
    print("\nTuples are immutable - they don't have methods like:")
    print("- append()")
    print("- insert()")
    print("- remove()")
    print("- pop()")
    print("- sort()")
    print("- reverse()")


def demonstrate_tuple_immutability():
    """Demonstrate tuple immutability"""
    print("\n" + "=" * 50)
    print("TUPLE IMMUTABILITY")
    print("=" * 50)
    
    my_tuple = (1, 2, 3)
    print(f"Original tuple: {my_tuple}")
    
    # Attempting to modify a tuple will raise an error
    try:
        my_tuple[1] = 4
        print("This won't print")
    except TypeError as e:
        print(f"Error: {e}")
        print("Tuples are immutable and cannot be modified!")
    
    # However, if a tuple contains mutable objects, those can be modified
    mutable_tuple = ([1, 2, 3], [4, 5, 6])
    print(f"\nTuple with mutable elements: {mutable_tuple}")
    
    # This works because we're modifying the list inside the tuple
    mutable_tuple[0].append(4)
    print(f"After modifying list inside tuple: {mutable_tuple}")
    
    # But this would still fail
    try:
        mutable_tuple[0] = [7, 8, 9]
        print("This won't print")
    except TypeError as e:
        print(f"Error: {e}")
        print("Cannot replace the list reference in the tuple!")


def demonstrate_tuple_unpacking():
    """Demonstrate tuple unpacking"""
    print("\n" + "=" * 50)
    print("TUPLE UNPACKING")
    print("=" * 50)
    
    # Basic unpacking
    point = (3, 4)
    x, y = point
    print(f"Point: {point}")
    print(f"Unpacked: x={x}, y={y}")
    
    # Multiple assignment
    a, b, c = 1, 2, 3
    print(f"Multiple assignment: a={a}, b={b}, c={c}")
    
    # Extended unpacking
    numbers = (1, 2, 3, 4, 5)
    first, second, *rest = numbers
    print(f"Numbers: {numbers}")
    print(f"First: {first}, Second: {second}, Rest: {rest}")
    
    # Ignoring values with underscore
    person = ("Alice", 25, "Engineer", "New York")
    name, age, _, city = person
    print(f"Person: {person}")
    print(f"Name: {name}, Age: {age}, City: {city}")
    
    # Swapping variables
    a, b = 10, 20
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    
    # Function returning multiple values
    def get_coordinates():
        return (10, 20)
    
    x, y = get_coordinates()
    print(f"Coordinates: x={x}, y={y}")


def demonstrate_named_tuples():
    """Demonstrate named tuples"""
    print("\n" + "=" * 50)
    print("NAMED TUPLES")
    print("=" * 50)
    
    from collections import namedtuple
    
    # Creating a named tuple
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    # Creating instances
    person1 = Person('Alice', 25, 'New York')
    person2 = Person('Bob', 30, 'Los Angeles')
    
    print(f"Person 1: {person1}")
    print(f"Person 2: {person2}")
    
    # Accessing by attribute names
    print(f"Person 1 name: {person1.name}")
    print(f"Person 1 age: {person1.age}")
    print(f"Person 1 city: {person1.city}")
    
    # Accessing by index
    print(f"Person 2 name (by index): {person2[0]}")
    print(f"Person 2 age (by index): {person2[1]}")
    
    # Named tuple methods
    print(f"Person 1 as dict: {person1._asdict()}")
    print(f"Person 1 fields: {person1._fields}")
    
    # Creating from iterable
    person3 = Person._make(['Charlie', 35, 'Chicago'])
    print(f"Person 3 from iterable: {person3}")
    
    # Replacing fields
    person4 = person1._replace(age=26)
    print(f"Person 1: {person1}")
    print(f"Person 4 (replaced age): {person4}")


def demonstrate_tuple_vs_list():
    """Demonstrate differences between tuples and lists"""
    print("\n" + "=" * 50)
    print("TUPLE VS LIST COMPARISON")
    print("=" * 50)
    
    # Creation
    my_list = [1, 2, 3]
    my_tuple = (1, 2, 3)
    
    print(f"List: {my_list}, Type: {type(my_list)}")
    print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")
    
    # Memory usage (tuples are generally more memory efficient)
    import sys
    print(f"List memory: {sys.getsizeof(my_list)} bytes")
    print(f"Tuple memory: {sys.getsizeof(my_tuple)} bytes")
    
    # Mutability
    print(f"\nMutability:")
    print(f"List before: {my_list}")
    my_list[1] = 99
    print(f"List after modification: {my_list}")
    
    print(f"Tuple before: {my_tuple}")
    try:
        my_tuple[1] = 99
    except TypeError:
        print("Cannot modify tuple - it's immutable!")
    
    # Use cases
    print(f"\nUse cases:")
    print("Lists: Use when you need a mutable sequence")
    print("Tuples: Use when you need an immutable sequence")
    print("Tuples: Good for returning multiple values from functions")
    print("Tuples: Good for dictionary keys (if they contain only immutable elements)")
    print("Tuples: Good for data that shouldn't change")


def demonstrate_tuple_advanced_operations():
    """Demonstrate advanced tuple operations"""
    print("\n" + "=" * 50)
    print("ADVANCED TUPLE OPERATIONS")
    print("=" * 50)
    
    # Tuple comprehension (generator expression)
    numbers = (1, 2, 3, 4, 5)
    squares = tuple(x**2 for x in numbers)
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    
    # Sorting tuples
    points = [(3, 4), (1, 2), (5, 1), (2, 3)]
    sorted_points = sorted(points)
    print(f"Points: {points}")
    print(f"Sorted points: {sorted_points}")
    
    # Sorting by specific element
    students = [("Alice", 25, 85), ("Bob", 20, 92), ("Charlie", 22, 78)]
    sorted_by_age = sorted(students, key=lambda x: x[1])
    sorted_by_grade = sorted(students, key=lambda x: x[2], reverse=True)
    
    print(f"Students: {students}")
    print(f"Sorted by age: {sorted_by_age}")
    print(f"Sorted by grade: {sorted_by_grade}")
    
    # Tuple as dictionary keys
    coordinates = {(0, 0): "origin", (1, 1): "diagonal", (-1, -1): "opposite"}
    print(f"Coordinates dictionary: {coordinates}")
    print(f"Value at (1, 1): {coordinates[(1, 1)]}")
    
    # Tuple unpacking in loops
    points = [(1, 2), (3, 4), (5, 6)]
    print(f"Points: {points}")
    print("Unpacking in loop:")
    for x, y in points:
        print(f"  Point: ({x}, {y})")


def practice_exercises():
    """Practice exercises for tuples"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Create a tuple of coordinates and find the distance from origin")
    point = (3, 4)
    distance = (point[0]**2 + point[1]**2)**0.5
    print(f"Point: {point}")
    print(f"Distance from origin: {distance}")
    
    print("\nExercise 2: Unpack RGB color values")
    color = (255, 128, 64)
    red, green, blue = color
    print(f"Color: {color}")
    print(f"Red: {red}, Green: {green}, Blue: {blue}")
    
    print("\nExercise 3: Find the maximum and minimum values in a tuple")
    numbers = (3, 7, 2, 9, 1, 8, 5)
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"Numbers: {numbers}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")
    
    print("\nExercise 4: Convert tuple to list and back")
    original_tuple = (1, 2, 3, 4, 5)
    to_list = list(original_tuple)
    back_to_tuple = tuple(to_list)
    print(f"Original tuple: {original_tuple}")
    print(f"Converted to list: {to_list}")
    print(f"Back to tuple: {back_to_tuple}")
    
    print("\nExercise 5: Create a named tuple for a book")
    from collections import namedtuple
    Book = namedtuple('Book', ['title', 'author', 'year', 'pages'])
    book = Book('Python Programming', 'John Doe', 2023, 450)
    print(f"Book: {book}")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.year}")
    print(f"Pages: {book.pages}")
    
    print("\nExercise 6: Find common elements in two tuples")
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 5, 6, 7, 8)
    common = tuple(set(tuple1) & set(tuple2))
    print(f"Tuple 1: {tuple1}")
    print(f"Tuple 2: {tuple2}")
    print(f"Common elements: {common}")


if __name__ == "__main__":
    print("PYTHON TUPLE TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_tuple_creation()
    demonstrate_tuple_operations()
    demonstrate_tuple_methods()
    demonstrate_tuple_immutability()
    demonstrate_tuple_unpacking()
    demonstrate_named_tuples()
    demonstrate_tuple_vs_list()
    demonstrate_tuple_advanced_operations()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 