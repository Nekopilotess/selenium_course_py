import math
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


<<<<<<< HEAD
class BasePage():
    def __init__(self, browser: Remote, url: str, timeout=10):
=======
class BasePage:
    def __init__(self, browser: Remote, url: str) -> None:
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482
        super().__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

<<<<<<< HEAD
    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login Link is not presented"

    def is_element_present(self, how: str, what: str):
=======
    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
<<<<<<< HEAD

    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
=======
>>>>>>> 915bd6a4b11bd8239385e71032a46d4c50f9d482
