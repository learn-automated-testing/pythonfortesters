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
driver.get("https://www.practiceautomatedtesting.com/webelements/DragDrop")
print("Opened practiceautomated testing")
time.sleep(2)
# Input field by XPathinfo@learnautomatedtesting.com
 # Wait until the draggable element is present
drag_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="draggable "]'))
)

time.sleep(4)
# Wait until the drop target is present
drop_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[class="dropzone"]'))
)

    # Perform drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(drag_element, drop_element).perform()

# Enter text



time.sleep(4)

   # Check if the drop zone contains the desired text
dropzone_text = drop_element.text
if '😊' in dropzone_text:
    print("Test Passed: Dropzone contains the emoji 😊")
else:
    print("Test Failed: Dropzone does not contain the emoji 😊")

# Close the driver
driver.quit()
