"""
Python Object-Oriented Programming - Inheritance
===============================================

This script covers inheritance concepts in Python:
- Single inheritance
- Method overriding
- Super() function
- Multiple inheritance
- Method resolution order (MRO)
- Abstract base classes
"""

print("=" * 50)
print("PYTHON OOP - INHERITANCE")
print("=" * 50)

# Basic single inheritance
class Animal:
    """Base class (parent class)"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        """Base method that can be overridden"""
        return "Some sound"
    
    def get_info(self):
        """Method that uses inherited attributes"""
        return f"{self.name} is a {self.species}"
    
    def move(self):
        """Base method for movement"""
        return f"{self.name} is moving"

class Dog(Animal):
    """Child class inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        """Override the speak method"""
        return "Woof!"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} is fetching the ball"
    
    def get_info(self):
        """Override get_info to include breed"""
        base_info = super().get_info()
        return f"{base_info} (Breed: {self.breed})"

class Cat(Animal):
    """Another child class inheriting from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def speak(self):
        """Override the speak method"""
        return "Meow!"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} is climbing a tree"
    
    def get_info(self):
        """Override get_info to include color"""
        base_info = super().get_info()
        return f"{base_info} (Color: {self.color})"

print("\n1. BASIC SINGLE INHERITANCE")
print("-" * 40)

# Create instances of child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

# Use inherited methods
print(dog.get_info())
print(cat.get_info())

# Use overridden methods
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

# Use child-specific methods
print(dog.fetch())
print(cat.climb())

# Use inherited methods from parent
print(dog.move())
print(cat.move())

# Multiple inheritance
class FlyingAnimal(Animal):
    """Mixin class for flying animals"""
    
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan
    
    def fly(self):
        return f"{self.name} is flying with {self.wingspan}m wingspan"

class SwimmingAnimal(Animal):
    """Mixin class for swimming animals"""
    
    def __init__(self, name, species, swim_speed):
        super().__init__(name, species)
        self.swim_speed = swim_speed
    
    def swim(self):
        return f"{self.name} is swimming at {self.swim_speed} km/h"

class Duck(Animal, FlyingAnimal, SwimmingAnimal):
    """Class with multiple inheritance"""
    
    def __init__(self, name):
        # Initialize all parent classes
        Animal.__init__(self, name, "Duck")
        FlyingAnimal.__init__(self, name, "Duck", 0.5)
        SwimmingAnimal.__init__(self, name, "Duck", 10)
    
    def speak(self):
        return "Quack!"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Wingspan: {self.wingspan}m, Swim speed: {self.swim_speed} km/h)"

print("\n2. MULTIPLE INHERITANCE")
print("-" * 40)

# Create a duck
duck = Duck("Donald")
print(duck.get_info())
print(f"{duck.name} says: {duck.speak()}")
print(duck.fly())
print(duck.swim())

# Check method resolution order
print(f"\nMethod Resolution Order (MRO) for Duck:")
for i, cls in enumerate(Duck.__mro__):
    print(f"  {i}: {cls.__name__}")

# Inheritance with abstract base classes
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    def get_info(self):
        """Concrete method that uses abstract methods"""
        return f"{self.color} shape with area {self.area():.2f} and perimeter {self.perimeter():.2f}"

class Rectangle(Shape):
    """Concrete class implementing Shape"""
    
    def __init__(self, width, height, color="blue"):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Concrete class implementing Shape"""
    
    def __init__(self, radius, color="red"):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

print("\n3. ABSTRACT BASE CLASSES")
print("-" * 40)

# Create concrete shapes
rectangle = Rectangle(5, 3, "green")
circle = Circle(4, "purple")

print(rectangle.get_info())
print(circle.get_info())

# Try to create an abstract class instance (this will fail)
try:
    shape = Shape("black")
except TypeError as e:
    print(f"Cannot instantiate abstract class: {e}")

# Inheritance with method chaining
class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._engine_started = False
    
    def start_engine(self):
        if not self._engine_started:
            self._engine_started = True
            return f"{self.brand} {self.model} engine started"
        return f"{self.brand} {self.model} engine is already running"
    
    def stop_engine(self):
        if self._engine_started:
            self._engine_started = False
            return f"{self.brand} {self.model} engine stopped"
        return f"{self.brand} {self.model} engine is already off"
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def open_door(self, door_number):
        if 1 <= door_number <= self.num_doors:
            return f"Opening door {door_number} of {self.brand} {self.model}"
        return f"Invalid door number. This car has {self.num_doors} doors"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} ({self.num_doors} doors)"

class ElectricCar(Car):
    """Electric car inheriting from Car"""
    
    def __init__(self, brand, model, year, num_doors, battery_capacity):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity
        self._battery_level = 100
    
    def charge(self, percentage):
        if 0 <= percentage <= 100:
            self._battery_level = min(100, self._battery_level + percentage)
            return f"Charged to {self._battery_level}%"
        return "Invalid charging percentage"
    
    def get_battery_level(self):
        return f"Battery level: {self._battery_level}%"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Electric, {self.battery_capacity}kWh battery)"

print("\n4. METHOD CHAINING AND MULTI-LEVEL INHERITANCE")
print("-" * 40)

# Create vehicles
car = Car("Toyota", "Camry", 2020, 4)
electric_car = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

# Use inherited methods
print(car.start_engine())
print(car.open_door(2))
print(car.get_info())

print(electric_car.start_engine())
print(electric_car.charge(20))
print(electric_car.get_battery_level())
print(electric_car.get_info())

# Inheritance with class methods and static methods
class Employee:
    """Base class for employees"""
    
    company = "TechCorp"
    total_employees = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
        self.employee_id = Employee.total_employees
    
    @classmethod
    def get_company_info(cls):
        return f"Company: {cls.company}, Total employees: {cls.total_employees}"
    
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
    
    def get_info(self):
        return f"Employee {self.employee_id}: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    """Manager class inheriting from Employee"""
    
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.subordinates = []
    
    def add_subordinate(self, employee):
        self.subordinates.append(employee)
        return f"Added {employee.name} to {self.department} department"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Department: {self.department}, Subordinates: {len(self.subordinates)}"
    
    @classmethod
    def get_company_info(cls):
        base_info = super().get_company_info()
        return f"{base_info} (Manager class)"

print("\n5. INHERITANCE WITH CLASS AND STATIC METHODS")
print("-" * 40)

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
manager = Manager("Charlie", 80000, "Engineering")

# Use class methods
print(Employee.get_company_info())
print(Manager.get_company_info())

# Use static methods
print(f"Is $50000 a valid salary? {Employee.is_valid_salary(50000)}")
print(f"Is $-1000 a valid salary? {Employee.is_valid_salary(-1000)}")

# Use instance methods
print(emp1.get_info())
print(manager.get_info())

# Add subordinates
manager.add_subordinate(emp1)
manager.add_subordinate(emp2)
print(manager.get_info())

print("\n" + "=" * 50)
print("INHERITANCE COMPLETED!")
print("=" * 50) 