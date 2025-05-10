import pytest
from playwright.sync_api import expect
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
])
def test_complete_checkout_flow(page, username, password):
    # Step 1: Login
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    # Step 2: Add to cart
    inventory = InventoryPage(page)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory.add_all_items_to_cart()
    inventory.cart_icon.click()

    # Step 3: Cart
    cart = CartPage(page)
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # Step 4: Checkout
    checkout = CheckoutPage(page)
    checkout.start_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    checkout.fill_customer_info("Usama", "Qamar", "46000")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    checkout.complete_order()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    # Final Assertion
    assert checkout.get_success_message() == "Thank you for your order!"
