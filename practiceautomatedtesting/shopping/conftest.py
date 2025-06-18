import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    """Create a new Chrome WebDriver instance for each test"""
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Yield the driver to the test
    yield driver
    
    # Take screenshot on test failure
    if pytest.test_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    
    # Cleanup after the test
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(pytest, "test_failed", rep.failed) 