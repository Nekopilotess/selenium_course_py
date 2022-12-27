import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import BasketPageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

def test_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_go_from_product_page_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                              "should not be "


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                              "should not be "

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket_page()
    assert page.basket_message_present(*BasketPageLocators.BASKET_MESSAGE), "Message 'Your basket is empty' " \
                                                                                 "should be "
    assert page.is_not_items_in_basket(*BasketPageLocators.BASKET_WITH_ITEMS), "Message 'Items to buy now' is " \
                                                                                    "displayed, but should not be "

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email=str(time.time()) + "@fakemail.org", password=str(time.time()) + "bihog860332")
        #page.should_be_authorized_user()
    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                              "should not be "

    def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_element_present(*ProductPageLocators.ADD_TO_CART), "'Add' button is not presented"

