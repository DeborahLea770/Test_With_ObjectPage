from pageObject_playwright.base_page import BasePage
from pageObject_playwright import home_page


class MyAccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {"home_btn": ".icon-home",
                          "info-account": ".info-account"}

    def go_home(self):
        self._page.locator(self.locator_dictionary["home_btn"]).click()
        return home_page.HomePage(self._page)

    def valid_authentication(self):
        return self._page.locator(self.locator_dictionary["info-account"]).inner_html()
