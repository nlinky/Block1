from .base_page import BasePage
from .locators import CheckoutPageLocators
from selenium.webdriver.support.ui import Select
from ..test_data.address import TestBillingAddress
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    def should_be_billing_address_form_required_fields(self):
        assert self.is_element_present(*CheckoutPageLocators.FIELD_FIRST_NAME), 'First name field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_LAST_NAME), 'Last name field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_EMAIL), 'Email field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.DROP_DOWN_COUNTRY), 'Country drop-down is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_CITY), 'City field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_ADDRESS_1), 'Address 1 field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_ZIP), 'Zip field is not presented'
        assert self.is_element_present(*CheckoutPageLocators.FIELD_PHONE_NUMBER), 'Phone number field is not presented'

    def filling_country_field(self):
        select = Select(self.browser.find_element(*CheckoutPageLocators.DROP_DOWN_COUNTRY))
        select.select_by_visible_text("Russia")

    def filling_city_field(self, value):
        input_city = self.browser.find_element(*CheckoutPageLocators.FIELD_CITY)
        input_city.send_keys(value)

    def filling_address1_field(self, value):
        input_address1 = self.browser.find_element(*CheckoutPageLocators.FIELD_ADDRESS_1)
        input_address1.send_keys(value)

    def filling_zip_field(self, value):
        input_zip = self.browser.find_element(*CheckoutPageLocators.FIELD_ZIP)
        input_zip.send_keys(value)

    def filling_phone_number_field(self, value):
        input_phone_number = self.browser.find_element(*CheckoutPageLocators.FIELD_PHONE_NUMBER)
        input_phone_number.send_keys(value)

    def button_continue_billing_address(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONTINUE_BILLING_ADDRESS)
        button_continue.click()

    def button_continue_shipping_address(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONTINUE_SHIPPING_ADDRESS)
        button_continue.click()

    def button_continue_shipping_method(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONTINUE_SHIPPING_METHOD)
        button_continue.click()

    def button_continue_payment_method(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONTINUE_PAYMENT_METHOD)
        button_continue.click()

    def button_continue_payment_information(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONTINUE_PAYMENT_INFORMATION)
        button_continue.click()

    def button_confirm_order(self):
        button_continue = self.browser.find_element(*CheckoutPageLocators.BUTTON_CONFIRM_ORDER)
        button_continue.click()

    def should_be_section_order_completed(self):
        self.browser.find_element(
            *CheckoutPageLocators.SECTION_ORDER_COMPLETED), 'There is no section that the order is completed'

    def filling_billing_address_form_required_fields(self, address: TestBillingAddress):
        self.filling_country_field()
        self.filling_city_field(address.city)
        self.filling_address1_field(address.address1)
        self.filling_zip_field(address.zip)
        self.filling_phone_number_field(address.phone)
        self.button_continue_billing_address()


