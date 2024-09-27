from playwright.sync_api import Page
from locators import SearchPageLocators


class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def get_result_list_titles(self):
        item_boxes = self.page.locator(SearchPageLocators.search_result_list)
        self.page.wait_for_selector(SearchPageLocators.search_result_list)
        titles = []

        for i in range(item_boxes.count()):
            title = item_boxes.nth(i).locator(SearchPageLocators.product_title).inner_text()
            titles.append(title)

        return titles

    def get_result_list_items(self):
        self.page.wait_for_selector(SearchPageLocators.search_result_list)
        item_boxes = self.page.locator(SearchPageLocators.search_result_list)
        items = []
        for i in range(item_boxes.count()):
            item = item_boxes.nth(i)
            items.append(item)
        return items

    def add_item_to_card(self, item):
        button = item.locator(SearchPageLocators.add_to_card_button)
        button.click()

