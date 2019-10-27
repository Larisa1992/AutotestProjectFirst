from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR,"#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    ARRAY_MESSAGE = (By.CSS_SELECTOR, ".alertinner  strong")
    PROD_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1") #фактическое название товара
    PROD_PRICE = (By.CSS_SELECTOR, "p.price_color") #фактическая цена товара