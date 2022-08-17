import time

from pageObject_playwright.base_page import BasePage
from pageObject_playwright.item_page import ItemPage


class SearchPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {
        "product-container": ".product-container",
        "product-name": ".product-name",
        "right-block": ".right-block",
        "content_price": ".content_price",
        "price": ".price",
        "add_to_cart_btn": ".button.ajax_add_to_cart_button.btn.btn-default"

    }

    def choose_cheapest_Item(self):
        time.sleep(2)
        product_containers = self._page.query_selector_all(self.locator_dictionary["product-container"])
        min_price = 1000
        min_product_container = product_containers
        for product_container in product_containers:
            right_block = product_container.query_selector(self.locator_dictionary["right-block"])
            content_price = right_block.query_selector(self.locator_dictionary["content_price"])
            price = content_price.query_selector(self.locator_dictionary["price"]).text_content()
            price_num = float(price.replace("$", ""))
            if min_price > price_num:
                min_price = price_num
                min_product_container = product_container
        right_block = min_product_container.query_selector(self.locator_dictionary["right-block"])
        right_block.query_selector(self.locator_dictionary["product-name"]).click()
        return ItemPage(self._page)

