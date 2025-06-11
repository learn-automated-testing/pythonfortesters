import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class TestGeolocation:
    @pytest.fixture(scope="function")
    def driver(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Add geolocation permissions
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.geolocation": 1  # 1:allow, 2:block
        })
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_get_current_location_mocked(self, driver):
        # Navigate to the web elements page
        print("Navigating to website...")
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Wait for page to load completely
        print("Waiting for page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Give extra time for JavaScript to initialize
        time.sleep(2)
        
        # Click on Interactions menu
        print("Looking for Interactions menu...")
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Geolocation link
        print("Looking for Geolocation link...")
        geolocation_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Geolocation')]"))
        )
        geolocation_link.click()
        
        # Set mock geolocation using JavaScript
        print("Setting mock geolocation...")
        driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": 51.5074,
            "longitude": -0.1278,
            "accuracy": 100
        })
        
        # Click the "Get My Location" button
        print("Looking for Get My Location button...")
        get_location_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Get My Location')]"))
        )
        get_location_button.click()
        
        # Wait for and verify the location data
        print("Waiting for location data...")
        location_data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[style*="background: rgb(227, 242, 253)"]'))
        )
        
        # Get all value divs with the specific color and font-weight
        value_divs = location_data.find_elements(By.CSS_SELECTOR, 'div[style*="color: rgb(25, 120, 229)"][style*="font-weight: 500"]')
        
        # Verify the latitude and longitude values
        print("Verifying location values...")
        assert value_divs[0].text == "51.5074"
        assert value_divs[1].text == "-0.1278" 