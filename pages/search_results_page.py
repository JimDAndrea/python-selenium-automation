from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, product):
        sleep(5)
        self.verify_partial_text(product, *self.SEARCH_RESULTS)

    def verify_search_url(self,product):
        self.verify_partial_url(product)


