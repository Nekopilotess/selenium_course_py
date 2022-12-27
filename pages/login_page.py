import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Login link is not presented"
        assert True

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "bihog860332"
        #self.browser.find_element(*BasePageLocators.EMAIL).send_keys("porzuzipsi@gufum.com")
        #self.browser.find_element(*BasePageLocators.PASSWORD).send_keys("bihog860332")
        #self.browser.find_element(*BasePageLocators.CONFIRM_PASSWORD).send_keys("bihog860332")
        #self.browser.find_element(*BasePageLocators.REGISTER_BTN).click()