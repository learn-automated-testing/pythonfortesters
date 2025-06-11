from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger(__name__)

class CheckoutPage:
    # URL
    URL = "https://practiceautomatedtesting.com/checkout"
    
    # Locators
    CART_ITEMS = (By.CSS_SELECTOR, "table.Checkout_cartTable__wp05q tbody tr")
    ITEM_NAME = (By.CSS_SELECTOR, "td:nth-child(2)")
    ITEM_PRICE = (By.CSS_SELECTOR, "td:nth-child(3)")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.Checkout_deleteButton__AxZ8\\+")
    CART_TOTAL = (By.CSS_SELECTOR, ".Checkout_amount__r+Nl4")
    
    # Payment fields
    CARD_NAME = (By.ID, "cc-name")
    CARD_NUMBER = (By.ID, "cc-number")
    EXPIRY_DATE = (By.ID, "cc-expiry")
    CVV = (By.ID, "cc-cvc")
    
    # PayPal specific locators
    PAYPAL_TAB = (By.ID, "tab-paypal")
    PAYPAL_EMAIL = (By.ID, "paypal-email")
    PAY_NOW_BUTTON = (By.CSS_SELECTOR, "form > button")
    
    # Success message locator
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".successText")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
    def navigate(self):
        """Navigate to the checkout page"""
        logger.info("Navigating to checkout page")
        self.driver.get(self.URL)
        # Wait for either cart table or empty cart message
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Checkout_cartTable__wp05q")))
        except:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Checkout_emptyCart__FMywP")))
    
    def get_cart_items(self):
        """Get all items in the cart"""
        try:
            empty_cart = self.driver.find_elements(By.CSS_SELECTOR, ".Checkout_emptyCart__FMywP")
            if empty_cart and empty_cart[0].is_displayed():
                return []
            items = self.driver.find_elements(*self.CART_ITEMS)
            return items
        except:
            return []
    
    def get_item_quantity(self, item_index=0):
        """Get quantity of an item"""
        # Since the current implementation doesn't have quantity controls,
        # we'll return 1 for each item
        return 1
    
    def update_item_quantity(self, item_index, new_quantity):
        """Update quantity of an item"""
        # Since the current implementation doesn't have quantity controls,
        # we'll just log that this operation is not supported
        logger.info("Quantity update not supported in current implementation")
        return False
    
    def remove_item(self, item_index=0):
        """Remove an item from cart"""
        logger.info(f"Removing item at index {item_index}")
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if item_index < len(remove_buttons):
            remove_buttons[item_index].click()
            return True
        return False
    
    def get_subtotal(self):
        """Get the subtotal amount"""
        try:
            total_element = self.wait.until(EC.presence_of_element_located(self.CART_TOTAL))
            return float(total_element.text.replace("$", ""))
        except:
            return 0.0
    
    def get_tax(self):
        """Get the tax amount"""
        # Since tax is not shown separately in the current implementation,
        # we'll return 0
        return 0.0
    
    def get_total(self):
        """Get the total amount"""
        return self.get_subtotal()
    
    def fill_payment_info(self, card_number, expiry_date, cvv, card_name="John Doe"):
        """Fill in payment information"""
        logger.info("Filling payment information")
        self.driver.find_element(*self.CARD_NAME).send_keys(card_name)
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.EXPIRY_DATE).send_keys(expiry_date)
        self.driver.find_element(*self.CVV).send_keys(cvv)
    
    def select_paypal(self):
        """Select PayPal as payment method"""
        logger.info("Selecting PayPal payment method")
        paypal_tab = self.wait.until(EC.element_to_be_clickable(self.PAYPAL_TAB))
        paypal_tab.click()
        # Wait for PayPal form to be visible
        self.wait.until(EC.presence_of_element_located(self.PAYPAL_EMAIL))
    
    def fill_paypal_email(self, email):
        """Fill in PayPal email"""
        logger.info(f"Filling PayPal email: {email}")
        email_input = self.wait.until(EC.element_to_be_clickable(self.PAYPAL_EMAIL))
        email_input.clear()
        email_input.send_keys(email)
    
    def submit_payment(self):
        """Submit the payment"""
        logger.info("Submitting payment")
        pay_button = self.wait.until(EC.element_to_be_clickable(self.PAY_NOW_BUTTON))
        pay_button.click()
        
        # Wait for payment form to be submitted
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "form[aria-labelledby='payment-form-title']")))
        
        # Check for success states with a single wait
        try:
            # First check for success overlay
            success_overlay = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Checkout_successOverlay__6TzsH")))
            if success_overlay.is_displayed():
                success_text = self.driver.find_element(By.CSS_SELECTOR, ".Checkout_successText__IEOTx")
                return success_text.text == "Payment Successful!"
        except:
            # If overlay not found, check for success page
            try:
                success_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".successCard")))
                return success_message.is_displayed()
            except:
                # Final fallback: Check page source
                return "Payment Successful!" in self.driver.page_source
    
    def place_order(self):
        """Click the place order button"""
        logger.info("Placing order")
        place_order_button = self.wait.until(EC.element_to_be_clickable(self.PAY_NOW_BUTTON))
        place_order_button.click()
    
    def verify_order_success(self):
        """Verify if order was placed successfully"""
        try:
            # Wait for the payment form to be submitted
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "form[aria-labelledby='payment-form-title']")))
            
            # Check for success states with a single wait
            try:
                # First check for success overlay
                success_overlay = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Checkout_successOverlay__6TzsH")))
                if success_overlay.is_displayed():
                    success_text = self.driver.find_element(By.CSS_SELECTOR, ".Checkout_successText__IEOTx")
                    return success_text.text == "Payment Successful!"
            except:
                # If overlay not found, check for success page
                try:
                    success_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".successCard")))
                    return success_message.is_displayed()
                except:
                    # Final fallback: Check page source
                    return "Payment Successful!" in self.driver.page_source
        except Exception as e:
            logger.error(f"Error verifying order success: {str(e)}")
            return False 