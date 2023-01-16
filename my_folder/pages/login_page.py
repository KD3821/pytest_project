from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)
        pass1_input = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        pass2_input = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        pass1_input.send_keys(password)
        pass2_input.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BTTN)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        my_url = self.browser.current_url
        assert my_url.find(LoginPageLocators.LOGIN_URL) != -1, "Login URL is not present"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_FORM), "Reg FORM is not presented"
