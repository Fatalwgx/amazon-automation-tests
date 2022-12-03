from selene import command
from selene.support.conditions import be
from selene.support.shared import browser

from amazon.model.pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self):
        self.add_to_cart_button = ...

    def add_to_cart(self):
        self.add_to_cart_button = browser.element("input[id^='add-to-cart-button']")
        command.js.scroll_into_view(self.add_to_cart_button)
        self.add_to_cart_button.click()
        browser.element('#sw-subtotal-item-count').should(be.visible)
        return self
