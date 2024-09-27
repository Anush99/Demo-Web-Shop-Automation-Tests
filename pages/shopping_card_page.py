from playwright.sync_api import Page
from locators import ShoppingCardLocators


class ShoppingCardPage:
    def __init__(self, page: Page):
        self.page = page

    def get_product_names(self):
        self.page.wait_for_selector(ShoppingCardLocators.card)

        product_names = []
        item_boxes = self.page.locator(ShoppingCardLocators.card)

        for i in range(item_boxes.count()):
            product_name = item_boxes.nth(i).locator(ShoppingCardLocators.product_name).inner_text()
            product_names.append(product_name)

        return product_names

    def click_checkout(self):
        self.page.click(ShoppingCardLocators.checkout_button)

    def click_tos(self):
        self.page.click(ShoppingCardLocators.tos_checkbox)
