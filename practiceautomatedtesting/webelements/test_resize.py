from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class TestResize:
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

    def navigate_to_resize_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Resize link
        resize_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Resize')]"))
        )
        resize_link.click()
        
        # Wait for the resize container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )

    def test_resize_initial_state(self, driver):
        self.navigate_to_resize_page(driver)
        
        # Get the resizable element
        resizable_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )
        size_text = resizable_element.find_element(By.TAG_NAME, "span")
        
        # Verify initial dimensions
        initial_size = resizable_element.size
        assert 200 <= initial_size['width'] <= 204
        assert 150 <= initial_size['height'] <= 154
        assert size_text.text == "200 x 150 px"

    def test_resize_horizontally(self, driver):
        self.navigate_to_resize_page(driver)
        
        # Get the resizable element and resize handle
        resizable_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )
        resize_handle = driver.find_element(By.CSS_SELECTOR, "div[title='Resize']")
        size_text = resizable_element.find_element(By.TAG_NAME, "span")
        
        # Get initial dimensions
        initial_size = resizable_element.size
        initial_width = initial_size['width']
        
        # Create action chain for horizontal resize
        actions = ActionChains(driver)
        actions.move_to_element(resize_handle)
        actions.click_and_hold()
        actions.move_by_offset(100, 0)
        actions.release()
        actions.perform()
        
        # Wait for resize to complete
        time.sleep(0.1)
        
        # Verify new dimensions
        new_size = resizable_element.size
        assert new_size['width'] > initial_width
        assert size_text.text == f"{int(new_size['width'] - 4)} x {int(new_size['height'] - 4)} px"

    def test_resize_vertically(self, driver):
        self.navigate_to_resize_page(driver)
        
        # Get the resizable element and resize handle
        resizable_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )
        resize_handle = driver.find_element(By.CSS_SELECTOR, "div[title='Resize']")
        size_text = resizable_element.find_element(By.TAG_NAME, "span")
        
        # Get initial dimensions
        initial_size = resizable_element.size
        initial_height = initial_size['height']
        
        # Create action chain for vertical resize
        actions = ActionChains(driver)
        actions.move_to_element(resize_handle)
        actions.click_and_hold()
        actions.move_by_offset(0, 100)
        actions.release()
        actions.perform()
        
        # Wait for resize to complete
        time.sleep(0.1)
        
        # Verify new dimensions
        new_size = resizable_element.size
        assert new_size['height'] > initial_height
        assert size_text.text == f"{int(new_size['width'] - 4)} x {int(new_size['height'] - 4)} px"

    def test_resize_diagonally(self, driver):
        self.navigate_to_resize_page(driver)
        
        # Get the resizable element and resize handle
        resizable_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )
        resize_handle = driver.find_element(By.CSS_SELECTOR, "div[title='Resize']")
        size_text = resizable_element.find_element(By.TAG_NAME, "span")
        
        # Get initial dimensions
        initial_size = resizable_element.size
        initial_width = initial_size['width']
        initial_height = initial_size['height']
        
        # Create action chain for diagonal resize
        actions = ActionChains(driver)
        actions.move_to_element(resize_handle)
        actions.click_and_hold()
        actions.move_by_offset(100, 100)
        actions.release()
        actions.perform()
        
        # Wait for resize to complete
        time.sleep(0.1)
        
        # Verify new dimensions
        new_size = resizable_element.size
        assert new_size['width'] > initial_width
        assert new_size['height'] > initial_height
        assert size_text.text == f"{int(new_size['width'] - 4)} x {int(new_size['height'] - 4)} px"

    def test_resize_limits(self, driver):
        self.navigate_to_resize_page(driver)
        
        # Get the resizable element and resize handle
        resizable_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[style*='background: rgb(227, 242, 253)']"))
        )
        resize_handle = driver.find_element(By.CSS_SELECTOR, "div[title='Resize']")
        
        # Try to resize beyond maximum (500x500)
        actions = ActionChains(driver)
        actions.move_to_element(resize_handle)
        actions.click_and_hold()
        actions.move_by_offset(300, 300)
        actions.release()
        actions.perform()
        
        # Wait for resize to complete
        time.sleep(0.1)
        
        # Verify dimensions are within maximum limits
        max_size = resizable_element.size
        assert max_size['width'] <= 504
        assert max_size['height'] <= 504
        
        # Try to resize below minimum (100x100)
        actions = ActionChains(driver)
        actions.move_to_element(resize_handle)
        actions.click_and_hold()
        actions.move_by_offset(-100, -100)
        actions.release()
        actions.perform()
        
        # Wait for resize to complete
        time.sleep(0.1)
        
        # Verify dimensions are within minimum limits
        min_size = resizable_element.size
        assert min_size['width'] >= 104
        assert min_size['height'] >= 104 