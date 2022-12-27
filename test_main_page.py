from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators

def test_guest_cant_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket_page()
    assert page.basket_message_present(*BasketPageLocators.BASKET_MESSAGE), "Message 'Your basket is empty' should be"
    assert page.is_not_items_in_basket(*BasketPageLocators.BASKET_WITH_ITEMS), "Message 'Items to buy now' is displayed, but should not be"


    #login_page = LoginPage(browser, browser.current_url)   #сохраняем в переменную страницу
    #login_page.should_be_login_page()  # используем методы новой страницы в тесте
