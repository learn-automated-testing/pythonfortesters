"""
Test Automation Examples
Real-world test automation scenarios using Python operators, conditionals, and loops
"""

import random
import time

print("=== Test Automation Examples ===")

# Example 1: API Response Validation
def validate_api_response(status_code, response_time, expected_data, actual_data):
    """Validate API response against expected criteria"""
    print(f"Validating API response:")
    print(f"  Status Code: {status_code}")
    print(f"  Response Time: {response_time}s")
    print(f"  Expected Data: {expected_data}")
    print(f"  Actual Data: {actual_data}")
    
    # Multiple validation checks
    status_ok = status_code == 200
    performance_ok = response_time < 1.0
    data_match = actual_data == expected_data
    
    # Overall test result
    test_passed = status_ok and performance_ok and data_match
    
    if test_passed:
        print("✅ Test PASSED - All criteria met")
    else:
        print("❌ Test FAILED - Issues found:")
        if not status_ok:
            print("  - Status code is not 200")
        if not performance_ok:
            print("  - Response time exceeds 1 second")
        if not data_match:
            print("  - Data mismatch")
    
    return test_passed

# Test the API validation
test_cases = [
    (200, 0.5, {"name": "John"}, {"name": "John"}),      # All pass
    (404, 0.3, {"name": "John"}, {"name": "John"}),      # Status fail
    (200, 1.5, {"name": "John"}, {"name": "John"}),      # Performance fail
    (200, 0.5, {"name": "John"}, {"name": "Jane"}),      # Data fail
    (500, 2.0, {"name": "John"}, {"name": "Jane"})       # Multiple fails
]

for status, time_val, expected, actual in test_cases:
    result = validate_api_response(status, time_val, expected, actual)
    print(f"Test result: {'PASS' if result else 'FAIL'}\n")

# Example 2: Data-Driven Testing
def test_user_registration(username, email, password, age):
    """Test user registration with various data combinations"""
    print(f"Testing registration: {username}, {email}, age: {age}")
    
    # Validation rules
    username_valid = len(username) >= 3 and username.isalnum()
    email_valid = '@' in email and '.' in email
    password_valid = len(password) >= 8 and any(c.isupper() for c in password)
    age_valid = 13 <= age <= 120
    
    # Overall validation
    registration_valid = username_valid and email_valid and password_valid and age_valid
    
    if registration_valid:
        print("✅ Registration data is valid")
    else:
        print("❌ Registration data is invalid:")
        if not username_valid:
            print("  - Username must be at least 3 characters and alphanumeric")
        if not email_valid:
            print("  - Email format is invalid")
        if not password_valid:
            print("  - Password must be at least 8 characters with uppercase")
        if not age_valid:
            print("  - Age must be between 13 and 120")
    
    return registration_valid

# Test data for registration
test_users = [
    ("john123", "john@example.com", "Password123", 25),
    ("ab", "invalid-email", "weak", 10),
    ("user456", "user@test.com", "NoUppercase", 30),
    ("test", "test@domain.org", "StrongPass1", 150),
    ("validuser", "valid@email.com", "GoodPass123", 35)
]

print("=== Data-Driven User Registration Tests ===")
for username, email, password, age in test_users:
    result = test_user_registration(username, email, password, age)
    print(f"Registration test: {'PASS' if result else 'FAIL'}\n")

# Example 3: Retry Logic for Unstable Tests
def simulate_api_call():
    """Simulate an API call that might fail"""
    # Simulate 70% success rate
    success = random.random() < 0.7
    time.sleep(0.1)  # Simulate network delay
    return success

def test_with_retry(max_attempts=3, delay=1):
    """Test function with retry logic"""
    print(f"Running test with retry (max {max_attempts} attempts):")
    
    attempts = 0
    success = False
    
    while attempts < max_attempts and not success:
        attempts += 1
        print(f"  Attempt {attempts}/{max_attempts}")
        
        success = simulate_api_call()
        
        if success:
            print(f"  ✅ Test passed on attempt {attempts}")
        else:
            if attempts < max_attempts:
                print(f"  ❌ Test failed, retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"  ❌ Test failed after {max_attempts} attempts")
    
    return success

# Run retry tests
print("=== Retry Logic Tests ===")
for i in range(3):
    print(f"\nTest run {i+1}:")
    test_with_retry()

# Example 4: Performance Testing
def performance_test(test_function, iterations=1000):
    """Run performance test on a function"""
    print(f"Running performance test ({iterations} iterations):")
    
    start_time = time.time()
    
    for i in range(iterations):
        test_function()
    
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / iterations
    
    print(f"  Total time: {total_time:.3f}s")
    print(f"  Average time per iteration: {avg_time*1000:.3f}ms")
    
    # Performance thresholds
    if avg_time < 0.001:  # Less than 1ms
        performance_grade = "Excellent"
    elif avg_time < 0.01:  # Less than 10ms
        performance_grade = "Good"
    elif avg_time < 0.1:   # Less than 100ms
        performance_grade = "Acceptable"
    else:
        performance_grade = "Poor"
    
    print(f"  Performance grade: {performance_grade}")
    return avg_time

# Test function for performance testing
def sample_function():
    """Sample function to test performance"""
    result = 0
    for i in range(100):
        result += i * 2
    return result

print("=== Performance Testing ===")
performance_test(sample_function, 1000)

# Example 5: Environment-Specific Testing
def run_environment_tests(environment):
    """Run tests specific to different environments"""
    print(f"Running tests for {environment} environment:")
    
    # Environment-specific configurations
    configs = {
        "development": {
            "timeout": 5,
            "retries": 2,
            "debug": True
        },
        "staging": {
            "timeout": 10,
            "retries": 3,
            "debug": False
        },
        "production": {
            "timeout": 30,
            "retries": 5,
            "debug": False
        }
    }
    
    config = configs.get(environment, configs["development"])
    
    print(f"  Timeout: {config['timeout']}s")
    print(f"  Retries: {config['retries']}")
    print(f"  Debug mode: {config['debug']}")
    
    # Simulate tests with environment-specific settings
    for test_num in range(1, 4):
        print(f"  Running test {test_num}...")
        success = random.random() > 0.2  # 80% success rate
        if success:
            print(f"    ✅ Test {test_num} passed")
        else:
            print(f"    ❌ Test {test_num} failed")
    
    return True

print("=== Environment-Specific Testing ===")
environments = ["development", "staging", "production"]
for env in environments:
    run_environment_tests(env)
    print()

# Example 6: Test Data Generation
def generate_test_data(count=5):
    """Generate test data for various scenarios"""
    print(f"Generating {count} test users:")
    
    test_users = []
    for i in range(count):
        user = {
            "id": i + 1,
            "username": f"user{i+1}",
            "email": f"user{i+1}@example.com",
            "age": random.randint(18, 65),
            "is_active": random.choice([True, False])
        }
        test_users.append(user)
    
    # Display generated data
    for user in test_users:
        status = "Active" if user["is_active"] else "Inactive"
        print(f"  User {user['id']}: {user['username']} ({user['email']}), Age: {user['age']}, Status: {status}")
    
    return test_users

print("=== Test Data Generation ===")
test_data = generate_test_data(5)

# Example 7: Test Result Aggregation
def aggregate_test_results(test_results):
    """Aggregate and analyze test results"""
    print("=== Test Results Aggregation ===")
    
    total_tests = len(test_results)
    passed_tests = sum(1 for result in test_results if result["status"] == "PASS")
    failed_tests = total_tests - passed_tests
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Pass rate: {pass_rate:.1f}%")
    
    # Analyze test categories
    categories = {}
    for result in test_results:
        category = result.get("category", "Unknown")
        if category not in categories:
            categories[category] = {"passed": 0, "failed": 0}
        
        if result["status"] == "PASS":
            categories[category]["passed"] += 1
        else:
            categories[category]["failed"] += 1
    
    print("\nResults by category:")
    for category, counts in categories.items():
        total = counts["passed"] + counts["failed"]
        category_pass_rate = (counts["passed"] / total) * 100 if total > 0 else 0
        print(f"  {category}: {counts['passed']}/{total} ({category_pass_rate:.1f}%)")
    
    return {
        "total": total_tests,
        "passed": passed_tests,
        "failed": failed_tests,
        "pass_rate": pass_rate
    }

# Sample test results
sample_results = [
    {"name": "API Test 1", "status": "PASS", "category": "API", "duration": 1.2},
    {"name": "API Test 2", "status": "FAIL", "category": "API", "duration": 0.8},
    {"name": "UI Test 1", "status": "PASS", "category": "UI", "duration": 3.5},
    {"name": "UI Test 2", "status": "PASS", "category": "UI", "duration": 2.1},
    {"name": "Database Test 1", "status": "FAIL", "category": "Database", "duration": 0.5},
    {"name": "Database Test 2", "status": "PASS", "category": "Database", "duration": 1.8}
]

aggregate_test_results(sample_results) 