
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver, it will install the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the practice page
driver.get("https://www.practiceautomatedtesting.com/webelements/form_button_elements.html")
print("Opened practice automated testing")
time.sleep(2)

# Input field by XPathinfo@learnautomatedtesting.com
inputusername = driver.find_element(By.XPATH, "//input[@id='name']" )
# Enter text
inputusername.send_keys('fetch CSS and XPATH the hard way')
print("Entered a name")

# Input email by CSS
inputemail = driver.find_element(By.CSS_SELECTOR, "[id='email']" )
# Enter text
inputemail.send_keys('info@learnautomatedtesting.com')
print("Entered an email")

# Input field by XPath
inputage = driver.find_element(By.XPATH, "//input[@id='age']" )
# Enter text
inputage.send_keys('30')
print("Entered an age")

# Submit button by CSS
btnsubmit = driver.find_element(By.CSS_SELECTOR, "[class='btn']" )
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