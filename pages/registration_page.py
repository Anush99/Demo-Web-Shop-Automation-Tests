from playwright.sync_api import Page
from locators import RegistrationPageLocators


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def select_gender_male(self):
        self.page.click(RegistrationPageLocators.gender_male)

    def select_gender_female(self):
        self.page.click(RegistrationPageLocators.gender_female)

    def fill_registration_form(self, first_name, last_name, email, password, confirm_password):
        self.page.fill(RegistrationPageLocators.first_name, first_name)
        self.page.fill(RegistrationPageLocators.last_name, last_name)
        self.page.fill(RegistrationPageLocators.email, email)
        self.page.fill(RegistrationPageLocators.password, password)
        self.page.fill(RegistrationPageLocators.confirm_password, confirm_password)
        self.page.click(RegistrationPageLocators.register_button)

    def get_registration_conf_text(self):
        element = self.page.locator(RegistrationPageLocators.register_confirmation)
        conf_text = element.text_content()
        return conf_text


