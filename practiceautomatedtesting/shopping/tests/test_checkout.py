import pytest
from pages.shopping_page import ShoppingPage
from pages.checkout_page import CheckoutPage
import logging

logger = logging.getLogger(__name__)

class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.shopping_page = ShoppingPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.shopping_page.navigate()
    
    def test_paypal_checkout(self, driver):
        """Test checkout using PayPal payment method"""
        # Add Bluetooth Headphones to cart
        self.shopping_page.add_product_to_cart_by_aria("Bluetooth Headphones")
        
        # Go to cart
        self.shopping_page.go_to_cart()
        
        # Select PayPal as payment method
        self.checkout_page.select_paypal()
        
        # Fill PayPal email
        self.checkout_page.fill_paypal_email("test@gmail.com")
        
        # Submit payment
        self.checkout_page.submit_payment()
        
        # Verify order success
        assert self.checkout_page.verify_order_success(), "Order was not placed successfully"
    
    def test_add_items_and_checkout(self, driver):
        """Test adding items to cart and completing checkout"""
        # Sort products by price
        self.shopping_page.sort_by_price()
        
        # Set price range
        self.shopping_page.set_price_range(0, 100)
        
        # Add items to cart with debugging
        print("\nAttempting to add first item...")
        first_item_added = self.shopping_page.add_product_to_cart("Bluetooth Headphones")
        assert first_item_added, "Failed to add first item to cart"
        print("First item added successfully")
        
        print("\nAttempting to add second item...")
        second_item_added = self.shopping_page.add_product_to_cart("Desk Lamp")
        assert second_item_added, "Failed to add second item to cart"
        print("Second item added successfully")
        
        # Go to checkout
        print("\nNavigating to cart...")
        self.shopping_page.go_to_cart()
        
        # Take screenshot for debugging
        driver.save_screenshot("cart_debug.png")
        print("Screenshot saved as cart_debug.png")
        
        # Print page source for debugging
        print("\nCurrent page source:")
        print(driver.page_source)
        
        # Verify items in cart
        cart_items = self.checkout_page.get_cart_items()
        print(f"\nFound {len(cart_items)} items in cart")
        assert len(cart_items) == 2, f"Expected 2 items in cart, but found {len(cart_items)}"
        
        # Remove second item
        self.checkout_page.remove_item(1)
        cart_items = self.checkout_page.get_cart_items()
        assert len(cart_items) == 1, "Item not removed from cart"
        
        # Fill payment information
        self.checkout_page.fill_payment_info(
            card_number="4111111111111111",
            expiry_date="12/25",
            cvv="123",
            card_name="John Doe"
        )
        
        # Place order
        self.checkout_page.place_order()
        
        # Verify order success
        assert self.checkout_page.verify_order_success(), "Order was not placed successfully"
    
    def test_empty_cart_checkout(self, driver):
        """Test attempting checkout with empty cart"""
        self.checkout_page.navigate()
        
        # Verify no items in cart
        cart_items = self.checkout_page.get_cart_items()
        assert len(cart_items) == 0, "Your cart is empty"
        
        # Verify totals
        assert self.checkout_page.get_subtotal() == 0.0, "Subtotal should be 0"
        assert self.checkout_page.get_tax() == 0.0, "Tax should be 0"
        assert self.checkout_page.get_total() == 0.0, "Total should be 0" 