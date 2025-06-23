"""
Module 5: Practical Examples for Test Automation
===============================================

This module covers applying Python basics to test automation:
- Applying Python basics to test automation
- Generating test data
- Working with URLs and test results
- Data validation

Learning Objectives:
- Apply concepts to test automation scenarios
- Generate test data programmatically
- Work with test configurations and URLs
- Validate test data and results
"""

print("=" * 50)
print("MODULE 5: TEST AUTOMATION EXAMPLES")
print("=" * 50)

# Test Data Generation
print("\n1. Test Data Generation:")

def generate_test_user(user_id):
    """Generate test user data"""
    return {
        "id": user_id,
        "username": f"user{user_id:03d}",
        "email": f"user{user_id:03d}@example.com",
        "password": f"pass{user_id:03d}123",
        "is_active": True
    }

# Generate test users
test_users = []
for i in range(1, 4):
    user = generate_test_user(i)
    test_users.append(user)

print("Generated test users:")
for user in test_users:
    print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")

# URL Construction
print("\n2. URL Construction:")

base_url = "https://practiceautomatedtesting.com"
endpoints = ["login", "dashboard", "profile", "settings"]

print("Generated test URLs:")
for endpoint in endpoints:
    full_url = f"{base_url}/{endpoint}"
    print(f"  {full_url}")

# Test Result Formatting
print("\n3. Test Result Formatting:")

test_results = [
    {"name": "Login Test", "status": "PASS", "duration": 2.5},
    {"name": "Search Test", "status": "FAIL", "duration": 1.8},
    {"name": "Logout Test", "status": "PASS", "duration": 1.2}
]

print("Test Results:")
for result in test_results:
    status_icon = "✅" if result["status"] == "PASS" else "❌"
    print(f"  {status_icon} {result['name']}: {result['duration']}s ({result['status']})")

# String Validation
print("\n4. String Validation:")

def validate_email(email):
    """Simple email validation"""
    if "@" in email and "." in email:
        return True
    return False

test_emails = [
    "user@example.com",
    "invalid-email",
    "user@.com",
    "user@domain.org"
]

print("Email validation:")
for email in test_emails:
    is_valid = validate_email(email)
    print(f"  '{email}': {'Valid' if is_valid else 'Invalid'}")

# Data Type Validation
print("\n5. Data Type Validation:")

def validate_test_data(data):
    """Validate test data types"""
    expected_types = {
        "username": str,
        "password": str,
        "age": int,
        "is_active": bool
    }
    
    print("Test data validation:")
    for field, expected_type in expected_types.items():
        if field in data:
            actual_type = type(data[field])
            if actual_type != expected_type:
                print(f"  ❌ {field}: Expected {expected_type.__name__}, got {actual_type.__name__}")
            else:
                print(f"  ✅ {field}: Correct type ({actual_type.__name__})")

test_data = {
    "username": "testuser",
    "password": "testpass123",
    "age": 25,
    "is_active": True
}

validate_test_data(test_data)

# Advanced Test Automation Examples
print("\n6. Advanced Test Automation Examples:")

# Test Configuration Management
print("\nTest Configuration Management:")

class TestConfig:
    """Test configuration class"""
    def __init__(self, environment="staging"):
        self.environment = environment
        self.configs = {
            "production": {
                "base_url": "https://app.production.com",
                "timeout": 30,
                "headless": True,
                "screenshot_on_failure": True
            },
            "staging": {
                "base_url": "https://app.staging.com",
                "timeout": 20,
                "headless": False,
                "screenshot_on_failure": True
            },
            "development": {
                "base_url": "http://localhost:3000",
                "timeout": 10,
                "headless": False,
                "screenshot_on_failure": False
            }
        }
    
    def get_config(self):
        """Get configuration for current environment"""
        return self.configs.get(self.environment, self.configs["development"])
    
    def get_url(self, endpoint=""):
        """Get full URL for given endpoint"""
        base_url = self.get_config()["base_url"]
        return f"{base_url}/{endpoint}" if endpoint else base_url

# Test configuration usage
config = TestConfig("staging")
staging_config = config.get_config()

print("Staging Environment Configuration:")
for key, value in staging_config.items():
    print(f"  {key}: {value}")

print(f"Login URL: {config.get_url('login')}")
print(f"Dashboard URL: {config.get_url('dashboard')}")

# Test Data Factory
print("\nTest Data Factory:")

class TestDataFactory:
    """Factory for generating test data"""
    
    @staticmethod
    def create_user(user_type="standard", user_id=1):
        """Create user test data"""
        base_data = {
            "id": user_id,
            "username": f"{user_type}_{user_id:03d}",
            "email": f"{user_type}_{user_id:03d}@example.com",
            "password": f"pass{user_id:03d}123",
            "is_active": True
        }
        
        if user_type == "admin":
            base_data.update({
                "role": "admin",
                "permissions": ["read", "write", "delete", "admin"]
            })
        elif user_type == "premium":
            base_data.update({
                "role": "premium",
                "permissions": ["read", "write"],
                "subscription": "premium"
            })
        else:
            base_data.update({
                "role": "user",
                "permissions": ["read"]
            })
        
        return base_data
    
    @staticmethod
    def create_product(product_id=1, category="electronics"):
        """Create product test data"""
        return {
            "id": product_id,
            "name": f"Test Product {product_id:03d}",
            "category": category,
            "price": round(10.0 + (product_id * 5.5), 2),
            "in_stock": True,
            "description": f"This is a test product in the {category} category"
        }

# Generate test data using factory
print("Generated Test Data:")

# Users
admin_user = TestDataFactory.create_user("admin", 1)
standard_user = TestDataFactory.create_user("standard", 2)
premium_user = TestDataFactory.create_user("premium", 3)

print("Users:")
for user in [admin_user, standard_user, premium_user]:
    print(f"  {user['username']} ({user['role']}): {user['email']}")

# Products
products = []
for i in range(1, 4):
    product = TestDataFactory.create_product(i, "electronics")
    products.append(product)

print("\nProducts:")
for product in products:
    print(f"  {product['name']}: ${product['price']} ({product['category']})")

# Test Result Analysis
print("\n7. Test Result Analysis:")

class TestResultAnalyzer:
    """Analyze test results"""
    
    def __init__(self):
        self.results = []
    
    def add_result(self, test_name, status, duration, error_message=None):
        """Add a test result"""
        self.results.append({
            "name": test_name,
            "status": status,
            "duration": duration,
            "error_message": error_message,
            "timestamp": "2024-01-15 10:30:00"
        })
    
    def get_summary(self):
        """Get test summary"""
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r["status"] == "PASS")
        failed_tests = total_tests - passed_tests
        total_duration = sum(r["duration"] for r in self.results)
        
        return {
            "total": total_tests,
            "passed": passed_tests,
            "failed": failed_tests,
            "pass_rate": (passed_tests / total_tests * 100) if total_tests > 0 else 0,
            "total_duration": total_duration,
            "average_duration": total_duration / total_tests if total_tests > 0 else 0
        }
    
    def get_failed_tests(self):
        """Get list of failed tests"""
        return [r for r in self.results if r["status"] == "FAIL"]
    
    def print_report(self):
        """Print test report"""
        summary = self.get_summary()
        
        print("Test Execution Report")
        print("=" * 40)
        print(f"Total Tests: {summary['total']}")
        print(f"Passed: {summary['passed']} ✅")
        print(f"Failed: {summary['failed']} ❌")
        print(f"Pass Rate: {summary['pass_rate']:.1f}%")
        print(f"Total Duration: {summary['total_duration']:.2f}s")
        print(f"Average Duration: {summary['average_duration']:.2f}s")
        
        if summary['failed'] > 0:
            print("\nFailed Tests:")
            for test in self.get_failed_tests():
                print(f"  ❌ {test['name']}: {test['error_message']}")

# Test the analyzer
analyzer = TestResultAnalyzer()
analyzer.add_result("Login Test", "PASS", 2.5)
analyzer.add_result("Search Test", "FAIL", 1.8, "Element not found")
analyzer.add_result("Logout Test", "PASS", 1.2)
analyzer.add_result("Profile Test", "PASS", 3.1)
analyzer.add_result("Settings Test", "FAIL", 2.0, "Timeout error")

analyzer.print_report()

# Test Environment Setup
print("\n8. Test Environment Setup:")

def setup_test_environment(environment="staging"):
    """Setup test environment"""
    print(f"Setting up {environment} environment...")
    
    # Environment-specific setup
    if environment == "production":
        print("  ⚠️  Production environment - extra caution required")
        base_url = "https://app.production.com"
        timeout = 30
        headless = True
    elif environment == "staging":
        print("  🧪 Staging environment - safe for testing")
        base_url = "https://app.staging.com"
        timeout = 20
        headless = False
    else:
        print("  🏠 Local environment - development mode")
        base_url = "http://localhost:3000"
        timeout = 10
        headless = False
    
    # Test data setup
    test_users = [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "user1", "password": "user123", "role": "user"},
        {"username": "user2", "password": "user123", "role": "user"}
    ]
    
    print(f"  Base URL: {base_url}")
    print(f"  Timeout: {timeout}s")
    print(f"  Headless: {headless}")
    print(f"  Test Users: {len(test_users)}")
    
    return {
        "base_url": base_url,
        "timeout": timeout,
        "headless": headless,
        "test_users": test_users
    }

# Setup different environments
environments = ["development", "staging", "production"]

for env in environments:
    config = setup_test_environment(env)
    print(f"  Environment '{env}' configured successfully\n")

print("\n" + "=" * 50)
print("MODULE 5 COMPLETED!")
print("=" * 50)

"""
Practice Exercises:

Exercise 1: Test Data Generator
Create a function that generates test data for different scenarios:
- User registration data
- Product catalog data
- Order data
- Payment information

Exercise 2: Test Result Validator
Create a function that validates test results:
- Check if all required fields are present
- Validate data types
- Ensure values are within expected ranges
- Generate validation reports

Exercise 3: Configuration Manager
Create a configuration manager that:
- Loads settings from different environments
- Validates configuration values
- Provides default values for missing settings
- Supports environment-specific overrides

Test Automation Applications:
- Automated test data generation
- Test result analysis and reporting
- Environment configuration management
- Data validation and verification
- Test execution monitoring

Next Steps:
- Learn about operators and expressions
- Explore control flow statements
- Practice with loops and iteration
- Master functions and modularity
""" 