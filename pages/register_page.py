from .base_page import BasePage
from .locators import RegisterPageLocators
from ..test_data.user import TestUserRegister


class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert 'register' in self.browser.current_url, 'register is not in url'

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), 'Register form is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_GENDER_MALE_RADIO), 'Gender male radio button is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_GENDER_FEMALE_RADIO), 'Gender female radio button is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FIRST_NAME), 'First name field is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_LAST_NAME), 'Last name field is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_EMAIL), 'Email field is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_PASSWORD), 'Password field is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM), 'Confirm password field is not presented'
        assert self.is_element_present(*RegisterPageLocators.REGISTER_BUTTON), 'Register button is not presented'

    def is_all_fields_has_error_class(self):
        self.is_first_name_field_has_error_class()
        self.is_last_name_field_has_error_class()
        self.is_email_field_has_error_class()
        self.is_password_field_has_error_class()
        self.is_confirm_password_field_has_error_class()

    def is_first_name_field_has_error_class(self):
        first_name_input_field = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        assert 'error' in first_name_input_field.get_attribute("class"), "The First Name field has no Error class"

    def is_last_name_field_has_error_class(self):
        last_name_input_field = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        assert 'error' in last_name_input_field.get_attribute("class"), "The Last Name field has no Error class"

    def is_email_field_has_error_class(self):
        email_input_field = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        assert 'error' in email_input_field.get_attribute("class"), "The Email field has no Error class"

    def is_password_field_has_error_class(self):
        password_input_field = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        assert 'error' in password_input_field.get_attribute("class"), "The Password field has no Error class"

    def is_confirm_password_field_has_error_class(self):
        confirm_password_input_field = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM)
        assert 'error' in confirm_password_input_field.get_attribute("class"), "The Confirm password field has no " \
                                                                               "Error class "

    def filling_registration_form(self, user: TestUserRegister):
        self.filling_first_name_field(user.first_name)
        self.filling_last_name_field(user.last_name)
        self.filling_email_field(user.email)
        self.filling_password_field(user.password)
        self.filling_password_confirm_field(user.password)

    def filling_first_name_field(self, value):
        input_first_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        input_first_name.send_keys(value)

    def filling_last_name_field(self, value):
        input_last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        input_last_name.send_keys(value)

    def filling_email_field(self, value):
        input_email = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_email.send_keys(value)

    def filling_password_field(self, value):
        input_password = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(value)

    def filling_password_confirm_field(self, value):
        input_password_confirm = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM)
        input_password_confirm.send_keys(value)

    def gender(self, gender):
        choose_gender_male = self.browser.find_element(*RegisterPageLocators.REGISTER_GENDER_MALE_RADIO)
        choose_gender_female = self.browser.find_element(*RegisterPageLocators.REGISTER_GENDER_FEMALE_RADIO)

        if gender == 'female':
            return choose_gender_female.click()
        else:
            return choose_gender_male.click()

    def register_new_user(self):
        button_register = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        button_register.click()

    def should_be_success_message_registration(self):
        message_registration = self.browser.find_element(*RegisterPageLocators.SUCCESS_MESSAGE_REGISTRATION)
        assert message_registration.text == 'Your registration completed', "There is no message about registration " \
                                                                           "completion "







