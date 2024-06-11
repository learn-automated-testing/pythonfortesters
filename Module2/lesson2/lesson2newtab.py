from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the provided URL
    driver.get("https://www.practiceautomatedtesting.com/webelements/newtaborwindowpage")
    print("Opened practiceautomated testing new tab or window page")

    # Locate the "Open New Tab" button and click it
    open_new_tab_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Open New Tab']"))
    )
    print("Open New Tab button found")
    open_new_tab_button.click()
    print("Open New Tab button clicked")

    # Wait for the new tab to open
    time.sleep(2)  # Adjust the sleep time if needed

    # Get the handle of the original tab
    original_tab = driver.current_window_handle

    # Get the handles of all open tabs
    all_tabs = driver.window_handles

    # Switch to the new tab (the one that is not the original tab)
    for tab in all_tabs:
        if tab != original_tab:
            driver.switch_to.window(tab)
            break

    print("Switched to the new tab")

    # Perform actions or verifications in the new tab
    # For example, wait for an element to be present on the new tab page
    new_tab_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    print("Element found in the new tab")

    # Perform any further actions or verifications as needed

finally:
    # Close the new tab and switch back to the original tab
    driver.close()
    driver.switch_to.window(original_tab)
    print("Closed the new tab and switched back to the original tab")

    # Quit the WebDriver session
    driver.quit()
