import pytest
import os
import allure
from datetime import datetime
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
    
    # Only add user data directory if explicitly set (CI environment)
    chrome_user_data_dir = os.getenv('CHROME_USER_DATA_DIR')
    if chrome_user_data_dir:
        chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
    
    # Check if running in headless environment (GitHub Actions)
    if os.getenv('CHROME_HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-plugins")
    else:
        # Local development - maximize window
        chrome_options.add_argument("--start-maximized")
    
    # Additional options for stability
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Cache clearing options for CI/CD
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--disable-offline-load-stale-cache")
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--media-cache-size=0")
    
    # Set user agent
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    try:
        # Use webdriver-manager for automatic driver management
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Only capture screenshot if test failed
    if rep.when == "call" and rep.failed:
        try:
            # Get the driver from the test
            driver = item.funcargs.get("driver")
            if driver:
                # Create screenshots directory if it doesn't exist
                screenshots_dir = "allure-results/screenshots"
                os.makedirs(screenshots_dir, exist_ok=True)
                
                # Generate unique filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                test_name = item.name.replace("/", "_").replace("\\", "_")
                screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"
                
                # Take screenshot
                driver.save_screenshot(screenshot_path)
                
                # Attach screenshot to Allure report
                with open(screenshot_path, "rb") as f:
                    allure.attach(
                        f.read(),
                        name=f"Screenshot - {test_name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                
                print(f"📸 Screenshot saved: {screenshot_path}")
                
        except Exception as e:
            print(f"❌ Failed to capture screenshot: {e}")

@pytest.fixture(autouse=True)
def allure_environment_info(driver):
    """
    Add environment information to Allure report
    """
    if driver:
        try:
            # Add browser info
            browser_info = {
                "Browser": driver.capabilities.get("browserName", "Unknown"),
                "Browser Version": driver.capabilities.get("browserVersion", "Unknown"),
                "Platform": driver.capabilities.get("platformName", "Unknown"),
                "Headless": os.getenv('CHROME_HEADLESS', 'false').lower() == 'true'
            }
            
            # Write environment info to allure-results
            env_file = "allure-results/environment.properties"
            os.makedirs("allure-results", exist_ok=True)
            
            with open(env_file, "w") as f:
                for key, value in browser_info.items():
                    f.write(f"{key}={value}\n")
                    
        except Exception as e:
            print(f"❌ Failed to add environment info: {e}") 