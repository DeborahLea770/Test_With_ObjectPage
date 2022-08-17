from pageObject_selenium.base_page import BasePage
import time
from selenium.webdriver.common.by import By
from pageObject_selenium.item_page import ItemPage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "product-container": (By.CLASS_NAME, "product-container"),
        "product-name": (By.CLASS_NAME, "product-name"),
        "right-block": (By.CLASS_NAME, "right-block"),
        "content_price": (By.CLASS_NAME, "content_price"),
        "price": (By.CLASS_NAME, "price"),
        "add_to_cart_btn": (By.CLASS_NAME, "button.ajax_add_to_cart_button.btn.btn-default")

    }

    def choose_cheapest_Item(self):
        product_containers = self._driver.find_elements(*self.locator_dictionary["product-container"])
        min_price = 1000
        min_product_container = product_containers
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locator_dictionary["right-block"])
            content_price = right_block.find_element(*self.locator_dictionary["content_price"])
            price = content_price.find_element(*self.locator_dictionary["price"]).text
            price_num = float(price[1:len(price)])
            if min_price > price_num:
                min_price = price_num
                min_product_container = product_container
        right_block = min_product_container.find_element(*self.locator_dictionary["right-block"])
        right_block.find_element(*self.locator_dictionary["product-name"]).click()
        return ItemPage(self._driver)
