import pytest
from playwright.sync_api import expect
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce")
])
def test_add_all_items_to_cart(page, username, password):
    # Step 1: Login
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    # Step 2: Validate landing page
    inventory = InventoryPage(page)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory.page_title).to_have_text("Products")

    # Step 3: Add all items to cart
    inventory.add_all_items_to_cart()

    # Step 4: Assert number of items in cart badge
    count = inventory.add_to_cart_buttons.count()
    expect(inventory.cart_badge).to_have_text(str(count))
