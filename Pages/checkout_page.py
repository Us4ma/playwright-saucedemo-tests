from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def start_checkout(self):
        self.checkout_button.click()

    def fill_customer_info(self, first, last, zip_code):
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.postal_code_input.fill(zip_code)
        self.continue_button.click()

    def complete_order(self):
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.inner_text()
