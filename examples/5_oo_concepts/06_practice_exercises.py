"""
Python Object-Oriented Programming - Practice Exercises
=====================================================

This script contains practice exercises for OOP concepts:
- Class design exercises
- Inheritance challenges
- Encapsulation practice
- Polymorphism exercises
- Real-world application problems
"""

print("=" * 50)
print("PYTHON OOP - PRACTICE EXERCISES")
print("=" * 50)

# Exercise 1: Library Management System
print("\nEXERCISE 1: LIBRARY MANAGEMENT SYSTEM")
print("-" * 40)
print("Create a library management system with the following classes:")
print("- Book: title, author, isbn, available")
print("- Library: collection of books, methods to add/remove/borrow/return")
print("- Member: name, member_id, borrowed_books")
print("- Implement proper encapsulation and inheritance")

class Book:
    """Book class for library management"""
    
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = True
        self._borrowed_by = None
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def available(self):
        return self._available
    
    def borrow(self, member_id):
        """Borrow the book"""
        if self._available:
            self._available = False
            self._borrowed_by = member_id
            return True
        return False
    
    def return_book(self):
        """Return the book"""
        if not self._available:
            self._available = True
            self._borrowed_by = None
            return True
        return False
    
    def __str__(self):
        status = "Available" if self._available else f"Borrowed by {self._borrowed_by}"
        return f"'{self._title}' by {self._author} (ISBN: {self._isbn}) - {status}"

class Member:
    """Library member class"""
    
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def member_id(self):
        return self._member_id
    
    @property
    def borrowed_books(self):
        return self._borrowed_books.copy()
    
    def borrow_book(self, book):
        """Borrow a book"""
        if book.borrow(self._member_id):
            self._borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        """Return a book"""
        if book in self._borrowed_books:
            if book.return_book():
                self._borrowed_books.remove(book)
                return True
        return False
    
    def __str__(self):
        return f"Member: {self._name} (ID: {self._member_id}) - Books: {len(self._borrowed_books)}"

class Library:
    """Library management class"""
    
    def __init__(self, name):
        self._name = name
        self._books = {}
        self._members = {}
    
    def add_book(self, book):
        """Add a book to the library"""
        self._books[book.isbn] = book
        return f"Added book: {book.title}"
    
    def remove_book(self, isbn):
        """Remove a book from the library"""
        if isbn in self._books:
            book = self._books.pop(isbn)
            return f"Removed book: {book.title}"
        return "Book not found"
    
    def add_member(self, member):
        """Add a member to the library"""
        self._members[member.member_id] = member
        return f"Added member: {member.name}"
    
    def borrow_book(self, member_id, isbn):
        """Borrow a book for a member"""
        if member_id not in self._members:
            return "Member not found"
        if isbn not in self._books:
            return "Book not found"
        
        member = self._members[member_id]
        book = self._books[isbn]
        
        if member.borrow_book(book):
            return f"Book '{book.title}' borrowed by {member.name}"
        else:
            return f"Book '{book.title}' is not available"
    
    def return_book(self, member_id, isbn):
        """Return a book from a member"""
        if member_id not in self._members:
            return "Member not found"
        if isbn not in self._books:
            return "Book not found"
        
        member = self._members[member_id]
        book = self._books[isbn]
        
        if member.return_book(book):
            return f"Book '{book.title}' returned by {member.name}"
        else:
            return f"Book '{book.title}' was not borrowed by {member.name}"
    
    def list_books(self):
        """List all books"""
        return [str(book) for book in self._books.values()]
    
    def list_members(self):
        """List all members"""
        return [str(member) for member in self._members.values()]
    
    def search_books(self, keyword):
        """Search books by title or author"""
        results = []
        keyword = keyword.lower()
        for book in self._books.values():
            if (keyword in book.title.lower() or 
                keyword in book.author.lower()):
                results.append(str(book))
        return results

# Test the library system
print("Testing Library Management System:")
library = Library("Central Library")

# Add books
book1 = Book("Python Programming", "John Smith", "1234567890")
book2 = Book("Data Science", "Jane Doe", "0987654321")
book3 = Book("Machine Learning", "Bob Johnson", "1122334455")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

# Add members
member1 = Member("Alice Brown", "M001")
member2 = Member("Charlie Wilson", "M002")

print(library.add_member(member1))
print(library.add_member(member2))

# Borrow and return books
print(library.borrow_book("M001", "1234567890"))
print(library.borrow_book("M002", "0987654321"))
print(library.return_book("M001", "1234567890"))

# List books and members
print("\nAll books:")
for book in library.list_books():
    print(f"  {book}")

print("\nAll members:")
for member in library.list_members():
    print(f"  {member}")

# Search books
print("\nSearch results for 'python':")
for result in library.search_books("python"):
    print(f"  {result}")

# Exercise 2: Shape Calculator
print("\n\nEXERCISE 2: SHAPE CALCULATOR")
print("-" * 40)
print("Create a shape calculator with inheritance:")
print("- Base Shape class with abstract methods")
print("- Rectangle, Circle, Triangle classes")
print("- Calculate area, perimeter, and other properties")
print("- Use polymorphism to handle different shapes")

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass
    
    def describe(self):
        """Describe the shape"""
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
    
    def is_square(self):
        """Check if rectangle is a square"""
        return self.width == self.height
    
    def diagonal(self):
        """Calculate diagonal length"""
        return math.sqrt(self.width**2 + self.height**2)

class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """Calculate diameter"""
        return 2 * self.radius
    
    def circumference(self):
        """Calculate circumference (same as perimeter)"""
        return self.perimeter()

class Triangle(Shape):
    """Triangle class"""
    
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
        self._validate_triangle()
    
    def _validate_triangle(self):
        """Validate triangle inequality"""
        sides = [self.a, self.b, self.c]
        if not all(s > 0 for s in sides):
            raise ValueError("All sides must be positive")
        if not (sides[0] + sides[1] > sides[2] and 
                sides[1] + sides[2] > sides[0] and 
                sides[0] + sides[2] > sides[1]):
            raise ValueError("Triangle inequality not satisfied")
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def is_equilateral(self):
        """Check if triangle is equilateral"""
        return self.a == self.b == self.c
    
    def is_isosceles(self):
        """Check if triangle is isosceles"""
        return (self.a == self.b or self.b == self.c or self.a == self.c)
    
    def is_right_angled(self):
        """Check if triangle is right-angled"""
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10

# Test the shape calculator
print("Testing Shape Calculator:")

# Create shapes
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(3, 4, 5)
]

# Calculate properties for all shapes
for shape in shapes:
    print(f"\n{shape.describe()}")
    
    # Shape-specific properties
    if isinstance(shape, Rectangle):
        print(f"  Is square: {shape.is_square()}")
        print(f"  Diagonal: {shape.diagonal():.2f}")
    elif isinstance(shape, Circle):
        print(f"  Diameter: {shape.diameter():.2f}")
        print(f"  Circumference: {shape.circumference():.2f}")
    elif isinstance(shape, Triangle):
        print(f"  Is equilateral: {shape.is_equilateral()}")
        print(f"  Is isosceles: {shape.is_isosceles()}")
        print(f"  Is right-angled: {shape.is_right_angled()}")

# Exercise 3: Bank Account System
print("\n\nEXERCISE 3: BANK ACCOUNT SYSTEM")
print("-" * 40)
print("Create a bank account system with:")
print("- Base Account class with common functionality")
print("- Savings and Checking account types")
print("- Interest calculation and transaction limits")
print("- Proper encapsulation and validation")

class Account:
    """Base account class"""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = initial_balance
        self._transactions = []
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def holder_name(self):
        return self._holder_name
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def transactions(self):
        return self._transactions.copy()
    
    def deposit(self, amount):
        """Deposit money"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transactions.append({
            'type': 'deposit',
            'amount': amount,
            'balance': self._balance
        })
        return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def withdraw(self, amount):
        """Withdraw money - to be overridden by subclasses"""
        raise NotImplementedError("Withdraw method must be implemented by subclasses")
    
    def get_statement(self):
        """Get account statement"""
        statement = f"Account Statement for {self._holder_name}\n"
        statement += f"Account Number: {self._account_number}\n"
        statement += f"Current Balance: ${self._balance:.2f}\n\n"
        statement += "Transactions:\n"
        
        for i, transaction in enumerate(self._transactions, 1):
            statement += f"{i}. {transaction['type'].title()}: ${transaction['amount']:.2f} "
            statement += f"(Balance: ${transaction['balance']:.2f})\n"
        
        return statement

class SavingsAccount(Account):
    """Savings account with interest"""
    
    def __init__(self, account_number, holder_name, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, holder_name, initial_balance)
        self._interest_rate = interest_rate
        self._minimum_balance = 100
    
    def withdraw(self, amount):
        """Withdraw from savings account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if self._balance - amount < self._minimum_balance:
            raise ValueError(f"Insufficient funds. Minimum balance required: ${self._minimum_balance}")
        
        self._balance -= amount
        self._transactions.append({
            'type': 'withdrawal',
            'amount': amount,
            'balance': self._balance
        })
        return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def add_interest(self):
        """Add interest to the account"""
        interest = self._balance * self._interest_rate
        self._balance += interest
        self._transactions.append({
            'type': 'interest',
            'amount': interest,
            'balance': self._balance
        })
        return f"Interest added: ${interest:.2f}. New balance: ${self._balance:.2f}"
    
    def get_interest_rate(self):
        """Get current interest rate"""
        return self._interest_rate

class CheckingAccount(Account):
    """Checking account with transaction limits"""
    
    def __init__(self, account_number, holder_name, initial_balance=0, daily_limit=1000):
        super().__init__(account_number, holder_name, initial_balance)
        self._daily_limit = daily_limit
        self._daily_withdrawals = 0
        self._last_reset_date = None
    
    def withdraw(self, amount):
        """Withdraw from checking account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        # Reset daily withdrawals if it's a new day
        self._reset_daily_limit()
        
        if self._daily_withdrawals + amount > self._daily_limit:
            raise ValueError(f"Daily withdrawal limit exceeded. Limit: ${self._daily_limit}")
        
        if self._balance < amount:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._daily_withdrawals += amount
        self._transactions.append({
            'type': 'withdrawal',
            'amount': amount,
            'balance': self._balance
        })
        return f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
    
    def _reset_daily_limit(self):
        """Reset daily withdrawal limit"""
        import datetime
        today = datetime.date.today()
        if self._last_reset_date != today:
            self._daily_withdrawals = 0
            self._last_reset_date = today
    
    def get_daily_limit_remaining(self):
        """Get remaining daily withdrawal limit"""
        self._reset_daily_limit()
        return self._daily_limit - self._daily_withdrawals

# Test the bank account system
print("Testing Bank Account System:")

# Create accounts
savings = SavingsAccount("SA001", "Alice Johnson", 1000, 0.03)
checking = CheckingAccount("CA001", "Bob Smith", 500, 800)

# Test savings account
print(savings.deposit(200))
print(savings.withdraw(50))
print(savings.add_interest())
print(f"Interest rate: {savings.get_interest_rate():.1%}")

# Test checking account
print(checking.deposit(300))
print(checking.withdraw(100))
print(f"Daily limit remaining: ${checking.get_daily_limit_remaining()}")

# Try to exceed limits
try:
    checking.withdraw(1000)  # Exceeds daily limit
except ValueError as e:
    print(f"Error: {e}")

try:
    savings.withdraw(1000)  # Exceeds minimum balance
except ValueError as e:
    print(f"Error: {e}")

# Print statements
print("\nSavings Account Statement:")
print(savings.get_statement())

print("\nChecking Account Statement:")
print(checking.get_statement())

print("\n" + "=" * 50)
print("PRACTICE EXERCISES COMPLETED!")
print("=" * 50) 