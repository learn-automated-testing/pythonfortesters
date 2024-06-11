from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver it will install the chrome manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open my learnportal and go to the input screen
driver.get("https://www.practiceautomatedtesting.com/webelements/FormButtonElements")
print("Opened practiceautomated testing")
time.sleep(2)

#input field by xpath
inputusername = driver.find_element(By.XPATH, '//input[@name="name"]')

# Enter text
inputusername.send_keys('fetch CSS and XPATH the hard way')
print("entered a name")

#input email by css field by xpath

#input field by xpath
inputemail = driver.find_element(By.CSS_SELECTOR, '[name="email"]')

# Enter text
inputemail.send_keys('info@learnautomatedtesting.com')
print("entered an email")

#input field by xpath
inputage = driver.find_element(By.XPATH, '//input[@name="age"]')

# Enter text
inputage.send_keys('30')
print("add an age")


btnsubmit = driver.find_element(By.CSS_SELECTOR,'[type="submit"]')


btnsubmit.click()


# Wait for the expected text to be present in the DOM
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'All fields were filled successfully!')]"))
    )
    print("Text found on the page")
except:
    print("Text not found on the page")

# Close the driver
driver.quit()
