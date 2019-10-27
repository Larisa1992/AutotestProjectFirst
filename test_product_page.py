from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import time

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    #time.sleep(100)
    product_page.is_right_good(product_page.return_prod_name())
    product_page.is_right_price(product_page.return_prod_price())
    time.sleep(60)
