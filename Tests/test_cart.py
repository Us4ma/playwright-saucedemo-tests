import pytest
from playwright.sync_api import expect
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
])
def test_cart_items_listed(page, username, password):
    # Step 1: Login
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    # Step 2: Add items to cart
    inventory = InventoryPage(page)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory.add_all_items_to_cart()
    count = inventory.add_to_cart_buttons.count()

    # Step 3: Go to Cart Page
    inventory.cart_icon.click()
    cart = CartPage(page)

    # Step 4: Validate
    # Step 4: Validate
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    assert cart.get_cart_items_count() == count
    assert cart.get_title_text() == "Your Cart"


