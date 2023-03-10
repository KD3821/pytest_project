from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_same_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text, "Имя товара не совпадает"

    def should_be_same_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text, "Цена товара не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "Success message did not disappear"
