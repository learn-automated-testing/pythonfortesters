# Error Handling - Essential for Robust Automation

# Basic try-except
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Please provide numbers only!")
        return None

print(divide_numbers(10, 2))  # Works fine
print(divide_numbers(10, 0))  # Handles division by zero
print(divide_numbers("10", 2))  # Handles type error

# Multiple exception types
def process_user_input(user_input):
    try:
        number = int(user_input)
        result = number * 2
        return result
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Try-except with else and finally
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    else:
        print("File read successfully!")
        return content
    finally:
        print("File operation completed")

# Custom exceptions
class ValidationError(Exception):
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be a number", "age")
    if age < 0:
        raise ValidationError("Age cannot be negative", "age")
    if age > 150:
        raise ValidationError("Age seems unrealistic", "age")
    return True

# Testing custom exception
try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation failed for {e.field}: {e.message}") 