import pytest
import allure
from pages.shopping_page import ShoppingPage
from pages.checkout_page import CheckoutPage
import logging

logger = logging.getLogger(__name__)

@allure.epic("Shopping Cart")
@allure.feature("Checkout Process")
class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.shopping_page = ShoppingPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.shopping_page.navigate()
    
    @allure.story("PayPal Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_paypal_checkout(self, driver):
        """Test checkout using PayPal payment method"""
        with allure.step("Add Bluetooth Headphones to cart"):
            self.shopping_page.add_product_to_cart_by_aria("Bluetooth Headphones")
        
        with allure.step("Navigate to cart"):
            self.shopping_page.go_to_cart()
        
        with allure.step("Select PayPal payment method"):
            self.checkout_page.select_paypal()
        
        with allure.step("Fill PayPal email"):
            self.checkout_page.fill_paypal_email("test@gmail.com")
        
        with allure.step("Submit payment"):
            self.checkout_page.submit_payment()
        
        with allure.step("Verify order success"):
            assert self.checkout_page.verify_order_success(), "Order was not placed successfully"
    
    @allure.story("Standard Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_items_and_checkout(self, driver):
        """Test adding items to cart and completing checkout"""
        with allure.step("Sort products and set price range"):
            self.shopping_page.sort_by_price()
            self.shopping_page.set_price_range(0, 100)
        
        with allure.step("Add items to cart"):
            first_item_added = self.shopping_page.add_product_to_cart("Bluetooth Headphones")
            assert first_item_added, "Failed to add first item to cart"
            
            second_item_added = self.shopping_page.add_product_to_cart("Desk Lamp")
            assert second_item_added, "Failed to add second item to cart"
        
        with allure.step("Navigate to cart"):
            self.shopping_page.go_to_cart()
        
        with allure.step("Verify cart items"):
            cart_items = self.checkout_page.get_cart_items()
            assert len(cart_items) == 2, f"Expected 2 items in cart, but found {len(cart_items)}"
        
        with allure.step("Remove second item"):
            self.checkout_page.remove_item(1)
            cart_items = self.checkout_page.get_cart_items()
            assert len(cart_items) == 1, "Item not removed from cart"
        
        with allure.step("Fill payment information"):
            self.checkout_page.fill_payment_info(
                card_number="4111111111111111",
                expiry_date="12/25",
                cvv="123",
                card_name="John Doe"
            )
        
        with allure.step("Place order"):
            self.checkout_page.place_order()
        
        with allure.step("Verify order success"):
            assert self.checkout_page.verify_order_success(), "Order was not placed successfully"
    
    @allure.story("Empty Cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_cart_checkout(self, driver):
        """Test attempting checkout with empty cart"""
        with allure.step("Navigate to checkout"):
            self.checkout_page.navigate()
        
        with allure.step("Verify empty cart"):
            cart_items = self.checkout_page.get_cart_items()
            assert len(cart_items) == 0, "Your cart is empty"
        
        with allure.step("Verify totals"):
            assert self.checkout_page.get_subtotal() == 0.0, "Subtotal should be 0"
            assert self.checkout_page.get_tax() == 0.0, "Tax should be 0"
            assert self.checkout_page.get_total() == 0.0, "Total should be 0" 