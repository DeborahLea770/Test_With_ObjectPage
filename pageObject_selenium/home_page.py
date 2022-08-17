from pageObject_selenium.authntication_page import *
from pageObject_selenium.search_page import *


class HomePage(BasePage):
    locator_dictionary = {"sing_in_btn": (By.CLASS_NAME, "login"),
                          "search_query_top": (By.ID, "search_query_top"),
                          "submit_search": (By.NAME, "submit_search")
                          }

    def __init__(self, driver):
        super().__init__(driver)

    def SingIn(self):
        self._driver.find_element(*self.locator_dictionary["sing_in_btn"]).click()
        return AuthnticationPage(self._driver)

    def search(self, search_text):
        self._driver.find_element(*self.locator_dictionary["search_query_top"]).send_keys(search_text)
        self._driver.find_element(*self.locator_dictionary["submit_search"]).click()
        return SearchPage(self._driver)