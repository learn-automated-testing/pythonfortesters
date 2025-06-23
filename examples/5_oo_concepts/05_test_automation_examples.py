"""
Python Object-Oriented Programming - Test Automation Examples
===========================================================

This script demonstrates how OOP concepts are used in test automation:
- Page Object Model (POM)
- Test base classes
- Test data classes
- Test utilities
- Test configuration management
"""

print("=" * 50)
print("PYTHON OOP - TEST AUTOMATION EXAMPLES")
print("=" * 50)

# Page Object Model (POM) - Base page class
class BasePage:
    """Base page class with common functionality"""
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
    
    def find_element(self, locator):
        """Find element with timeout"""
        # Simulate finding element
        return f"Element found: {locator}"
    
    def click(self, locator):
        """Click on element"""
        element = self.find_element(locator)
        return f"Clicked on {element}"
    
    def type_text(self, locator, text):
        """Type text into element"""
        element = self.find_element(locator)
        return f"Typed '{text}' into {element}"
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return f"Text from {element}: Sample text"
    
    def is_element_present(self, locator):
        """Check if element is present"""
        return True  # Simulate element presence
    
    def wait_for_element(self, locator, timeout=None):
        """Wait for element to be present"""
        timeout = timeout or self.timeout
        return f"Waited {timeout}s for {locator}"

# Login page class
class LoginPage(BasePage):
    """Login page object"""
    
    # Page elements (locators)
    USERNAME_FIELD = "id=username"
    PASSWORD_FIELD = "id=password"
    LOGIN_BUTTON = "id=login-btn"
    ERROR_MESSAGE = "class=error-msg"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://example.com/login"
    
    def navigate_to(self):
        """Navigate to login page"""
        return f"Navigated to {self.url}"
    
    def enter_username(self, username):
        """Enter username"""
        return self.type_text(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        """Enter password"""
        return self.type_text(self.PASSWORD_FIELD, password)
    
    def click_login(self):
        """Click login button"""
        return self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def login(self, username, password):
        """Complete login process"""
        steps = [
            self.enter_username(username),
            self.enter_password(password),
            self.click_login()
        ]
        return steps

# Dashboard page class
class DashboardPage(BasePage):
    """Dashboard page object"""
    
    # Page elements
    WELCOME_MESSAGE = "id=welcome-msg"
    LOGOUT_BUTTON = "id=logout-btn"
    PROFILE_LINK = "id=profile-link"
    SETTINGS_LINK = "id=settings-link"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://example.com/dashboard"
    
    def get_welcome_message(self):
        """Get welcome message"""
        return self.get_text(self.WELCOME_MESSAGE)
    
    def click_logout(self):
        """Click logout button"""
        return self.click(self.LOGOUT_BUTTON)
    
    def navigate_to_profile(self):
        """Navigate to profile page"""
        return self.click(self.PROFILE_LINK)
    
    def navigate_to_settings(self):
        """Navigate to settings page"""
        return self.click(self.SETTINGS_LINK)
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return self.is_element_present(self.WELCOME_MESSAGE)

print("\n1. PAGE OBJECT MODEL (POM)")
print("-" * 40)

# Simulate driver
class MockDriver:
    def __init__(self):
        self.current_url = "https://example.com"

driver = MockDriver()

# Create page objects
login_page = LoginPage(driver)
dashboard_page = DashboardPage(driver)

# Use page objects
print(login_page.navigate_to())
login_steps = login_page.login("testuser", "password123")
for step in login_steps:
    print(f"  {step}")

print(dashboard_page.get_welcome_message())
print(dashboard_page.navigate_to_profile())

# Test base classes
class TestBase:
    """Base class for all tests"""
    
    def __init__(self):
        self.driver = None
        self.test_data = {}
    
    def setup(self):
        """Setup method called before each test"""
        print("Setting up test environment...")
        self.driver = MockDriver()
        self.load_test_data()
    
    def teardown(self):
        """Teardown method called after each test"""
        print("Cleaning up test environment...")
        if self.driver:
            self.driver = None
    
    def load_test_data(self):
        """Load test data"""
        self.test_data = {
            "valid_username": "testuser",
            "valid_password": "password123",
            "invalid_username": "invaliduser",
            "invalid_password": "wrongpass"
        }
    
    def take_screenshot(self, name):
        """Take screenshot"""
        return f"Screenshot saved: {name}.png"
    
    def log_test_step(self, step):
        """Log test step"""
        print(f"TEST STEP: {step}")

# Login test class
class LoginTest(TestBase):
    """Test class for login functionality"""
    
    def __init__(self):
        super().__init__()
        self.login_page = None
        self.dashboard_page = None
    
    def setup(self):
        """Setup for login tests"""
        super().setup()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
    
    def test_valid_login(self):
        """Test valid login"""
        self.log_test_step("Testing valid login")
        
        # Navigate to login page
        print(self.login_page.navigate_to())
        
        # Perform login
        login_steps = self.login_page.login(
            self.test_data["valid_username"],
            self.test_data["valid_password"]
        )
        
        for step in login_steps:
            print(f"  {step}")
        
        # Verify login success
        if self.dashboard_page.is_logged_in():
            print("  ✓ Login successful")
            welcome_msg = self.dashboard_page.get_welcome_message()
            print(f"  Welcome message: {welcome_msg}")
        else:
            print("  ✗ Login failed")
        
        # Take screenshot
        self.take_screenshot("valid_login_test")
    
    def test_invalid_login(self):
        """Test invalid login"""
        self.log_test_step("Testing invalid login")
        
        # Navigate to login page
        print(self.login_page.navigate_to())
        
        # Perform login with invalid credentials
        login_steps = self.login_page.login(
            self.test_data["invalid_username"],
            self.test_data["invalid_password"]
        )
        
        for step in login_steps:
            print(f"  {step}")
        
        # Verify error message
        error_msg = self.login_page.get_error_message()
        print(f"  Error message: {error_msg}")
        
        # Take screenshot
        self.take_screenshot("invalid_login_test")

print("\n2. TEST BASE CLASSES")
print("-" * 40)

# Run login tests
login_test = LoginTest()
login_test.setup()

print("Running valid login test:")
login_test.test_valid_login()
print()

print("Running invalid login test:")
login_test.test_invalid_login()
print()

login_test.teardown()

# Test data classes
class TestData:
    """Class to manage test data"""
    
    def __init__(self):
        self.users = {}
        self.config = {}
        self.load_data()
    
    def load_data(self):
        """Load test data from configuration"""
        self.users = {
            "admin": {
                "username": "admin",
                "password": "admin123",
                "role": "administrator",
                "permissions": ["read", "write", "delete"]
            },
            "user": {
                "username": "user",
                "password": "user123",
                "role": "user",
                "permissions": ["read", "write"]
            },
            "guest": {
                "username": "guest",
                "password": "guest123",
                "role": "guest",
                "permissions": ["read"]
            }
        }
        
        self.config = {
            "base_url": "https://example.com",
            "timeout": 10,
            "browser": "chrome",
            "headless": False
        }
    
    def get_user(self, user_type):
        """Get user data by type"""
        return self.users.get(user_type, {})
    
    def get_config(self, key):
        """Get configuration value"""
        return self.config.get(key)
    
    def add_user(self, user_type, user_data):
        """Add new user data"""
        self.users[user_type] = user_data
    
    def update_config(self, key, value):
        """Update configuration"""
        self.config[key] = value

# Test utilities class
class TestUtils:
    """Utility class for test automation"""
    
    @staticmethod
    def generate_random_string(length=8):
        """Generate random string"""
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    @staticmethod
    def generate_random_email():
        """Generate random email"""
        username = TestUtils.generate_random_string(6)
        domain = TestUtils.generate_random_string(4)
        return f"{username}@{domain}.com"
    
    @staticmethod
    def wait_for_condition(condition_func, timeout=10, interval=0.5):
        """Wait for a condition to be true"""
        import time
        start_time = time.time()
        while time.time() - start_time < timeout:
            if condition_func():
                return True
            time.sleep(interval)
        return False
    
    @staticmethod
    def retry_operation(operation_func, max_attempts=3, delay=1):
        """Retry an operation multiple times"""
        import time
        for attempt in range(max_attempts):
            try:
                return operation_func()
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                time.sleep(delay)
    
    @staticmethod
    def format_test_name(test_method):
        """Format test method name for display"""
        return test_method.replace('_', ' ').title()

print("\n3. TEST DATA AND UTILITIES")
print("-" * 40)

# Use test data
test_data = TestData()
admin_user = test_data.get_user("admin")
print(f"Admin user: {admin_user}")

base_url = test_data.get_config("base_url")
print(f"Base URL: {base_url}")

# Use test utilities
random_string = TestUtils.generate_random_string(10)
random_email = TestUtils.generate_random_email()
print(f"Random string: {random_string}")
print(f"Random email: {random_email}")

# Test configuration management
class TestConfig:
    """Configuration management for tests"""
    
    def __init__(self, environment="qa"):
        self.environment = environment
        self.configs = {
            "qa": {
                "base_url": "https://qa.example.com",
                "timeout": 10,
                "browser": "chrome",
                "headless": True
            },
            "staging": {
                "base_url": "https://staging.example.com",
                "timeout": 15,
                "browser": "firefox",
                "headless": False
            },
            "prod": {
                "base_url": "https://example.com",
                "timeout": 20,
                "browser": "chrome",
                "headless": True
            }
        }
        self.current_config = self.configs[environment]
    
    def get(self, key, default=None):
        """Get configuration value"""
        return self.current_config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        self.current_config[key] = value
    
    def switch_environment(self, environment):
        """Switch to different environment"""
        if environment in self.configs:
            self.environment = environment
            self.current_config = self.configs[environment]
            return f"Switched to {environment} environment"
        else:
            raise ValueError(f"Unknown environment: {environment}")
    
    def get_all_configs(self):
        """Get all configurations"""
        return self.configs

# Advanced test automation with OOP
class WebDriverManager:
    """Manages web driver lifecycle"""
    
    def __init__(self, browser="chrome", headless=False):
        self.browser = browser
        self.headless = headless
        self.driver = None
    
    def create_driver(self):
        """Create web driver instance"""
        # Simulate driver creation
        self.driver = MockDriver()
        return f"Created {self.browser} driver (headless: {self.headless})"
    
    def quit_driver(self):
        """Quit web driver"""
        if self.driver:
            self.driver = None
            return "Driver quit successfully"
        return "No driver to quit"
    
    def get_driver(self):
        """Get current driver instance"""
        return self.driver

class TestSuite:
    """Manages a collection of tests"""
    
    def __init__(self, name):
        self.name = name
        self.tests = []
        self.results = {}
    
    def add_test(self, test_method):
        """Add test method to suite"""
        self.tests.append(test_method)
    
    def run_all_tests(self):
        """Run all tests in the suite"""
        print(f"Running test suite: {self.name}")
        print("=" * 50)
        
        for test_method in self.tests:
            try:
                print(f"Running: {test_method.__name__}")
                test_method()
                self.results[test_method.__name__] = "PASSED"
                print("✓ Test passed")
            except Exception as e:
                self.results[test_method.__name__] = f"FAILED: {str(e)}"
                print(f"✗ Test failed: {e}")
            print()
        
        self.print_summary()
    
    def print_summary(self):
        """Print test results summary"""
        print("TEST SUMMARY")
        print("-" * 30)
        passed = sum(1 for result in self.results.values() if result == "PASSED")
        failed = len(self.results) - passed
        
        print(f"Total tests: {len(self.results)}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        
        if failed > 0:
            print("\nFailed tests:")
            for test_name, result in self.results.items():
                if result != "PASSED":
                    print(f"  {test_name}: {result}")

print("\n4. ADVANCED TEST AUTOMATION")
print("-" * 40)

# Create test configuration
config = TestConfig("qa")
print(f"Environment: {config.environment}")
print(f"Base URL: {config.get('base_url')}")
print(f"Timeout: {config.get('timeout')}")

# Switch environment
print(config.switch_environment("staging"))
print(f"New base URL: {config.get('base_url')}")

# Create test suite
def test_login_functionality():
    """Test login functionality"""
    login_test = LoginTest()
    login_test.setup()
    login_test.test_valid_login()
    login_test.teardown()

def test_registration():
    """Test user registration"""
    print("Testing user registration...")
    # Simulate registration test
    print("  ✓ Registration test completed")

test_suite = TestSuite("Login and Registration Tests")
test_suite.add_test(test_login_functionality)
test_suite.add_test(test_registration)

# Run test suite
test_suite.run_all_tests()

print("\n" + "=" * 50)
print("TEST AUTOMATION EXAMPLES COMPLETED!")
print("=" * 50) 