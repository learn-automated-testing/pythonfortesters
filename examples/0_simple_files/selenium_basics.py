# Selenium Basics - Web Browser Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Note: This example assumes ChromeDriver is installed
# For actual use, you'll need to install:
# pip install selenium
# And download ChromeDriver from: https://chromedriver.chromium.org/

class WebAutomationDemo:
    def __init__(self):
        # Setup Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")  # Run in background
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Initialize driver (commented out for safety)
        # self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.wait = WebDriverWait(self.driver, 10)
        
        print("WebAutomationDemo initialized (driver not started for safety)")
    
    def setup_driver(self):
        """Initialize the web driver"""
        try:
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            print("Chrome driver started successfully")
            return True
        except Exception as e:
            print(f"Error starting driver: {e}")
            return False
    
    def basic_navigation(self):
        """Basic navigation examples"""
        print("=== Basic Navigation ===\n")
        
        if not hasattr(self, 'driver'):
            print("Driver not initialized. Call setup_driver() first.")
            return
        
        try:
            # Navigate to a website
            self.driver.get("https://www.google.com")
            print(f"Current URL: {self.driver.current_url}")
            print(f"Page title: {self.driver.title}")
            
            # Get page source
            page_source = self.driver.page_source
            print(f"Page source length: {len(page_source)} characters")
            
            # Navigate to another page
            self.driver.get("https://www.python.org")
            print(f"New URL: {self.driver.current_url}")
            print(f"New title: {self.driver.title}")
            
            # Go back and forward
            self.driver.back()
            print(f"After back: {self.driver.current_url}")
            
            self.driver.forward()
            print(f"After forward: {self.driver.current_url}")
            
        except Exception as e:
            print(f"Navigation error: {e}")
    
    def element_interaction(self):
        """Finding and interacting with elements"""
        print("=== Element Interaction ===\n")
        
        if not hasattr(self, 'driver'):
            print("Driver not initialized. Call setup_driver() first.")
            return
        
        try:
            # Navigate to a test page
            self.driver.get("https://httpbin.org/forms/post")
            
            # Find elements by different selectors
            # By ID
            customer_name = self.driver.find_element(By.ID, "custname")
            print(f"Found customer name field: {customer_name.get_attribute('name')}")
            
            # By Name
            telephone = self.driver.find_element(By.NAME, "custtel")
            print(f"Found telephone field: {telephone.get_attribute('id')}")
            
            # By CSS Selector
            email_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='custemail']")
            print(f"Found email field: {email_field.get_attribute('type')}")
            
            # By XPath
            pizza_size = self.driver.find_element(By.XPATH, "//input[@name='size']")
            print(f"Found pizza size field: {pizza_size.get_attribute('value')}")
            
            # Interact with elements
            customer_name.clear()
            customer_name.send_keys("John Doe")
            print("Entered customer name")
            
            telephone.clear()
            telephone.send_keys("123-456-7890")
            print("Entered telephone number")
            
            # Check if element is displayed and enabled
            print(f"Customer name field displayed: {customer_name.is_displayed()}")
            print(f"Customer name field enabled: {customer_name.is_enabled()}")
            
        except Exception as e:
            print(f"Element interaction error: {e}")
    
    def wait_examples(self):
        """Explicit and implicit waits"""
        print("=== Wait Examples ===\n")
        
        if not hasattr(self, 'driver'):
            print("Driver not initialized. Call setup_driver() first.")
            return
        
        try:
            # Navigate to a page that loads dynamically
            self.driver.get("https://httpbin.org/delay/2")
            
            # Wait for page to load completely
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("Page loaded successfully")
            
            # Wait for specific element
            pre_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre")))
            print("Found pre element")
            
            # Wait for element to be clickable
            # (This is a common pattern in real applications)
            try:
                clickable_element = self.wait.until(
                    EC.element_to_be_clickable((By.TAG_NAME, "body"))
                )
                print("Body element is clickable")
            except:
                print("Body element not clickable (expected)")
            
        except Exception as e:
            print(f"Wait error: {e}")
    
    def form_submission(self):
        """Complete form submission example"""
        print("=== Form Submission ===\n")
        
        if not hasattr(self, 'driver'):
            print("Driver not initialized. Call setup_driver() first.")
            return
        
        try:
            # Navigate to form page
            self.driver.get("https://httpbin.org/forms/post")
            
            # Fill out the form
            self.driver.find_element(By.ID, "custname").send_keys("Test User")
            self.driver.find_element(By.NAME, "custtel").send_keys("555-1234")
            self.driver.find_element(By.CSS_SELECTOR, "input[name='custemail']").send_keys("test@example.com")
            
            # Select radio button
            size_radio = self.driver.find_element(By.CSS_SELECTOR, "input[value='large']")
            size_radio.click()
            print("Selected large size")
            
            # Select checkbox
            toppings = self.driver.find_elements(By.NAME, "topping")
            for topping in toppings:
                if topping.get_attribute('value') in ['bacon', 'cheese']:
                    topping.click()
                    print(f"Selected topping: {topping.get_attribute('value')}")
            
            # Select from dropdown
            delivery_time = self.driver.find_element(By.NAME, "delivery")
            delivery_time.send_keys("20:30")
            print("Set delivery time")
            
            # Get form data before submission
            comments = self.driver.find_element(By.NAME, "comments")
            comments.send_keys("Please deliver to back door")
            print("Added comments")
            
            print("Form filled successfully")
            
        except Exception as e:
            print(f"Form submission error: {e}")
    
    def screenshot_example(self):
        """Take screenshots"""
        print("=== Screenshot Example ===\n")
        
        if not hasattr(self, 'driver'):
            print("Driver not initialized. Call setup_driver() first.")
            return
        
        try:
            self.driver.get("https://www.python.org")
            
            # Take screenshot
            screenshot_path = "python_org_screenshot.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
            
        except Exception as e:
            print(f"Screenshot error: {e}")
    
    def cleanup(self):
        """Clean up resources"""
        if hasattr(self, 'driver'):
            self.driver.quit()
            print("Driver closed")

# Example usage (commented out for safety)
def run_selenium_examples():
    """Run all Selenium examples"""
    demo = WebAutomationDemo()
    
    # Uncomment the following lines to run actual examples
    # if demo.setup_driver():
    #     demo.basic_navigation()
    #     demo.element_interaction()
    #     demo.wait_examples()
    #     demo.form_submission()
    #     demo.screenshot_example()
    #     demo.cleanup()
    
    print("Selenium examples ready to run (uncomment in code to execute)")

if __name__ == "__main__":
    run_selenium_examples() 