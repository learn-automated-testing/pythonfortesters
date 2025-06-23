#!/usr/bin/env python3
"""
Python Set Examples
===================

This file contains examples of Python's set data type:
- Set creation and basic operations
- Set methods and manipulation
- Set operations (union, intersection, difference)
- Set comprehension
- Frozen sets
- Set vs list comparison

Author: Python for Testers
Date: 2024
"""

def demonstrate_set_creation():
    """Demonstrate different ways to create sets"""
    print("=" * 50)
    print("SET CREATION")
    print("=" * 50)
    
    # Empty set
    empty_set = set()
    print(f"Empty set: {empty_set}, Type: {type(empty_set)}")
    
    # Set with elements
    fruits = {"apple", "banana", "cherry"}
    print(f"Fruits set: {fruits}")
    
    # Set with different data types
    mixed_set = {1, "hello", 3.14, True}
    print(f"Mixed set: {mixed_set}")
    
    # Set from list (removes duplicates)
    list_to_set = set([1, 2, 2, 3, 3, 4])
    print(f"Set from list (duplicates removed): {list_to_set}")
    
    # Set from string
    string_to_set = set("hello")
    print(f"Set from string: {string_to_set}")
    
    # Set comprehension
    squares = {x**2 for x in range(5)}
    print(f"Set comprehension: {squares}")
    
    # Set from range
    range_set = set(range(5))
    print(f"Set from range: {range_set}")


def demonstrate_set_operations():
    """Demonstrate basic set operations"""
    print("\n" + "=" * 50)
    print("SET OPERATIONS")
    print("=" * 50)
    
    numbers = {1, 2, 3, 4, 5}
    
    # Length
    print(f"Set: {numbers}")
    print(f"Length: {len(numbers)}")
    
    # Membership
    print(f"3 in numbers: {3 in numbers}")
    print(f"10 in numbers: {10 in numbers}")
    
    # Iteration
    print("Iterating through set:")
    for item in numbers:
        print(f"  {item}")
    
    # Adding elements
    numbers.add(6)
    print(f"After adding 6: {numbers}")
    
    # Adding multiple elements
    numbers.update([7, 8, 9])
    print(f"After updating with [7, 8, 9]: {numbers}")
    
    # Removing elements
    numbers.remove(3)
    print(f"After removing 3: {numbers}")
    
    # Discard (doesn't raise error if element doesn't exist)
    numbers.discard(10)  # 10 doesn't exist, no error
    print(f"After discarding 10: {numbers}")
    
    # Pop (removes and returns arbitrary element)
    popped = numbers.pop()
    print(f"Popped: {popped}, Set: {numbers}")
    
    # Clear
    temp_set = {1, 2, 3}
    temp_set.clear()
    print(f"After clear: {temp_set}")


def demonstrate_set_methods():
    """Demonstrate set methods"""
    print("\n" + "=" * 50)
    print("SET METHODS")
    print("=" * 50)
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    
    # Union
    union = set1.union(set2)
    print(f"Union: {union}")
    
    # Intersection
    intersection = set1.intersection(set2)
    print(f"Intersection: {intersection}")
    
    # Difference
    difference = set1.difference(set2)
    print(f"Difference (set1 - set2): {difference}")
    
    # Symmetric difference
    symmetric_diff = set1.symmetric_difference(set2)
    print(f"Symmetric difference: {symmetric_diff}")
    
    # Subset and superset
    subset = {1, 2}
    superset = {1, 2, 3, 4, 5}
    print(f"\nSubset: {subset}")
    print(f"Superset: {superset}")
    print(f"Is subset: {subset.issubset(superset)}")
    print(f"Is superset: {superset.issuperset(subset)}")
    
    # Disjoint sets
    disjoint1 = {1, 2, 3}
    disjoint2 = {4, 5, 6}
    print(f"\nDisjoint1: {disjoint1}")
    print(f"Disjoint2: {disjoint2}")
    print(f"Are disjoint: {disjoint1.isdisjoint(disjoint2)}")


def demonstrate_set_operators():
    """Demonstrate set operators"""
    print("\n" + "=" * 50)
    print("SET OPERATORS")
    print("=" * 50)
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    
    # Union operator
    union = set1 | set2
    print(f"Union (|): {union}")
    
    # Intersection operator
    intersection = set1 & set2
    print(f"Intersection (&): {intersection}")
    
    # Difference operator
    difference = set1 - set2
    print(f"Difference (-): {difference}")
    
    # Symmetric difference operator
    symmetric_diff = set1 ^ set2
    print(f"Symmetric difference (^): {symmetric_diff}")
    
    # In-place operators
    set1_copy = set1.copy()
    set1_copy |= set2  # Union in-place
    print(f"Union in-place (|=): {set1_copy}")
    
    set1_copy = set1.copy()
    set1_copy &= set2  # Intersection in-place
    print(f"Intersection in-place (&=): {set1_copy}")
    
    set1_copy = set1.copy()
    set1_copy -= set2  # Difference in-place
    print(f"Difference in-place (-=): {set1_copy}")
    
    set1_copy = set1.copy()
    set1_copy ^= set2  # Symmetric difference in-place
    print(f"Symmetric difference in-place (^=): {set1_copy}")


def demonstrate_set_comprehension():
    """Demonstrate set comprehension"""
    print("\n" + "=" * 50)
    print("SET COMPREHENSION")
    print("=" * 50)
    
    # Basic set comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = {x**2 for x in numbers if x % 2 == 0}
    print(f"Numbers: {numbers}")
    print(f"Even squares: {even_squares}")
    
    # Set comprehension with string operations
    words = ["hello", "world", "python", "programming"]
    word_lengths = {len(word) for word in words}
    print(f"Words: {words}")
    print(f"Word lengths: {word_lengths}")
    
    # Set comprehension with conditional expression
    numbers = [1, 2, 3, 4, 5]
    even_odd_labels = {"even" if x % 2 == 0 else "odd" for x in numbers}
    print(f"Numbers: {numbers}")
    print(f"Even/Odd labels: {even_odd_labels}")
    
    # Set comprehension from existing set
    original_set = {1, 2, 3, 4, 5}
    doubled = {x * 2 for x in original_set}
    print(f"Original set: {original_set}")
    print(f"Doubled: {doubled}")


def demonstrate_frozen_sets():
    """Demonstrate frozen sets (immutable sets)"""
    print("\n" + "=" * 50)
    print("FROZEN SETS")
    print("=" * 50)
    
    # Creating frozen sets
    regular_set = {1, 2, 3, 4, 5}
    frozen_set = frozenset([1, 2, 3, 4, 5])
    
    print(f"Regular set: {regular_set}, Type: {type(regular_set)}")
    print(f"Frozen set: {frozen_set}, Type: {type(frozen_set)}")
    
    # Frozen sets are immutable
    try:
        frozen_set.add(6)
        print("This won't print")
    except AttributeError as e:
        print(f"Error: {e}")
        print("Frozen sets are immutable!")
    
    # Frozen sets support set operations
    frozen1 = frozenset([1, 2, 3])
    frozen2 = frozenset([3, 4, 5])
    
    union = frozen1 | frozen2
    intersection = frozen1 & frozen2
    difference = frozen1 - frozen2
    
    print(f"Frozen1: {frozen1}")
    print(f"Frozen2: {frozen2}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference: {difference}")
    
    # Frozen sets can be used as dictionary keys
    coordinates = {
        frozenset([0, 0]): "origin",
        frozenset([1, 1]): "diagonal",
        frozenset([-1, -1]): "opposite"
    }
    print(f"Coordinates dictionary: {coordinates}")


def demonstrate_set_vs_list():
    """Demonstrate differences between sets and lists"""
    print("\n" + "=" * 50)
    print("SET VS LIST COMPARISON")
    print("=" * 50)
    
    # Creation
    my_list = [1, 2, 2, 3, 3, 4]
    my_set = {1, 2, 2, 3, 3, 4}
    
    print(f"List: {my_list}, Type: {type(my_list)}")
    print(f"Set: {my_set}, Type: {type(my_set)}")
    
    # Memory usage
    import sys
    print(f"List memory: {sys.getsizeof(my_list)} bytes")
    print(f"Set memory: {sys.getsizeof(my_set)} bytes")
    
    # Performance comparison
    import time
    
    # Membership test
    large_list = list(range(10000))
    large_set = set(range(10000))
    
    start_time = time.time()
    result = 9999 in large_list
    list_time = time.time() - start_time
    
    start_time = time.time()
    result = 9999 in large_set
    set_time = time.time() - start_time
    
    print(f"\nMembership test performance:")
    print(f"List time: {list_time:.6f} seconds")
    print(f"Set time: {set_time:.6f} seconds")
    
    # Use cases
    print(f"\nUse cases:")
    print("Lists: Use when you need ordered, indexed access")
    print("Lists: Use when you need to allow duplicates")
    print("Lists: Use when you need to modify the collection")
    print("Sets: Use when you need unique elements")
    print("Sets: Use when you need fast membership testing")
    print("Sets: Use when you need set operations (union, intersection, etc.)")


def demonstrate_set_advanced_operations():
    """Demonstrate advanced set operations"""
    print("\n" + "=" * 50)
    print("ADVANCED SET OPERATIONS")
    print("=" * 50)
    
    # Removing duplicates from a list
    duplicate_list = [1, 2, 2, 3, 3, 4, 5, 5]
    unique_list = list(set(duplicate_list))
    print(f"Original list: {duplicate_list}")
    print(f"Unique list: {unique_list}")
    
    # Finding common elements
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = set(list1) & set(list2)
    print(f"List1: {list1}")
    print(f"List2: {list2}")
    print(f"Common elements: {common}")
    
    # Finding unique elements in each list
    unique_to_list1 = set(list1) - set(list2)
    unique_to_list2 = set(list2) - set(list1)
    print(f"Unique to list1: {unique_to_list1}")
    print(f"Unique to list2: {unique_to_list2}")
    
    # Set partitioning
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even = {x for x in numbers if x % 2 == 0}
    odd = {x for x in numbers if x % 2 != 0}
    print(f"Numbers: {numbers}")
    print(f"Even: {even}")
    print(f"Odd: {odd}")
    
    # Set for data validation
    valid_colors = {"red", "green", "blue", "yellow", "purple"}
    user_input = "red"
    if user_input in valid_colors:
        print(f"'{user_input}' is a valid color")
    else:
        print(f"'{user_input}' is not a valid color")
    
    # Set for tracking visited items
    visited = set()
    items_to_process = ["item1", "item2", "item1", "item3", "item2"]
    
    for item in items_to_process:
        if item not in visited:
            print(f"Processing: {item}")
            visited.add(item)
        else:
            print(f"Skipping (already processed): {item}")


def practice_exercises():
    """Practice exercises for sets"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Remove duplicates from a list")
    duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    unique_list = list(set(duplicate_list))
    print(f"Original: {duplicate_list}")
    print(f"Unique: {unique_list}")
    
    print("\nExercise 2: Find common elements in three sets")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {5, 6, 9, 10}
    common = set1 & set2 & set3
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Set3: {set3}")
    print(f"Common elements: {common}")
    
    print("\nExercise 3: Find elements that are in exactly two sets")
    in_two = (set1 & set2 - set3) | (set1 & set3 - set2) | (set2 & set3 - set1)
    print(f"Elements in exactly two sets: {in_two}")
    
    print("\nExercise 4: Create a set of all unique characters in a string")
    text = "hello world python programming"
    unique_chars = set(text)
    print(f"Text: '{text}'")
    print(f"Unique characters: {unique_chars}")
    
    print("\nExercise 5: Find the symmetric difference of two sets")
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    symmetric_diff = set_a ^ set_b
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Symmetric difference: {symmetric_diff}")
    
    print("\nExercise 6: Check if one set is a subset of another")
    subset = {1, 2}
    superset = {1, 2, 3, 4, 5}
    is_subset = subset.issubset(superset)
    print(f"Subset: {subset}")
    print(f"Superset: {superset}")
    print(f"Is subset: {is_subset}")


if __name__ == "__main__":
    print("PYTHON SET TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_set_creation()
    demonstrate_set_operations()
    demonstrate_set_methods()
    demonstrate_set_operators()
    demonstrate_set_comprehension()
    demonstrate_frozen_sets()
    demonstrate_set_vs_list()
    demonstrate_set_advanced_operations()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 