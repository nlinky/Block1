from .base_page import BasePage
from .locators import BooksPageLocators, ProductBookLocators, CategoriesPageLocators


# страница - http://demowebshop.tricentis.com/books
class BooksPage(BasePage):
    def should_be_button_add_to_cart_book_health(self):
        assert self.is_element_present(*BooksPageLocators.BUTTON_ADD_TO_CART_BOOK_NAME_HEALTH), 'There is no add to cart button'

    def adding_to_cart_from_books_page(self):
        # button_add_to_cart_fiction_book = self.browser.find_element(*BooksPageLocators.BUTTON_ADD_TO_CART_BOOK_NAME_HEALTH)
        # button_add_to_cart_fiction_book.click()
        self.browser.find_element(*BooksPageLocators.BUTTON_ADD_TO_CART_BOOK_NAME_HEALTH).click()

    def should_be_success_message(self):
        success_message = self.browser.find_element(*CategoriesPageLocators.NOTIFICATION_SUCCESS)
        assert success_message.text in 'The product has been added to your shopping cart', 'There is no notification that the product has been added to the cart'

