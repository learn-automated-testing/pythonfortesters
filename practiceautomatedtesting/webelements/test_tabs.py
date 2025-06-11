from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestTabs:
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

    def test_tabs_initial_state(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Tabs link
        tabs_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Tabs')]"))
        )
        tabs_link.click()
        
        # Wait for tabs section to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_tabsSection']"))
        )
        
        # Get all tab buttons and content panel
        tab_buttons = driver.find_elements(By.CSS_SELECTOR, "[class*='WebElements_tabButton']")
        content_pane = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tabPane']")
        
        # Verify initial state
        assert len(tab_buttons) == 3  # There are 3 tabs
        assert content_pane.is_displayed()
        
        # Verify first tab is active by default
        assert tab_buttons[0].get_attribute('aria-selected') == 'true'
        assert 'WebElements_active' in tab_buttons[0].get_attribute('class')
        assert content_pane.text == 'Content for Tab 1'
        
        # Verify other tabs are not active
        for i in range(1, 3):
            assert tab_buttons[i].get_attribute('aria-selected') == 'false'
            assert 'WebElements_active' not in tab_buttons[i].get_attribute('class')

    def test_tab_switching(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Tabs link
        tabs_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Tabs')]"))
        )
        tabs_link.click()
        
        # Wait for tabs section to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_tabsSection']"))
        )
        
        # Get all tab buttons and content panel
        tab_buttons = driver.find_elements(By.CSS_SELECTOR, "[class*='WebElements_tabButton']")
        content_pane = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tabPane']")
        
        # Click second tab
        tab_buttons[1].click()
        
        # Verify second tab is active
        assert tab_buttons[1].get_attribute('aria-selected') == 'true'
        assert 'WebElements_active' in tab_buttons[1].get_attribute('class')
        assert content_pane.text == 'Content for Tab 2'
        
        # Verify other tabs are not active
        assert tab_buttons[0].get_attribute('aria-selected') == 'false'
        assert tab_buttons[2].get_attribute('aria-selected') == 'false'
        assert 'WebElements_active' not in tab_buttons[0].get_attribute('class')
        assert 'WebElements_active' not in tab_buttons[2].get_attribute('class')
        
        # Click third tab
        tab_buttons[2].click()
        
        # Verify third tab is active
        assert tab_buttons[2].get_attribute('aria-selected') == 'true'
        assert 'WebElements_active' in tab_buttons[2].get_attribute('class')
        assert content_pane.text == 'Content for Tab 3'
        
        # Verify other tabs are not active
        assert tab_buttons[0].get_attribute('aria-selected') == 'false'
        assert tab_buttons[1].get_attribute('aria-selected') == 'false'
        assert 'WebElements_active' not in tab_buttons[0].get_attribute('class')
        assert 'WebElements_active' not in tab_buttons[1].get_attribute('class')

    def test_tab_content_verification(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Tabs link
        tabs_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Tabs')]"))
        )
        tabs_link.click()
        
        # Wait for tabs section to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_tabsSection']"))
        )
        
        # Get all tab buttons and content panel
        tab_buttons = driver.find_elements(By.CSS_SELECTOR, "[class*='WebElements_tabButton']")
        content_pane = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tabPane']")
        
        # Verify content of each tab
        expected_content = [
            'Content for Tab 1',
            'Content for Tab 2',
            'Content for Tab 3'
        ]
        
        for i in range(3):
            tab_buttons[i].click()
            assert content_pane.is_displayed()
            assert content_pane.text == expected_content[i] 