#!/usr/bin/env python3
"""
Debug script for WebElements tests
Run this locally to test if the website is accessible and elements are present
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver(headless=False):
    """Set up Chrome driver with appropriate options"""
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        chrome_options.add_argument("--start-maximized")
    
    # Additional options for stability
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Error setting up driver: {e}")
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(10)
    return driver

def test_website_accessibility():
    """Test if the website is accessible"""
    print("🔍 Testing website accessibility...")
    
    driver = setup_driver(headless=True)
    try:
        # Test basic page load
        driver.get("https://practiceautomatedtesting.com/webelements")
        print(f"✅ Page loaded successfully. Title: {driver.title}")
        
        # Check if page contains expected elements
        wait = WebDriverWait(driver, 10)
        
        # Look for Elements menu
        try:
            elements_menu = wait.until(
                EC.presence_of_element_located((By.XPATH, "//summary[contains(., 'Elements')]"))
            )
            print("✅ Elements menu found")
        except Exception as e:
            print(f"❌ Elements menu not found: {e}")
            
        # Look for any navigation elements
        nav_elements = driver.find_elements(By.TAG_NAME, "nav")
        if nav_elements:
            print(f"✅ Navigation elements found: {len(nav_elements)}")
        else:
            print("❌ No navigation elements found")
            
        # Check page source for common elements
        page_source = driver.page_source.lower()
        if "checkbox" in page_source:
            print("✅ Checkbox elements mentioned in page")
        if "radio" in page_source:
            print("✅ Radio button elements mentioned in page")
            
        # Take screenshot for debugging
        driver.save_screenshot("debug_screenshot.png")
        print("📸 Screenshot saved as debug_screenshot.png")
        
    except Exception as e:
        print(f"❌ Error accessing website: {e}")
    finally:
        driver.quit()

def test_checkbox_page():
    """Test checkbox page specifically"""
    print("\n🔍 Testing checkbox page...")
    
    driver = setup_driver(headless=False)  # Use visible browser for debugging
    try:
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Click on Elements menu
        wait = WebDriverWait(driver, 10)
        elements_menu = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        print("✅ Elements menu clicked")
        
        # Look for Check Box link
        try:
            checkbox_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Check Box')]"))
            )
            checkbox_link.click()
            print("✅ Check Box link clicked")
            
            # Wait for checkbox component
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='componentContainer']"))
            )
            print("✅ Checkbox component loaded")
            
            # Look for checkboxes
            checkboxes = driver.find_elements(By.ID, "checkbox1")
            if checkboxes:
                print(f"✅ Found {len(checkboxes)} checkbox(es)")
            else:
                print("❌ No checkboxes found")
                
        except Exception as e:
            print(f"❌ Error navigating to checkbox page: {e}")
            
        # Take screenshot
        driver.save_screenshot("checkbox_debug.png")
        print("📸 Checkbox page screenshot saved as checkbox_debug.png")
        
    except Exception as e:
        print(f"❌ Error in checkbox test: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    print("🚀 Starting WebElements Debug Tests\n")
    
    # Test 1: Basic website accessibility
    test_website_accessibility()
    
    # Test 2: Checkbox page navigation
    test_checkbox_page()
    
    print("\n✅ Debug tests completed!")
    print("📁 Check the generated screenshots for visual debugging") 