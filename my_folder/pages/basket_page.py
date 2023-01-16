from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Product list is empty"

    def should_be_text_empty_basket(self):
        basket_notice = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert basket_notice.find("Your basket is empty") != -1, "No text about empty basket"
