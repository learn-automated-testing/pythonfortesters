"""
Conditional Statements in Python
Examples and exercises for if, elif, else statements
"""

print("=== Conditional Statements Examples ===")

# Basic if statement
temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 20:
    print("It's warm outside.")

# if-else statement
temperature = 15
print(f"\nTemperature: {temperature}°C")

if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# if-elif-else statement
temperature = 20
print(f"\nTemperature: {temperature}°C")

if temperature > 25:
    print("It's hot.")
elif temperature > 18:
    print("It's mild.")
else:
    print("It's cold.")

print("\n=== Nested Conditionals ===")

# Nested if statements
age = 25
income = 50000
print(f"Age: {age}, Income: ${income}")

if age >= 18:
    if income >= 30000:
        print("Eligible for premium credit card")
    elif income >= 20000:
        print("Eligible for standard credit card")
    else:
        print("Eligible for basic credit card")
else:
    print("Too young for credit card")

print("\n=== Multiple Conditions ===")

# Multiple conditions with logical operators
username = "admin"
password = "1234"
is_active = True

print(f"Username: {username}, Password: {password}, Active: {is_active}")

if username == "admin" and password == "1234" and is_active:
    print("✅ Access granted")
elif username == "admin" and password == "1234" and not is_active:
    print("❌ Account is deactivated")
elif username == "admin" and password != "1234":
    print("❌ Wrong password")
else:
    print("❌ Invalid username")

print("\n=== Practical Examples ===")

# Grade calculator
def calculate_grade(score):
    """Calculate letter grade based on numerical score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test grade calculator
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = calculate_grade(score)
    print(f"Score {score}: Grade {grade}")

# Shopping discount calculator
def calculate_discount(total_amount, customer_type):
    """Calculate discount based on purchase amount and customer type"""
    if customer_type == "premium":
        if total_amount >= 100:
            discount = 0.20  # 20% discount
        elif total_amount >= 50:
            discount = 0.15  # 15% discount
        else:
            discount = 0.10  # 10% discount
    elif customer_type == "regular":
        if total_amount >= 100:
            discount = 0.10  # 10% discount
        elif total_amount >= 50:
            discount = 0.05  # 5% discount
        else:
            discount = 0.0   # No discount
    else:
        discount = 0.0       # No discount for unknown customer type
    
    final_amount = total_amount * (1 - discount)
    return final_amount, discount

# Test discount calculator
purchases = [
    (25, "regular"),
    (75, "regular"),
    (150, "regular"),
    (25, "premium"),
    (75, "premium"),
    (150, "premium"),
    (50, "unknown")
]

for amount, customer in purchases:
    final, discount = calculate_discount(amount, customer)
    print(f"Amount: ${amount}, Customer: {customer} -> Discount: {discount*100}%, Final: ${final:.2f}")

print("\n=== Practice Exercises ===")

# Exercise 1: BMI Calculator
def calculate_bmi_category(weight_kg, height_m):
    """Calculate BMI and return category"""
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Test BMI calculator
people = [
    (50, 1.6),   # Underweight
    (65, 1.7),   # Normal
    (80, 1.7),   # Overweight
    (100, 1.7)   # Obese
]

for weight, height in people:
    bmi, category = calculate_bmi_category(weight, height)
    print(f"Weight: {weight}kg, Height: {height}m -> BMI: {bmi:.1f} ({category})")

# Exercise 2: Tax Calculator
def calculate_tax(income, filing_status):
    """Calculate tax based on income and filing status"""
    if filing_status == "single":
        if income <= 10000:
            tax_rate = 0.10
        elif income <= 40000:
            tax_rate = 0.15
        elif income <= 100000:
            tax_rate = 0.25
        else:
            tax_rate = 0.35
    elif filing_status == "married":
        if income <= 20000:
            tax_rate = 0.10
        elif income <= 80000:
            tax_rate = 0.15
        elif income <= 200000:
            tax_rate = 0.25
        else:
            tax_rate = 0.35
    else:
        tax_rate = 0.0
    
    tax_amount = income * tax_rate
    return tax_amount, tax_rate

# Test tax calculator
taxpayers = [
    (5000, "single"),
    (50000, "single"),
    (150000, "single"),
    (15000, "married"),
    (100000, "married"),
    (250000, "married"),
    (50000, "unknown")
]

for income, status in taxpayers:
    tax, rate = calculate_tax(income, status)
    print(f"Income: ${income}, Status: {status} -> Tax Rate: {rate*100}%, Tax: ${tax:.2f}")

# Exercise 3: Shipping Calculator
def calculate_shipping(weight, destination, express=False):
    """Calculate shipping cost based on weight, destination, and service type"""
    # Base rates by destination
    if destination == "domestic":
        base_rate = 5.00
        if weight > 5:
            base_rate += (weight - 5) * 1.50
    elif destination == "international":
        base_rate = 15.00
        if weight > 2:
            base_rate += (weight - 2) * 3.00
    else:
        return "Invalid destination"
    
    # Express shipping multiplier
    if express:
        base_rate *= 2.5
    
    return base_rate

# Test shipping calculator
shipments = [
    (2, "domestic", False),
    (8, "domestic", False),
    (2, "domestic", True),
    (1, "international", False),
    (5, "international", False),
    (3, "international", True),
    (2, "invalid", False)
]

for weight, dest, express in shipments:
    cost = calculate_shipping(weight, dest, express)
    service = "Express" if express else "Standard"
    print(f"Weight: {weight}kg, Destination: {dest}, Service: {service} -> Cost: ${cost}") 