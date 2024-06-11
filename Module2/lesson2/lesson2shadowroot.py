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
    driver.get("https://www.practiceautomatedtesting.com/webelements/shadowdompage")  # Replace with your actual file path or URL
    print("Opened the website with shadow DOM")

    # Wait for the shadow host element to be present
    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#shadow-host"))
    )
    print("Shadow host element found")

    # Execute JavaScript to get the shadow root and then find the shadow element
    shadow_input = driver.execute_script('return document.querySelector("#shadow-host").shadowRoot.querySelector("#shadow-input")')
    print("Shadow element found")

    # Interact with the shadow element
    shadow_input.send_keys("Hello, Shadow DOM!")
    print("Text entered into shadow element")

    time.sleep(3)  # Pause to observe the interaction

finally:
    # Quit the WebDriver session
    driver.quit()
