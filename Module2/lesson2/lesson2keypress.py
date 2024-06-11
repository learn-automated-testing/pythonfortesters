from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the provided URL
    driver.get("https://www.practiceautomatedtesting.com/webelements/KeyPressesPage")
    print("Opened practiceautomated testing key presses page")

    # Locate the input box using its class name
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".KeyPresses_inputBox__-5die"))
    )
    print("Input box found")

    # Click the input box and send a key press
    input_box.click()
    input_box.send_keys('c')
    print("Key 'c' pressed")

    # Verify the result displayed in the second div
    result_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".KeyPresses_keyPressed__k5B5a"))
    )
    result_text = result_div.text
    print(f"Result text: {result_text}")

    # Validate the result
    expected_text = "You pressed: c"
    if result_text == expected_text:
        print("OK: The result is correct.")
    else:
        print(f"Error: The result is incorrect. Expected '{expected_text}', but got '{result_text}'.")

finally:
    # Quit the WebDriver session
    driver.quit()
