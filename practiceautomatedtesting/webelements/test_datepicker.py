from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import pytest
from datetime import datetime
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestDatepicker:
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

    def test_datepicker_interactions(self, driver):
        try:
            # Navigate to the web elements page
            logger.info("Navigating to the web elements page")
            driver.get("https://practiceautomatedtesting.com/webelements")
            
            # Click on Widgets menu
            logger.info("Looking for Widgets menu")
            widgets_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
            )
            widgets_menu.click()
            logger.info("Clicked Widgets menu")
            
            # Click on Date Picker link
            logger.info("Looking for Date Picker link")
            datepicker_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Date Picker')]"))
            )
            datepicker_link.click()
            logger.info("Clicked Date Picker link")
            
            # Wait for the datepicker component to be visible
            logger.info("Waiting for datepicker component")
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
            )
            
            # Find the date input element
            logger.info("Looking for date input element")
            date_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']"))
            )
            
            # Get the position of the date input
            input_rect = date_input.rect
            
            # Try clicking at different positions, more to the left
            positions = [
                (input_rect['x'] + input_rect['width'] - 35, input_rect['y'] + (input_rect['height'] / 2)),  # 35px from right
                (input_rect['x'] + input_rect['width'] - 40, input_rect['y'] + (input_rect['height'] / 2)),  # 40px from right
                (input_rect['x'] + input_rect['width'] - 45, input_rect['y'] + (input_rect['height'] / 2)),  # 45px from right
            ]
            
            for i, (icon_x, icon_y) in enumerate(positions):
                # Add a visual indicator at the click position
                logger.info(f"Adding visual indicator at click position {i+1}")
                driver.execute_script("""
                    var dot = document.createElement('div');
                    dot.style.position = 'absolute';
                    dot.style.left = arguments[0] + 'px';
                    dot.style.top = arguments[1] + 'px';
                    dot.style.width = '10px';
                    dot.style.height = '10px';
                    dot.style.backgroundColor = 'red';
                    dot.style.borderRadius = '50%';
                    dot.style.zIndex = '10000';
                    document.body.appendChild(dot);
                """, icon_x, icon_y)
                
                # Take a screenshot before clicking
                logger.info(f"Taking screenshot before click {i+1}")
                driver.save_screenshot(f'datepicker-before-click-{i+1}.png')
                
                # Create ActionChains instance
                actions = ActionChains(driver)
                
                # Move to the calendar icon position and click
                logger.info(f"Clicking calendar icon at position {i+1}")
                actions.move_by_offset(icon_x, icon_y).click().perform()
                
                # Wait a moment for the calendar to appear
                time.sleep(1)
                
                # Take a screenshot after clicking
                logger.info(f"Taking screenshot after click {i+1}")
                driver.save_screenshot(f'datepicker-after-click-{i+1}.png')
                
                # Optionally, check if the calendar appeared and break if successful
                # (You can add a check here if you want to stop after a successful click)
            
            logger.info("Test completed successfully")
            
        except Exception as e:
            logger.error(f"Test failed with error: {str(e)}")
            # Take a screenshot on failure
            driver.save_screenshot('datepicker-error.png')
            raise 