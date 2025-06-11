from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

class TestAccordion:
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

    def navigate_to_accordion_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Widgets menu
        widgets_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
        )
        widgets_menu.click()
        
        # Click on Accordion link
        accordion_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Accordion')]"))
        )
        accordion_link.click()
        
        # Wait for the accordion component to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "section"))
        )

    def test_accordion_initial_state(self, driver):
        self.navigate_to_accordion_page(driver)
        
        # Get all accordion sections
        accordion_sections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section details"))
        )
        
        # Verify there are multiple sections
        assert len(accordion_sections) == 2

        # Click first section to expand it
        first_section = accordion_sections[0]
        first_header = first_section.find_element(By.TAG_NAME, "summary")
        first_header.click()
        
        # Wait for and verify first section content
        first_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Content for Section 1')]"))
        )
        assert first_content.text == "Content for Section 1"

    def test_accordion_expand_collapse(self, driver):
        self.navigate_to_accordion_page(driver)
        
        # Get the second section
        accordion_sections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section details"))
        )
        second_section = accordion_sections[1]
        second_header = second_section.find_element(By.TAG_NAME, "summary")
        
        # Initially collapsed
        second_content = driver.find_element(By.XPATH, "//div[contains(text(), 'Content for Section 2')]")
        assert not second_content.is_displayed()

        # Click to expand
        second_header.click()
        # Wait for content to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Content for Section 2')]"))
        )
        assert second_content.text == "Content for Section 2"

        # Click to collapse
        second_header.click()
        # Wait for content to be hidden
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Content for Section 2')]"))
        )

    def test_multiple_accordion_sections(self, driver):
        self.navigate_to_accordion_page(driver)
        
        accordion_sections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section details"))
        )
        
        # Test each section
        for i in range(len(accordion_sections)):
            section = accordion_sections[i]
            header = section.find_element(By.TAG_NAME, "summary")
            content_xpath = f"//div[contains(text(), 'Content for Section {i + 1}')]"
            
            # Initially collapsed
            content = driver.find_element(By.XPATH, content_xpath)
            assert not content.is_displayed()

            # Click to expand
            header.click()
            # Wait for content to be visible
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, content_xpath))
            )

            # Click to collapse
            header.click()
            # Wait for content to be hidden
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, content_xpath))
            )

    def test_accordion_content_verification(self, driver):
        self.navigate_to_accordion_page(driver)
        
        accordion_sections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section details"))
        )
        expected_content = [
            'Content for Section 1',
            'Content for Section 2'
        ]

        # Test each section's content
        for i in range(2):
            section = accordion_sections[i]
            header = section.find_element(By.TAG_NAME, "summary")
            content_xpath = f"//div[contains(text(), 'Content for Section {i + 1}')]"
            
            # Initially collapsed
            content = driver.find_element(By.XPATH, content_xpath)
            assert not content.is_displayed()

            # Click to expand and verify content
            header.click()
            # Wait for content to be visible
            content = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, content_xpath))
            )
            assert content.text == expected_content[i]

            # Collapse for next iteration
            header.click()
            # Wait for content to be hidden
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, content_xpath))
            ) 