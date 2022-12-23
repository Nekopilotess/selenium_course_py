import pytest

from .pages.product_page import ProductPage

@pytest.mark.parametrize("promo_number", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_cart(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_can_add_non_promo_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()
