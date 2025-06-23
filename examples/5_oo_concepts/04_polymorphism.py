"""
Python Object-Oriented Programming - Polymorphism
================================================

This script covers polymorphism concepts in Python:
- Method overriding
- Duck typing
- Operator overloading
- Function polymorphism
- Interface polymorphism
"""

print("=" * 50)
print("PYTHON OOP - POLYMORPHISM")
print("=" * 50)

# Method overriding (runtime polymorphism)
class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Base method to be overridden"""
        return "Some sound"
    
    def move(self):
        """Base method to be overridden"""
        return f"{self.name} is moving"

class Dog(Animal):
    """Dog class with overridden methods"""
    
    def speak(self):
        """Override speak method"""
        return "Woof!"
    
    def move(self):
        """Override move method"""
        return f"{self.name} is running on four legs"

class Cat(Animal):
    """Cat class with overridden methods"""
    
    def speak(self):
        """Override speak method"""
        return "Meow!"
    
    def move(self):
        """Override move method"""
        return f"{self.name} is walking gracefully"

class Bird(Animal):
    """Bird class with overridden methods"""
    
    def speak(self):
        """Override speak method"""
        return "Tweet!"
    
    def move(self):
        """Override move method"""
        return f"{self.name} is flying"

print("\n1. METHOD OVERRIDING (RUNTIME POLYMORPHISM)")
print("-" * 40)

# Create different animals
animals = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Bird("Tweety")
]

# Polymorphic behavior - same method call, different results
for animal in animals:
    print(f"{animal.name}: {animal.speak()}")
    print(f"{animal.name}: {animal.move()}")
    print()

# Duck typing - objects with same interface
class Duck:
    """Duck class with speak and move methods"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Quack!"
    
    def move(self):
        return f"{self.name} is swimming"

class Robot:
    """Robot class with same interface as animals"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Beep beep!"
    
    def move(self):
        return f"{self.name} is rolling on wheels"

print("\n2. DUCK TYPING")
print("-" * 40)

# Add more objects with same interface
animals.append(Duck("Donald"))
animals.append(Robot("R2D2"))

# All objects work the same way regardless of their class
for animal in animals:
    print(f"{animal.name}: {animal.speak()}")
    print(f"{animal.name}: {animal.move()}")
    print()

# Function polymorphism
def make_sound(animal):
    """Function that works with any object that has a speak method"""
    return animal.speak()

def describe_movement(animal):
    """Function that works with any object that has a move method"""
    return animal.move()

print("\n3. FUNCTION POLYMORPHISM")
print("-" * 40)

# Use polymorphic functions
for animal in animals:
    print(f"{animal.name} sound: {make_sound(animal)}")
    print(f"{animal.name} movement: {describe_movement(animal)}")
    print()

# Operator overloading
class Point:
    """Class demonstrating operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError(f"Cannot add Point and {type(other).__name__}")
    
    def __sub__(self, other):
        """Overload - operator"""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        else:
            raise TypeError(f"Cannot subtract {type(other).__name__} from Point")
    
    def __eq__(self, other):
        """Overload == operator"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Overload < operator (compare by distance from origin)"""
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented
    
    def __str__(self):
        """String representation"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Point(x={self.x}, y={self.y})"

print("\n4. OPERATOR OVERLOADING")
print("-" * 40)

# Create points
p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(5, 6)

# Use overloaded operators
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")

# Addition
result = p1 + p2
print(f"p1 + p2 = {result}")

# Addition with scalar
result = p1 + 5
print(f"p1 + 5 = {result}")

# Subtraction
result = p1 - p2
print(f"p1 - p2 = {result}")

# Comparison
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p3: {p1 < p3}")

# Container polymorphism
class Shape:
    """Base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """To be overridden by subclasses"""
        return 0
    
    def perimeter(self):
        """To be overridden by subclasses"""
        return 0
    
    def describe(self):
        """Common method for all shapes"""
        return f"{self.name} with area {self.area():.2f} and perimeter {self.perimeter():.2f}"

class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Triangle(Shape):
    """Triangle class"""
    
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

print("\n5. CONTAINER POLYMORPHISM")
print("-" * 40)

# Create different shapes
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

# Process all shapes polymorphically
total_area = 0
total_perimeter = 0

for shape in shapes:
    print(shape.describe())
    total_area += shape.area()
    total_perimeter += shape.perimeter()

print(f"\nTotal area: {total_area:.2f}")
print(f"Total perimeter: {total_perimeter:.2f}")

# Interface polymorphism with abstract base classes
from abc import ABC, abstractmethod

class Drawable(ABC):
    """Abstract interface for drawable objects"""
    
    @abstractmethod
    def draw(self):
        """Abstract method to draw the object"""
        pass
    
    @abstractmethod
    def get_color(self):
        """Abstract method to get the color"""
        pass

class Square(Drawable):
    """Square implementing Drawable interface"""
    
    def __init__(self, size, color="blue"):
        self.size = size
        self.color = color
    
    def draw(self):
        return f"Drawing a {self.color} square with size {self.size}"
    
    def get_color(self):
        return self.color

class Star(Drawable):
    """Star implementing Drawable interface"""
    
    def __init__(self, points, color="yellow"):
        self.points = points
        self.color = color
    
    def draw(self):
        return f"Drawing a {self.color} star with {self.points} points"
    
    def get_color(self):
        return self.color

print("\n6. INTERFACE POLYMORPHISM")
print("-" * 40)

# Create drawable objects
drawables = [
    Square(10, "red"),
    Star(5, "gold"),
    Square(5, "green")
]

# Process all drawable objects
for drawable in drawables:
    print(drawable.draw())
    print(f"Color: {drawable.get_color()}")
    print()

# Polymorphic function that works with any drawable
def draw_all(objects):
    """Draw all objects in a list"""
    for obj in objects:
        print(obj.draw())

print("Drawing all objects:")
draw_all(drawables)

# Polymorphism with built-in functions
class Book:
    """Book class with custom string representation"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation for str()"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Detailed representation for repr()"""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
    def __len__(self):
        """Length representation"""
        return self.pages
    
    def __contains__(self, item):
        """Check if item is in book (title or author)"""
        return item.lower() in self.title.lower() or item.lower() in self.author.lower()

print("\n7. POLYMORPHISM WITH BUILT-IN FUNCTIONS")
print("-" * 40)

# Create books
books = [
    Book("Python Programming", "John Smith", 300),
    Book("Data Science", "Jane Doe", 250),
    Book("Machine Learning", "Bob Johnson", 400)
]

# Use built-in functions polymorphically
for book in books:
    print(f"Book: {book}")  # Uses __str__
    print(f"Length: {len(book)} pages")  # Uses __len__
    print(f"Contains 'python': {'python' in book}")  # Uses __contains__
    print(f"Repr: {repr(book)}")  # Uses __repr__
    print()

print("\n" + "=" * 50)
print("POLYMORPHISM COMPLETED!")
print("=" * 50) 