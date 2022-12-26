from .base_page import BasePage
from .locators import BasePageLocators


class MainPage(BasePage):
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
=======
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482
