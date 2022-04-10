from .base_page import BasePage
from .locators import ProductBookLocators, CategoriesPageLocators


# страница - http://demowebshop.tricentis.com/health
class ProductBookPage(BasePage):
    def should_be_link_product_book_health_page(self):
        assert self.browser.find_element(*ProductBookLocators.PRODUCT_LINK_HEALTH), 'There is no link to the product'

    def go_to_product_book_health_page(self):
        product_book_link = self.browser.find_element(*ProductBookLocators.PRODUCT_LINK_HEALTH)
        # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);", product_book_link)
        product_book_link.click()

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductBookLocators.BUTTON_ADD_TO_CART), 'There is no add to cart button'

    def adding_to_cart_from_product_page(self):
        button_add_to_cart = self.browser.find_element(*ProductBookLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()

    def should_be_success_message(self):
        success_message = self.browser.find_element(*CategoriesPageLocators.NOTIFICATION_SUCCESS)
        assert success_message.text in 'The product has been added to your shopping cart', 'There is no notification that the product has been added to the cart'
