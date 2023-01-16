from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "header a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form#basket_summary")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REG_PASS2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REG_BTTN = (By.CSS_SELECTOR, "form#register_form > button.btn-primary")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
