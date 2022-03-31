import pytest, time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .test_data.user import UserLogin
from .pages.customer_page import CustomerPage

link = "http://demowebshop.tricentis.com/"


@pytest.mark.smoke
class TestChangePasswordFromMainPage:
    # проверка changepassword в урле, наличие формы смены пароля со всеми полями
    def test_user_can_go_to_change_password_page(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form(UserLogin)
        page.user_authorization()
        page.go_to_customer_page()
        customer_page = CustomerPage(browser, browser.current_url)
        customer_page.go_to_change_password_page()
        customer_page.should_be_change_password_page()


class TestUserChangePassword:
    @pytest.mark.smoke
    def test_user_can_change_password(self, browser):
        # проверка смена пароля и сообщения об успехе
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form(UserLogin)
        page.user_authorization()
        page.go_to_customer_page()
        customer_page = CustomerPage(browser, browser.current_url)
        customer_page.go_to_change_password_page()
        new_password = '123456'
        customer_page.filling_change_password_form(UserLogin, new_password)
        customer_page.change_password_button()
        customer_page.should_be_success_message_change_password()
