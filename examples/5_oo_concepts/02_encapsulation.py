"""
Python Object-Oriented Programming - Encapsulation
=================================================

This script covers encapsulation concepts in Python:
- Private attributes (double underscore)
- Protected attributes (single underscore)
- Getter and setter methods
- Property decorators
- Data hiding principles
"""

print("=" * 50)
print("PYTHON OOP - ENCAPSULATION")
print("=" * 50)

# Basic encapsulation with private attributes
class BankAccount:
    """A class demonstrating basic encapsulation"""
    
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (double underscore)
        self._account_type = "Savings"  # Protected attribute (single underscore)
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Public getter method for balance"""
        return self.__balance
    
    def set_balance(self, new_balance):
        """Public setter method for balance (with validation)"""
        if new_balance >= 0:
            self.__balance = new_balance
            return f"Balance updated to ${self.__balance}"
        else:
            return "Invalid balance amount"

print("\n1. BASIC ENCAPSULATION")
print("-" * 40)

# Create a bank account
account = BankAccount(1000)
print(f"Initial balance: ${account.get_balance()}")

# Use public methods to interact with private data
print(account.deposit(500))
print(account.withdraw(200))
print(account.set_balance(1500))

# Try to access private attribute directly (this will work but is not recommended)
try:
    print(f"Direct access to private attribute: {account._BankAccount__balance}")
except AttributeError as e:
    print(f"Error accessing private attribute: {e}")

# Protected attribute access
print(f"Protected attribute: {account._account_type}")

# Advanced encapsulation with property decorators
class Temperature:
    """A class demonstrating property decorators for encapsulation"""
    
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """Property getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Property setter for celsius with validation"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Property getter for fahrenheit (computed from celsius)"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Property setter for fahrenheit (converts to celsius)"""
        celsius = (value - 32) * 5/9
        self.celsius = celsius  # Uses the celsius setter for validation
    
    @property
    def kelvin(self):
        """Property getter for kelvin (computed from celsius)"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Property setter for kelvin (converts to celsius)"""
        celsius = value - 273.15
        self.celsius = celsius  # Uses the celsius setter for validation

print("\n2. PROPERTY DECORATORS")
print("-" * 40)

# Create a temperature object
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Use property setters
temp.celsius = 30
print(f"After setting celsius to 30: {temp.celsius}°C, {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"After setting fahrenheit to 86: {temp.celsius}°C, {temp.fahrenheit}°F")

# Try to set invalid temperature
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

# Encapsulation with computed properties
class Rectangle:
    """A class demonstrating computed properties"""
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        """Computed property - area cannot be set directly"""
        return self._width * self._height
    
    @property
    def perimeter(self):
        """Computed property - perimeter cannot be set directly"""
        return 2 * (self._width + self._height)
    
    @property
    def is_square(self):
        """Computed property - boolean property"""
        return self._width == self._height

print("\n3. COMPUTED PROPERTIES")
print("-" * 40)

# Create a rectangle
rect = Rectangle(5, 3)
print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")
print(f"Is square: {rect.is_square}")

# Change dimensions
rect.width = 4
rect.height = 4
print(f"After changing to 4x4:")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")
print(f"Is square: {rect.is_square}")

# Try to set area directly (this will fail)
try:
    rect.area = 20
except AttributeError as e:
    print(f"Cannot set area directly: {e}")

# Encapsulation with read-only properties
class Circle:
    """A class with read-only properties"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Read-only property for radius"""
        return self._radius
    
    @property
    def diameter(self):
        """Read-only computed property"""
        return 2 * self._radius
    
    @property
    def area(self):
        """Read-only computed property"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Read-only computed property"""
        import math
        return 2 * math.pi * self._radius
    
    def resize(self, new_radius):
        """Method to change radius (not a property setter)"""
        if new_radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = new_radius

print("\n4. READ-ONLY PROPERTIES")
print("-" * 40)

# Create a circle
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# Resize the circle
circle.resize(7)
print(f"After resizing to radius 7:")
print(f"Radius: {circle.radius}")
print(f"Area: {circle.area:.2f}")

# Try to set read-only properties
try:
    circle.radius = 10
except AttributeError as e:
    print(f"Cannot set radius directly: {e}")

# Encapsulation with validation and business logic
class Student:
    """A class demonstrating encapsulation with validation"""
    
    def __init__(self, name, age, student_id):
        self._name = name
        self._age = age
        self._student_id = student_id
        self._grades = []
        self._courses = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("Age must be a positive integer between 0 and 120")
        self._age = value
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def grades(self):
        """Return a copy to prevent external modification"""
        return self._grades.copy()
    
    @property
    def average_grade(self):
        """Computed property for average grade"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)
    
    def add_grade(self, grade):
        """Method to add a grade with validation"""
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
        self._grades.append(grade)
    
    def get_grade_report(self):
        """Method that provides controlled access to internal data"""
        return {
            "name": self._name,
            "student_id": self._student_id,
            "average_grade": self.average_grade,
            "total_grades": len(self._grades)
        }

print("\n5. ENCAPSULATION WITH VALIDATION")
print("-" * 40)

# Create a student
student = Student("Alice Johnson", 20, "S001")
print(f"Student: {student.name}, Age: {student.age}")

# Add grades
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(f"Grades: {student.grades}")
print(f"Average: {student.average_grade:.2f}")

# Get grade report
report = student.get_grade_report()
print(f"Grade report: {report}")

# Try to modify grades directly (this won't work)
grades = student.grades
grades.append(100)  # This modifies the copy, not the original
print(f"After trying to modify grades: {student.grades}")  # Original unchanged

# Try invalid operations
try:
    student.age = -5
except ValueError as e:
    print(f"Error setting age: {e}")

try:
    student.add_grade(150)
except ValueError as e:
    print(f"Error adding grade: {e}")

print("\n" + "=" * 50)
print("ENCAPSULATION COMPLETED!")
print("=" * 50) 