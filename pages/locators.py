from selenium.webdriver.common.by import By


class BasePageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, '.ico-register')
    LOG_IN_LINK = (By.CSS_SELECTOR, '.ico-login') #text
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout') #text
    ACCOUNT_LINK = (By.CSS_SELECTOR, 'div.header-links a.account')


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
    LOGIN_FORM = (By.CSS_SELECTOR, '.returning-wrapper')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#Email')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#Password')
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, '#RememberMe')
    FORGET_PASSWORD_LINK = (By.CSS_SELECTOR, 'span.forgot-password a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button-1 login-button')
    REGISTER_BLOCK = (By.CSS_SELECTOR, 'div.new-wrapper.register-block')
    REGISTER_BUTTON_ON_PAGE_LOGIN = (By.CSS_SELECTOR, '.button-1.register-button')

