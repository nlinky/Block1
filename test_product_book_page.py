import pytest, time
from .pages.login_page import LoginPage
from .pages.product_book_page import ProductBookPage
from .pages.books_page import BooksPage
from .test_data.user import UserLogin

link = 'http://demowebshop.tricentis.com/'


@pytest.mark.smoke
# гость может добавить товар в корзину со страницы продукта и увидеть успешное сообщение
def test_guest_can_add_product_to_cart(browser):
    page = BooksPage(browser, link)
    page.open()
    page.go_to_books_link()
    page_product = ProductBookPage(browser, link)
    page_product.should_be_link_product_book_health_page()
    page_product.go_to_product_book_health_page()
    page_product.should_be_button_add_to_cart()
    page_product.adding_to_cart_from_product_page()
    page_product.should_be_success_message()


@pytest.mark.smoke
# гость может добавить товар в корзину со страницы BOOKS и увидеть успешное сообщение
def test_guest_can_add_product_to_cart_from_books_page(browser):
    page = BooksPage(browser, link)
    page.open()
    page.go_to_books_link()
    page.should_be_button_add_to_cart_book_health()
    page.adding_to_cart_from_books_page()
    page.should_be_success_message()


@pytest.mark.smoke
class TestUserAddProductToCart:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.filling_login_form(UserLogin)
        page.user_authorization()

    # юзер может добавить товар в корзину со страницы продукта и увидеть успешное сообщение
    def test_user_can_add_product_to_cart(self, browser):
        page = BooksPage(browser, link)
        page.open()
        page.go_to_books_link()
        page_product = ProductBookPage(browser, link)
        page_product.should_be_link_product_book_health_page()
        page_product.go_to_product_book_health_page()
        page_product.should_be_button_add_to_cart()
        page_product.adding_to_cart_from_product_page()
        page_product.should_be_success_message()

    # юзер может добавить товар в корзину со страницы BOOKS и увидеть успешное сообщение
    def test_user_can_add_product_to_cart_from_books_page(self, browser):
        page = BooksPage(browser, link)
        page.open()
        page.go_to_books_link()
        page.should_be_button_add_to_cart_book_health()
        page.adding_to_cart_from_books_page()
        page.should_be_success_message()
