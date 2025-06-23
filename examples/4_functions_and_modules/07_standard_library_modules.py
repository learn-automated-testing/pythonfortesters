"""
Python Modules - Standard Library Examples
==========================================

This script covers standard library modules in Python:
- datetime module
- random module
- os module
- json module
- Other useful standard library modules
"""

print("=" * 50)
print("PYTHON MODULES - STANDARD LIBRARY EXAMPLES")
print("=" * 50)

# datetime module
import datetime

print("\n1. DATETIME MODULE")
print("-" * 40)

current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")
print(f"Current year: {current_time.year}")
print(f"Current month: {current_time.month}")
print(f"Current day: {current_time.day}")
print(f"Current hour: {current_time.hour}")
print(f"Current minute: {current_time.minute}")
print(f"Current second: {current_time.second}")

# Formatting dates
formatted_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# Different date formats
print(f"Date only: {current_time.strftime('%Y-%m-%d')}")
print(f"Time only: {current_time.strftime('%H:%M:%S')}")
print(f"Day name: {current_time.strftime('%A')}")
print(f"Month name: {current_time.strftime('%B')}")

# Creating specific dates
specific_date = datetime.datetime(2024, 1, 15, 10, 30, 0)
print(f"Specific date: {specific_date}")

# Date arithmetic
tomorrow = current_time + datetime.timedelta(days=1)
yesterday = current_time - datetime.timedelta(days=1)
next_week = current_time + datetime.timedelta(weeks=1)

print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d')}")

# Date comparison
if tomorrow > current_time:
    print("Tomorrow is in the future")

# random module
import random

print("\n2. RANDOM MODULE")
print("-" * 40)

# Random numbers
print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random float (0-1): {random.random()}")
print(f"Random float (0-100): {random.uniform(0, 100)}")

# Random choices
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(f"Random fruit: {random.choice(fruits)}")
print(f"Random sample (3 fruits): {random.sample(fruits, 3)}")

# Shuffling
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled numbers: {numbers}")

# Random with seed (for reproducible results)
random.seed(42)
print(f"Random with seed 42: {random.randint(1, 100)}")
print(f"Another random with seed 42: {random.randint(1, 100)}")

random.seed(42)
print(f"Random with seed 42 again: {random.randint(1, 100)}")

# os module
import os

print("\n3. OS MODULE")
print("-" * 40)

# Current working directory
print(f"Current working directory: {os.getcwd()}")

# List directory contents
print(f"Directory contents: {os.listdir('.')}")

# Environment variables
print(f"Python version: {os.environ.get('PYTHON_VERSION', 'Not set')}")
print(f"User: {os.environ.get('USER', 'Unknown')}")
print(f"Home directory: {os.environ.get('HOME', 'Unknown')}")

# Path operations
path = "/home/user/documents/file.txt"
print(f"Directory: {os.path.dirname(path)}")
print(f"Filename: {os.path.basename(path)}")
print(f"Extension: {os.path.splitext(path)[1]}")

# Check if file/directory exists
print(f"Current directory exists: {os.path.exists('.')}")
print(f"Non-existent file exists: {os.path.exists('nonexistent.txt')}")

# Create and remove directories
test_dir = "test_directory"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)
    print(f"Created directory: {test_dir}")

# json module
import json

print("\n4. JSON MODULE")
print("-" * 40)

# Python object to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "swimming", "coding"],
    "active": True,
    "score": 95.5
}

json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# JSON string to Python object
parsed_data = json.loads(json_string)
print(f"\nParsed data type: {type(parsed_data)}")
print(f"Name: {parsed_data['name']}")
print(f"Hobbies: {parsed_data['hobbies']}")

# Working with JSON files
test_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ],
    "settings": {
        "theme": "dark",
        "language": "en",
        "notifications": True
    }
}

# Write to JSON file
with open("test_data.json", "w") as f:
    json.dump(test_data, f, indent=2)

# Read from JSON file
with open("test_data.json", "r") as f:
    loaded_data = json.load(f)

print(f"\nLoaded data from file:")
print(f"Number of users: {len(loaded_data['users'])}")
print(f"Settings: {loaded_data['settings']}")

# collections module
import collections

print("\n5. COLLECTIONS MODULE")
print("-" * 40)

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = collections.Counter(words)
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# DefaultDict
dd = collections.defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")
print(f"DefaultDict: {dict(dd)}")

# NamedTuple
Person = collections.namedtuple("Person", ["name", "age", "city"])
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "Los Angeles")
print(f"Person 1: {person1}")
print(f"Person 1 name: {person1.name}")

# itertools module
import itertools

print("\n6. ITERTOOLS MODULE")
print("-" * 40)

# Infinite iterators
counter = itertools.count(1)
print(f"First 5 numbers: {list(itertools.islice(counter, 5))}")

# Permutations
letters = ["A", "B", "C"]
perms = list(itertools.permutations(letters, 2))
print(f"Permutations of {letters} (length 2): {perms}")

# Combinations
combs = list(itertools.combinations(letters, 2))
print(f"Combinations of {letters} (length 2): {combs}")

# Chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = list(itertools.chain(list1, list2))
print(f"Chained lists: {chained}")

# re module (regular expressions)
import re

print("\n7. RE MODULE (REGULAR EXPRESSIONS)")
print("-" * 40)

# Basic pattern matching
text = "Hello, my email is alice@example.com and phone is 123-456-7890"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print(f"Found emails: {emails}")
print(f"Found phones: {phones}")

# String replacement
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(f"Text with masked phone: {new_text}")

# urllib module
import urllib.request
import urllib.parse

print("\n8. URLLIB MODULE")
print("-" * 40)

# URL parsing
url = "https://www.example.com/path?name=alice&age=25"
parsed_url = urllib.parse.urlparse(url)
print(f"Scheme: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")

# URL encoding/decoding
params = {"name": "Alice Smith", "age": 25}
encoded_params = urllib.parse.urlencode(params)
print(f"Encoded params: {encoded_params}")

decoded_params = urllib.parse.parse_qs(encoded_params)
print(f"Decoded params: {decoded_params}")

# Practical example: Data processing with multiple modules
print("\n9. PRACTICAL EXAMPLE - DATA PROCESSING")
print("-" * 40)

# Create a simple data logging system
def log_event(event_type, message):
    """Log an event with timestamp"""
    timestamp = datetime.datetime.now().isoformat()
    event_id = random.randint(1000, 9999)
    
    log_entry = {
        "id": event_id,
        "timestamp": timestamp,
        "type": event_type,
        "message": message
    }
    
    return log_entry

# Create some log entries
events = [
    log_event("INFO", "Application started"),
    log_event("WARNING", "High memory usage detected"),
    log_event("ERROR", "Database connection failed"),
    log_event("INFO", "User login successful"),
    log_event("INFO", "Data processing completed")
]

# Convert to JSON and display
log_json = json.dumps(events, indent=2)
print("Event Log:")
print(log_json)

# Filter events by type
info_events = [event for event in events if event["type"] == "INFO"]
error_events = [event for event in events if event["type"] == "ERROR"]

print(f"\nInfo events count: {len(info_events)}")
print(f"Error events count: {len(error_events)}")

# Save to file
with open("events.json", "w") as f:
    json.dump(events, f, indent=2)

print(f"\nEvents saved to events.json")

# Clean up test files
if os.path.exists("test_data.json"):
    os.remove("test_data.json")
    print("Cleaned up test_data.json")

if os.path.exists("events.json"):
    os.remove("events.json")
    print("Cleaned up events.json")

if os.path.exists(test_dir):
    os.rmdir(test_dir)
    print(f"Cleaned up {test_dir}")

print("\n" + "=" * 50)
print("STANDARD LIBRARY MODULES COMPLETED!")
print("=" * 50) 