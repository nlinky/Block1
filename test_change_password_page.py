import pytest, time

from .pages.login_page import LoginPage
from .test_data.user import UserLogin
from .pages.change_password_page import ChangePasswordPage

link = "http://demowebshop.tricentis.com/"


class TestUserChangePassword:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form(UserLogin)
        page.user_authorization()

    @pytest.mark.smoke
    def test_user_can_go_to_change_password_page(self, browser):
        # проверка changepassword в урле, наличие формы смены пароля со всеми полями
        customer_page = ChangePasswordPage(browser, link)
        customer_page.open()
        customer_page.go_to_customer_page()
        customer_page = ChangePasswordPage(browser, browser.current_url)
        customer_page.go_to_change_password_page()
        customer_page.should_be_change_password_page()

    @pytest.mark.smoke
    def test_user_can_change_password(self, browser):
        # проверка смена пароля и сообщения об успехе
        customer_page = ChangePasswordPage(browser, link)
        customer_page.open()
        customer_page.go_to_customer_page()
        customer_page.go_to_change_password_page()
        new_password = '123456'
        customer_page.filling_change_password_form(UserLogin.password, new_password, new_password)
        customer_page.change_password_button()
        customer_page.should_be_success_message_change_password()

    def test_user_should_see_warning_if_field_old_password_is_invalid(self, browser):
        # проверка сообщения об ошибке при вводе неправильного старого пароля
        customer_page = ChangePasswordPage(browser, link)
        customer_page.open()
        customer_page.go_to_customer_page()
        customer_page.go_to_change_password_page()
        old_password = '12345'
        customer_page.filling_change_password_form(old_password, UserLogin.password, UserLogin.password)
        customer_page.change_password_button()
        customer_page.should_be_error_message_old_password()
