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

# Open the Google page
driver.get("https://www.learnautomatedtesting.com/blog")
print("Opened learnautomatedtesting")
time.sleep(2)
# Find the search box
search_box = driver.find_element(By.CSS_SELECTOR, '[enterkeyhint="search"]')



# Enter text
search_box.send_keys('Selenium Learning to fetch CSS and XPATH the hard way')


print("Performed a search")

# Optionally, you can add a wait to ensure the search results load
gotoblog = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="/course/css-xpath/"]')))
print("selected a blog Querying XPATH and CSS")
gotoblog.click()

# Close the driver
driver.quit()
