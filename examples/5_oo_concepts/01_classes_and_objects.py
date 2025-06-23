"""
Python Object-Oriented Programming - Classes and Objects
=======================================================

This script covers the fundamentals of classes and objects in Python:
- Class definition
- Object instantiation
- Constructors (__init__)
- Instance methods
- Instance attributes
"""

print("=" * 50)
print("PYTHON OOP - CLASSES AND OBJECTS")
print("=" * 50)

# Basic class definition
class Person:
    """A simple class representing a person"""
    
    def __init__(self, name, age):
        """Constructor method - called when creating a new object"""
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def greet(self):
        """Instance method - can access instance attributes"""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def have_birthday(self):
        """Method that modifies instance state"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."
    
    def introduce(self, other_person):
        """Method that takes another object as parameter"""
        return f"Hi {other_person.name}, I'm {self.name}!"

print("\n1. BASIC CLASS AND OBJECT CREATION")
print("-" * 40)

# Creating objects (instances) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# Using instance methods
print(person1.greet())
print(person2.greet())
print(person3.greet())

# Accessing instance attributes
print(f"\n{person1.name} is {person1.age} years old")
print(f"{person2.name} is {person2.age} years old")

# Using methods that modify state
print(f"\n{person1.have_birthday()}")
print(f"Now {person1.name} is {person1.age} years old")

# Using methods with other objects
print(f"\n{person1.introduce(person2)}")

# More complex class example
class Student:
    """A class representing a student with grades"""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # List to store grades
        self.courses = []  # List to store courses
    
    def add_grade(self, course, grade):
        """Add a grade for a specific course"""
        self.grades.append({"course": course, "grade": grade})
        if course not in self.courses:
            self.courses.append(course)
    
    def get_average(self):
        """Calculate and return the average grade"""
        if not self.grades:
            return 0
        total = sum(grade["grade"] for grade in self.grades)
        return total / len(self.grades)
    
    def get_course_grade(self, course):
        """Get the grade for a specific course"""
        for grade in self.grades:
            if grade["course"] == course:
                return grade["grade"]
        return None
    
    def display_info(self):
        """Display student information"""
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Average Grade: {self.get_average():.2f}")
        print("Grades:")
        for grade in self.grades:
            print(f"  {grade['course']}: {grade['grade']}")

print("\n2. COMPLEX CLASS EXAMPLE - STUDENT")
print("-" * 40)

# Create a student and add grades
student1 = Student("Alice Johnson", "S001")
student1.add_grade("Math", 85)
student1.add_grade("Science", 92)
student1.add_grade("English", 78)
student1.add_grade("Math", 88)  # Update grade

# Display student information
student1.display_info()

# Create another student
student2 = Student("Bob Smith", "S002")
student2.add_grade("Math", 95)
student2.add_grade("Science", 89)

print(f"\n{student2.name}'s Math grade: {student2.get_course_grade('Math')}")
print(f"{student2.name}'s average: {student2.get_average():.2f}")

# Class with class attributes (shared across all instances)
class BankAccount:
    """A class representing a bank account"""
    
    # Class attribute - shared by all instances
    bank_name = "Python Bank"
    interest_rate = 0.02  # 2% interest rate
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
    
    def _generate_account_number(self):
        """Private method to generate account number"""
        import random
        return f"ACC{random.randint(10000, 99999)}"
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def add_interest(self):
        """Add interest to the account"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}"
    
    def get_info(self):
        """Get account information"""
        return {
            "account_holder": self.account_holder,
            "account_number": self.account_number,
            "balance": self.balance,
            "bank_name": self.bank_name
        }

print("\n3. CLASS WITH CLASS ATTRIBUTES - BANK ACCOUNT")
print("-" * 40)

# Create bank accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Use instance methods
print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.add_interest())

print(account2.deposit(300))
print(account2.withdraw(50))

# Access class attributes
print(f"\nBank name: {BankAccount.bank_name}")
print(f"Interest rate: {BankAccount.interest_rate}")

# Get account information
print(f"\nAccount 1 info: {account1.get_info()}")
print(f"Account 2 info: {account2.get_info()}")

# Demonstrating object identity and equality
print("\n4. OBJECT IDENTITY AND EQUALITY")
print("-" * 40)

# Create two people with same attributes
person_a = Person("Alice", 30)
person_b = Person("Alice", 30)

print(f"person_a == person_b: {person_a == person_b}")  # False (different objects)
print(f"person_a is person_b: {person_a is person_b}")  # False (different memory locations)

# Create a reference to the same object
person_c = person_a
print(f"person_a is person_c: {person_a is person_c}")  # True (same object)

# Custom equality method
class Point:
    """A class representing a 2D point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Custom equality method"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        """String representation"""
        return f"Point({self.x}, {self.y})"

# Test custom equality
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 6)

print(f"point1: {point1}")
print(f"point2: {point2}")
print(f"point3: {point3}")
print(f"point1 == point2: {point1 == point2}")  # True (custom equality)
print(f"point1 == point3: {point1 == point3}")  # False

print("\n" + "=" * 50)
print("CLASSES AND OBJECTS COMPLETED!")
print("=" * 50) 