from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver it will install the chrome manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open my learnportal and go to the input screen
driver.get("https://www.practiceautomatedtesting.com/webelements/SelectBoxPage")
print("Opened practiceautomated testing")
time.sleep(2)


dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//select'))
)


select = Select(dropdown)

select.select_by_value('Option 1')




# Wait for the expected text to be present in the DOM
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='SelectBox']"))
    )
    print("Selected the option 1")
except:
    print("something went wrong ")

time.sleep(5)


select.select_by_visible_text('Option 2')

# Wait for the expected text to be present in the DOM
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='SelectBox']"))
    )
    print("Selected the option 1")
except:
    print("something went wrong ")


time.sleep(2)

# Enter text




# Close the driver
driver.quit()
