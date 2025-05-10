from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")  # 👈 Add this
        self.add_to_cart_buttons = page.locator("button.btn_inventory")

    def get_title_text(self):
        return self.page_title.inner_text()

    def add_all_items_to_cart(self):
        count = self.add_to_cart_buttons.count()
        for i in range(count):
            self.add_to_cart_buttons.nth(i).click()

