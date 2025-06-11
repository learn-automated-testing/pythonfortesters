from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestFrame:
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

    def navigate_to_frame_page(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Interactions menu
        interactions_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Interactions')]"))
        )
        interactions_menu.click()
        
        # Click on Frame link
        frame_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Frame')]"))
        )
        frame_link.click()
        
        # Wait for the frame container to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(., 'Nested Frames Example')]"))
        )

    def get_frame(self, driver, title):
        # Switch to the frame by title
        frame = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"iframe[title='{title}']"))
        )
        return frame

    def test_top_frame_content(self, driver):
        self.navigate_to_frame_page(driver)
        
        # Switch to top frame
        top_frame = self.get_frame(driver, 'top')
        driver.switch_to.frame(top_frame)
        
        # Verify frame content
        frame_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        assert frame_content.text == "Top Frame"
        
        # Switch back to default content
        driver.switch_to.default_content()

    def test_middle_row_frames(self, driver):
        self.navigate_to_frame_page(driver)
        
        frames = {
            'left': 'Left Frame',
            'middle': 'Middle Frame',
            'right': 'Right Frame'
        }
        
        for frame_title, expected_text in frames.items():
            # Switch to frame
            frame = self.get_frame(driver, frame_title)
            driver.switch_to.frame(frame)
            
            # Verify frame content
            frame_content = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            assert frame_content.text == expected_text
            
            # Switch back to default content
            driver.switch_to.default_content()

    def test_bottom_frame_content(self, driver):
        self.navigate_to_frame_page(driver)
        
        # Switch to bottom frame
        bottom_frame = self.get_frame(driver, 'bottom')
        driver.switch_to.frame(bottom_frame)
        
        # Verify frame content
        frame_content = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )
        assert frame_content.text == "Bottom Frame"
        
        # Switch back to default content
        driver.switch_to.default_content()

    def test_frame_interactions(self, driver):
        self.navigate_to_frame_page(driver)
        
        frame_titles = ['top', 'left', 'middle', 'right', 'bottom']
        
        for title in frame_titles:
            # Switch to frame
            frame = self.get_frame(driver, title)
            driver.switch_to.frame(frame)
            
            # Verify frame is interactive
            frame_body = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            assert frame_body.is_displayed()
            frame_body.click()
            
            # Switch back to default content
            driver.switch_to.default_content()

    def test_frame_layout(self, driver):
        self.navigate_to_frame_page(driver)
        
        # Get all frames
        frames = driver.find_elements(By.TAG_NAME, "iframe")
        assert len(frames) == 5
        
        for frame in frames:
            # Verify frame dimensions
            size = frame.size
            assert size['width'] > 0
            assert size['height'] > 0 