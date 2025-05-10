from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")  # usually says "Your Cart"
        self.cart_items = page.locator(".cart_item")  # all added products

    def get_title_text(self):
        return self.page_title.inner_text()

    def get_cart_items_count(self):
        return self.cart_items.count()
