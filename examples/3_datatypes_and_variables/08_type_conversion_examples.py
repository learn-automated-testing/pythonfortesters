#!/usr/bin/env python3
"""
Python Type Conversion Examples
===============================

This file contains examples of Python's type conversion:
- Converting between different data types
- Type validation and checking
- Safe conversion methods
- Common conversion patterns
- Error handling in conversions

Author: Python for Testers
Date: 2024
"""

def demonstrate_basic_conversions():
    """Demonstrate basic type conversions"""
    print("=" * 50)
    print("BASIC TYPE CONVERSIONS")
    print("=" * 50)
    
    # String to number conversions
    str_number = "123"
    int_number = int(str_number)
    float_number = float(str_number)
    print(f"String '{str_number}' -> int: {int_number}, float: {float_number}")
    
    # Number to string conversions
    number = 42
    str_number = str(number)
    print(f"Number {number} -> string: '{str_number}'")
    
    # Float to int (truncates decimal part)
    float_val = 3.14
    int_val = int(float_val)
    print(f"Float {float_val} -> int: {int_val}")
    
    # Int to float
    int_val = 5
    float_val = float(int_val)
    print(f"Int {int_val} -> float: {float_val}")
    
    # Boolean conversions
    print(f"\nBoolean conversions:")
    print(f"bool(0): {bool(0)}")
    print(f"bool(1): {bool(1)}")
    print(f"bool(42): {bool(42)}")
    print(f"bool(''): {bool('')}")
    print(f"bool('hello'): {bool('hello')}")
    print(f"bool([]): {bool([])}")
    print(f"bool([1, 2]): {bool([1, 2])}")
    print(f"bool(None): {bool(None)}")


def demonstrate_collection_conversions():
    """Demonstrate conversions between collections"""
    print("\n" + "=" * 50)
    print("COLLECTION CONVERSIONS")
    print("=" * 50)
    
    # List conversions
    original_list = [1, 2, 3, 4, 5]
    print(f"Original list: {original_list}")
    
    # List to tuple
    list_to_tuple = tuple(original_list)
    print(f"List -> tuple: {list_to_tuple}")
    
    # List to set (removes duplicates)
    list_with_duplicates = [1, 2, 2, 3, 3, 4]
    list_to_set = set(list_with_duplicates)
    print(f"List with duplicates -> set: {list_to_set}")
    
    # Tuple to list
    original_tuple = (1, 2, 3, 4, 5)
    tuple_to_list = list(original_tuple)
    print(f"Tuple -> list: {tuple_to_list}")
    
    # Set to list
    original_set = {1, 2, 3, 4, 5}
    set_to_list = list(original_set)
    print(f"Set -> list: {set_to_list}")
    
    # String to list of characters
    text = "Python"
    string_to_list = list(text)
    print(f"String '{text}' -> list: {string_to_list}")
    
    # List to string (join)
    char_list = ['P', 'y', 't', 'h', 'o', 'n']
    list_to_string = ''.join(char_list)
    print(f"Character list -> string: '{list_to_string}'")


def demonstrate_dictionary_conversions():
    """Demonstrate dictionary-related conversions"""
    print("\n" + "=" * 50)
    print("DICTIONARY CONVERSIONS")
    print("=" * 50)
    
    # List of tuples to dictionary
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    list_to_dict = dict(pairs)
    print(f"List of tuples -> dict: {list_to_dict}")
    
    # Dictionary to list of tuples
    original_dict = {"x": 10, "y": 20, "z": 30}
    dict_to_list = list(original_dict.items())
    print(f"Dict -> list of tuples: {dict_to_list}")
    
    # Dictionary keys and values
    keys_list = list(original_dict.keys())
    values_list = list(original_dict.values())
    print(f"Dict keys: {keys_list}")
    print(f"Dict values: {values_list}")
    
    # Two lists to dictionary
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "New York"]
    lists_to_dict = dict(zip(keys, values))
    print(f"Two lists -> dict: {lists_to_dict}")


def demonstrate_safe_conversions():
    """Demonstrate safe conversion methods with error handling"""
    print("\n" + "=" * 50)
    print("SAFE CONVERSIONS")
    print("=" * 50)
    
    # Safe string to int conversion
    def safe_int_conversion(value, default=0):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    test_values = ["123", "45.67", "hello", "", None]
    for value in test_values:
        result = safe_int_conversion(value)
        print(f"safe_int_conversion('{value}') -> {result}")
    
    # Safe float conversion
    def safe_float_conversion(value, default=0.0):
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    for value in test_values:
        result = safe_float_conversion(value)
        print(f"safe_float_conversion('{value}') -> {result}")
    
    # Safe list conversion
    def safe_list_conversion(value):
        if value is None:
            return []
        if isinstance(value, (list, tuple, set)):
            return list(value)
        if isinstance(value, str):
            return list(value)
        return [value]
    
    test_values = [None, [1, 2, 3], (1, 2, 3), {1, 2, 3}, "hello", 42]
    for value in test_values:
        result = safe_list_conversion(value)
        print(f"safe_list_conversion({value}) -> {result}")


def demonstrate_type_checking():
    """Demonstrate type checking and validation"""
    print("\n" + "=" * 50)
    print("TYPE CHECKING")
    print("=" * 50)
    
    # Using isinstance()
    test_values = [42, 3.14, "hello", True, [1, 2, 3], (1, 2), {1, 2}, {"a": 1}]
    
    for value in test_values:
        print(f"{value} ({type(value).__name__}):")
        print(f"  is int: {isinstance(value, int)}")
        print(f"  is float: {isinstance(value, float)}")
        print(f"  is str: {isinstance(value, str)}")
        print(f"  is bool: {isinstance(value, bool)}")
        print(f"  is list: {isinstance(value, list)}")
        print(f"  is tuple: {isinstance(value, tuple)}")
        print(f"  is set: {isinstance(value, set)}")
        print(f"  is dict: {isinstance(value, dict)}")
        print()
    
    # Type checking with multiple types
    def check_numeric(value):
        return isinstance(value, (int, float))
    
    numeric_values = [42, 3.14, "hello", True, [1, 2, 3]]
    for value in numeric_values:
        is_numeric = check_numeric(value)
        print(f"{value} is numeric: {is_numeric}")


def demonstrate_advanced_conversions():
    """Demonstrate advanced conversion patterns"""
    print("\n" + "=" * 50)
    print("ADVANCED CONVERSIONS")
    print("=" * 50)
    
    # Converting string representations
    import ast
    
    # Safe eval for literals
    def safe_eval_literal(value):
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value
    
    test_strings = ["123", "[1, 2, 3]", "{'a': 1, 'b': 2}", "(1, 2, 3)", "hello"]
    for string in test_strings:
        result = safe_eval_literal(string)
        print(f"safe_eval_literal('{string}') -> {result} ({type(result).__name__})")
    
    # Converting between number bases
    decimal_num = 42
    binary = bin(decimal_num)
    octal = oct(decimal_num)
    hexadecimal = hex(decimal_num)
    print(f"\nNumber base conversions:")
    print(f"Decimal {decimal_num}:")
    print(f"  Binary: {binary}")
    print(f"  Octal: {octal}")
    print(f"  Hexadecimal: {hexadecimal}")
    
    # Converting from different bases
    binary_str = "101010"
    octal_str = "52"
    hex_str = "2a"
    
    from_binary = int(binary_str, 2)
    from_octal = int(octal_str, 8)
    from_hex = int(hex_str, 16)
    
    print(f"\nConverting from different bases:")
    print(f"Binary '{binary_str}' -> decimal: {from_binary}")
    print(f"Octal '{octal_str}' -> decimal: {from_octal}")
    print(f"Hex '{hex_str}' -> decimal: {from_hex}")


def demonstrate_data_validation():
    """Demonstrate data validation patterns"""
    print("\n" + "=" * 50)
    print("DATA VALIDATION")
    print("=" * 50)
    
    # Email validation
    def is_valid_email(email):
        if not isinstance(email, str):
            return False
        return '@' in email and '.' in email.split('@')[1]
    
    email_tests = ["user@example.com", "invalid-email", "user@", "@example.com", 123]
    for email in email_tests:
        is_valid = is_valid_email(email)
        print(f"'{email}' is valid email: {is_valid}")
    
    # Number range validation
    def is_in_range(value, min_val, max_val):
        try:
            num = float(value)
            return min_val <= num <= max_val
        except (ValueError, TypeError):
            return False
    
    range_tests = [5, 15, 25, "10", "abc", -5]
    for value in range_tests:
        in_range = is_in_range(value, 0, 20)
        print(f"{value} in range [0, 20]: {in_range}")
    
    # List validation
    def validate_list(value, expected_type=str, min_length=0):
        if not isinstance(value, list):
            return False
        if len(value) < min_length:
            return False
        return all(isinstance(item, expected_type) for item in value)
    
    list_tests = [
        ["a", "b", "c"],
        [1, 2, 3],
        ["a", 1, "b"],
        [],
        "not a list"
    ]
    
    for test_list in list_tests:
        is_valid = validate_list(test_list, str, 1)
        print(f"{test_list} is valid string list (min length 1): {is_valid}")


def demonstrate_conversion_utilities():
    """Demonstrate useful conversion utility functions"""
    print("\n" + "=" * 50)
    print("CONVERSION UTILITIES")
    print("=" * 50)
    
    # Convert mixed list to specific types
    def convert_list_types(mixed_list, target_type):
        converted = []
        for item in mixed_list:
            try:
                converted.append(target_type(item))
            except (ValueError, TypeError):
                converted.append(None)
        return converted
    
    mixed_data = ["123", "45.67", "hello", "789", "12.34"]
    int_list = convert_list_types(mixed_data, int)
    float_list = convert_list_types(mixed_data, float)
    
    print(f"Mixed data: {mixed_data}")
    print(f"Converted to int: {int_list}")
    print(f"Converted to float: {float_list}")
    
    # Flatten nested lists
    def flatten_list(nested_list):
        flattened = []
        for item in nested_list:
            if isinstance(item, list):
                flattened.extend(flatten_list(item))
            else:
                flattened.append(item)
        return flattened
    
    nested = [1, [2, 3], [4, [5, 6]], 7]
    flattened = flatten_list(nested)
    print(f"Nested list: {nested}")
    print(f"Flattened: {flattened}")
    
    # Convert dictionary values
    def convert_dict_values(data_dict, value_type):
        converted = {}
        for key, value in data_dict.items():
            try:
                converted[key] = value_type(value)
            except (ValueError, TypeError):
                converted[key] = None
        return converted
    
    sample_dict = {"a": "123", "b": "45.67", "c": "hello", "d": "789"}
    int_dict = convert_dict_values(sample_dict, int)
    print(f"Original dict: {sample_dict}")
    print(f"Converted to int: {int_dict}")


def practice_exercises():
    """Practice exercises for type conversion"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Convert string numbers to integers and sum them")
    number_strings = ["1", "2", "3", "4", "5"]
    numbers = [int(num) for num in number_strings]
    total = sum(numbers)
    print(f"String numbers: {number_strings}")
    print(f"Converted to int: {numbers}")
    print(f"Sum: {total}")
    
    print("\nExercise 2: Create a function to safely convert any value to string")
    def safe_to_string(value):
        if value is None:
            return "None"
        return str(value)
    
    test_values = [42, 3.14, "hello", True, [1, 2, 3], None]
    for value in test_values:
        result = safe_to_string(value)
        print(f"safe_to_string({value}) -> '{result}'")
    
    print("\nExercise 3: Convert a list of tuples to a dictionary")
    tuple_list = [("name", "Alice"), ("age", "25"), ("city", "New York")]
    person_dict = dict(tuple_list)
    print(f"Tuple list: {tuple_list}")
    print(f"Dictionary: {person_dict}")
    
    print("\nExercise 4: Validate and convert user input")
    def process_user_input(input_value):
        # Try to convert to int first, then float, then keep as string
        try:
            return int(input_value)
        except ValueError:
            try:
                return float(input_value)
            except ValueError:
                return input_value
    
    user_inputs = ["123", "45.67", "hello", "0", "-5"]
    for user_input in user_inputs:
        result = process_user_input(user_input)
        print(f"Input: '{user_input}' -> {result} ({type(result).__name__})")
    
    print("\nExercise 5: Convert between different number formats")
    decimal = 255
    binary = bin(decimal)[2:]  # Remove '0b' prefix
    octal = oct(decimal)[2:]   # Remove '0o' prefix
    hex_val = hex(decimal)[2:] # Remove '0x' prefix
    
    print(f"Decimal: {decimal}")
    print(f"Binary: {binary}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hex_val}")
    
    # Convert back
    from_binary = int(binary, 2)
    from_octal = int(octal, 8)
    from_hex = int(hex_val, 16)
    
    print(f"From binary: {from_binary}")
    print(f"From octal: {from_octal}")
    print(f"From hex: {from_hex}")


if __name__ == "__main__":
    print("PYTHON TYPE CONVERSION TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_basic_conversions()
    demonstrate_collection_conversions()
    demonstrate_dictionary_conversions()
    demonstrate_safe_conversions()
    demonstrate_type_checking()
    demonstrate_advanced_conversions()
    demonstrate_data_validation()
    demonstrate_conversion_utilities()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 