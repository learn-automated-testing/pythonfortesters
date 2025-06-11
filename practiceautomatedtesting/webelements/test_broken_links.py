from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestBrokenLinks:
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

    def navigate_to_broken_links_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Broken Links link
        broken_links_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Broken Links')]"))
        )
        broken_links_link.click()
        
        # Wait for the broken links component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
        )

    def test_broken_image(self, driver):
        self.navigate_to_broken_links_page(driver)
        
        # Find the broken image
        broken_image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Broken']"))
        )
        
        # Verify the image is visible
        assert broken_image.is_displayed()
        
        # Verify the alt attribute
        alt_text = broken_image.get_attribute('alt')
        assert alt_text == 'Broken'
        
        # Print all text content in the component container for debugging
        component = driver.find_element(By.CSS_SELECTOR, "[class*='componentContainer']")
        print("\nComponent text content:")
        print(component.text)
        
        # Find all paragraphs in the component
        paragraphs = component.find_elements(By.TAG_NAME, "p")
        print("\nParagraph texts:")
        for p in paragraphs:
            print(f"Paragraph text: '{p.text}'")
        
        # Verify the broken image text exists in the correct paragraph
        broken_image_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Broken Image')]"))
        )
        assert broken_image_text.is_displayed() 