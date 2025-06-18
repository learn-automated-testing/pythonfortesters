#!/usr/bin/env python3
"""
Simple test to verify the setup works in GitHub Actions
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_basic_setup():
    """Test basic Chrome and ChromeDriver setup"""
    print("🔍 Testing basic setup...")
    
    # Set up Chrome options
    chrome_options = Options()
    
    # Check if running in headless environment
    if os.getenv('CHROME_HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        chrome_options.add_argument("--start-maximized")
    
    try:
        # Use webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("✅ Chrome driver created successfully")
        
        # Test basic navigation
        driver.get("https://practiceautomatedtesting.com/webelements")
        print(f"✅ Page loaded successfully. Title: {driver.title}")
        
        # Take screenshot
        driver.save_screenshot("test_screenshot.png")
        print("✅ Screenshot saved")
        
        driver.quit()
        print("✅ Test completed successfully")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_basic_setup()
    exit(0 if success else 1) 