import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    """
    Fixture to provide a configured Chrome WebDriver instance.
    Handles both local development and CI/CD environments.
    """
    # Set up Chrome options
    chrome_options = Options()
    
    # Check if running in headless environment (GitHub Actions)
    if os.getenv('CHROME_HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        # Local development - maximize window
        chrome_options.add_argument("--start-maximized")
    
    # Additional options for stability
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Set user agent
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        # Try to use webdriver-manager for automatic driver management
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"WebDriver Manager failed: {e}")
        try:
            # Fallback to system ChromeDriver
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as e2:
            print(f"System ChromeDriver failed: {e2}")
            # Last resort - try without service
            driver = webdriver.Chrome(options=chrome_options)
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    yield driver
    
    # Clean up
    try:
        driver.quit()
    except Exception:
        pass 