import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class TestWebTable:
    @pytest.fixture(scope="function")
    def driver(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_verify_table_structure_and_content(self, driver):
        # Navigate to the web elements page
        print("Navigating to website...")
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Wait for page to load completely
        print("Waiting for page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Click on Elements menu
        print("Looking for Elements menu...")
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Web Tables link
        print("Looking for Web Tables link...")
        web_tables_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Web Tables')]"))
        )
        web_tables_link.click()
        
        # Wait for table component
        print("Waiting for table component...")
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="componentContainer"]'))
        )
        
        # Get table elements
        table_element = driver.find_element(By.TAG_NAME, "table")
        headers = table_element.find_elements(By.TAG_NAME, "th")
        rows = table_element.find_elements(By.CSS_SELECTOR, "tbody tr")
        
        # Verify table is visible
        assert table_element.is_displayed()
        
        # Verify table headers
        assert len(headers) == 7  # Including Actions column
        assert headers[0].text == "First Name"
        assert headers[1].text == "Last Name"
        assert headers[2].text == "Email"
        assert headers[3].text == "Age"
        assert headers[4].text == "Salary"
        assert headers[5].text == "Department"
        assert headers[6].text == "Actions"
        
        # Verify table has rows
        assert len(rows) > 0
        
        # Verify first row data
        first_row = rows[0]
        cells = first_row.find_elements(By.TAG_NAME, "td")
        assert cells[0].text != ""  # First Name
        assert cells[1].text != ""  # Last Name
        assert cells[2].text != ""  # Email
        assert cells[3].text != ""  # Age
        assert cells[4].text != ""  # Salary
        assert cells[5].text != ""  # Department
        assert cells[6].is_displayed()  # Actions column

    def test_add_new_row_to_table(self, driver):
        # Navigate to the web elements page
        print("Navigating to website...")
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Wait for page to load completely
        print("Waiting for page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Click on Elements menu
        print("Looking for Elements menu...")
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Web Tables link
        print("Looking for Web Tables link...")
        web_tables_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Web Tables')]"))
        )
        web_tables_link.click()
        
        # Wait for table component
        print("Waiting for table component...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="componentContainer"]'))
        )
        
        # Click add button
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]"))
        )
        add_button.click()
        
        # Fill in the form
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys("John")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys("Doe")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email"]').send_keys("john.doe@example.com")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Age"]').send_keys("30")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Salary"]').send_keys("50000")
        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Department"]').send_keys("IT")
        
        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class*="addButton"]'))
        )
        submit_button.click()
        
        # Wait for the new row to appear and verify its content
        new_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table tbody tr:last-child'))
        )
        cells = new_row.find_elements(By.TAG_NAME, "td")
        
        assert cells[0].text == "John"
        assert cells[1].text == "Doe"
        assert cells[2].text == "john.doe@example.com"
        assert cells[3].text == "30"
        assert cells[4].text == "50000"
        assert cells[5].text == "IT"

    def test_delete_row_from_table(self, driver):
        # Navigate to the web elements page
        print("Navigating to website...")
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Wait for page to load completely
        print("Waiting for page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Click on Elements menu
        print("Looking for Elements menu...")
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Web Tables link
        print("Looking for Web Tables link...")
        web_tables_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Web Tables')]"))
        )
        web_tables_link.click()
        
        # Wait for table component
        print("Waiting for table component...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="componentContainer"]'))
        )
        
        # Get initial row count
        initial_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
        initial_row_count = len(initial_rows)
        
        # Delete the first row
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//table//tbody//tr[1]//button[contains(text(), 'Delete')]"))
        )
        delete_button.click()
        
        # Wait for the row to be removed
        time.sleep(1)  # Give time for the deletion to complete
        
        # Verify row was deleted
        new_rows = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
        new_row_count = len(new_rows)
        assert new_row_count == initial_row_count - 1 