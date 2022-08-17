from pageObject_selenium.base_page import BasePage
from selenium.webdriver.common.by import By
from pageObject_selenium import home_page


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {"home_btn": (By.CLASS_NAME, "icon-home"),
                          "info-account": (By.CLASS_NAME, "info-account")}

    def go_home(self):
        self._driver.find_element(*self.locator_dictionary["home_btn"]).click()
        return home_page.HomePage(self._driver)

    def valid_authentication(self):
        return self._driver.find_element(*self.locator_dictionary["info-account"]).text
