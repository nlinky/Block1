import pytest, time


from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://demowebshop.tricentis.com/"


class TestLoginFromMainPage:
    # проверка login в урле, наличия ссылки на авторизацию, наличие формы авторизации со всеми полями
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestAuthorizationUser:
    def test_authorization_user_without_checkbox(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = 'ttest@test.test'
        password = '123456'
        page.filling_login_form(email, password)
        page.user_authorization()
        page.should_be_authorized_user()
        time.sleep(3)

    def test_authorization_user_with_checkbox(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = 'ttest@test.test'
        password = '123456'
        page.filling_login_form(email, password)
        page.checkbox_remember_me()
        page.user_authorization()
        page.should_be_authorized_user()
        time.sleep(3)


# class TestErrorMessage:
#     # проверка сообщений об ошибке при не заполнении полей
#     def test_user_should_see_warning_if_fields_are_not_filled(self, browser):
#         page = LoginPage(browser, link)
#         page.open()
#         page.go_to_login_page()
#         page.user_authorization()
#         page.is_all_fields_has_error_class()