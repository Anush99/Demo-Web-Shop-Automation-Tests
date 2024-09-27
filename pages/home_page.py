from playwright.sync_api import Page
from locators import HomepageLocators
import data


class Homepage:
    def __init__(self, page: Page):
        self.page = page

    def open_homepage(self):
        self.page.goto(data.website_url, wait_until="load")

    def click_register_button(self):
        self.page.click(HomepageLocators.register_button)

    def click_login_button(self):
        self.page.click(HomepageLocators.login_button)

    def get_user_email(self):
        email = self.page.locator(HomepageLocators.email_on_header)
        email_text = email.text_content()
        return email_text

    def search(self, product):
        self.page.fill(HomepageLocators.search_field, product)
        self.page.click(HomepageLocators.search_button)

    def open_shopping_card(self):
        self.page.click(HomepageLocators.shopping_card_link)
