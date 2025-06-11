from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLinks:
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

    def navigate_to_links_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Links link
        links_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Links')]"))
        )
        links_link.click()
        
        # Wait for the links component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    def test_analyze_page_structure(self, driver):
        self.navigate_to_links_page(driver)
        
        # Get all links in the component
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[class*='componentContainer'] a"))
        )
        
        # Log all links
        print("\nAll links in the component:")
        for link in links:
            text = link.text
            href = link.get_attribute('href')
            print(f"Link text: \"{text}\", href: \"{href}\"")

    def test_verify_regular_links_functionality(self, driver):
        self.navigate_to_links_page(driver)
        
        # Test Home Page link
        home_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Home Page')]"))
        )
        assert home_link.is_displayed()
        assert home_link.get_attribute('href') == "https://practiceautomatedtesting.com/"
        
        # Test Checkboxes link
        checkboxes_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Checkboxes')]"))
        )
        assert checkboxes_link.is_displayed()
        assert checkboxes_link.get_attribute('href') == "https://practiceautomatedtesting.com/webelements/checkboxes"
        
        # Test Non-existent Page link
        non_existent_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Non-existent Page')]"))
        )
        assert non_existent_link.is_displayed()
        assert non_existent_link.get_attribute('href') == "https://practiceautomatedtesting.com/nonexistent-page"
        
        # Test Invalid Path link
        invalid_path_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Invalid Path')]"))
        )
        assert invalid_path_link.is_displayed()
        assert invalid_path_link.get_attribute('href') == "https://practiceautomatedtesting.com/webelements/invalid-path"
        
        # Test 404 Page link
        not_found_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., '404 Page')]"))
        )
        assert not_found_link.is_displayed()
        assert not_found_link.get_attribute('href') == "https://practiceautomatedtesting.com/webelements/404"

    def test_verify_link_response_messages(self, driver):
        self.navigate_to_links_page(driver)
        
        # Test Home Page link response
        home_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Home Page')]"))
        )
        home_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practiceautomatedtesting.com/"))
        driver.get("https://practiceautomatedtesting.com/webelements")
        self.navigate_to_links_page(driver)
        
        # Test Checkboxes link response
        checkboxes_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Checkboxes')]"))
        )
        checkboxes_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practiceautomatedtesting.com/webelements/checkboxes"))
        driver.get("https://practiceautomatedtesting.com/webelements")
        self.navigate_to_links_page(driver)
        
        # Test Non-existent Page link response
        non_existent_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Non-existent Page')]"))
        )
        non_existent_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practiceautomatedtesting.com/nonexistent-page"))
        
        # Verify 404 page content
        error_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '404')]"))
        )
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Page Not Found')]"))
        )
        error_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The page you are looking for does not exist.')]"))
        )
        
        assert error_title.is_displayed()
        assert error_message.is_displayed()
        assert error_description.is_displayed()
        
        driver.get("https://practiceautomatedtesting.com/webelements")
        self.navigate_to_links_page(driver)
        
        # Test Invalid Path link response
        invalid_path_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Invalid Path')]"))
        )
        invalid_path_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practiceautomatedtesting.com/webelements/invalid-path"))
        
        # Verify 404 page content again
        error_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '404')]"))
        )
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Page Not Found')]"))
        )
        error_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The page you are looking for does not exist.')]"))
        )
        
        assert error_title.is_displayed()
        assert error_message.is_displayed()
        assert error_description.is_displayed()
        
        driver.get("https://practiceautomatedtesting.com/webelements")
        self.navigate_to_links_page(driver)
        
        # Test 404 Page link response
        not_found_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., '404 Page')]"))
        )
        not_found_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://practiceautomatedtesting.com/webelements/404"))
        
        # Verify 404 page content one more time
        error_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '404')]"))
        )
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Page Not Found')]"))
        )
        error_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'The page you are looking for does not exist.')]"))
        )
        
        assert error_title.is_displayed()
        assert error_message.is_displayed()
        assert error_description.is_displayed() 