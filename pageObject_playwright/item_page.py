import time

from pageObject_playwright.base_page import BasePage


class ItemPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {
        "Submit": "text='Add to cart'",
        "proceed_to_checkout_btn": "text='Proceed to checkout'",
        "proceed_to_checkout_btn1": "#center_column >> text='Proceed to checkout'",
        "processAddress": "button >> text='Proceed to checkout'",
        "checkbox": "input#cgv",
        "processCarrier": "button >> text='Proceed to checkout'",
        "bankwire": "text='Pay by bank wire'",
        "button.button-medium": "button >> text='I confirm my order'"
    }

    def complet_buy(self):
        self._page.locator(self.locator_dictionary["Submit"]).click()
        time.sleep(5)
        self._page.locator(self.locator_dictionary["proceed_to_checkout_btn"]).click()
        time.sleep(5)
        self._page.locator(self.locator_dictionary["proceed_to_checkout_btn1"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["processAddress"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["checkbox"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["processCarrier"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["bankwire"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["button.button-medium"]).click()
        time.sleep(2)
        return self._page
