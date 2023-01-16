from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "header a.btn-default")


class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form#basket_summary")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REG_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
