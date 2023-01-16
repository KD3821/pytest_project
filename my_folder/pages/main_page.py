from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def open_basket(self):
    #     basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
    #     basket_link.click()

