from .base_page import BasePage
from .locators import ChangePasswordPageLocators
from ..test_data.user import TestUserLogin


class ChangePasswordPage(BasePage):
    def go_to_change_password_page(self):
        change_password_link = self.browser.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_LINK)
        change_password_link.click()

    def should_be_change_password_page(self):
        self.should_be_change_password_url()
        self.should_be_change_password_form()

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

    def filling_change_password_form(self, user:TestUserLogin, new_password):
        input_old_password = self.browser.find_element(*ChangePasswordPageLocators.OLD_PASSWORD)
        input_old_password.send_keys(user.password)
        input_new_password = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD)
        input_new_password.send_keys(new_password)
        input_confirm_password = self.browser.find_element(*ChangePasswordPageLocators.CONFIRM_PASSWORD)
        input_confirm_password.send_keys(new_password)

    def change_password_button(self):
        button_change_password = self.browser.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON)
        button_change_password.click()

    def should_be_success_message_change_password(self):
        message_change_password = self.browser.find_element(*ChangePasswordPageLocators.RESULT_MESSAGE)
        assert message_change_password.text == 'Password was changed', "There is no message about password change"
