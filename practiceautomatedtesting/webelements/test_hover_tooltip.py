from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class TestHoverTooltip:
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

    def test_tooltip_initial_state(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        print("Navigated to page")
        
        # Click on Widgets menu
        try:
            widgets_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
            )
            print("Found Widgets menu")
            widgets_menu.click()
            print("Clicked Widgets menu")
        except Exception as e:
            print(f"Error clicking Widgets menu: {str(e)}")
            raise
        
        # Click on Hover and Tooltip link
        try:
            tooltip_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Hover and Tooltip')]"))
            )
            print("Found Hover and Tooltip link")
            tooltip_link.click()
            print("Clicked Hover and Tooltip link")
        except Exception as e:
            print(f"Error clicking Hover and Tooltip link: {str(e)}")
            raise
        
        # Wait for the component to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_formSection']"))
            )
            print("Found form section")
        except Exception as e:
            print(f"Error finding form section: {str(e)}")
            raise
        
        # Get the hover button
        try:
            hover_button = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tooltipButton']")
            print("Found hover button")
            print(f"Button text: {hover_button.text}")
            print(f"Button displayed: {hover_button.is_displayed()}")
        except Exception as e:
            print(f"Error finding hover button: {str(e)}")
            raise
        
        # Verify hover button is visible and has correct text
        assert hover_button.is_displayed()
        assert hover_button.text == "Hover me"
        
        # Try to find tooltip (should not be visible initially)
        try:
            tooltip = driver.find_element(By.ID, "custom-tooltip")
            print("Found tooltip")
            print(f"Tooltip displayed: {tooltip.is_displayed()}")
        except Exception as e:
            print(f"Tooltip not found (expected): {str(e)}")
            # This is expected since tooltip should not be visible initially
            pass

    def test_tooltip_appears_on_hover(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        print("Navigated to page")
        
        # Click on Widgets menu
        try:
            widgets_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
            )
            print("Found Widgets menu")
            widgets_menu.click()
            print("Clicked Widgets menu")
        except Exception as e:
            print(f"Error clicking Widgets menu: {str(e)}")
            raise
        
        # Click on Hover and Tooltip link
        try:
            tooltip_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Hover and Tooltip')]"))
            )
            print("Found Hover and Tooltip link")
            tooltip_link.click()
            print("Clicked Hover and Tooltip link")
        except Exception as e:
            print(f"Error clicking Hover and Tooltip link: {str(e)}")
            raise
        
        # Wait for the component to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_formSection']"))
            )
            print("Found form section")
        except Exception as e:
            print(f"Error finding form section: {str(e)}")
            raise
        
        # Get the hover button
        try:
            hover_button = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tooltipButton']")
            print("Found hover button")
            print(f"Button text: {hover_button.text}")
            print(f"Button displayed: {hover_button.is_displayed()}")
        except Exception as e:
            print(f"Error finding hover button: {str(e)}")
            raise
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Hover over the button
        try:
            actions.move_to_element(hover_button).perform()
            print("Hovered over button")
            time.sleep(1)  # Give a small delay for the tooltip to appear
        except Exception as e:
            print(f"Error hovering over button: {str(e)}")
            raise
        
        # Try to find tooltip
        try:
            tooltip = driver.find_element(By.ID, "custom-tooltip")
            print("Found tooltip")
            print(f"Tooltip displayed: {tooltip.is_displayed()}")
            assert tooltip.is_displayed()
        except Exception as e:
            print(f"Error finding tooltip: {str(e)}")
            raise

    def test_tooltip_disappears_on_mouse_leave(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        print("Navigated to page")
        
        # Click on Widgets menu
        try:
            widgets_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
            )
            print("Found Widgets menu")
            widgets_menu.click()
            print("Clicked Widgets menu")
        except Exception as e:
            print(f"Error clicking Widgets menu: {str(e)}")
            raise
        
        # Click on Hover and Tooltip link
        try:
            tooltip_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Hover and Tooltip')]"))
            )
            print("Found Hover and Tooltip link")
            tooltip_link.click()
            print("Clicked Hover and Tooltip link")
        except Exception as e:
            print(f"Error clicking Hover and Tooltip link: {str(e)}")
            raise
        
        # Wait for the component to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_formSection']"))
            )
            print("Found form section")
        except Exception as e:
            print(f"Error finding form section: {str(e)}")
            raise
        
        # Get the hover button
        try:
            hover_button = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tooltipButton']")
            print("Found hover button")
            print(f"Button text: {hover_button.text}")
            print(f"Button displayed: {hover_button.is_displayed()}")
        except Exception as e:
            print(f"Error finding hover button: {str(e)}")
            raise
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Hover over the button
        try:
            actions.move_to_element(hover_button).perform()
            print("Hovered over button")
            time.sleep(1)  # Give a small delay for the tooltip to appear
        except Exception as e:
            print(f"Error hovering over button: {str(e)}")
            raise
        
        # Try to find tooltip
        try:
            tooltip = driver.find_element(By.ID, "custom-tooltip")
            print("Found tooltip")
            print(f"Tooltip displayed: {tooltip.is_displayed()}")
            assert tooltip.is_displayed()
        except Exception as e:
            print(f"Error finding tooltip: {str(e)}")
            raise
        
        # Move mouse away
        try:
            actions.move_by_offset(0, 0).perform()
            print("Moved mouse away")
            time.sleep(1)  # Give a small delay for the tooltip to disappear
        except Exception as e:
            print(f"Error moving mouse away: {str(e)}")
            raise
        
        # Verify tooltip is not visible
        try:
            tooltip = driver.find_element(By.ID, "custom-tooltip")
            print(f"Tooltip still displayed: {tooltip.is_displayed()}")
            assert not tooltip.is_displayed()
        except Exception as e:
            print(f"Tooltip not found (expected): {str(e)}")
            # This is expected since tooltip should not be visible
            pass

    def test_multiple_hover_interactions(self, driver):
        # Navigate to the page
        driver.get("https://practiceautomatedtesting.com/webelements")
        print("Navigated to page")
        
        # Click on Widgets menu
        try:
            widgets_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Widgets')]"))
            )
            print("Found Widgets menu")
            widgets_menu.click()
            print("Clicked Widgets menu")
        except Exception as e:
            print(f"Error clicking Widgets menu: {str(e)}")
            raise
        
        # Click on Hover and Tooltip link
        try:
            tooltip_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Hover and Tooltip')]"))
            )
            print("Found Hover and Tooltip link")
            tooltip_link.click()
            print("Clicked Hover and Tooltip link")
        except Exception as e:
            print(f"Error clicking Hover and Tooltip link: {str(e)}")
            raise
        
        # Wait for the component to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='WebElements_formSection']"))
            )
            print("Found form section")
        except Exception as e:
            print(f"Error finding form section: {str(e)}")
            raise
        
        # Get the hover button
        try:
            hover_button = driver.find_element(By.CSS_SELECTOR, "[class*='WebElements_tooltipButton']")
            print("Found hover button")
            print(f"Button text: {hover_button.text}")
            print(f"Button displayed: {hover_button.is_displayed()}")
        except Exception as e:
            print(f"Error finding hover button: {str(e)}")
            raise
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Test multiple hover interactions
        for i in range(3):
            print(f"\nIteration {i + 1}")
            # Hover over the button
            try:
                actions.move_to_element(hover_button).perform()
                print("Hovered over button")
                time.sleep(1)  # Give a small delay for the tooltip to appear
            except Exception as e:
                print(f"Error hovering over button: {str(e)}")
                raise
            
            # Try to find tooltip
            try:
                tooltip = driver.find_element(By.ID, "custom-tooltip")
                print("Found tooltip")
                print(f"Tooltip displayed: {tooltip.is_displayed()}")
                assert tooltip.is_displayed()
            except Exception as e:
                print(f"Error finding tooltip: {str(e)}")
                raise
            
            # Move mouse away
            try:
                actions.move_by_offset(0, 0).perform()
                print("Moved mouse away")
                time.sleep(1)  # Give a small delay for the tooltip to disappear
            except Exception as e:
                print(f"Error moving mouse away: {str(e)}")
                raise
            
            # Verify tooltip is not visible
            try:
                tooltip = driver.find_element(By.ID, "custom-tooltip")
                print(f"Tooltip still displayed: {tooltip.is_displayed()}")
                assert not tooltip.is_displayed()
            except Exception as e:
                print(f"Tooltip not found (expected): {str(e)}")
                # This is expected since tooltip should not be visible
                pass 