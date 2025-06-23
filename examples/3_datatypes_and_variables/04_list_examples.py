#!/usr/bin/env python3
"""
Python List Examples
====================

This file contains examples of Python's list data type:
- List creation and basic operations
- List methods and manipulation
- List comprehension
- List slicing and indexing
- List sorting and searching
- Nested lists and advanced operations

Author: Python for Testers
Date: 2024
"""

def demonstrate_list_creation():
    """Demonstrate different ways to create lists"""
    print("=" * 50)
    print("LIST CREATION")
    print("=" * 50)
    
    # Empty list
    empty_list = []
    print(f"Empty list: {empty_list}, Type: {type(empty_list)}")
    
    # List with elements
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits list: {fruits}")
    
    # List with different data types
    mixed_list = [1, "hello", 3.14, True]
    print(f"Mixed list: {mixed_list}")
    
    # List using list() constructor
    numbers = list(range(5))
    print(f"Numbers from range: {numbers}")
    
    # List from string
    char_list = list("Python")
    print(f"Characters from string: {char_list}")
    
    # Nested lists
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Nested list (matrix): {matrix}")


def demonstrate_list_operations():
    """Demonstrate basic list operations"""
    print("\n" + "=" * 50)
    print("LIST OPERATIONS")
    print("=" * 50)
    
    numbers = [1, 2, 3, 4, 5]
    
    # Length
    print(f"List: {numbers}")
    print(f"Length: {len(numbers)}")
    
    # Indexing
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Third element: {numbers[2]}")
    
    # Slicing
    print(f"First 3 elements: {numbers[0:3]}")
    print(f"Last 3 elements: {numbers[-3:]}")
    print(f"Every second element: {numbers[::2]}")
    print(f"Reverse list: {numbers[::-1]}")
    
    # Concatenation
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(f"Concatenation: {list1} + {list2} = {combined}")
    
    # Repetition
    repeated = [1, 2] * 3
    print(f"Repetition: {repeated}")
    
    # Membership
    print(f"3 in numbers: {3 in numbers}")
    print(f"10 in numbers: {10 in numbers}")


def demonstrate_list_methods():
    """Demonstrate list methods"""
    print("\n" + "=" * 50)
    print("LIST METHODS")
    print("=" * 50)
    
    # Adding elements
    fruits = ["apple", "banana"]
    print(f"Original: {fruits}")
    
    fruits.append("cherry")
    print(f"After append: {fruits}")
    
    fruits.insert(1, "orange")
    print(f"After insert at index 1: {fruits}")
    
    fruits.extend(["grape", "kiwi"])
    print(f"After extend: {fruits}")
    
    # Removing elements
    removed = fruits.pop()
    print(f"Popped: {removed}, List: {fruits}")
    
    fruits.remove("banana")
    print(f"After removing 'banana': {fruits}")
    
    # Clear list
    temp_list = [1, 2, 3]
    temp_list.clear()
    print(f"After clear: {temp_list}")
    
    # Count and index
    numbers = [1, 2, 2, 3, 2, 4]
    print(f"\nNumbers: {numbers}")
    print(f"Count of 2: {numbers.count(2)}")
    print(f"Index of 3: {numbers.index(3)}")
    
    # Sorting
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nUnsorted: {unsorted}")
    
    sorted_list = sorted(unsorted)
    print(f"Sorted (new list): {sorted_list}")
    
    unsorted.sort()
    print(f"Sorted (in-place): {unsorted}")
    
    # Reverse
    numbers = [1, 2, 3, 4, 5]
    print(f"\nOriginal: {numbers}")
    numbers.reverse()
    print(f"Reversed: {numbers}")


def demonstrate_list_comprehension():
    """Demonstrate list comprehension"""
    print("\n" + "=" * 50)
    print("LIST COMPREHENSION")
    print("=" * 50)
    
    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    
    # List comprehension with condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # List comprehension with multiple variables
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(f"Pairs: {pairs}")
    
    # List comprehension with string operations
    words = ["hello", "world", "python"]
    upper_words = [word.upper() for word in words]
    print(f"Words: {words}")
    print(f"Upper words: {upper_words}")
    
    # List comprehension with conditional expression
    numbers = [1, 2, 3, 4, 5]
    even_odd = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print(f"Numbers: {numbers}")
    print(f"Even/Odd: {even_odd}")


def demonstrate_nested_lists():
    """Demonstrate nested lists and matrix operations"""
    print("\n" + "=" * 50)
    print("NESTED LISTS")
    print("=" * 50)
    
    # 2D matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(f"Matrix: {matrix}")
    print(f"Matrix[0][1]: {matrix[0][1]}")
    print(f"Matrix[2][2]: {matrix[2][2]}")
    
    # Accessing rows and columns
    print(f"First row: {matrix[0]}")
    print(f"Second row: {matrix[1]}")
    
    # Transpose matrix
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(f"Transpose: {transpose}")
    
    # Flatten matrix
    flattened = [item for row in matrix for item in row]
    print(f"Flattened: {flattened}")
    
    # 3D list
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    print(f"3D cube: {cube}")
    print(f"cube[0][1][0]: {cube[0][1][0]}")


def demonstrate_list_advanced_operations():
    """Demonstrate advanced list operations"""
    print("\n" + "=" * 50)
    print("ADVANCED LIST OPERATIONS")
    print("=" * 50)
    
    # Copying lists
    original = [1, 2, 3]
    shallow_copy = original.copy()
    deep_copy = original[:]  # Another way to copy
    
    print(f"Original: {original}")
    print(f"Shallow copy: {shallow_copy}")
    print(f"Deep copy: {deep_copy}")
    
    # Modifying copy
    shallow_copy[0] = 99
    print(f"After modifying copy: {shallow_copy}")
    print(f"Original unchanged: {original}")
    
    # List unpacking
    numbers = [1, 2, 3, 4, 5]
    first, second, *rest = numbers
    print(f"Numbers: {numbers}")
    print(f"First: {first}, Second: {second}, Rest: {rest}")
    
    # Zip function
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    zipped = list(zip(names, ages))
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Zipped: {zipped}")
    
    # Enumerate
    fruits = ["apple", "banana", "cherry"]
    enumerated = list(enumerate(fruits))
    print(f"Fruits: {fruits}")
    print(f"Enumerated: {enumerated}")
    
    # Filter and map
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    doubled = list(map(lambda x: x * 2, numbers))
    
    print(f"Numbers: {numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Doubled: {doubled}")


def demonstrate_list_sorting():
    """Demonstrate advanced sorting techniques"""
    print("\n" + "=" * 50)
    print("ADVANCED SORTING")
    print("=" * 50)
    
    # Simple sorting
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original: {numbers}")
    
    sorted_numbers = sorted(numbers)
    print(f"Sorted: {sorted_numbers}")
    
    # Reverse sorting
    reverse_sorted = sorted(numbers, reverse=True)
    print(f"Reverse sorted: {reverse_sorted}")
    
    # Sorting strings
    words = ["banana", "apple", "cherry", "date"]
    sorted_words = sorted(words)
    print(f"Words: {words}")
    print(f"Sorted words: {sorted_words}")
    
    # Sorting by length
    length_sorted = sorted(words, key=len)
    print(f"Sorted by length: {length_sorted}")
    
    # Sorting complex objects
    students = [
        {"name": "Alice", "age": 20, "grade": 85},
        {"name": "Bob", "age": 19, "grade": 92},
        {"name": "Charlie", "age": 21, "grade": 78}
    ]
    
    print(f"Students: {students}")
    
    # Sort by age
    age_sorted = sorted(students, key=lambda x: x["age"])
    print(f"Sorted by age: {age_sorted}")
    
    # Sort by grade (descending)
    grade_sorted = sorted(students, key=lambda x: x["grade"], reverse=True)
    print(f"Sorted by grade (descending): {grade_sorted}")


def practice_exercises():
    """Practice exercises for lists"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Find the maximum and minimum in a list")
    numbers = [3, 7, 2, 9, 1, 8, 5]
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"Numbers: {numbers}")
    print(f"Maximum: {max_num}")
    print(f"Minimum: {min_num}")
    
    print("\nExercise 2: Remove duplicates from a list")
    duplicate_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = list(set(duplicate_list))
    print(f"Original: {duplicate_list}")
    print(f"Unique: {unique_list}")
    
    print("\nExercise 3: Find common elements in two lists")
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = list(set(list1) & set(list2))
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Common elements: {common}")
    
    print("\nExercise 4: Rotate a list by n positions")
    original = [1, 2, 3, 4, 5]
    n = 2
    rotated = original[n:] + original[:n]
    print(f"Original: {original}")
    print(f"Rotated by {n}: {rotated}")
    
    print("\nExercise 5: Flatten a nested list")
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"Nested: {nested}")
    print(f"Flattened: {flattened}")
    
    print("\nExercise 6: Find the second largest number")
    numbers = [3, 7, 2, 9, 1, 8, 5]
    sorted_nums = sorted(numbers, reverse=True)
    second_largest = sorted_nums[1]
    print(f"Numbers: {numbers}")
    print(f"Second largest: {second_largest}")


if __name__ == "__main__":
    print("PYTHON LIST TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_list_creation()
    demonstrate_list_operations()
    demonstrate_list_methods()
    demonstrate_list_comprehension()
    demonstrate_nested_lists()
    demonstrate_list_advanced_operations()
    demonstrate_list_sorting()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 