from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pytest
import time

class TestSorting:
    @pytest.fixture
    def driver(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Initialize the Chrome driver with automatic driver management
        driver = webdriver.Chrome(options=chrome_options)
        
        yield driver
        
        # Clean up
        driver.quit()

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        # Navigate to the web elements page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click the Interactions accordion in the sidebar
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click the Sorting link in the sidebar
        sorting_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Sorting')]"))
        )
        sorting_link.click()
        
        # Wait for the component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "section"))
        )

    def wait_for_table_update(self, driver, expected_first_item):
        def table_updated(driver):
            try:
                table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
                if not table_rows:
                    return False
                first_item = table_rows[0].find_element(By.CSS_SELECTOR, "div:first-child").text
                return first_item == expected_first_item
            except StaleElementReferenceException:
                return False

        WebDriverWait(driver, 10).until(table_updated)

    def test_initial_table_state(self, driver):
        # Get all table rows (excluding header)
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        
        # Verify there are multiple rows
        assert len(table_rows) > 0

        # Verify first row contains Apple (initial sort by name ascending)
        first_row = table_rows[0]
        first_cell = first_row.find_element(By.CSS_SELECTOR, "div:first-child")
        assert first_cell.text == "Apple"

    def test_sort_by_name(self, driver):
        name_header = driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:first-child")
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        
        # Initial state (ascending)
        first_item = table_rows[0].find_element(By.CSS_SELECTOR, "div:first-child").text
        assert first_item == "Apple"

        # Click to sort descending
        name_header.click()
        self.wait_for_table_update(driver, "Fennel")
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_item = table_rows[0].find_element(By.CSS_SELECTOR, "div:first-child").text
        assert first_item == "Fennel"

        # Click again to sort ascending
        name_header.click()
        self.wait_for_table_update(driver, "Apple")
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_item = table_rows[0].find_element(By.CSS_SELECTOR, "div:first-child").text
        assert first_item == "Apple"

    def test_sort_by_price(self, driver):
        price_header = driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:nth-child(2)")
        
        # Click to sort ascending
        price_header.click()
        self.wait_for_table_update(driver, "Carrot")  # Carrot has the lowest price
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_price = table_rows[0].find_element(By.CSS_SELECTOR, "div:nth-child(2)").text
        assert first_price == "$0.79"

        # Click to sort descending
        price_header.click()
        self.wait_for_table_update(driver, "Dragon Fruit")  # Dragon Fruit has the highest price
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_price = table_rows[0].find_element(By.CSS_SELECTOR, "div:nth-child(2)").text
        assert first_price == "$3.99"

    def test_sort_by_category(self, driver):
        category_header = driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:nth-child(3)")
        
        # Click to sort ascending
        category_header.click()
        self.wait_for_table_update(driver, "Apple")  # Apple is first in Fruit category
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_category = table_rows[0].find_element(By.CSS_SELECTOR, "div:nth-child(3)").text
        assert first_category == "Fruit"

        # Click to sort descending
        category_header.click()
        self.wait_for_table_update(driver, "Carrot")  # Carrot is first in Vegetable category
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        first_category = table_rows[0].find_element(By.CSS_SELECTOR, "div:nth-child(3)").text
        assert first_category == "Vegetable"

    def test_verify_all_items_present_after_sorting(self, driver):
        table_rows = driver.find_elements(By.CSS_SELECTOR, "section > div:nth-child(n+2)")
        expected_items = [
            {"name": "Apple", "price": "$1.99", "category": "Fruit"},
            {"name": "Banana", "price": "$0.99", "category": "Fruit"},
            {"name": "Carrot", "price": "$0.79", "category": "Vegetable"},
            {"name": "Dragon Fruit", "price": "$3.99", "category": "Fruit"},
            {"name": "Eggplant", "price": "$1.49", "category": "Vegetable"},
            {"name": "Fennel", "price": "$1.29", "category": "Vegetable"}
        ]

        # Sort by each column
        headers = [
            driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:first-child"),  # Name
            driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:nth-child(2)"),  # Price
            driver.find_element(By.CSS_SELECTOR, "section > div:first-child > div:nth-child(3)")   # Category
        ]
        
        for header in headers:
            # Sort ascending
            header.click()
            time.sleep(0.5)  # Wait for table to update
            ascending_items = [row.text for row in table_rows]
            assert len(ascending_items) == len(expected_items)

            # Sort descending
            header.click()
            time.sleep(0.5)  # Wait for table to update
            descending_items = [row.text for row in table_rows]
            assert len(descending_items) == len(expected_items) 