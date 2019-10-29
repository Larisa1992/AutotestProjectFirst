from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
import pytest
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{index}" for index in range(0,10) if index != 7]
for_xfail = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
urls.insert(7,for_xfail)

#@pytest.mark.parametrize('link', urls)
#def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #product_page = ProductPage(browser, link)
    #product_page.open()
    #product_page.add_to_basket()
    #product_page.solve_quiz_and_get_code()
    #time.sleep(100)
    #product_page.is_right_good(product_page.return_prod_name())
    #product_page.is_right_price(product_page.return_prod_price())
    #time.sleep(60)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    #time.sleep(120)
    assert not product_page.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented"

#проверяем, что нет сообщения об успехе
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    assert product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented and not disappeared!"

