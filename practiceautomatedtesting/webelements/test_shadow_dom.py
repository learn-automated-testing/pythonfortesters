from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
import pytest

class TestShadowDOM:
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

    def navigate_to_shadow_dom_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Shadow DOM link
        shadow_dom_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Shadow DOM')]"))
        )
        shadow_dom_link.click()
        
        # Wait for the shadow DOM component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    def get_shadow_element(self, driver, host_id, selector):
        # Get the shadow host element
        shadow_host = driver.find_element(By.ID, host_id)
        
        # Execute JavaScript to get the shadow root and find the element
        shadow_element = driver.execute_script(
            "return arguments[0].shadowRoot.querySelector(arguments[1])",
            shadow_host, selector
        )
        return shadow_element

    def test_shadow_dom_interactions(self, driver):
        self.navigate_to_shadow_dom_page(driver)
        
        # Get shadow DOM elements
        shadow_input = self.get_shadow_element(driver, "shadow-host", ".shadow-input")
        shadow_button = self.get_shadow_element(driver, "shadow-host", ".shadow-button")
        
        # Verify elements are visible
        assert shadow_input.is_displayed()
        assert shadow_button.is_displayed()
        
        # Interact with shadow DOM elements
        shadow_input.clear()
        shadow_input.send_keys("Test Input")
        
        # Click the button and handle the alert
        shadow_button.click()
        
        # Wait for and handle the alert
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            assert "Button clicked! Input value: Test Input" in alert_text
            alert.accept()
        except UnexpectedAlertPresentException:
            # If alert is already present, handle it
            alert = driver.switch_to.alert
            alert_text = alert.text
            assert "Button clicked! Input value: Test Input" in alert_text
            alert.accept()
        
        # Verify the input value after alert is handled
        assert shadow_input.get_attribute("value") == "Test Input"

    def test_shadow_dom_styling(self, driver):
        self.navigate_to_shadow_dom_page(driver)
        
        # Get shadow DOM elements
        shadow_input = self.get_shadow_element(driver, "shadow-host", ".shadow-input")
        shadow_button = self.get_shadow_element(driver, "shadow-host", ".shadow-button")
        
        # Verify elements have proper styling
        assert shadow_input.get_attribute("class") == "shadow-input"
        assert shadow_button.get_attribute("class") == "shadow-button"
        
        # Verify elements are properly positioned
        input_location = shadow_input.location
        button_location = shadow_button.location
        
        assert input_location['x'] > 0
        assert input_location['y'] > 0
        assert button_location['x'] > 0
        assert button_location['y'] > 0 