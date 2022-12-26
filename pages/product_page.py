from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
<<<<<<< HEAD
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()
        self.solve_quiz_and_get_code()
        alert_name_product = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        return alert_name_product.text
=======
    def add_to_cart(self, is_promo=False):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482

    def should_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "'Add' button is not presented"
    def product_name(self):
        name=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text
    def product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

<<<<<<< HEAD
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
=======
    def should_be_present_in_cart(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not present"
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ADDED_TO_CART), "No alert that a product has been added to cart"
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_CART).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name in alert_text, \
            f"The alert contains wrong product name: {alert_text} - {product_name}"

    def should_check_overall_cost(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*ProductPageLocators.ALERT_CART_STATUS
                                       ), "No alert with cart status"
        alert_text = self.browser.find_element(
            *ProductPageLocators.ALERT_CART_STATUS).text.split()[-1]
        product_cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost {alert_text} != {product_cost}"
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482
