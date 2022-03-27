from selenium.webdriver.common.by import By


class BasePageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, '.ico-register')


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
