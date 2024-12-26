from cgitb import text


class.BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self):
        return self.driver.find_element(*locator)

    def find_elements(self):
        return self.driver.find_elements(*locator)

    def click(self, *locator ):
        self.driver.find_element(*locator).click()

     def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


# page = BasePage
# element = page.find_element((By.CSS_SELECTOR, "[data-test='@web/CartLink']"))
# element.text


