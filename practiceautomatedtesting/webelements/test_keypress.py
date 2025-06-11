from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestKeypress:
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

    def navigate_to_keypress_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Keypress link
        keypress_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Keypress')]"))
        )
        keypress_link.click()
        
        # Wait for the keypress container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "KeyPresses_container__IvRHJ"))
        )

    def test_single_key_press(self, driver):
        self.navigate_to_keypress_page(driver)
        
        # Find and click the input field
        input_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "KeyPresses_inputBox__-5die"))
        )
        input_field.click()
        input_field.send_keys('a')
        
        # Verify the result
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "KeyPresses_keyPressed__k5B5a"))
        )
        assert result.text == "You pressed: a"

    def test_multiple_key_presses(self, driver):
        self.navigate_to_keypress_page(driver)
        
        input_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "KeyPresses_inputBox__-5die"))
        )
        
        keys = ['a', 'b', 'c', '1', '2', '3']
        for key in keys:
            input_field.click()
            input_field.send_keys(key)
            
            result = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "KeyPresses_keyPressed__k5B5a"))
            )
            assert result.text == f"You pressed: {key}"

    def test_special_keys(self, driver):
        self.navigate_to_keypress_page(driver)
        
        input_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "KeyPresses_inputBox__-5die"))
        )
        
        special_keys = {
            Keys.ENTER: "Enter",
            Keys.TAB: "Tab",
            Keys.ESCAPE: "Escape",
            Keys.BACKSPACE: "Backspace"
        }
        
        for key, key_name in special_keys.items():
            input_field.click()
            input_field.send_keys(key)
            
            result = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "KeyPresses_keyPressed__k5B5a"))
            )
            assert result.text == f"You pressed: {key_name}"

    def test_input_field_focus(self, driver):
        self.navigate_to_keypress_page(driver)
        
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "KeyPresses_inputBox__-5die"))
        )
        
        # Verify input is not focused initially
        assert driver.switch_to.active_element != input_field
        
        # Click to focus
        input_field.click()
        assert driver.switch_to.active_element == input_field
        
        # Press a key
        input_field.send_keys('a')
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "KeyPresses_keyPressed__k5B5a"))
        )
        assert result.text == "You pressed: a" 