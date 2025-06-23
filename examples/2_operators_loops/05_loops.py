"""
Loops in Python
Examples and exercises for for and while loops
"""

print("=== Loops Examples ===")

# Basic for loop with range
print("Counting from 0 to 4:")
for i in range(5):
    print(i)

# for loop with list
fruits = ["apple", "banana", "cherry"]
print("\nFruits I like:")
for fruit in fruits:
    print(f"I like {fruit}")

# for loop with enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# while loop
print("\nCounting with while loop:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Loop control statements
print("\nLoop control examples:")
print("Break example:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

print("\n\nContinue example:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print("\n\n=== Practical Examples ===")

# Sum of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Find maximum value
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum value in {numbers}: {max_num}")

# Count occurrences
text = "hello world"
letter_count = {}
for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(f"Letter count in '{text}': {letter_count}")

# Password retry logic
def simulate_login(password):
    """Simulate login attempt"""
    correct_password = "secret123"
    return password == correct_password

attempts = 0
max_attempts = 3
success = False

print("\nPassword retry simulation:")
while attempts < max_attempts and not success:
    attempts += 1
    test_password = "wrong" if attempts < 3 else "secret123"
    print(f"Attempt {attempts}: Trying '{test_password}'")
    
    if simulate_login(test_password):
        success = True
        print("✅ Login successful!")
    else:
        if attempts < max_attempts:
            print("❌ Wrong password, try again")
        else:
            print("❌ Account locked")

print("\n=== Practice Exercises ===")

# Exercise 1: FizzBuzz
def fizzbuzz(n):
    """Print FizzBuzz for numbers from 1 to n"""
    print(f"FizzBuzz from 1 to {n}:")
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)

# Exercise 2: Find prime numbers
def find_primes(max_num):
    """Find all prime numbers up to max_num"""
    primes = []
    for num in range(2, max_num + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(f"\nPrime numbers up to 30: {find_primes(30)}")

# Exercise 3: Multiplication table
def print_multiplication_table(n):
    """Print multiplication table for n"""
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

print_multiplication_table(7)

# Exercise 4: Pattern printing
def print_pattern(rows):
    """Print a pattern of asterisks"""
    print(f"Pattern with {rows} rows:")
    for i in range(1, rows + 1):
        print("*" * i)

print_pattern(5)

# Exercise 5: List operations
def analyze_list(numbers):
    """Analyze a list of numbers"""
    if not numbers:
        return "Empty list"
    
    total = sum(numbers)
    average = total / len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Count even and odd numbers
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return {
        "total": total,
        "average": average,
        "min": min_val,
        "max": max_val,
        "even_count": even_count,
        "odd_count": odd_count
    }

# Test list analysis
test_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    []
]

for lst in test_lists:
    result = analyze_list(lst)
    print(f"\nAnalysis of {lst}:")
    if isinstance(result, dict):
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"  {result}")

# Exercise 6: Number guessing game simulation
import random

def number_guessing_game():
    """Simulate a number guessing game"""
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    
    print(f"\nNumber guessing game (1-10):")
    print(f"Secret number: {secret_number}")  # For demonstration
    
    while attempts < max_attempts:
        attempts += 1
        # Simulate different guesses
        if attempts == 1:
            guess = 5
        elif attempts == 2:
            guess = 8
        else:
            guess = secret_number
        
        print(f"Attempt {attempts}: Guessing {guess}")
        
        if guess == secret_number:
            print(f"✅ Correct! You found it in {attempts} attempts")
            return True
        elif guess < secret_number:
            print("Hint: Too low")
        else:
            print("Hint: Too high")
    
    print(f"❌ Game over! The number was {secret_number}")
    return False

number_guessing_game()

# Exercise 7: Data processing
def process_student_data(students):
    """Process student data and generate statistics"""
    total_students = len(students)
    total_score = 0
    passed_count = 0
    failed_count = 0
    
    print(f"\nProcessing {total_students} students:")
    
    for student in students:
        name, score = student
        total_score += score
        
        if score >= 60:
            passed_count += 1
            status = "PASS"
        else:
            failed_count += 1
            status = "FAIL"
        
        print(f"  {name}: {score} ({status})")
    
    average_score = total_score / total_students if total_students > 0 else 0
    pass_rate = (passed_count / total_students) * 100 if total_students > 0 else 0
    
    print(f"\nSummary:")
    print(f"  Total students: {total_students}")
    print(f"  Average score: {average_score:.1f}")
    print(f"  Passed: {passed_count}")
    print(f"  Failed: {failed_count}")
    print(f"  Pass rate: {pass_rate:.1f}%")

# Test student data processing
student_data = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 45),
    ("Diana", 95),
    ("Eve", 58)
]

process_student_data(student_data) 