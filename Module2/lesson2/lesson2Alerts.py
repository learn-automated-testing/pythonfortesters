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
    driver.get("https://www.practiceautomatedtesting.com/webelements/AlertPage")
    print("Opened practiceautomated testing alert page")

    # Locate the alert button using XPath contains text
    alert_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show Alert')]"))
    )
    print("Alert button found")

    # Click the alert button to trigger the alert
    alert_button.click()
    print("Alert button clicked")

    # Wait for the alert to be present and handle it
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(f"Alert text: {alert.text}")
    alert.accept()
    print("Alert accepted")
    time.sleep(3)
    # Locate and click the "Show Confirm" button
    confirm_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show Confirm')]"))
    )
    print("Confirm button found")
    confirm_button.click()
    print("Confirm button clicked")

    # Handle the confirm alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm = driver.switch_to.alert
    print(f"Confirm text: {confirm.text}")
    confirm.accept()  # or confirm.dismiss() to cancel
    print("Confirm accepted")
    
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    confirm = driver.switch_to.alert
    print(f"Confirm text: {confirm.text}")
    confirm.accept()  # or confirm.dismiss() to cancel
    print("Confirm accepted")
     
    
    time.sleep(3)
    # Locate and click the "Show Prompt" button
    prompt_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show Prompt')]"))
    )
    print("Prompt button found")
    prompt_button.click()
    print("Prompt button clicked")

    # Handle the prompt alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    prompt = driver.switch_to.alert
    print(f"Prompt text: {prompt.text}")
    time.sleep(3)
    prompt.send_keys("John Doe")
    # visual issue https://stackoverflow.com/questions/53567385/selenium-alert-sendkeys-with-chrome-is-not-working
    time.sleep(3)
    prompt.accept()
    print("Prompt accepted with input")

finally:
    # Quit the WebDriver session
    driver.quit()
