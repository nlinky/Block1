from .base_page import BasePage
from .locators import ChangePasswordPageLocators


class ChangePasswordPage(BasePage):
    def should_be_change_password_url(self):
        assert 'changepassword' in self.browser.current_url, 'changepassword is not in url'

    def should_be_change_password_form(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_FORM), 'Change password form is ' \
                                                                                          'not presented '
        assert self.is_element_present(*ChangePasswordPageLocators.OLD_PASSWORD), 'Old password field is not presented'
        assert self.is_element_present(*ChangePasswordPageLocators.NEW_PASSWORD), 'New password field is not presented'
        assert self.is_element_present(*ChangePasswordPageLocators.CONFIRM_PASSWORD), 'Confirm password field is not ' \
                                                                                      'presented '
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON), 'Change password button ' \
                                                                                            'is not presented '
