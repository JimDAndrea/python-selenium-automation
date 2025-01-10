from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep

class SignInPage(BasePage):

    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "[id*='username']")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "[data-test*='login-password']")
    SIGN_IN_WITH_PWD_BTN = (By.XPATH, "//span[text()='Sign in with password']")

    def InputEmail(self, email):
        self.input_text(email, *self.SIGN_IN_EMAIL)

    def InputPassword(self, password):
        self.input_text(password,*self.SIGN_IN_PASSWORD)

    def VerifyUserLoggedIn(self):
         self.driver.find_element(*self.SIGN_IN_WITH_PWD_BTN).click()

