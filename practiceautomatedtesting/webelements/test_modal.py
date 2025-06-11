from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestModal:
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

    def test_open_modal(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Modal link
        modal_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Modal')]"))
        )
        modal_link.click()
        
        # Verify work instruction is visible
        work_instruction = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(., 'Work Instruction:')]"))
        )
        assert "Work Instruction: Click the button to open the modal dialog." in work_instruction.text
        
        # Click open modal button
        open_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Open Modal')]"))
        )
        open_button.click()
        
        # Verify modal is visible
        modal_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(., 'This is a Modal Dialog')]"))
        )
        assert modal_title.is_displayed()
        
        modal_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(., 'You can put any content here')]"))
        )
        assert modal_content.is_displayed()

    def test_modal_content(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Modal link
        modal_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Modal')]"))
        )
        modal_link.click()
        
        # Click open modal button
        open_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Open Modal')]"))
        )
        open_button.click()
        
        # Verify modal content
        modal_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(., 'This is a Modal Dialog')]"))
        )
        assert modal_title.text == "This is a Modal Dialog"
        
        modal_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(., 'You can put any content here')]"))
        )
        assert modal_content.text == "You can put any content here. Click outside or the button below to close." 