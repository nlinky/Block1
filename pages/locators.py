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
    SHOPPING_CART_LINK_NOTIFICATION = (By.CSS_SELECTOR, '.content [href="/cart"]')


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
    CHECKBOX_TERMS_OF_SERVICE = (By.ID, 'termsofservice')
    BUTTON_CHECKOUT = (By.ID, 'checkout')


class CheckoutPageLocators:
    FIELD_FIRST_NAME = (By.ID, 'BillingNewAddress_FirstName')
    FIELD_LAST_NAME = (By.ID, 'BillingNewAddress_LastName')
    FIELD_EMAIL = (By.ID, 'BillingNewAddress_Email')
    DROP_DOWN_COUNTRY = (By.ID, 'BillingNewAddress_CountryId')
    FIELD_CITY = (By.ID, 'BillingNewAddress_City')
    FIELD_ADDRESS_1 = (By.ID, 'BillingNewAddress_Address1')
    FIELD_ZIP = (By.ID, 'BillingNewAddress_ZipPostalCode')
    FIELD_PHONE_NUMBER = (By.ID, 'BillingNewAddress_PhoneNumber')
    BUTTON_CONTINUE_BILLING_ADDRESS = (By.CSS_SELECTOR, '#billing-buttons-container .button-1')
    BUTTON_CONTINUE_SHIPPING_ADDRESS = (By.CSS_SELECTOR, '#shipping-buttons-container .button-1')
    BUTTON_CONTINUE_SHIPPING_METHOD = (By.CSS_SELECTOR, '#shipping-method-buttons-container .button-1')
    BUTTON_CONTINUE_PAYMENT_METHOD = (By.CSS_SELECTOR, '#payment-method-buttons-container .button-1')
    BUTTON_CONTINUE_PAYMENT_INFORMATION = (By.CSS_SELECTOR, '#payment-info-buttons-container .button-1')
    BUTTON_CONFIRM_ORDER = (By.CSS_SELECTOR, '#confirm-order-buttons-container .button-1')
    SECTION_ORDER_COMPLETED = (By.CSS_SELECTOR, '.section.order-completed')


