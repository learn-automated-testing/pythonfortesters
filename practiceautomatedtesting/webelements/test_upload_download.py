import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time

class TestUploadDownload:
    @pytest.fixture(scope="function")
    def driver(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Set download preferences
        prefs = {
            "download.default_directory": os.path.join(os.path.dirname(__file__), "downloads"),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_upload_download_functionality(self, driver):
        # Navigate to the web elements page
        print("Navigating to website...")
        driver.get("https://practiceautomatedtesting.com/webelements")
        
        # Wait for page to load completely
        print("Waiting for page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Click on Elements menu
        print("Looking for Elements menu...")
        elements_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//summary[contains(., 'Elements')]"))
        )
        elements_menu.click()
        
        # Click on Upload and Download link
        print("Looking for Upload and Download link...")
        upload_download_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Upload and Download')]"))
        )
        upload_download_link.click()
        
        # Wait for the upload and download component to be visible
        print("Waiting for component container...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class*="componentContainer"]'))
        )

        # Test file upload
        print("Testing file upload...")
        # Create a sample text file if it doesn't exist
        sample_file_path = os.path.join(os.path.dirname(__file__), "sample.txt")
        with open(sample_file_path, "w") as f:
            f.write("This is a sample file for testing upload functionality.")
        
        # Find and upload the file
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(sample_file_path)
        
        # Click the Upload button
        upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Upload')]"))
        )
        upload_button.click()
        
        # Wait for upload to complete
        time.sleep(1)

        # Test file download
        print("Testing file download...")
        # Find and click the PDF download button
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Example PDF')]//button"))
        )
        download_button.click()
        
        # Wait for download to complete
        time.sleep(2)
        
        # Verify the downloaded file exists
        download_path = os.path.join(os.path.dirname(__file__), "downloads", "Example PDF.pdf")
        assert os.path.exists(download_path), "Downloaded file does not exist"
        
        # Cleanup
        print("Cleaning up test files...")
        if os.path.exists(sample_file_path):
            os.remove(sample_file_path)
        if os.path.exists(download_path):
            os.remove(download_path) 