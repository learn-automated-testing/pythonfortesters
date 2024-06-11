from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver it will install the chrome manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open my learnportal and go to the input screen
driver.get("https://www.practiceautomatedtesting.com/webelements/Checkboxes")
print("Opened practiceautomated testing")
time.sleep(2)
# Input field by XPathinfo@learnautomatedtesting.com
inputusername = driver.find_element(By.XPATH, '//label[contains(@for,"checkbox1")]')
inputusername.click()
time.sleep(2)



try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[class="checkbox-label checked"]'))
    )
    print("Checkbox1 is clicked")
except:
    print("Checkbox1 is clicked")
#


# Enter text


# Close the driver
driver.quit()
