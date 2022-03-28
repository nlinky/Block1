from .base_page import BasePage
from .locators import LoginPageLocators


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
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login button is not presented'

    def should_be_register_form_new_user(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BLOCK), 'Register block is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_ON_PAGE_LOGIN), 'Register button on page ' \
                                                                                          'login is not presented '

    def go_to_register_page_with_login_page(self):
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_ON_PAGE_LOGIN)
        button_register.click()
