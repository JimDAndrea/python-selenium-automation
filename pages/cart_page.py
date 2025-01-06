from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

class CartPage(BasePage):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def VerifyCartEmpty(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

