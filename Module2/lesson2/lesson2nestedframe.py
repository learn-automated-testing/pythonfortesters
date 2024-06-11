from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the provided URL
    driver.get("https://www.practiceautomatedtesting.com/webelements/NestedFramePage")
    
    print("Opened practiceautomated testing nested frame page")
    
    time.sleep(3)

    driver.get("https://www.practiceautomatedtesting.com/webelements/NestedFramePage")
    # Switch to the iframe with title "top"
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='top']"))
    )
    print("Switched to iframe with title 'top'")

    # Check for the presence of "Top Frame" text inside the iframe using XPath
    # The 'srcdoc' attribute contains the "Top Frame" text, so we verify that directly in the iframe's body
    frame_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body[contains(text(), 'Top Frame')]"))
    )
    print("Frame text 'Top Frame' found:", frame_text.is_displayed())

    # Optionally perform a hover action or any other interaction
    actions = ActionChains(driver)
    actions.move_to_element(frame_text).perform()
    print("Hover action performed on the text element")

    time.sleep(3)  # Wait for a few seconds to observe any actions

finally:
    # Quit the WebDriver session
    driver.quit()
