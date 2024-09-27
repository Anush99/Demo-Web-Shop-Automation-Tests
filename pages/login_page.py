import time

from playwright.sync_api import Page
from locators import LoginLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_login_form(self, email, password):
        self.page.fill(LoginLocators.email, email)
        self.page.fill(LoginLocators.password, password)
        self.page.click(LoginLocators.login_button)
