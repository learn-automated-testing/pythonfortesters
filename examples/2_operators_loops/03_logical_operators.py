"""
Logical Operators in Python
Examples and exercises for logical operators: and, or, not
"""

print("=== Logical Operators Examples ===")

# Basic logical operations
x = 5
y = 10
z = 3

print(f"x = {x}, y = {y}, z = {z}")
print(f"x > 0 and x < 10: {x > 0 and x < 10}")      # True
print(f"x > 0 and x > 10: {x > 0 and x > 10}")      # False
print(f"x > 0 or x > 10: {x > 0 or x > 10}")        # True
print(f"x < 0 or x > 10: {x < 0 or x > 10}")        # False
print(f"not x == 5: {not x == 5}")                   # False
print(f"not x == 10: {not x == 10}")                 # True

print("\n=== Complex Logical Expressions ===")

# Multiple conditions
age = 25
income = 50000
credit_score = 750

print(f"Age: {age}, Income: ${income}, Credit Score: {credit_score}")

# Loan approval logic
is_adult = age >= 18
has_good_income = income >= 30000
has_good_credit = credit_score >= 700

loan_approved = is_adult and has_good_income and has_good_credit
print(f"Loan approved: {loan_approved}")

# Alternative approval (any two conditions)
alternative_approval = (is_adult and has_good_income) or (is_adult and has_good_credit) or (has_good_income and has_good_credit)
print(f"Alternative approval: {alternative_approval}")

print("\n=== Practical Examples ===")

# User authentication
username = "admin"
password = "1234"
is_active = True

print(f"Username: {username}, Password: {password}, Active: {is_active}")

if username == "admin" and password == "1234" and is_active:
    print("✅ Access granted")
else:
    print("❌ Access denied")

# Data validation
data = [5, -3, 8, 0, 2, 15, -5]
print(f"\nValidating data: {data}")

for number in data:
    is_positive = number > 0
    is_single_digit = number < 10
    is_valid = is_positive and is_single_digit
    
    if is_valid:
        print(f"{number}: Valid positive single-digit")
    else:
        print(f"{number}: Invalid")

print("\n=== Practice Exercises ===")

# Exercise 1: Student grade calculator with conditions
def calculate_student_grade(attendance, homework, exam):
    """Calculate final grade based on multiple conditions"""
    # Check if student meets minimum requirements
    attendance_ok = attendance >= 0.8  # 80% attendance
    homework_ok = homework >= 0.7      # 70% homework completion
    exam_ok = exam >= 0.6              # 60% exam score
    
    # Calculate final grade
    if attendance_ok and homework_ok and exam_ok:
        final_grade = (attendance * 0.2 + homework * 0.3 + exam * 0.5)
        if final_grade >= 0.9:
            return "A"
        elif final_grade >= 0.8:
            return "B"
        elif final_grade >= 0.7:
            return "C"
        elif final_grade >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "F (Requirements not met)"

# Test the function
students = [
    (0.9, 0.8, 0.85),  # Good student
    (0.7, 0.6, 0.9),   # Poor attendance
    (0.9, 0.9, 0.5),   # Poor exam
    (0.95, 0.95, 0.95) # Excellent student
]

for attendance, homework, exam in students:
    grade = calculate_student_grade(attendance, homework, exam)
    print(f"Attendance: {attendance*100}%, Homework: {homework*100}%, Exam: {exam*100}% -> Grade: {grade}")

# Exercise 2: Shopping cart validation
def validate_shopping_cart(items, total_amount, payment_method):
    """Validate shopping cart for checkout"""
    has_items = len(items) > 0
    valid_amount = 0 < total_amount <= 1000
    valid_payment = payment_method in ["credit", "debit", "paypal"]
    
    # Check if cart is ready for checkout
    ready_for_checkout = has_items and valid_amount and valid_payment
    
    # Additional checks
    if ready_for_checkout:
        if total_amount > 500 and payment_method == "paypal":
            return "Ready for checkout (PayPal limit warning)"
        elif total_amount > 100:
            return "Ready for checkout (Free shipping eligible)"
        else:
            return "Ready for checkout"
    else:
        issues = []
        if not has_items:
            issues.append("No items in cart")
        if not valid_amount:
            issues.append("Invalid amount")
        if not valid_payment:
            issues.append("Invalid payment method")
        return f"Checkout failed: {', '.join(issues)}"

# Test the function
test_carts = [
    (["book", "pen"], 25.50, "credit"),
    ([], 0, "credit"),
    (["laptop"], 1500, "credit"),
    (["shirt"], 50, "invalid_method"),
    (["phone"], 600, "paypal")
]

for items, amount, payment in test_carts:
    result = validate_shopping_cart(items, amount, payment)
    print(f"Cart: {items}, Amount: ${amount}, Payment: {payment} -> {result}")

# Exercise 3: Weather activity planner
def plan_activity(temperature, humidity, wind_speed, is_weekend):
    """Plan outdoor activity based on weather conditions"""
    good_temp = 15 <= temperature <= 30
    good_humidity = humidity < 80
    good_wind = wind_speed < 20
    good_timing = is_weekend
    
    # Activity recommendations
    if good_temp and good_humidity and good_wind and good_timing:
        return "Perfect day for outdoor activities!"
    elif good_temp and good_humidity and not good_wind:
        return "Good for outdoor activities, but windy"
    elif good_temp and not good_humidity:
        return "Temperature is good, but humidity is high"
    elif not good_temp and good_timing:
        return "Indoor activities recommended"
    else:
        return "Stay indoors today"

# Test the function
weather_conditions = [
    (25, 60, 10, True),   # Perfect weekend
    (25, 60, 25, True),   # Windy weekend
    (25, 85, 10, True),   # Humid weekend
    (35, 60, 10, True),   # Hot weekend
    (25, 60, 10, False),  # Perfect weekday
    (5, 60, 10, True)     # Cold weekend
]

for temp, humidity, wind, weekend in weather_conditions:
    recommendation = plan_activity(temp, humidity, wind, weekend)
    print(f"Temp: {temp}°C, Humidity: {humidity}%, Wind: {wind}km/h, Weekend: {weekend} -> {recommendation}") 