from pageObject_playwright.authntication_page import AuthnticationPage
from pageObject_playwright.base_page import BasePage
import time
from playwright.sync_api import Page

from pageObject_playwright.search_page import SearchPage


class HomePage(BasePage):
    locator_dictionary = {"sing_in_btn": "a.login",
                          "search_query_top": '#search_query_top',
                          "submit_search": 'button.button-search'
                          }

    def __init__(self, page):
        super().__init__(page)

    def SingIn(self):
        self._page.locator(self.locator_dictionary["sing_in_btn"]).click()
        return AuthnticationPage(self._page)

    def search(self, search_text):
        self._page.locator(self.locator_dictionary["search_query_top"]).fill(search_text)
        self._page.locator(self.locator_dictionary["submit_search"]).click()
        return SearchPage(self._page)


