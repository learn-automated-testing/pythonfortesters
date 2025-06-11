from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging

logger = logging.getLogger(__name__)

class ShoppingPage:
    # URL
    URL = "https://practiceautomatedtesting.com/webelements"
    
    # Locators
    ELEMENTS_MENU = (By.XPATH, "//summary[contains(., 'Elements')]")
    SHOPPING_LINK = (By.XPATH, "//a[contains(., 'Shopping')]")
    
    # Modern Shopping Interface Locators
    SEARCH_INPUT = (By.ID, "product-search")
    SORT_NAME_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Sort by Name')]")
    SORT_PRICE_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Sort by Price')]")
    MIN_PRICE_SLIDER = (By.XPATH, "//input[@aria-label='Minimum price slider']")
    MAX_PRICE_SLIDER = (By.XPATH, "//input[@aria-label='Maximum price slider']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".ModernShopping_productCard__u75E5")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".ModernShopping_productName__mWJdU")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".ModernShopping_productPrice__CmjlW")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[aria-label^='Add']")
    PAGINATION_BUTTONS = (By.CSS_SELECTOR, ".ModernShopping_pageBtn__j+HGB")
    CART_ICON = (By.CSS_SELECTOR, "nav ul li:nth-child(5) a")
    CART_COUNT = (By.CSS_SELECTOR, ".cart-count")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def navigate(self):
        """Navigate to the shopping page"""
        logger.info("Navigating to shopping page")
        self.driver.get(self.URL)
        
        # Click on Elements menu
        elements_menu = self.wait.until(EC.element_to_be_clickable(self.ELEMENTS_MENU))
        elements_menu.click()
        
        # Click on Shopping link
        shopping_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_LINK))
        shopping_link.click()
        
        # Wait for product cards to be visible
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_CARDS))
    
    def search_product(self, search_term):
        """Search for a product using the search input"""
        logger.info(f"Searching for product: {search_term}")
        search_input = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(search_term)
    
    def sort_by_name(self):
        """Sort products by name"""
        logger.info("Sorting products by name")
        sort_button = self.wait.until(EC.element_to_be_clickable(self.SORT_NAME_BUTTON))
        sort_button.click()
    
    def sort_by_price(self):
        """Sort products by price"""
        logger.info("Sorting products by price")
        sort_button = self.wait.until(EC.element_to_be_clickable(self.SORT_PRICE_BUTTON))
        sort_button.click()
    
    def set_price_range(self, min_price, max_price):
        """Set the price range using sliders"""
        logger.info(f"Setting price range: ${min_price} - ${max_price}")
        min_slider = self.wait.until(EC.presence_of_element_located(self.MIN_PRICE_SLIDER))
        max_slider = self.wait.until(EC.presence_of_element_located(self.MAX_PRICE_SLIDER))
        
        # Set minimum price
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'))",
            min_slider, min_price
        )
        
        # Set maximum price
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'))",
            max_slider, max_price
        )
    
    def add_product_to_cart(self, product_name):
        """Add a product to cart by name"""
        logger.info(f"Adding product {product_name} to cart")
        try:
            # Get current cart count
            try:
                current_count = int(self.driver.find_element(*self.CART_COUNT).text)
            except:
                current_count = 0
            
            # Find the button with the exact aria-label
            button_selector = f'button[aria-label="Add {product_name} to cart"]'
            logger.info(f"Looking for button with selector: {button_selector}")
            
            button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
            )
            button.click()
            
            # Wait for cart count to update
            def cart_count_updated(driver):
                try:
                    new_count = int(driver.find_element(*self.CART_COUNT).text)
                    return new_count > current_count
                except:
                    return False
            
            self.wait.until(cart_count_updated)
            return True
        except Exception as e:
            logger.error(f"Failed to add product {product_name} to cart: {str(e)}")
            return False
    
    def add_product_to_cart_by_aria(self, product_name):
        """Add a product to cart using aria-label"""
        return self.add_product_to_cart(product_name)
    
    def go_to_cart(self):
        """Navigate to cart by clicking the cart icon"""
        logger.info("Navigating to cart")
        cart_icon = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart_icon.click()
        # Wait for cart page to load
        self.wait.until(EC.url_contains("checkout"))
    
    def get_product_names(self):
        """Get all product names"""
        names = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [name.text for name in names]
    
    def get_product_prices(self):
        """Get all product prices"""
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [price.text for price in prices]
    
    def go_to_page(self, page_number):
        """Navigate to a specific page"""
        logger.info(f"Navigating to page {page_number}")
        pagination_buttons = self.driver.find_elements(*self.PAGINATION_BUTTONS)
        for button in pagination_buttons:
            if button.text == str(page_number):
                button.click()
                return True
        return False 