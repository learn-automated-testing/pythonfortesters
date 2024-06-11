from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the practice website and go to the input screen
    driver.get("https://www.practiceautomatedtesting.com/webelements/Slider")
    print("Opened practiceautomated testing")

    # Wait until the slider is present
    slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.Slider_slider__d1Ld9'))
    )

    # Get the width of the slider
    slider_width = slider.size['width']
    print(f"Slider width: {slider_width}px")

    # Calculate the slider's properties
    min_value = float(slider.get_attribute('min'))
    max_value = float(slider.get_attribute('max'))
    current_value = float(slider.get_attribute('value'))
    target_value = 2.5
    step_value = float(slider.get_attribute('step'))

    # Calculate the total number of steps and pixels per step
    total_steps = (max_value - min_value) / step_value
    pixels_per_step = slider_width / total_steps
    print(f"Pixels per step: {pixels_per_step}")

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Move the slider in finer increments and check value
    move_increment = pixels_per_step / 10  # Move in smaller increments
    actions.click_and_hold(slider).perform()
    
    while current_value < target_value:
        actions.move_by_offset(move_increment, 0).perform()
        time.sleep(0.1)  # Give some time for the slider to update
        current_value = float(slider.get_attribute('value'))
        print(f"Current slider value: {current_value}")

    actions.release().perform()

    # Verify if the slider is set to the target value
    final_value = float(slider.get_attribute('value'))
    if final_value == target_value:
        print("OK: Slider moved to the target value.")
    else:
        print(f"Error: Slider is at {final_value} instead of {target_value}.")

finally:
    # Quit the WebDriver session
    driver.quit()
