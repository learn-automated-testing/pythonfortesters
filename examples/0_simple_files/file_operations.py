# File Operations - Important for Data Handling in Automation

import json
import csv
import os

# Basic file operations
def write_text_file():
    with open('sample.txt', 'w') as file:
        file.write("Hello, this is a sample file!\n")
        file.write("This is the second line.\n")
        file.write("And this is the third line.")

def read_text_file():
    with open('sample.txt', 'r') as file:
        content = file.read()
        print("Full content:")
        print(content)
    
    # Read line by line
    with open('sample.txt', 'r') as file:
        print("\nLine by line:")
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")

# JSON operations - Common in API testing
def create_json_data():
    user_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com",
        "skills": ["Python", "Selenium", "API Testing"],
        "active": True
    }
    
    # Write JSON to file
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file, indent=2)
    
    return user_data

def read_json_data():
    with open('user_data.json', 'r') as file:
        data = json.load(file)
        print("JSON Data:")
        print(f"Name: {data['name']}")
        print(f"Skills: {', '.join(data['skills'])}")
        return data

# CSV operations - Common for test data
def create_csv_data():
    test_data = [
        ['Name', 'Age', 'City'],
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]
    
    with open('test_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(test_data)

def read_csv_data():
    with open('test_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Row: {row}")

# File and directory operations
def file_operations_demo():
    # Check if file exists
    if os.path.exists('sample.txt'):
        print("sample.txt exists")
        
        # Get file size
        size = os.path.getsize('sample.txt')
        print(f"File size: {size} bytes")
    
    # List files in current directory
    print("\nFiles in current directory:")
    for file in os.listdir('.'):
        if file.endswith('.py'):
            print(f"Python file: {file}")

# Practical example: Logging test results
def log_test_result(test_name, status, duration):
    log_entry = {
        "test_name": test_name,
        "status": status,
        "duration": duration,
        "timestamp": "2024-01-01T10:00:00"
    }
    
    # Append to log file
    try:
        with open('test_log.json', 'a') as file:
            file.write(json.dumps(log_entry) + '\n')
        print(f"Test result logged: {test_name} - {status}")
    except Exception as e:
        print(f"Error logging test result: {e}")

# Run examples
if __name__ == "__main__":
    print("=== File Operations Demo ===\n")
    
    write_text_file()
    read_text_file()
    
    print("\n=== JSON Operations ===")
    create_json_data()
    read_json_data()
    
    print("\n=== CSV Operations ===")
    create_csv_data()
    read_csv_data()
    
    print("\n=== File System Operations ===")
    file_operations_demo()
    
    print("\n=== Test Logging ===")
    log_test_result("login_test", "PASS", 2.5)
    log_test_result("search_test", "FAIL", 1.8) 