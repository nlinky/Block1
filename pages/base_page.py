from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_register_page(self):
        register_link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        register_link.click()

    def should_be_register_link(self):
        assert self.is_element_present(*BasePageLocators.REGISTER_LINK), "Register link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOG_IN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOG_IN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        # account_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        # assert account_link.text == 'ttest@test.test', 'Account link is not presented," \
        #                                                              " probably unauthorised user"'
        assert self.browser.find_element(*BasePageLocators.LOG_OUT_LINK), "Log out link is not presented," \
                                                                     " probably unauthorised user"

    def go_to_customer_page(self):
        customer_link = self.browser.find_element(*BasePageLocators.ACCOUNT_LINK)
        customer_link.click()

    def should_be_customer_link(self):
        assert self.is_element_present(*BasePageLocators.ACCOUNT_LINK), "Account link is not presented"



