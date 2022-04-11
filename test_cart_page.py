import pytest, time
from .pages.register_page import RegisterPage
from .pages.books_page import BooksPage
from .pages.cart_page import CartPage
from .test_data.user import UserRegister1
from .pages.checkout_page import CheckoutPage
from .test_data.address import BillingAddress

link = 'http://demowebshop.tricentis.com/'


# есть сообщение что корзина пуста при не добавлении товаров, товаров нет
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page_cart = CartPage(browser, link)
    page_cart.open()
    page_cart.go_to_shopping_cart_link()
    page_cart.should_not_be_cart_items()
    page_cart.should_be_message_cart_is_empty()


@pytest.mark.smoke
# изменение количества товара в корзине и перерасчет корзины
def test_changing_quantity_goods_in_basket_and_recalculating(browser):
    page = BooksPage(browser, link)
    page.open()
    page.go_to_books_link()
    page.adding_to_cart_from_books_page()
    page.go_to_shopping_cart_link_notification()
    page_cart = CartPage(browser, link)
    page_cart.price_should_change_when_changing_the_quantity_of_goods()


@pytest.mark.smoke
# зарестрированный пользователь оформляет заказ
def test_user_decorates_order_with_filling_in_the_address(browser):
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_register_page()
    page.filling_registration_form(UserRegister1)
    page.register_new_user()
    page_books = BooksPage(browser, link)
    page_books.go_to_books_link()
    page_books.adding_to_cart_from_books_page()
    page_books.go_to_shopping_cart_link_notification()
    page_cart = CartPage(browser, link)
    page_cart.checkbox_terms_of_service()
    page_cart.button_checkout()
    page_checkout = CheckoutPage(browser, link)
    page_checkout.filling_billing_address_form_required_fields(BillingAddress)
    page_checkout.button_continue_shipping_address()
    page_checkout.button_continue_shipping_method()
    page_checkout.button_continue_payment_method()
    page_checkout.button_continue_payment_information()
    page_checkout.button_confirm_order()
    page_checkout.should_be_section_order_completed()


# def guest_decorates_order_with_filling_in_the_address(browser):
#     pass


