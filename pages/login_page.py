from .base_page import BasePage
from .locators import LoginPageLocators
from ..test_data.user import TestUserLogin


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login is not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Email field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Password field is not presented'
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_CHECKBOX), 'Remember me checkbox is not presented'
        assert self.is_element_present(*LoginPageLocators.FORGET_PASSWORD_LINK), 'Forget password link is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login button is not presented'

    def should_be_register_form_new_user(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BLOCK), 'Register block is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_ON_PAGE_LOGIN), 'Register button on page ' \
                                                                                          'login is not presented '

    def go_to_register_page_with_login_page(self):
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_PAGE_LOGIN)
        button_register.click()

    def filling_login_form(self, user: TestUserLogin):
        input_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        input_email.send_keys(user.email)
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        input_password.send_keys(user.password)

    def checkbox_remember_me(self):
        checkbox_remember_me = self.browser.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)
        checkbox_remember_me.click()

    def user_authorization(self):
        button_login = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        button_login.click()

    def message_error(self):
        message_error = self.browser.find_element(*LoginPageLocators.MESSAGE_ERROR)
        assert message_error.text == 'Login was unsuccessful. Please correct the errors and try again.', 'No error message when not filling in all or any fields'

