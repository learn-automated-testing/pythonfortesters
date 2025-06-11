from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

class TestProgressBar:
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

    def navigate_to_progress_bar_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Progress Bar link
        progress_bar_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Progress Bar')]"))
        )
        progress_bar_link.click()
        
        # Wait for the progress bar to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_formSection']"))
        )

    def get_start_button(self, driver):
        return WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Start progress animation"]'))
        )

    def get_reset_button(self, driver):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Reset progress"]'))
        )

    def test_progress_bar_initial_state(self, driver):
        self.navigate_to_progress_bar_page(driver)
        
        # Get elements with explicit waits
        progress_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_progressBar']"))
        )
        
        # Verify initial state
        assert progress_bar.get_attribute('aria-valuenow') == '0'

    def test_progress_bar_animation(self, driver):
        self.navigate_to_progress_bar_page(driver)
        
        # Get elements with explicit waits
        progress_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_progressBar']"))
        )
        
        # Verify initial state
        assert progress_bar.get_attribute('aria-valuenow') == '0'
        
        # Start the progress animation
        assert self.get_start_button(driver).is_enabled(), "Start button is not enabled."
        self.get_start_button(driver).click()
        
        # Wait for progress to reach 100%
        WebDriverWait(driver, 15).until(lambda d: progress_bar.get_attribute('aria-valuenow') == '100')
        
        # Verify final state
        assert progress_bar.get_attribute('aria-valuenow') == '100'

    def test_progress_bar_reset(self, driver):
        self.navigate_to_progress_bar_page(driver)
        
        # Get elements with explicit waits
        progress_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_progressBar']"))
        )
        
        # Start and complete the progress
        self.get_start_button(driver).click()
        WebDriverWait(driver, 15).until(lambda d: progress_bar.get_attribute('aria-valuenow') == '100')
        
        # Reset the progress
        self.get_reset_button(driver).click()
        
        # Wait for reset to complete
        WebDriverWait(driver, 10).until(lambda d: progress_bar.get_attribute('aria-valuenow') == '0')
        
        # Verify reset state
        assert progress_bar.get_attribute('aria-valuenow') == '0'

    def test_progress_bar_accessibility(self, driver):
        self.navigate_to_progress_bar_page(driver)
        
        # Get elements with explicit waits
        progress_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_progressBar']"))
        )
        
        # Verify ARIA attributes
        assert progress_bar.get_attribute('aria-valuemin') == '0'
        assert progress_bar.get_attribute('aria-valuemax') == '100'
        
        # Verify button accessibility
        assert self.get_start_button(driver).get_attribute('aria-label') == 'Start progress animation'
        assert self.get_reset_button(driver).get_attribute('aria-label') == 'Reset progress'

    def test_progress_bar_page_load(self, driver):
        self.navigate_to_progress_bar_page(driver)
        
        # Wait for the page to be fully loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Get elements with explicit waits
        progress_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_progressBar']"))
        )
        
        # Verify initial state
        assert progress_bar.get_attribute('aria-valuenow') == '0'
 