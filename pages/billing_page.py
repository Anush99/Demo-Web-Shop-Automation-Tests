from playwright.sync_api import Page
from locators import BillingPageLocators


class BillingPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_billing_form(self, first_name, last_name, email, city, address, zip, phone):
        self.page.fill(BillingPageLocators.first_name, first_name)
        self.page.fill(BillingPageLocators.last_name, last_name)
        self.page.fill(BillingPageLocators.email, email)
        self.page.fill(BillingPageLocators.address, address)
        self.page.fill(BillingPageLocators.zip, zip)
        self.page.fill(BillingPageLocators.phone_number, phone)
        self.page.fill(BillingPageLocators.city, city)

    def select_country(self, country_name):
        self.page.click(BillingPageLocators.country_dropdown)
        self.page.select_option(BillingPageLocators.country_id, country_name)

    def click_continue(self):
        self.page.click(BillingPageLocators.continue_button)

    def click_continue_billing(self):
        self.page.click(BillingPageLocators.continue_billing_button)

    def click_continue_shipping(self):
        self.page.click(BillingPageLocators.shipping_continue_button)

    def click_continue_payment(self):
        self.page.click(BillingPageLocators.payment_continue_button)

    def click_continue_payment_info(self):
        self.page.click(BillingPageLocators.payment_info_continue_button)

    def confirm_order(self):
        self.page.click(BillingPageLocators.confirm_order)

    def get_registration_conf_text(self):
        element = self.page.locator(BillingPageLocators.confirmation_text)
        conf_text = element.text_content()
        return conf_text
