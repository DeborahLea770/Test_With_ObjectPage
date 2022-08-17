from pageObject_selenium.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    locator_dictionary = {
        "Submit": (By.ID, "add_to_cart"),
        "proceed_to_checkout_btn": (By.CSS_SELECTOR, "a.button-medium"),
        "proceed_to_checkout_btn1": (By.CSS_SELECTOR,
                                     'a[href="http://automationpractice.com/index.php?controller=order&step=1"]'),
        "processAddress": (By.CSS_SELECTOR, '[name=processAddress]'),
        "checkbox": (By.CSS_SELECTOR, '[type=checkbox]'),
        "processCarrier": (By.CSS_SELECTOR, '[name=processCarrier]'),
        "bankwire": (By.CLASS_NAME, "bankwire"),
        "button.button-medium": (By.CSS_SELECTOR, "button.button-medium")
    }

    def complet_buy(self):
        self._driver.find_elements(*self.locator_dictionary["Submit"])[0].click()
        time.sleep(5)
        self._driver.find_element(*self.locator_dictionary["proceed_to_checkout_btn"]).click()
        time.sleep(5)
        self._driver.find_element(*self.locator_dictionary["proceed_to_checkout_btn1"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["processAddress"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["checkbox"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["processCarrier"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["bankwire"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["button.button-medium"]).click()
        time.sleep(2)
        return self._driver
