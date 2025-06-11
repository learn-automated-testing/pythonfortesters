from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

class TestSelectBox:
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

    def navigate_to_select_box_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Select Box link
        select_box_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Select Box')]"))
        )
        select_box_link.click()
        
        # Wait for the select box container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    def test_select_box_interactions(self, driver):
        self.navigate_to_select_box_page(driver)
        
        # Find the select element
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "select"))
        )
        
        # Create Select object
        select = Select(select_element)
        
        # Verify the select box is visible
        assert select_element.is_displayed()
        
        # Get all options
        options = select.options
        assert len(options) == 6  # Including the disabled default option
        
        # Select an option by value
        select.select_by_value("apple")
        assert select_element.get_attribute("value") == "apple"
        
        # Select an option by visible text
        select.select_by_visible_text("Banana")
        assert select_element.get_attribute("value") == "banana"
        
        # Select an option by index (skipping the disabled default option)
        select.select_by_index(3)  # This will select 'carrot'
        assert select_element.get_attribute("value") == "carrot"
        
        # Select another option by value
        select.select_by_value("dragonfruit")
        assert select_element.get_attribute("value") == "dragonfruit" 