from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    INVALID_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_inc")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form>button")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_WITH_ITEMS = (By.CSS_SELECTOR, "div.basket-title.hidden-xs>div>h2")
    BASKET_MESSAGE = (By.ID, "content_inner")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
