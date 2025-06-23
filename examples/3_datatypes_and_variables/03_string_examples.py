#!/usr/bin/env python3
"""
Python String Examples
======================

This file contains examples of Python's string data type:
- String creation and basic operations
- String methods and manipulation
- String formatting
- String slicing and indexing
- String concatenation and joining
- String validation and checking

Author: Python for Testers
Date: 2024
"""

def demonstrate_string_creation():
    """Demonstrate different ways to create strings"""
    print("=" * 50)
    print("STRING CREATION")
    print("=" * 50)
    
    # Single quotes
    name = 'John Doe'
    print(f"Single quotes: {name}, Type: {type(name)}")
    
    # Double quotes
    message = "Hello, World!"
    print(f"Double quotes: {message}, Type: {type(message)}")
    
    # Triple quotes for multi-line strings
    multi_line = """This is a
multi-line string
with multiple lines"""
    print(f"Multi-line string:\n{multi_line}")
    
    # Triple single quotes
    multi_line2 = '''Another way to create
multi-line strings'''
    print(f"Triple single quotes:\n{multi_line2}")
    
    # String with special characters
    special_string = "Line 1\nLine 2\tTabbed\tText"
    print(f"Special characters:\n{special_string}")
    
    # Raw strings (r-prefix)
    raw_string = r"C:\Users\Documents\file.txt"
    print(f"Raw string: {raw_string}")


def demonstrate_string_operations():
    """Demonstrate basic string operations"""
    print("\n" + "=" * 50)
    print("STRING OPERATIONS")
    print("=" * 50)
    
    text = "Hello, World!"
    
    # Length
    print(f"Text: '{text}'")
    print(f"Length: {len(text)}")
    
    # Indexing
    print(f"First character: {text[0]}")
    print(f"Last character: {text[-1]}")
    print(f"Fifth character: {text[4]}")
    
    # Slicing
    print(f"First 5 characters: '{text[0:5]}'")
    print(f"Last 6 characters: '{text[-6:]}'")
    print(f"Characters 2-7: '{text[2:7]}'")
    print(f"Every second character: '{text[::2]}'")
    print(f"Reverse string: '{text[::-1]}'")
    
    # Concatenation
    first = "Hello"
    second = "World"
    combined = first + ", " + second + "!"
    print(f"Concatenation: {combined}")
    
    # Repetition
    repeated = "Ha" * 3
    print(f"Repetition: {repeated}")


def demonstrate_string_methods():
    """Demonstrate string methods"""
    print("\n" + "=" * 50)
    print("STRING METHODS")
    print("=" * 50)
    
    text = "  Hello, World!  "
    
    print(f"Original: '{text}'")
    
    # Case methods
    print(f"Upper: '{text.upper()}'")
    print(f"Lower: '{text.lower()}'")
    print(f"Title: '{text.title()}'")
    print(f"Capitalize: '{text.capitalize()}'")
    print(f"Swapcase: '{text.swapcase()}'")
    
    # Whitespace methods
    print(f"Strip: '{text.strip()}'")
    print(f"Lstrip: '{text.lstrip()}'")
    print(f"Rstrip: '{text.rstrip()}'")
    
    # Search and replace
    sample = "Hello, World! Hello, Python!"
    print(f"\nSample text: '{sample}'")
    print(f"Count 'Hello': {sample.count('Hello')}")
    print(f"Find 'World': {sample.find('World')}")
    print(f"Find 'Python': {sample.find('Python')}")
    print(f"Find 'Java': {sample.find('Java')}")  # Returns -1 if not found
    print(f"Replace 'Hello' with 'Hi': '{sample.replace('Hello', 'Hi')}'")
    
    # Split and join
    words = sample.split()
    print(f"Split by space: {words}")
    joined = " ".join(words)
    print(f"Joined back: '{joined}'")
    
    # Split by specific character
    comma_split = sample.split(',')
    print(f"Split by comma: {comma_split}")


def demonstrate_string_formatting():
    """Demonstrate string formatting methods"""
    print("\n" + "=" * 50)
    print("STRING FORMATTING")
    print("=" * 50)
    
    name = "Alice"
    age = 25
    height = 5.6
    
    # f-strings (Python 3.6+)
    print("F-strings:")
    print(f"Name: {name}, Age: {age}, Height: {height}")
    print(f"Age in 5 years: {age + 5}")
    print(f"Height in cm: {height * 30.48:.1f}")
    
    # .format() method
    print("\n.format() method:")
    print("Name: {}, Age: {}, Height: {}".format(name, age, height))
    print("Name: {0}, Age: {1}, Height: {2}".format(name, age, height))
    print("Name: {n}, Age: {a}, Height: {h}".format(n=name, a=age, h=height))
    
    # % operator (old style)
    print("\n% operator:")
    print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))
    
    # Format specifiers
    number = 3.14159
    print(f"\nFormat specifiers:")
    print(f"Default: {number}")
    print(f"2 decimal places: {number:.2f}")
    print(f"Scientific notation: {number:.2e}")
    print(f"Percentage: {0.85:.1%}")
    print(f"Integer: {number:.0f}")
    
    # Alignment and padding
    text = "Python"
    print(f"\nAlignment:")
    print(f"Left aligned: '{text:<10}'")
    print(f"Right aligned: '{text:>10}'")
    print(f"Center aligned: '{text:^10}'")
    print(f"Zero padded: '{text:0>10}'")


def demonstrate_string_validation():
    """Demonstrate string validation methods"""
    print("\n" + "=" * 50)
    print("STRING VALIDATION")
    print("=" * 50)
    
    # Test strings
    test_strings = [
        "Hello123",
        "123456",
        "Hello World",
        "hello",
        "HELLO",
        "   ",
        "",
        "Hello@World",
        "Hello_World"
    ]
    
    for text in test_strings:
        print(f"Text: '{text}'")
        print(f"  isalpha(): {text.isalpha()}")
        print(f"  isdigit(): {text.isdigit()}")
        print(f"  isalnum(): {text.isalnum()}")
        print(f"  isspace(): {text.isspace()}")
        print(f"  islower(): {text.islower()}")
        print(f"  isupper(): {text.isupper()}")
        print(f"  istitle(): {text.istitle()}")
        print(f"  startswith('Hello'): {text.startswith('Hello')}")
        print(f"  endswith('World'): {text.endswith('World')}")
        print(f"  contains('o'): {'o' in text}")
        print()


def demonstrate_string_manipulation():
    """Demonstrate advanced string manipulation"""
    print("\n" + "=" * 50)
    print("ADVANCED STRING MANIPULATION")
    print("=" * 50)
    
    # String reversal
    text = "Hello, World!"
    reversed_text = text[::-1]
    print(f"Original: {text}")
    print(f"Reversed: {reversed_text}")
    
    # Palindrome check
    palindrome = "racecar"
    is_palindrome = palindrome == palindrome[::-1]
    print(f"\n'{palindrome}' is palindrome: {is_palindrome}")
    
    # Word count
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_count = len(words)
    print(f"\nSentence: '{sentence}'")
    print(f"Word count: {word_count}")
    
    # Character frequency
    text = "hello world"
    char_count = {}
    for char in text:
        if char != ' ':  # Skip spaces
            char_count[char] = char_count.get(char, 0) + 1
    
    print(f"\nCharacter frequency in '{text}':")
    for char, count in char_count.items():
        print(f"'{char}': {count}")
    
    # String cleaning
    dirty_text = "  Hello,   World!  \n\t"
    clean_text = dirty_text.strip().replace("  ", " ")
    print(f"\nDirty text: '{dirty_text}'")
    print(f"Clean text: '{clean_text}'")


def demonstrate_string_encoding():
    """Demonstrate string encoding and decoding"""
    print("\n" + "=" * 50)
    print("STRING ENCODING")
    print("=" * 50)
    
    text = "Hello, 世界!"  # Contains Unicode characters
    
    print(f"Original text: {text}")
    print(f"Length: {len(text)}")
    
    # Encode to bytes
    utf8_bytes = text.encode('utf-8')
    print(f"UTF-8 bytes: {utf8_bytes}")
    
    # Decode back to string
    decoded_text = utf8_bytes.decode('utf-8')
    print(f"Decoded text: {decoded_text}")
    
    # Different encodings
    ascii_text = "Hello, World!"
    ascii_bytes = ascii_text.encode('ascii')
    print(f"\nASCII text: {ascii_text}")
    print(f"ASCII bytes: {ascii_bytes}")


def practice_exercises():
    """Practice exercises for strings"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Reverse words in a sentence")
    sentence = "Python is awesome"
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    print(f"Original: '{sentence}'")
    print(f"Reversed words: '{reversed_sentence}'")
    
    print("\nExercise 2: Check if string is palindrome")
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for text in test_strings:
        # Remove spaces and convert to lowercase
        clean_text = text.replace(" ", "").lower()
        is_palindrome = clean_text == clean_text[::-1]
        print(f"'{text}' is palindrome: {is_palindrome}")
    
    print("\nExercise 3: Count vowels in a string")
    text = "Hello, World!"
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    print(f"Text: '{text}'")
    print(f"Vowel count: {vowel_count}")
    
    print("\nExercise 4: Convert string to title case")
    text = "hello world python programming"
    title_case = text.title()
    print(f"Original: '{text}'")
    print(f"Title case: '{title_case}'")
    
    print("\nExercise 5: Extract domain from email")
    email = "user@example.com"
    domain = email.split('@')[1]
    print(f"Email: {email}")
    print(f"Domain: {domain}")


if __name__ == "__main__":
    print("PYTHON STRING TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_string_creation()
    demonstrate_string_operations()
    demonstrate_string_methods()
    demonstrate_string_formatting()
    demonstrate_string_validation()
    demonstrate_string_manipulation()
    demonstrate_string_encoding()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 