import pytest, time, names


from .pages.register_page import RegisterPage
from .pages.main_page import MainPage

link = "http://demowebshop.tricentis.com/"


class TestRegisterFromMainPage:
    # проверка register в урле, проверка наличия формы регистрации
    def test_guest_can_go_to_register_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_register_page()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_page()

    # проверка наличия ссылки на регистрацию и переход на нее
    def test_guest_should_see_register_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_register_link()


@pytest.mark.register_user
class TestRegisterNewUser:
    # регистрация без выбора пола
    def test_register_new_user(self, browser):
        page = RegisterPage(browser, link)
        page.open()
        page.go_to_register_page()
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        email = str(time.time()) + '@mail.org'
        password = '123qwe789'
        page.filling_registration_form(first_name, last_name, email, password)
        page.register_new_user()
        page.should_be_success_message_registration()
        time.sleep(3)

    # регистрация с выбором мужского пола
    def test_register_new_user_male(self, browser):
        page = RegisterPage(browser, link)
        page.open()
        page.go_to_register_page()
        first_name = names.get_first_name(gender='male')
        last_name = names.get_last_name()
        email = str(time.time()) + '@mail.org'
        password = '123qwe789'
        page.filling_registration_form(first_name, last_name, email, password)
        page.gender(gender='male')
        page.register_new_user()
        page.should_be_success_message_registration()
        time.sleep(3)

    # регистрация с выбором женского пола
    def test_register_new_user_female(self, browser):
        page = RegisterPage(browser, link)
        page.open()
        page.go_to_register_page()
        first_name = names.get_first_name(gender='female')
        last_name = names.get_last_name()
        email = str(time.time()) + '@mail.org'
        password = '123qwe789'
        page.filling_registration_form(first_name, last_name, email, password)
        page.gender(gender='female')
        page.register_new_user()
        page.should_be_success_message_registration()
        time.sleep(3)


# проверка сообщений об ошибке при не заполнении обязательных полей
def test_user_should_see_warning_if_fields_are_not_filled(self, browser):
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_register_page()
    page.register_new_user()
    page.is_all_fields_has_error_class()
    
# pytest -v --tb=line -m register_user .\test_register_page.py
