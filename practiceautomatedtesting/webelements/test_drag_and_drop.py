from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestDragAndDrop:
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

    def navigate_to_drag_and_drop_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Drag and Drop link
        drag_drop_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Drag and Drop')]"))
        )
        drag_drop_link.click()
        
        # Wait for the drag and drop container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropzone"))
        )

    def test_simple_drag_and_drop(self, driver):
        self.navigate_to_drag_and_drop_page(driver)
        
        # Get the draggable element and drop target
        draggable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[draggable='true']"))
        )
        drop_target = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".dropzone"))
        )
        
        # Verify initial state
        assert drop_target.text == "Drop Here"
        
        # Perform drag and drop
        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, drop_target).perform()
        
        # Verify the drop was successful
        assert drop_target.text == "😊"
        
        # Test reset functionality
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reset')]"))
        )
        reset_button.click()
        
        # Verify reset state
        assert drop_target.text == "Drop Here" 