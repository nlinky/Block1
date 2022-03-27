from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert 'register' in self.browser.current_url, 'register is not in url'

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), 'Register form is not presented'

    def filling_registration_form(self, first_name, last_name, email, password):
        input_first_name = self.browser.find_element(*RegisterPageLocators.REGISTER_FIRST_NAME)
        input_first_name.send_keys(first_name)
        input_last_name = self.browser.find_element(*RegisterPageLocators.REGISTER_LAST_NAME)
        input_last_name.send_keys(last_name)
        input_email = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        input_password.send_keys(password)
        input_password_confirm = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD_CONFIRM)
        input_password_confirm.send_keys(password)

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





