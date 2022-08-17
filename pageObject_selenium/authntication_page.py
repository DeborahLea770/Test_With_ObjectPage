from pageObject_selenium.base_page import BasePage
import time
from selenium.webdriver.common.by import By
from pageObject_selenium.account_page import *


class AuthnticationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {"email": (By.ID, "email"),
                          "password": (By.ID, "passwd"),
                          "icon-lock": (By.CLASS_NAME, "icon-lock"),
                          "alert": (By.CLASS_NAME, "alert"),
                          "forget_password": (By.XPATH, '//a[text()="Forgot your password?"]'),
                          "page-subheading": (By.CLASS_NAME, "page-subheading")
                          }

    def Login(self, user, password):
        self._driver.find_element(*self.locator_dictionary["email"]).send_keys(user)
        self._driver.find_element(*self.locator_dictionary["password"]).send_keys(password)
        self._driver.find_element(*self.locator_dictionary["icon-lock"]).click()

        return MyAccountPage(self._driver)

    def msg_error(self):
        text = self._driver.find_element(*self.locator_dictionary["alert"]).text
        return text

    def Forget_password(self):
        self._driver.find_element(*self.locator_dictionary["forget_password"]).click()
        msg_forget_pass = self._driver.find_element(*self.locator_dictionary["page-subheading"]).text
        return msg_forget_pass
