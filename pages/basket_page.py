from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators

from .base_page import BasePage

class BasketPage(BasePage):

    def basket_message_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


    def is_not_items_in_basket(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        assert self.basket_message_present(*BasketPageLocators.BASKET_MESSAGE), "Message 'Your basket is empty' " \
                                                                                "should be "

    def guest_is_not_items_in_basket(self):
        assert self.is_not_items_in_basket(*BasketPageLocators.BASKET_WITH_ITEMS), "Message 'Items to buy now' is " \
                                                                                   "displayed, but should not be "
