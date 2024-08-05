from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure 
import pytest

@pytest.fixture 
def browser(): 
    browser = webdriver.Chrome() 
    browser.maximize_window() 
    browser.implicitly_wait(3)
    yield browser 
    browser.quit()

#открыть сайт Читай-город и принять cookie
cookie = {"name": "cookie_policy", "value": "1"}

@allure.title("согласие на принятие cookie") 
@allure.description("проверка добавления cookie (плашка исчезает)") 
@allure.severity("major") 
def test_open_site_and_add_cookie(browser):
    browser.get("https://www.chitai-gorod.ru/")
    browser.implicitly_wait(3)
    browser.maximize_window()
    with allure.step("добавление cookie"):
        browser.add_cookie(cookie)

#поиск книги по названию
@allure.title("поиск книги по названию оливер твист") 
@allure.description("проверка поиска книги по названию") 
@allure.severity("blocker") 
def test_add_book_in_cart(browser):
    browser.get("https://www.chitai-gorod.ru/")
    with allure.step("добавление ожидания и открытие окна"): 
        browser.implicitly_wait(3)
        browser.maximize_window()
    with allure.step("выполнение поиска книги"): 
        browser.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys("оливер твист")
        browser.find_element(By.CSS_SELECTOR, ".header-search__button").click()  
    assert "результаты запроса" in browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
    

#добавить все книги в корзину и посчитать их количество
def add_book_in_cart_and_count(browser):
    with allure.step("Добавить все книги"): 
        buy_buttons = browser.find_elements(
    By.CSS_SELECTOR, "button action-button blue")
    with allure.step("считаем все книги"):
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

#переход в корзину
    with allure.step("выполняем переход в корзину"): 
        browser.get("https://www.chitai-gorod.ru/cart")
    txt = browser.find_element_by_class_name("badge-notice header-cart__badge").text
    with allure.step("Проверить счетчик товаров"): 
#проверка счетчика товаров
        assert counter == int(txt)

    browser.quit()