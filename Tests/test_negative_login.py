import pytest
from Pages.login_page import LoginPage

def test_login_with_empty_fields(page):
    login = LoginPage(page)
    login.navigate()
    login.login_with_empty_fields()
    assert "Username is required" in login.get_error_message()
