import pytest, time


from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .test_data.user import UserLogin, UserLoginInvalid

link = "http://demowebshop.tricentis.com/"


@pytest.mark.smoke
class TestLoginFromMainPage:
    # проверка login в урле, наличия ссылки на авторизацию, наличие формы авторизации со всеми полями
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.smoke
class TestAuthorizationUser:
    # авторизация без галочки чекбокса (вал емайл, вал пароль)
    def test_authorization_user_without_checkbox(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form()
        page.user_authorization()
        page.should_be_authorized_user()

    # авторизация с галочкой чекбокса (вал емайл, вал пароль)
    def test_authorization_user_with_checkbox(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form()
        page.checkbox_remember_me()
        page.user_authorization()
        page.should_be_authorized_user()


@pytest.mark.error
class TestErrorMessage:
    # проверка сообщения об ошибке при не заполнении всех полей или любого одного из полей (пустой емайл и/или пустой пароль)
    def test_user_should_see_warning_if_fields_are_not_filled(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.user_authorization()
        page.message_error_empty_fields()
        time.sleep(3)

    # проверка сообщения об ошибке при не заполнении поля емайл (пустой емайл, вал пароль)
    def test_user_should_see_warning_if_field_email_is_not_filled(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_password_field(UserLogin)
        page.user_authorization()
        page.message_error_account_empty()

    # проверка сообщения об ошибке при не заполнении поля пароля (вал емайл, пустой пароль)
    def test_user_should_see_warning_if_field_password_is_not_filled(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_email_field(UserLogin)
        page.user_authorization()
        page.message_error_password_empty()

    # проверка сообщения об ошибке при заполнении всех полей невалидными данными (невал емайл и невал пароль)
    def test_user_should_see_warning_if_fields_are_invalid(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form(UserLoginInvalid)
        page.user_authorization()
        page.message_error_invalid_fields()
        time.sleep(3)

    # проверка сообщения об ошибке при заполнении поля емайл невалидными данными(невал емайл, вал пароль)
    def test_user_should_see_warning_if_field_email_is_invalid(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_email_field(UserLoginInvalid)
        page.filling_password_field(UserLogin)
        page.user_authorization()
        page.message_error_invalid_email()

    # проверка сообщения об ошибке при заполнении поля пароля невалидными данными(вал емайл, невал пароль)
    def test_user_should_see_warning_if_field_password_is_invalid(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_email_field(UserLogin)
        page.filling_password_field(UserLoginInvalid)
        page.user_authorization()
        page.message_error_invalid_password()
