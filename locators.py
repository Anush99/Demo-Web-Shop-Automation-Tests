class HomepageLocators:
    register_button = '[class="ico-register"]'
    login_button = '[class="ico-login"]'
    search_field = '[class="search-box-text ui-autocomplete-input"]'
    search_button = '[class="button-1 search-box-button"]'
    email_on_header = '[class="header-links"] [href="/customer/info"]'
    logout_button = '[class="ico-logout"]'
    shopping_card_link = '[class="ico-cart"]'

class RegistrationPageLocators:
    gender_female = '[id="gender-female"]'
    gender_male = '[id="gender-male"]'
    first_name = '[id="FirstName"]'
    last_name = '[id="LastName"]'
    email = '[id="Email"]'
    password = '[id="Password"]'
    confirm_password = '[id="ConfirmPassword"]'
    register_button = '[id="register-button"]'
    register_confirmation = '[class="result"]'


class LoginLocators:
    email = '[id="Email"]'
    password = '[id="Password"]'
    login_button = '[class="button-1 login-button"]'


class SearchPageLocators:
    search_result_list = '[class="item-box"]'
    product_title = '[class="product-title"] a'
    product_item = '[class="product-item"]'
    add_to_card_button = '[class="prices"]+[class="buttons"] input'

class ProductPageLocators:
    add_to_card_button = '[id="add-to-cart-button-31"]'
    product_details = '[id="product-details-form"]'
    product_price = '[class="price-value-31"]'


class ShoppingCardLocators:
    card = '[class="cart-item-row"]'
    product_name = '[class="product"] a[class="product-name"]'
    tos_checkbox = '[id="termsofservice"]'
    checkout_button = '[id="checkout"]'


class BillingPageLocators:
    first_name = '[id="BillingNewAddress_FirstName"]'
    last_name = '[id="BillingNewAddress_LastName"]'
    email = '[id="BillingNewAddress_Email"]'
    country_dropdown = '[id="BillingNewAddress_CountryId"]'
    city = '[name="BillingNewAddress.City"]'
    address = '[id="BillingNewAddress_Address1"]'
    zip = '[id="BillingNewAddress_ZipPostalCode"]'
    phone_number = '[id="BillingNewAddress_PhoneNumber"]'
    continue_button = '[title="Continue"][onclick="Billing.save()"]'
    continue_billing_button = '[title="Continue"][onclick="Shipping.save()"]'
    shipping_continue_button = '[onclick="ShippingMethod.save()"]'
    payment_continue_button = '[onclick="PaymentMethod.save()"]'
    country_id = '#BillingNewAddress_CountryId'
    payment_info_continue_button = '[onclick="PaymentInfo.save()"]'
    confirm_order = '[onclick="ConfirmOrder.save()"]'
    confirmation_text = '[class="section order-completed"] strong'





