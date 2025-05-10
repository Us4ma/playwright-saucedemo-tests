import pytest
from playwright.sync_api import expect
from Pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, should_succeed", [
    ("standard_user", "secret_sauce", True),        # ✅ Valid user
    ("locked_out_user", "secret_sauce", False),     # ❌ Locked out
    ("problem_user", "wrong_pass", False),          # ❌ Wrong password
])
def test_login_flow(page, username, password, should_succeed):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    if should_succeed:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(login.error_message).to_be_visible()

