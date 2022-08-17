import time
from playwright.async_api import Page
from pageObject_playwright.base_page import BasePage
from pageObject_playwright.my_account_page import MyAccountPage


class AuthnticationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    locator_dictionary = {"email": "input#email",
                          "password": "input#passwd",
                          "icon-lock": "#SubmitLogin",
                          "alert": ".alert",
                          "forget_password": 'text=Forgot your password?',
                          "page-subheading": ".page-subheading"
                          }

    def Login(self, user, password):
        self._page.locator(self.locator_dictionary["email"]).fill(user)
        self._page.locator(self.locator_dictionary["password"]).fill(password)
        self._page.locator(self.locator_dictionary["icon-lock"]).click()
        return MyAccountPage(self._page)

    def msg_error(self):
        time.sleep(2)
        text = self._page.locator(self.locator_dictionary["alert"]).all_text_contents()
        return text[0]

    def Forget_password(self):
        self._page.locator(self.locator_dictionary["forget_password"]).click()
        return self._page.title()
