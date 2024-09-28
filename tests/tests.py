import time
import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import Homepage
from pages.registration_page import RegistrationPage
from pages.search_page import SearchPage
from pages.shopping_card_page import ShoppingCardPage
from pages.login_page import LoginPage
from pages.billing_page import BillingPage
import data

password = data.password

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


def test_user_registration(browser):
    """Verify that a new user can register successfully.
    """
    page = browser.new_page()
    home_page = Homepage(page)
    registration_page = RegistrationPage(page)
    home_page.open_homepage()
    home_page.click_register_button()
    registration_page.select_gender_female()
    data.create_random_email()
    email = data.get_random_email()
    registration_page.fill_registration_form('Test', 'Test', email, password, password)

    confirmation_text = registration_page.get_registration_conf_text()
    expected_url = f'{data.website_url}/registerresult/1'
    user_email_on_header = home_page.get_user_email()
    current_url = page.url
    assert confirmation_text == '\n            Your registration completed\n        '
    assert current_url == expected_url
    assert user_email_on_header == email
    page.close()


def test_product_search_and_navigation(browser):
    """Verify that searching for a product displays relevant results.
    """
    page = browser.new_page()
    home_page = Homepage(page)
    home_page.open_homepage()
    home_page.search("Laptop")
    search_page = SearchPage(page)

    result_list = search_page.get_result_list_titles()

    for title in result_list:
        assert "Laptop" in title, f"Title '{title}' does not contain 'Laptop'"


def test_add_to_card(browser):
    """Verify that a user can add a product to the shopping cart."""
    page = browser.new_page()
    home_page = Homepage(page)
    home_page.open_homepage()
    home_page.click_login_button()
    login_page = LoginPage(page)
    email = data.get_random_email()
    login_page.fill_login_form(email, password)
    home_page.search("Laptop")
    search_page = SearchPage(page)
    card_page = ShoppingCardPage(page)

    result_list = search_page.get_result_list_items()
    first_result = result_list[0]
    search_page.add_item_to_card(first_result)
    home_page.open_shopping_card()
    card_items = card_page.get_product_names()
    assert any("Laptop" in title for title in card_items), f"Expected 'Laptop' in {card_items}"


def test_checkout(browser):
    """Verify that a user can complete the checkout process."""
    page = browser.new_page()
    home_page = Homepage(page)
    home_page.open_homepage()
    home_page.click_login_button()
    login_page = LoginPage(page)
    email = data.get_random_email()
    login_page.fill_login_form(email, password)
    home_page.search("Laptop")
    search_page = SearchPage(page)
    card_page = ShoppingCardPage(page)
    result_list = search_page.get_result_list_items()
    first_result = result_list[0]
    search_page.add_item_to_card(first_result)
    home_page.open_shopping_card()
    card_page.click_tos()
    card_page.click_checkout()

    billing_page = BillingPage(page)
    billing_page.fill_billing_form("name", "last name", email, "city", "address 1", "001", "+1234566")
    billing_page.select_country("United States")
    billing_page.click_continue()
    billing_page.click_continue_billing()
    billing_page.click_continue_shipping()
    billing_page.click_continue_payment()
    billing_page.click_continue_payment_info()
    billing_page.confirm_order()

    confirmation_text = billing_page.get_registration_conf_text()
    assert confirmation_text == 'Your order has been successfully processed!'


