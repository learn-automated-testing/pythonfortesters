from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestSlider:
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

    def test_slider_interaction(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Slider link
        slider_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Slider')]"))
        )
        slider_link.click()
        
        # Wait for the slider component to be visible
        slider = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='range']"))
        )
        
        # Get the size and location of the slider
        slider_size = slider.size
        slider_location = slider.location
        
        # Calculate the position to move the slider (75% of its width)
        target_x = slider_location['x'] + (slider_size['width'] * 0.75)
        target_y = slider_location['y'] + (slider_size['height'] / 2)
        
        # Create an ActionChains instance and perform the drag operation
        actions = ActionChains(driver)
        actions.move_to_element(slider)
        actions.click_and_hold()
        actions.move_by_offset(target_x - slider_location['x'], 0)
        actions.release()
        actions.perform()
        
        # Get the current value of the slider and convert to float
        slider_value = float(slider.get_attribute('value'))
        
        # Verify the slider value is within expected range
        assert slider_value >= 100.0, f"Slider value {slider_value} is less than expected minimum of 100"
        assert slider_value <= 200.0, f"Slider value {slider_value} is greater than expected maximum of 200" 