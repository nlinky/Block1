from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class BasePageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, '.ico-register')
    LOG_IN_LINK = (By.CSS_SELECTOR, '.ico-login')
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')
    ACCOUNT_LINK = (By.CSS_SELECTOR, 'div.header-links a.account')
    BOOKS_LINK = (By.CSS_SELECTOR, '.top-menu [href="/books"]')
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, '.ico-cart')


class RegisterPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, 'form[action="/register"]')
    REGISTER_GENDER_MALE_RADIO = (By.CSS_SELECTOR, '#gender-male')
    REGISTER_GENDER_FEMALE_RADIO = (By.CSS_SELECTOR, '#gender-female')
    REGISTER_FIRST_NAME = (By.CSS_SELECTOR, '#FirstName')
    REGISTER_LAST_NAME = (By.CSS_SELECTOR, '#LastName')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#Email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#Password')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#ConfirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')
    SUCCESS_MESSAGE_REGISTRATION = (By.CSS_SELECTOR, 'div .result')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form[action="/login"]')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#Email')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#Password')
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, '#RememberMe')
    FORGET_PASSWORD_LINK = (By.CSS_SELECTOR, 'span.forgot-password a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button-1.login-button')
    REGISTER_BLOCK = (By.CSS_SELECTOR, 'div.new-wrapper.register-block')
    REGISTER_BUTTON_ON_PAGE_LOGIN = (By.CSS_SELECTOR, '.button-1.register-button')
    MESSAGE_ERROR_EMPTY = (By.CSS_SELECTOR, '.validation-summary-errors span')
    MESSAGE_ERROR_EMPTY_ACCOUNT_OR_PASSWORD = (By.CSS_SELECTOR, '.validation-summary-errors li')
    MESSAGE_ERROR_EMAIL_INVALID = (By.CSS_SELECTOR, '.field-validation-error span')


class ChangePasswordPageLocators:
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, 'div.listbox > ul > li:nth-child(7) > a')
    CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, 'form[action="/customer/changepassword"]')
    OLD_PASSWORD = (By.CSS_SELECTOR, '#OldPassword')
    NEW_PASSWORD = (By.CSS_SELECTOR, '#NewPassword')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#ConfirmNewPassword')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.button-1.change-password-button')
    RESULT_MESSAGE = (By.CSS_SELECTOR, '.result')
    MESSAGE_ERROR_OLD_PASSWORD = (By.CSS_SELECTOR, '.validation-summary-errors li')


class CategoriesPageLocators:
    NOTIFICATION_SUCCESS = (By.CSS_SELECTOR, 'p.content')


class BooksPageLocators:
    BUTTON_ADD_TO_CART_BOOK_NAME_HEALTH = (By.CSS_SELECTOR, '[data-productid="22"] .button-2')


class ProductBookLocators:
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '.add-to-cart-button')
    PRODUCT_LINK_HEALTH = (By.CSS_SELECTOR, ".product-title [href='/health']")


class CartPageLocators:
    ITEMS_CART = (By.CSS_SELECTOR, '[action="/cart"]')
    SUMMARY_CONTENT = (By.CSS_SELECTOR, '.order-summary-content')
    ITEMS_QUANTITY = (By.CSS_SELECTOR, '.qty-input')
    PRICE = (By.CSS_SELECTOR, '.product-unit-price')
    TOTAL = (By.CSS_SELECTOR, '.product-subtotal')
    UPDATE_SHOPPING_CART = (By.NAME, 'updatecart')
    SUB_TOTAL = (By.CSS_SELECTOR, '.product-price')


