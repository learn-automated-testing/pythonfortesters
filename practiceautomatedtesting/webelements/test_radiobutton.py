from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestRadioButton:
    def navigate_to_radio_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Radio Button link
        radio_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Radio Button')]"))
        )
        radio_link.click()
        
        # Wait for the radio button container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    def test_radio_button_selection(self, driver):
        self.navigate_to_radio_page(driver)
        
        # Get radio button elements
        radio1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "radio1"))
        )
        radio2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "radio2"))
        )
        
        # Test Radio 2 selection first
        radio2.click()
        message2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'You selected: Radio 2')]"))
        )
        assert message2.is_displayed()
        
        # Then test Radio 1 selection
        radio1.click()
        message1 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'You selected: Radio 1')]"))
        )
        assert message1.is_displayed() 