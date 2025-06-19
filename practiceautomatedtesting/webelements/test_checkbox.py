from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import pytest
import allure

class TestCheckbox:
    def navigate_to_checkbox_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Check Box link
        checkbox_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Check Box')]"))
        )
        checkbox_link.click()
        
        # Wait for the checkbox component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    @allure.feature("Checkbox Functionality")
    @allure.story("Label Click Interaction")
    @allure.severity(allure.severity_level.NORMAL)
    def test_checkbox_label_clicks(self, driver):
        """
        Test that clicking labels properly toggles checkbox states
        """
        # Navigate to checkbox page
        self.navigate_to_checkbox_page(driver)
        
        # Get checkbox and label elements
        checkbox1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkbox1"))
        )
        checkbox2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkbox2"))
        )
        label1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Checkbox 1')]"))
        )
        label2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Checkbox 2')]"))
        )
        
        # Test clicking labels to check
        label1.click()
        assert checkbox1.is_selected()
        
        label2.click()
        assert checkbox2.is_selected()
        
        # Test clicking labels to uncheck
        label1.click()
        assert not checkbox1.is_selected()
        
        label2.click()
        assert not checkbox2.is_selected()

    