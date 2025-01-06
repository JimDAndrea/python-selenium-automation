from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

class CartPage(BasePage):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def VerifyCartEmpty(self):
        sleep(10)
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.CART_EMPTY_MSG).text
        sleep(10)
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
