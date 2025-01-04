from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

class CartPage(BasePage):

    def ClickCart(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
        self.driver.find_element(*CART_ICON).click()


    def VerifyCartEmpty(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
        assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
