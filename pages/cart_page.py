from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_cart_items(self):
        assert self.is_not_element_present(*CartPageLocators.ITEMS_CART), 'The items in the cart are displayed, but they should not be'

    def should_be_message_cart_is_empty(self):
        message_cart_is_empty = self.browser.find_element(*CartPageLocators.SUMMARY_CONTENT)
        assert message_cart_is_empty.text == 'Your Shopping Cart is empty!', 'There is no message that the trash is empty'

    def changing_the_number_of_products(self):
        cnt = self.browser.find_element(*CartPageLocators.ITEMS_QUANTITY)
        # val = cnt.get_attribute('value')
        cnt.clear()
        cnt.send_keys(5)

    def button_update_shopping_cart(self):
        button_update = self.browser.find_element(*CartPageLocators.UPDATE_SHOPPING_CART)
        button_update.click()

    def price_product(self):
        price = self.browser.find_element(*CartPageLocators.PRICE)
        return price.text

    def total_product_price(self):
        total = self.browser.find_element(*CartPageLocators.TOTAL)
        return total.text

    def sub_total_product_price(self):
        sub_total = self.browser.find_element(*CartPageLocators.SUB_TOTAL)
        return sub_total.text

    def price_should_change_when_changing_the_quantity_of_goods(self):
        self.changing_the_number_of_products()
        self.button_update_shopping_cart()
        price = float(self.price_product()) * 5
        assert price == float(self.total_product_price()) and price == float(self.sub_total_product_price()), 'the final price of the product does not match'

    def checkbox_terms_of_service(self):
        terms_of_service = self.browser.find_element(*CartPageLocators.CHECKBOX_TERMS_OF_SERVICE)
        terms_of_service.click()

    def button_checkout(self):
        checkout = self.browser.find_element(*CartPageLocators.BUTTON_CHECKOUT)
        checkout.click()
