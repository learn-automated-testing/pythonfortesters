from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver it will install the chrome manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open my learnportal and go to the input screen
driver.get("https://www.practiceautomatedtesting.com/webelements/HoverToClickButton")
print("Opened practiceautomated testing")
time.sleep(2)
# Input field by XPathinfo@learnautomatedtesting.com
 # Wait until the draggable element is present
hover_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="HoverToClickButton_hoverText__wtIgh"]'))
)

actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()

time.sleep(4)

hidden_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="HoverToClickButton_hiddenButton__WL3-l"'))
)

if hidden_button.is_displayed():
        print("OK: Hidden button is now visible.")

# Close the driver
driver.quit()
