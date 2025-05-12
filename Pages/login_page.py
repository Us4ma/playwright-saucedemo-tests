from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def login_with_empty_fields(self):
        self.click(self.login_button)

    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()

