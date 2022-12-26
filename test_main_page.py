from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def go_to_login_page(browser):
    browser.find_element(By.CSS_SELECTOR, "#login_link").click()
    browser.switch_to.alert.accept()



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)   #сохраняем в переменную страницу
    login_page.should_be_login_page()  # используем методы новой страницы в тесте
