#!/usr/bin/env python3
"""
Python Numbers Examples
=======================

This file contains examples of Python's numeric data types:
- Integers (int)
- Floating Point Numbers (float) 
- Complex Numbers (complex)
- Mathematical operations

Author: Python for Testers
Date: 2024
"""

def demonstrate_integers():
    """Demonstrate integer operations"""
    print("=" * 50)
    print("INTEGER EXAMPLES")
    print("=" * 50)
    
    # Basic integer creation
    int_number = 5
    negative_int = -10
    large_int = 1000000
    
    print(f"Integer: {int_number}, Type: {type(int_number)}")
    print(f"Negative integer: {negative_int}, Type: {type(negative_int)}")
    print(f"Large integer: {large_int}, Type: {type(large_int)}")
    
    # Integer operations
    a = 10
    b = 3
    print(f"\nInteger Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Power: {a} ** {b} = {a ** b}")
    
    # Integer conversion
    float_to_int = int(3.14)
    string_to_int = int("123")
    print(f"\nType Conversions:")
    print(f"float(3.14) -> int: {float_to_int}")
    print(f"string('123') -> int: {string_to_int}")


def demonstrate_floats():
    """Demonstrate floating point operations"""
    print("\n" + "=" * 50)
    print("FLOAT EXAMPLES")
    print("=" * 50)
    
    # Basic float creation
    float_number = 5.0
    pi = 3.14159
    scientific = 1.23e-4
    
    print(f"Float: {float_number}, Type: {type(float_number)}")
    print(f"Pi: {pi}, Type: {type(pi)}")
    print(f"Scientific notation: {scientific}, Type: {type(scientific)}")
    
    # Float operations
    x = 10.5
    y = 3.2
    print(f"\nFloat Operations:")
    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Floor Division: {x} // {y} = {x // y}")
    print(f"Modulus: {x} % {y} = {x % y}")
    print(f"Power: {x} ** {y} = {x ** y}")
    
    # Float conversion
    int_to_float = float(5)
    string_to_float = float("3.14")
    print(f"\nType Conversions:")
    print(f"int(5) -> float: {int_to_float}")
    print(f"string('3.14') -> float: {string_to_float}")


def demonstrate_complex_numbers():
    """Demonstrate complex number operations"""
    print("\n" + "=" * 50)
    print("COMPLEX NUMBER EXAMPLES")
    print("=" * 50)
    
    # Basic complex number creation
    complex_number = 3 + 4j
    real_part = 5
    imag_part = 2
    complex_from_parts = complex(real_part, imag_part)
    
    print(f"Complex: {complex_number}, Type: {type(complex_number)}")
    print(f"From parts: {complex_from_parts}, Type: {type(complex_from_parts)}")
    
    # Complex number properties
    print(f"\nComplex Number Properties:")
    print(f"Real part: {complex_number.real}")
    print(f"Imaginary part: {complex_number.imag}")
    print(f"Conjugate: {complex_number.conjugate()}")
    
    # Complex number operations
    c1 = 1 + 2j
    c2 = 3 + 4j
    print(f"\nComplex Operations:")
    print(f"c1 = {c1}, c2 = {c2}")
    print(f"Addition: {c1} + {c2} = {c1 + c2}")
    print(f"Subtraction: {c1} - {c2} = {c1 - c2}")
    print(f"Multiplication: {c1} * {c2} = {c1 * c2}")
    print(f"Division: {c1} / {c2} = {c1 / c2}")


def demonstrate_mathematical_functions():
    """Demonstrate mathematical functions"""
    print("\n" + "=" * 50)
    print("MATHEMATICAL FUNCTIONS")
    print("=" * 50)
    
    import math
    
    # Basic math functions
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Absolute value of -5: {abs(-5)}")
    print(f"Round 3.7: {round(3.7)}")
    print(f"Ceiling of 3.2: {math.ceil(3.2)}")
    print(f"Floor of 3.8: {math.floor(3.8)}")
    print(f"Maximum of 5, 10, 3: {max(5, 10, 3)}")
    print(f"Minimum of 5, 10, 3: {min(5, 10, 3)}")
    
    # Trigonometric functions
    angle = math.pi / 4  # 45 degrees
    print(f"\nTrigonometric Functions (angle = π/4):")
    print(f"Sine: {math.sin(angle)}")
    print(f"Cosine: {math.cos(angle)}")
    print(f"Tangent: {math.tan(angle)}")


def practice_exercises():
    """Practice exercises for numbers"""
    print("\n" + "=" * 50)
    print("PRACTICE EXERCISES")
    print("=" * 50)
    
    print("Exercise 1: Calculate the area of a circle with radius 5")
    radius = 5
    import math
    area = math.pi * radius ** 2
    print(f"Area = π × {radius}² = {area:.2f}")
    
    print("\nExercise 2: Convert temperature from Celsius to Fahrenheit")
    celsius = 25
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    
    print("\nExercise 3: Calculate compound interest")
    principal = 1000
    rate = 0.05  # 5%
    time = 3
    amount = principal * (1 + rate) ** time
    print(f"Principal: ${principal}")
    print(f"Rate: {rate*100}%")
    print(f"Time: {time} years")
    print(f"Final amount: ${amount:.2f}")


if __name__ == "__main__":
    print("PYTHON NUMBERS TUTORIAL")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_integers()
    demonstrate_floats()
    demonstrate_complex_numbers()
    demonstrate_mathematical_functions()
    practice_exercises()
    
    print("\n" + "=" * 50)
    print("TUTORIAL COMPLETE!")
    print("=" * 50) 